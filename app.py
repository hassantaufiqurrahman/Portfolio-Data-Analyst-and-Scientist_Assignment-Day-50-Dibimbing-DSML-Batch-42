# Import Library
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, mean_absolute_percentage_error

# Membuat Judul Website
st.set_page_config(
    page_title="My Portfolio with Streamlit",
    page_icon="🤖",
    layout="wide",
)

# Membuat Header Website
st.title("Hassan Taufiqurrahman's Data Analysis & Science Portfolio ")

# Membuat Deskripsi Singkat Website
st.markdown("""
Hi, welcome to my interactive portfolio website 👋

This interactive portfolio website is designed to showcase my professional background highlighting my strong interest in 
**Data Analyst** and **Data Scientist** as well as a list of data analysis and data science projects I have completed. 
Additionally, this site features simulations of machine learning model-based predictions, data visualizations, 
and machine learning model performance evaluations.

""")

# Membuat Tab Navigasi
tab_home, tab_project, tab_predict, tab_visual = st.tabs([
    "About Me",
    "My Projects",
    "Model Prediction",
    "Data Visualization & Model Performance",
])

# Membuat Isi Tab "About Me"
with tab_home:
    st.header("👨‍💻 About Me")

    # Membuat 2 Kolom untuk Menampilkan Foto & Bio
    col_photo, col_bio = st.columns([1, 2.5], vertical_alignment="center")

    with col_photo:
        st.image("picture/Hassan Photo.jpg", use_container_width=True)

    with col_bio:
        st.write(
            """
            I'm a Fresh Graduate from Universitas Pendidikan Indonesia majoring in **Mathematics** with strong analytical and problem-solving skills, 
            specializing in **Data Analysis** and **Data Science**. Experienced in **data processing**, **visualization**, **business reporting**, and **data modelling**
            using **Excel**, **SQL**, **Python**, **Looker Studio**, and **Tableau** through independent study projects and internship. 
            Proven ability to manage operational data with high accuracy and transform datasets into actionable **business insights**.
            """
        )

        st.markdown(
            """
            <div style="display: flex; gap: 10px; margin-top: 10px;">
                <a href="mailto:hassan.taufiqurrahman@gmail.com" target="_blank" style="text-decoration: none; padding: 8px 16px; background-color: #EA4335; color: white; border-radius: 6px; font-weight: bold; font-size: 14px;">📧 Gmail</a>
                <a href="https://linkedin.com/in/hassantaufiqurrahman" target="_blank" style="text-decoration: none; padding: 8px 16px; background-color: #0A66C2; color: white; border-radius: 6px; font-weight: bold; font-size: 14px;">💼 LinkedIn</a>
                <a href="https://github.com/hassantaufiqurrahman" target="_blank" style="text-decoration: none; padding: 8px 16px; background-color: #24292E; color: white; border-radius: 6px; font-weight: bold; font-size: 14px;">🐙 GitHub</a>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.divider()

    
    st.subheader("🛠️ Skills")

    # Membuat 4 Kolom untuk Menampilkan Kategori Skill
    col_s1, col_s2, col_s3, col_s4 = st.columns(4)

    with col_s1:
        st.markdown("**Analytics & Modelling**")
        st.write(
            """
            Excel, SQL, Pandas, NumPy, Scikit-Learn.
            
            """
        )

    with col_s2:
        st.markdown("**Data Visualization**")
        st.write(
            """
             Excel, Matplotlib, Seaborn, Plotly, Looker Studio, Tableau.
            
            """
        )

    with col_s3:
        st.markdown("**Languange**")
        st.write(
            """
            Indonesian (Native), English (Intermediate)
                        
            """
        )

    with col_s4:
        st.markdown("**Soft Skills**")
        st.write(
            """
            Communication, Teamwork, Analytical Thinking, Desire to Continue Learning.
                            
            """
        )

    st.divider()

    # Membuat 2 Kolom untuk Menampilkan Education & Work Experience
    col_edu, col_work = st.columns(2)

    with col_edu:
        st.subheader("🎓 Education")

        with st.container(border=True):
            st.markdown("#### **Bootcamp Data Science & AI Machine Learning**")
            st.caption("**Dibimbing.id | Apr 2026 – Present**")
            st.markdown(
                """
                Learn the complete data science workflow including data collection, pre-processing, EDA, and model evaluation using real-world datasets.

                """
            )

        with st.container(border=True):
            st.markdown("#### **Independent Study Data Analyst**")
            st.caption(
                "**Magang & Studi Independen Bersertifikat (MSIB) x PT Cerdas Digital Nusantara (Cakap) | Sep –"
                " Des 2024**"
            )
            st.markdown(
                """
                - Learn data presentation, data analysis, and data visualization techniques using real-world datasets.
                - **Capstone Project:** Designing an interactive dashboard to analyze E-Commerce Olist Store.
                """
            )

        with st.container(border=True):
            st.markdown("#### **Bachelor of Mathematics**")
            st.caption("**Universitas Pendidikan Indonesia | 2021 – 2025**")
            st.markdown(
                """
                - GPA: 3.65 / 4.00
                - Thesis: Solving Inventory Control Problems Using Robust Capacitated Single Station Case Model.
                """
            )

    with col_work:
        st.subheader("💼 Work Experience")

        with st.container(border=True):
            st.markdown("#### **Admin Operation Intern**")
            st.caption(
                "**PT Guthrie Agri Bio (Sime Darby Guthrie) | Sep 2025 – Mar 2026**"
            )
            st.markdown(
                """
                - Prepared **20+** sales and operational documents monthly, including Despatch Notes and supporting administrative reports.
                - Verified and monitored approximately **50** Purchase Orders and Invoice per month to ensure compliance with company procedures.
                - Coordinated delivery tracking for **30-60** monthly orders, maintaining a **95%** on-time delivery rate.
                - Managed warehouse stock recapitulation for **200+** items with **98%** data accuracy across manual and digital systems.
                """
            )

    st.divider()

    # Membuat dan Menampilkan Organization Experience
    st.subheader("🏛️ Organization Experience")

    with st.container(border=True):
        st.markdown(
            "#### **Senior Staff of Research In Mathematics Organization (RIEMANN) Program**"
        )
        st.caption("**BEM Himatika 'Identika' UPI | Jan 2023 – Jan 2024**")
        st.markdown(
            """
            - Supervising and guiding research and development to junior staff during **1** period.
            - Conducting performance monitoring in **6** divisions with a total of more than **100** board members through routine monthly evaluations.
            - Monitor the dynamics and working relationships between managers in all divisions through routine monthly evaluations.
            """
        )

    with st.container(border=True):
            st.markdown(
                "#### **Team Coordinator of Research In Mathematics Organization (RIEMANN) Program**"
            )
            st.caption("**BEM Himatika 'Identika' UPI | Mar 2022 – Jan 2023**")
            st.markdown(
                """
                - Prepare a program plan for **1** period with team members and monitor the work progress of each team member.
                - Conducting performance monitoring in **7** divisions with a total of more than **100** board members through routine monthly evaluations.
                - Monitor the dynamics and working relationships between managers in all divisions through routine monthly evaluations.
                """
            )

# Membuat Isi Tab "My Projects"
with tab_project:
  st.header("📁 My Projects")
  
  st.divider()

  # Membuat 3 Container untuk Menampilkan Masing-masing 3 Proyek dengan Gambar, Deskripsi, dan Link
  with st.container(border=True):
        st.subheader("1. Olist Store E-Commerce Analysis")

        st.markdown(
            """
            This project analyzes over **100,000** e-commerce transaction records from the Olist store spanning 2016 to 2018 
            to identify monthly sales trends, high-revenue product categories, and customer purchasing patterns, 
            presenting the findings in an interactive dashboard.
            """
        )

        st.image(
            "picture/Olist Store E-Commerce Analysis Dashboard.png",
            use_container_width=True,
        )

        st.write("")  

        col_tab1, col_git1 = st.columns(2)
        with col_tab1:
            st.link_button(
                "📊 Interactive Dashboard",
                "https://public.tableau.com/app/profile/hassan.taufiqurrahman/viz/BrazillianEcommerceDashboard/Dashboard1",
                type="primary",
                use_container_width=True,
            )
        with col_git1:
            st.link_button(
                "🗃️ Repository GitHub",
                "https://github.com/hassantaufiqurrahman/Olist-Store-Ecommerce-Analysis",
                type="primary",
                use_container_width=True,
            )

  st.write("")  


  with st.container(border=True):
        st.subheader("2. Telco Customer Churn Analysis")

        st.markdown(
            """
            This project analyzes data from over **1,000** customers of a telecommunications company to identify factors driving churn, specifically 
            through variable correlations that map high risk customer segments based on contract and service types and presents the findings via an interactive dashboard.
            """
        )

        st.image(
            "picture/Telco Churn Analysis Dashboard.png",
            use_container_width=True,
        )

        st.write("")  

        col_tab2, col_git2 = st.columns(2)
        with col_tab2:
            st.link_button(
                "📊 Interactive Dashboard",
                "https://public.tableau.com/app/profile/hassan.taufiqurrahman/viz/shared/NHM7542XQ",
                type="primary",
                use_container_width=True,
            )
        with col_git2:
            st.link_button(
                "🗃️ Repository GitHub",
                "https://github.com/hassantaufiqurrahman/Telco-Churn-Analysis",
                type="primary",
                use_container_width=True,
            )

  st.write("")  


  with st.container(border=True):
        st.subheader("3. Bank Customer Churn Prediction")

        st.markdown(
            """
            This project develops an end-to-end classification system to predict potential bank customer churn using 
            machine learning models. The best-performing model for this project is XGBoost, achieving an ROC-AUC score of **0.9921**, 
            with the two key features driving the prediction being the number of transactions and the total transaction value over the past year.
            """
        )

        img_col1, img_col2 = st.columns(2)
        with img_col1:
            st.image(
                "picture/ROC Curve XGBoost.png", 
                use_container_width=True,
            )
        with img_col2:
            st.image(
                "picture/SHAP XGBoost.png",
                use_container_width=True,
            )

        st.write("")

        st.link_button(
            "🗃️ Repository GitHub",
            "https://github.com/hassantaufiqurrahman/Bank-Customer-Churn-Prediction", 
            type="primary",
            use_container_width=True,
        )


# Setup Direktori & Load Model Banyak
BASE_DIR = Path(__file__).parent if "__file__" in globals() else Path.cwd()

# Membuat Function Load Model dari File Pickle
@st.cache_resource
def load_all_models():
    models = {}
    model_mapping = {
        "Best Pipeline Model": "best_house_price_model_predict.pkl",
        "Random Forest Regressor": "model_rf.pkl",
        "Linear Regression": "model_lr.pkl",
        "Ridge Regression": "model_ridge.pkl",
        "Lasso Regression": "model_lasso.pkl",
    }

    for label, filename in model_mapping.items():
        path = BASE_DIR / "model" / filename
        if not path.exists():
            path = BASE_DIR / filename

        if path.exists():
            try:
                models[label] = joblib.load(path)
            except Exception:
                pass

    return models

# Melakukan Load Model dari File Pickle
all_models = load_all_models()
house_price_pipeline = all_models.get("Best Pipeline Model", None)

# Inisialisasi Session State untuk Data Prediksi
if "input_df" not in st.session_state:
    st.session_state.input_df = None
if "results_df" not in st.session_state:
    st.session_state.results_df = None

# Membuat Isi Tab "Model Prediction"
with tab_predict:
    st.header("🏠 House Price Prediction")
    st.write(
        "Upload the house price dataset as a CSV file to automatically run the house price prediction pipeline."
    )

    st.link_button(
        "📖 Dataset Format Guideline",
        "https://docs.google.com/spreadsheets/d/1rjtwX9AT5IUglK_uHImijVwwnVb-sKH32Uss1Q3Kzho/edit?usp=sharing",
        type="secondary",
    )

    st.divider()

    # Inisialisasi State di Awal untuk Mencegah AttributeError
    if "input_df" not in st.session_state:
        st.session_state.input_df = None
    if "results_df" not in st.session_state:
        st.session_state.results_df = None
    if "last_uploaded" not in st.session_state:
        st.session_state.last_uploaded = None

    # Membuat Tempat Upload Dataset
    with st.container(border=True):
        st.subheader("📥 Dataset Input")
        st.caption("**Ensure the uploaded CSV file complies with the dataset format guideline!**")

        col_upload, col_template = st.columns(2, vertical_alignment="bottom")

        with col_upload:
            uploaded_file = st.file_uploader(
                "Upload File CSV",
                type=["csv"],
                label_visibility="collapsed",
            )

        with col_template:
            use_template = st.button(
                "📄 Try with Example Dataset",
                use_container_width=True,
            )

        if uploaded_file is not None:
            if st.session_state.get("last_uploaded") != uploaded_file.name:
                st.session_state.input_df = pd.read_csv(uploaded_file)
                st.session_state.results_df = None
                st.session_state.last_uploaded = uploaded_file.name
                st.toast("CSV dataset loaded successfully!", icon="✅")
        else:
            st.session_state.last_uploaded = None

        if use_template:
            test_path = BASE_DIR / "test.csv"
            if not test_path.exists():
                test_path = BASE_DIR / "data" / "test.csv"

            if test_path.exists():
                st.session_state.input_df = pd.read_csv(test_path)
                st.session_state.results_df = None
                st.session_state.last_uploaded = None
                st.toast("Example dataset (test.csv) loaded!", icon="✅")
            else:
                st.error("File `test.csv` was not found in the project directory.")

        input_df = st.session_state.input_df

        if input_df is not None:
            st.write("---")
            st.markdown(
                f"**Preview Dataset Input** (`{input_df.shape[0]}` rows × `{input_df.shape[1]}` columns):"
            )
            st.dataframe(
                input_df.head(5),
                use_container_width=True,
                height=180,
            )

    # Membuat Tombol Trigger Pipeline Prediksi
    run_prediction = st.button(
        "🚀 Run Pipeline For House Price Prediction",
        type="primary",
        use_container_width=True,
    )

    if run_prediction:
        if input_df is None:
            st.warning("⚠️ Please upload a CSV file or load the example dataset first.")
        elif house_price_pipeline is None:
            st.error(
                "❌ Main inference pipeline model ('best_house_price_model_predict.pkl') was not found."
            )
        else:
            with st.spinner("Executing machine learning prediction pipeline..."):
                drop_cols = [c for c in ["Id", "SalePrice"] if c in input_df.columns]
                X_input = input_df.drop(columns=drop_cols)

                predicted_raw = house_price_pipeline.predict(X_input)
                if np.mean(predicted_raw) < 20:
                    predicted_price = np.expm1(predicted_raw)
                else:
                    predicted_price = predicted_raw

                res_df = input_df.copy()
                res_df["Predicted_SalePrice"] = predicted_price
                st.session_state.results_df = res_df

                st.success("✅ Prediction pipeline completed successfully!")

    # Menampilkan Hasil Prediksi & Export CSV
    if st.session_state.results_df is not None:
        st.divider()
        st.subheader("💵 Prediction Results")

        preds = st.session_state.results_df["Predicted_SalePrice"]

        with st.container(border=True):
            m1, m2, m3 = st.columns(3)
            m1.metric("Average Estimated Price", f"${preds.mean():,.2f}")
            m2.metric("Minimum Estimated Price", f"${preds.min():,.2f}")
            m3.metric("Maximum Estimated Price", f"${preds.max():,.2f}")

        with st.container(border=True):
            st.markdown("### 💾 Prediction Output Dataset")

            base_cols = ["Id"] if "Id" in st.session_state.results_df.columns else []
            if "SalePrice" in st.session_state.results_df.columns:
                base_cols.append("SalePrice")
            base_cols.append("Predicted_SalePrice")

            st.dataframe(
                st.session_state.results_df[base_cols],
                use_container_width=True,
                height=300,
            )

            csv_download = (
                st.session_state.results_df[base_cols]
                .to_csv(index=False)
                .encode("utf-8-sig")
            )

            st.download_button(
                label="📤 Download Full Results as CSV",
                data=csv_download,
                file_name="house_price_prediction_results.csv",
                mime="text/csv",
                type="primary",
                use_container_width=True,
            )


# Membuat Function untuk Mengambil Feature Importance dari Pipeline
def get_top_features(pipeline, top_n=5):
    try:
        # Ekstrak Model & Preprocessor dari Pipeline
        if hasattr(pipeline, "named_steps"):
            model = pipeline.steps[-1][1]
            preprocessor = pipeline.named_steps.get("preprocessor", None)

            if preprocessor and hasattr(preprocessor, "get_feature_names_out"):
                feature_names = preprocessor.get_feature_names_out()
            else:
                feature_names = getattr(model, "feature_names_in_", None)
        else:
            model = pipeline
            feature_names = getattr(model, "feature_names_in_", None)

        # Ambil Feature Importance dari Model 
        if hasattr(model, "feature_importances_"):
            importances = model.feature_importances_
        elif hasattr(model, "coef_"):
            coefs = model.coef_
            if coefs.ndim > 1:
                coefs = coefs.ravel()
            importances = np.abs(coefs)
        else:
            return None

        if feature_names is None or len(feature_names) != len(importances):
            feature_names = [f"Feature {i}" for i in range(len(importances))]

        # Buat DataFrame & Rapikan Nama Kolom
        df_feat = pd.DataFrame(
            {"Feature": feature_names, "Importance": importances}
        )

        df_feat["Feature"] = (
            df_feat["Feature"]
            .str.replace(r"^(num|cat)__", "", regex=True)
            .str.replace(r"^remainder__", "", regex=True)
        )
        df_feat = df_feat.groupby("Feature", as_index=False)["Importance"].sum()

        # Ambil Top N dan urutkan Ascending untuk Plotly Horizontal Bar
        df_feat = df_feat.sort_values(
            by="Importance", ascending=False
        ).head(top_n)

        return df_feat.sort_values(by="Importance", ascending=True)

    except Exception:
        return None

# Membuat Isi Tab "Data Visualization & Model Performance"
with tab_visual:
    st.header("📊 Data Visualization & Model Performance")

    # Load Data Train dari Sistem
    train_path = BASE_DIR / "train.csv"
    if not train_path.exists():
        train_path = BASE_DIR / "data" / "train.csv"

    train_df = pd.read_csv(train_path) if train_path.exists() else None

    # Membuat 2 Subtab untuk Visualisasi EDA & Evaluasi Model
    subtab_eda, subtab_eval = st.tabs(
        ["🔎 Exploratory Data Analysis Visualization", "🎯 Model Evaluation & Performance"]
    )

   # Membuat Isi Subtab "Exploratory Data Analysis Visualization"
    with subtab_eda:
        if train_df is not None:
            # Menyiapkan copy dataframe agar tidak mengubah dataframe utama
            eda_df = train_df.copy()

            # Mengubah Tipe Data "MSSubClass" menjadi String untuk Berubah Menjadi Kolom Kategorikal
            if "MSSubClass" in eda_df.columns:
                eda_df["MSSubClass"] = eda_df["MSSubClass"].astype(str)

            # Menentukan Kolom Numerik & Kategorikal 
            num_cols = [
                col
                for col in eda_df.select_dtypes(include=[np.number]).columns
                if col.lower() != "id"
            ]
            cat_cols = [
                col
                for col in eda_df.select_dtypes(
                    include=["object", "category"]
                ).columns
                if col.lower() != "id"
            ]

            # Menampilkan Preview Data Train & Membuat Tombol Download Data Train
            with st.container(border=True):
                st.subheader("Preview Data Train")
                st.markdown(
                    f"**The dataset used to train the model:** "
                    f"(`{train_df.shape[0]:,}` rows, `{train_df.shape[1]}` columns)"
                )

                st.dataframe(train_df.head(), use_container_width=True)

                csv_train = train_df.to_csv(index=False).encode("utf-8")

                st.download_button(
                    label="📥 Download Full Data Train (.csv)",
                    data=csv_train,
                    file_name="train_data.csv",
                    mime="text/csv",
                )

            st.write("")  

            # Membuat dan Menampilkan Visualisasi "Distribution of Numerical Column"
            with st.container(border=True):
                st.subheader("1. Distribution of Numerical Column")

                selected_num = st.selectbox(
                    "Select Numerical Column:",
                    num_cols,
                    index=(
                        num_cols.index("SalePrice")
                        if "SalePrice" in num_cols
                        else 0
                    ),
                    key="select_num",
                )

                col_num1, col_num2 = st.columns(2)

                with col_num1:
                    fig_hist = px.histogram(
                        train_df,
                        x=selected_num,
                        title=f"Histogram: {selected_num}",
                        color_discrete_sequence=["#1f77b4"],
                    )
                    fig_hist.update_layout(
                        margin=dict(l=60, r=20, t=50, b=60),
                        xaxis=dict(
                            title=dict(text=selected_num, standoff=15),
                            automargin=True,
                        ),
                        yaxis=dict(
                            title=dict(text="Frequency", standoff=15),
                            automargin=True,
                        ),
                        height=380,
                    )
                    st.plotly_chart(fig_hist, use_container_width=True, theme=None)

                with col_num2:
                    fig_box = px.box(
                        train_df,
                        y=selected_num,
                        title=f"Boxplot: {selected_num}",
                        color_discrete_sequence=["#d97706"],
                    )
                    fig_box.update_layout(
                        margin=dict(l=80, r=20, t=50, b=60),
                        xaxis=dict(automargin=True),
                        yaxis=dict(
                            title=dict(text=selected_num, standoff=15),
                            automargin=True,
                        ),
                        height=380,
                    )
                    st.plotly_chart(fig_box, use_container_width=True, theme=None)

            st.write("") 

            # Membuat dan Menampilkan Visualisasi "Top 5 Categories Distribution"
            with st.container(border=True):
                st.subheader("2. Top 5 Categories Distribution")

                if cat_cols:
                    selected_cat = st.selectbox(
                    "Select Categorical Column:", cat_cols, key="select_cat"
                    )

                    # Ambil 5 data terbanyak
                    cat_counts = (
                        train_df[selected_cat]
                        .astype(str)  
                        .value_counts()
                        .head(5)
                        .reset_index()
                    )
                    cat_counts.columns = [selected_cat, "Frequency"]

                    # Skala Gradasi Kuning-Keemasan
                    yellow_scale = ["#FACC15", "#854D0E"]

                    fig_bar = px.bar(
                        cat_counts,
                        x="Frequency",
                        y=selected_cat,
                        orientation="h",
                        text="Frequency",
                        color="Frequency",
                        title=f"Top 5 Categories: {selected_cat}",
                        color_continuous_scale=yellow_scale,  
                    )

                    fig_bar.update_traces(textposition="outside", cliponaxis=False)
                    fig_bar.update_layout(
                        coloraxis_showscale=False,  
                        margin=dict(l=120, r=60, t=50, b=50),
                        xaxis=dict(
                            title=dict(text="Frequency", standoff=15),
                            automargin=True,
                        ),
                        yaxis=dict(
                            title=dict(text=selected_cat, standoff=15),
                            automargin=True,
                            type="category",
                            autorange="reversed",  
                        ),
                        height=400,
                    )

                    st.plotly_chart(fig_bar, use_container_width=True, theme=None)
                else:
                    st.info("No categorical column found in the dataset.")

            st.write("")

            # Membuat dan Menampilkan Visualisasi "Correlation Between Numerical Columns"
            with st.container(border=True):
                st.subheader("3. Correlation Between Numerical Columns")

                col_scat1, col_scat2 = st.columns(2)
                with col_scat1:
                    x_num = st.selectbox(
                        "Select Numerical Column for X-axis:",
                        num_cols,
                        index=(
                            num_cols.index("GrLivArea")
                            if "GrLivArea" in num_cols
                            else 0
                        ),
                        key="scat_x",
                    )
                with col_scat2:
                    y_num = st.selectbox(
                        "Select Numerical Column for Y-axis:",
                        num_cols,
                        index=(
                            num_cols.index("SalePrice")
                            if "SalePrice" in num_cols
                            else (1 if len(num_cols) > 1 else 0)
                        ),
                        key="scat_y",
                    )

                fig_scat = px.scatter(
                    train_df,
                    x=x_num,
                    y=y_num,
                    opacity=0.6,
                    title=f"Scatterplot: {x_num} vs {y_num}",
                    color_discrete_sequence=["#2ca02c"],
                    trendline="ols",
                    trendline_color_override="#d62728",
                )
                fig_scat.update_layout(
                    title=dict(
                        text=f"<b>Scatterplot: {x_num} vs {y_num}</b>",
                        x=0,
                        font=dict(size=16),
                    ),
                    margin=dict(l=70, r=30, t=50, b=60),
                    xaxis=dict(
                        title=dict(text=x_num, standoff=15),
                        automargin=True,
                    ),
                    yaxis=dict(
                        title=dict(text=y_num, standoff=15),
                        automargin=True,
                    ),
                    height=400,
                )
                st.plotly_chart(fig_scat, use_container_width=True, theme=None)

            st.write("")  

            # Membuat dan Menampilkan Visualisasi "Distribution of Categorical Column by Numerical Column"
            with st.container(border=True):
                st.subheader("4. Distribution of Categorical Column by Numerical Column")

                if cat_cols:
                    col_boxcat1, col_boxcat2 = st.columns(2)
                    with col_boxcat1:
                        cat_group = st.selectbox(
                            "Select Categorical Column for X-axis:",
                            cat_cols,
                            key="boxcat_x",
                        )
                    with col_boxcat2:
                        num_target = st.selectbox(
                            "Select Numerical Column for Y-axis:",
                            num_cols,
                            index=(
                                num_cols.index("SalePrice")
                                if "SalePrice" in num_cols
                                else 0
                            ),
                            key="boxcat_y",
                        )

                    fig_boxcat = px.box(
                        train_df,
                        x=cat_group,
                        y=num_target,
                        color=cat_group,
                        title=f"Boxplot: {num_target} by {cat_group}",
                        color_discrete_sequence=px.colors.qualitative.Plotly,
                    )
                    fig_boxcat.update_layout(
                        title=dict(
                            text=f"<b>Boxplot: {num_target} by {cat_group}</b>",
                            x=0,
                            font=dict(size=16),
                        ),
                        showlegend=False,
                        margin=dict(l=70, r=30, t=50, b=60),
                        xaxis=dict(
                            title=dict(text=cat_group, standoff=15),
                            automargin=True,
                        ),
                        yaxis=dict(
                            title=dict(text=num_target, standoff=15),
                            automargin=True,
                        ),
                        height=400,
                    )
                    st.plotly_chart(fig_boxcat, use_container_width=True, theme=None)
                else:
                    st.info(
                        "No categorical column found to generate categorical"
                        " boxplots."
                    )

        else:
            st.warning(
                "⚠️ The `train.csv` dataset was not found in the project directory."
            )

    # Membuat Isi Subtab "Model Evaluation & Performance"
    with subtab_eval:

        # Membuat Filter agar Tidak Menampilkan Opsi "best pipeline model"
        filtered_models = {
            name: model
            for name, model in all_models.items()
            if "best pipeline" not in name.lower() and "pipeline" not in name.lower()
        }

        if not filtered_models:
            st.error(
                "❌ No individual `.pkl` model files were successfully loaded from the folder."
            )
        elif train_df is None or "SalePrice" not in train_df.columns:
            st.warning(
                "⚠️ The internal `train.csv` file is required to calculate the R², RMSE, MAE, and MAPE metrics.."
            )
        else:

            # Menentukan Data Validasi
            drop_cols = [
                c
                for c in ["Id", "SalePrice", "Predicted_SalePrice"]
                if c in train_df.columns
            ]
            X = train_df.drop(columns=drop_cols)
            y = train_df["SalePrice"]

            X_train, X_val, y_train, y_val = train_test_split(
                X, y, test_size=0.2, random_state=42
            )

            # Melakukan Evaluasi Model & Menampilkan Hasil Metrik Evaluasi Model
            with st.container(border=True):
                st.subheader(" 1. Model Evaluation")
                st.caption("**The dataset used for model evaluation consists of 20% of the data train**")
                selected_model_name = st.selectbox(
                    "Select Machine Learning Model:",
                    list(filtered_models.keys()),
                    key="select_eval_model",
                )

                chosen_model = filtered_models[selected_model_name]

                try:
                    raw_preds = chosen_model.predict(X_val)
                    y_pred = (
                        np.expm1(raw_preds) if np.mean(raw_preds) < 20 else raw_preds
                    )

                    r2_val = r2_score(y_val, y_pred)
                    mae_val = mean_absolute_error(y_val, y_pred)
                    mape_val = mean_absolute_percentage_error(y_val, y_pred) * 100
                    rmse_val = np.sqrt(mean_squared_error(y_val, y_pred))
                    residuals = y_val - y_pred

                    st.write("---")

                    m1, m2, m3, m4 = st.columns(4)
                    m1.metric("R² Score", f"{r2_val:.4f}")
                    m2.metric("MAE", f"${mae_val:,.2f}")
                    m3.metric("MAPE", f"{mape_val:.2f}%")
                    m4.metric("RMSE", f"${rmse_val:,.2f}")

                except Exception as e:
                    st.error(
                        f"Failed to evaluate the model {selected_model_name}: {str(e)}"
                    )

            st.write("")  

            # Menampilkan Top 5 Fitur Paling Berpengaruh pada Model yang Dipilih
            df_top_features = get_top_features(chosen_model, top_n=5)
            if df_top_features is not None:
                with st.container(border=True):
                    st.subheader("2. Top 5 Features that Influence House Price Estimation")
                    model_obj = (
                        chosen_model[-1]
                        if hasattr(chosen_model, "steps") or hasattr(chosen_model, "named_steps")
                        else chosen_model
                    )
                    x_label = (
                        "Absolute Coefficient Weight"
                        if hasattr(model_obj, "coef_")
                        else "Importance Score"
                    )

                    fig_importance = px.bar(
                        df_top_features,
                        x="Importance",
                        y="Feature",
                        orientation="h",
                        text_auto=".4f",
                        color="Importance",
                        color_continuous_scale="Greens",
                    )
                    fig_importance.update_traces(
                        textposition="outside",
                        cliponaxis=False,
                    )
                    fig_importance.update_layout(
                        showlegend=False,
                        coloraxis_showscale=False,
                        margin=dict(l=120, r=60, t=30, b=40),
                        xaxis=dict(
                            title=dict(text=x_label, standoff=10),
                            automargin=True,
                        ),
                        yaxis=dict(
                            title=dict(text="Feature Name", standoff=10),
                            automargin=True,
                        ),
                        height=300,
                    )
                    st.plotly_chart(fig_importance, use_container_width=True, theme=None)

                st.write("")  

            # Membuat dan Menampilkan Visualisasi "Actual vs Predicted Price" dan "Residual Plot" di "Performance Diagnostic Charts"
            if "y_pred" in locals():
                with st.container(border=True):
                    st.subheader("3. Performance Diagnostic Charts")

                    col_p1, col_p2 = st.columns(2)

                    with col_p1:
                        fig_act = px.scatter(
                            x=y_val,
                            y=y_pred,
                            opacity=0.6,
                            title="Actual vs Predicted Price",
                            color_discrete_sequence=["#1f77b4"],
                        )

                        min_val = min(y_val.min(), y_pred.min())
                        max_val = max(y_val.max(), y_pred.max())
                        fig_act.add_shape(
                            type="line",
                            x0=min_val,
                            y0=min_val,
                            x1=max_val,
                            y1=max_val,
                            line=dict(color="#d62728", width=2, dash="dash"),
                        )

                        fig_act.update_layout(
                            margin=dict(l=80, r=20, t=50, b=60),
                            xaxis=dict(
                                title=dict(text="Actual Price ($)", standoff=15),
                                automargin=True,
                            ),
                            yaxis=dict(
                                title=dict(text="Predicted Price ($)", standoff=15),
                                automargin=False,  
                                side="left",
                            ),
                            height=380,
                        )
                        st.plotly_chart(fig_act, use_container_width=True, theme=None)

            
                    with col_p2:
                        fig_res = px.scatter(
                            x=y_pred,
                            y=residuals,
                            opacity=0.6,
                            title="Residual Plot (Errors)",
                            color_discrete_sequence=["#FF7F0E"],
                        )

                        fig_res.add_hline(
                            y=0,
                            line_dash="dash",
                            line_color="#D62728",
                            line_width=2,
                        )

                        fig_res.update_layout(
                            margin=dict(l=80, r=20, t=50, b=60),  
                            xaxis=dict(
                                title=dict(text="Predicted Price ($)", standoff=15),
                                automargin=True,
                            ),
                            yaxis=dict(
                                title=dict(text="Residual Error ($)", standoff=15),
                                automargin=False,  
                                side="left",
                                zeroline=False,
                            ),
                            height=380,
                        )
                        st.plotly_chart(fig_res, use_container_width=True, theme=None)