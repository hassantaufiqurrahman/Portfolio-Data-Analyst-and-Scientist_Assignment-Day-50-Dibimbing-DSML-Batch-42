# Import Library
from pathlib import Path
import joblib
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Lasso, LinearRegression, Ridge
from sklearn.metrics import (
    mean_absolute_error,
    mean_absolute_percentage_error,
    mean_squared_error,
    r2_score,
)
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# Setup Folder Penyimpanan Model
BASE_DIR = Path(__file__).parent if "__file__" in globals() else Path.cwd()
MODEL_DIR = BASE_DIR / "model"
MODEL_DIR.mkdir(exist_ok=True)

# Mapping Nama Model ke Nama File .pkl
FILE_NAME_MAP = {
    "Linear Regression": "model_lr.pkl",
    "Ridge Regression": "model_ridge.pkl",
    "Lasso Regression": "model_lasso.pkl",
    "Random Forest Regression": "model_rf.pkl",
}

# Load Dataset
train_df = pd.read_csv("data/train.csv")

# Mengubah Tipe Data "MSSubClass" menjadi String untuk Berubah Menjadi Kolom Kategorikal
if "MSSubClass" in train_df.columns:
    train_df["MSSubClass"] = train_df["MSSubClass"].astype(str)

# Memisahkan Feature dan Target
X = train_df.drop(columns=["Id", "SalePrice"], errors="ignore")
y = np.log1p(train_df["SalePrice"])

# Split "train_df" Menjadi Data Training & Validation
X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Pemisahan Otomatis Kolom Numerik & Kategorikal
num_features = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
cat_features = X.select_dtypes(include=["object", "category"]).columns.tolist()

# Preprocessing Pipeline
num_pipeline = Pipeline(
    [
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ]
)

cat_pipeline = Pipeline(
    [
        ("imputer", SimpleImputer(strategy="most_frequent")),
        (
            "encoder",
            OneHotEncoder(handle_unknown="ignore", sparse_output=False),
        ),
    ]
)

preprocessor = ColumnTransformer(
    [
        ("num", num_pipeline, num_features),
        ("cat", cat_pipeline, cat_features),
    ]
)

# Definisi Model & Parameter Grid untuk Tuning
models_and_params = {
    "Linear Regression": {"model": LinearRegression(), "params": {}},
    "Ridge Regression": {
        "model": Ridge(random_state=42),
        "params": {"model__alpha": [0.1, 1.0, 10.0, 50.0, 100.0]},
    },
    "Lasso Regression": {
        "model": Lasso(max_iter=10000, random_state=42),
        "params": {"model__alpha": [0.0001, 0.001, 0.01, 0.1, 1.0]},
    },
    "Random Forest Regression": {
        "model": RandomForestRegressor(random_state=42),
        "params": {
            "model__n_estimators": [100, 200],
            "model__max_depth": [10, 20, None],
            "model__min_samples_split": [2, 5],
        },
    },
}

# Iterasi Pelatihan, Hyperparameter Tuning, Evaluasi, & Penyimpanan Model
results = []
best_overall_rmse = float("inf")
best_overall_model = None
best_overall_name = ""

for name, mp in models_and_params.items():
    pipeline = Pipeline(
        [("preprocessor", preprocessor), ("model", mp["model"])]
    )

    if mp["params"]:
        grid_search = GridSearchCV(
            pipeline,
            mp["params"],
            cv=5,
            scoring="neg_root_mean_squared_error",
            n_jobs=-1,
        )
        grid_search.fit(X_train, y_train)
        best_model = grid_search.best_estimator_
        best_params = grid_search.best_params_
    else:
        pipeline.fit(X_train, y_train)
        best_model = pipeline
        best_params = "N/A"

    # Prediksi pada Data Validation
    y_pred_log = best_model.predict(X_val)

    # Mengembalikan Skala Prediksi dan Nilai Aktual ke Harga Asli
    y_pred = np.expm1(y_pred_log)
    y_val_actual = np.expm1(y_val)

    # Kalkulasi Metrik Evaluasi pada Skala Asli
    r2 = r2_score(y_val_actual, y_pred)
    mae = mean_absolute_error(y_val_actual, y_pred)
    mape = mean_absolute_percentage_error(y_val_actual, y_pred)
    rmse = np.sqrt(mean_squared_error(y_val_actual, y_pred))

    results.append(
        {
            "Model": name,
            "Best Params": str(best_params),
            "R^2": round(r2, 4),
            "MAE": round(mae, 2),
            "MAPE (%)": round(mape * 100, 2),
            "RMSE": round(rmse, 2),
        }
    )

    # Simpan Masing-Masing Model ke Folder 'model/'
    save_filename = FILE_NAME_MAP.get(
        name, f"{name.lower().replace(' ', '_')}.pkl"
    )
    model_save_path = MODEL_DIR / save_filename
    joblib.dump(best_model, model_save_path)
    print(f"✅ Model {name} berhasil disimpan ke: {model_save_path}")

    # Memilih model terbaik berdasarkan nilai RMSE TERKECIL
    if rmse < best_overall_rmse:
        best_overall_rmse = rmse
        best_overall_model = best_model
        best_overall_name = name

# Menampilkan Ringkasan Evaluasi
print("\n" + "=" * 50)
print("📊 Ringkasan Evaluasi Model")
print("=" * 50)
results_df = pd.DataFrame(results)
print(results_df.to_string(index=False))
print(
    f"\n🏆 Model Terbaik: {best_overall_name} dengan RMSE = ${best_overall_rmse:,.2f}"
)

# Simpan Model Pipeline Terbaik Secara Terpisah
best_model_path = MODEL_DIR / "best_house_price_model_predict.pkl"
joblib.dump(best_overall_model, best_model_path)
print(
    f"🌟 Model pipeline terbaik ({best_overall_name}) berhasil disimpan ke '{best_model_path}'."
)