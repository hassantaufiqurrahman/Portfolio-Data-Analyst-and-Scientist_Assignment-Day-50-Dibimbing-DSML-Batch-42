# Assignment Portofolio Building with Streamlit_Dibimbing DSML Batch 42_Hassan Taufiqurrahman

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/hassantaufiqurrahman/Portfolio-Data-Analyst-and-Scientist_Assignment-Day-50-Dibimbing-DSML-Batch-42))
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/hassantaufiqurrahman)

🤖 **Live App Demo:** [Hassan Taufiqurrahman's Data Analysis & Science Portfolio](https://hassantaufiqurrahman-portfoliodataanalysisandscience.streamlit.app/)

## 📌 Features

- **About Me:** Description of background information regarding education, employment, organizational involvement, and skills.
- **My Projects:** List of data analysis and data science projects completed.
- **Model Prediction:** House price prediction simulation using a machine learning model.
- **Data Visualization & Model Performance:** Simulation of exploratory data analysis visualization and machine learning model evaluation.  

---

## 🛠️ Tech Stack & Libraries

- **Language:** Python
- **Framework UI:** Streamlit
- **Machine Learning:** Scikit-Learn
- **Data Manipulation:** Pandas, NumPy
- **Data Visualization:** Plotly

---

## 📁 Repository Structure

```text
.
├── data/
│   ├── train.csv         # Data Train
│   └── test.csv          # Data Test for Example Dataset in "Dataset Input"
├── model/                                   # List of Machine Learning Models Used in the Streamlit App
│   ├── best_house_price_model_predict.pkl   # Best Model Based On Result of "house_price_prediction.py"
│   ├── model_lasso.pkl                      # Lasso Regression
│   ├── model_lr.pkl                         # Linear Regression
│   ├── model_rf.pkl                         # Random Forest Regressor  
│   └── model_ridge.pkl                      # Ridge Regression
├── picture/                    # Image Assets
├── app.py                      # Main Script Streamlit App
├── house_price_prediction.py   # Script Model Training & Evaluation
├── requirements.txt            # List of library dependencies
└── README.md
