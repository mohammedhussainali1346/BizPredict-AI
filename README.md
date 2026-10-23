# 🚀 Global Startup Valuation Prediction & Business Intelligence System

An end-to-end Machine Learning and Business Intelligence application that analyzes startup data, explores financial performance, and predicts startup valuations using Linear Regression.

## 📌 Project Overview

This project combines Machine Learning, data analysis, and interactive visualization in a Streamlit web application.

Users can explore startup funding, revenue, valuation, profitability, industry performance, and regional trends. They can also enter startup characteristics to generate estimated valuations.

**Dataset:** 500 startup records with 12 columns.

> Note: The dataset is used for educational and analytical purposes. Predictions are estimates and should not be treated as verified market valuations or financial advice.

## ✨ Features

### 1. Overview Dashboard
- Key performance indicators
- Industry and regional analysis
- Profitability filtering
- Interactive visualizations
- Filtered dataset export to CSV

### 2. Business Intelligence
- Industry performance analysis
- Regional performance analysis
- Founding-year and startup growth analysis
- Profitability analysis
- Financial correlation heatmap
- Industry and regional report exports

### 3. Startup Valuation Prediction
- Machine Learning-based valuation estimates
- Input validation warnings
- Industry and regional valuation comparisons
- Prediction history
- Prediction history export
- Model process and limitation explanations

### 4. Model Performance
- R-squared (R²)
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Plotly
- Matplotlib
- Seaborn
- Joblib

## 🤖 Machine Learning Model

The project uses a trained Scikit-learn Pipeline containing:

- One-Hot Encoding for categorical features
- Standard Scaling for numerical features
- Linear Regression for valuation prediction

### Input Features

- Industry
- Funding Rounds
- Funding Amount
- Revenue
- Employees
- Market Share
- Profitability
- Year Founded
- Region

### Model Evaluation

Previously recorded test-set results:

| Metric | Result |
|---|---:|
| R² Score | 0.6715 |
| Mean Absolute Error | $426.71 million |
| Root Mean Squared Error | $567.90 million |

These are previously recorded evaluation results, not a guarantee of future performance. The model's accuracy depends on the dataset's quality and representativeness.

## 📂 Project Structure

```text
Project 02/
├── .streamlit/
│   └── config.toml
├── models/
│   └── startup_valuation_model.pkl
├── app.py
├── startup_data.csv
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd <YOUR_REPOSITORY_FOLDER>
```

Replace the placeholders with your actual GitHub repository URL and folder name.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python -m streamlit run app.py
```

The application will open in your browser.

## 🚀 Deployment

The application can be deployed using Streamlit Community Cloud by connecting the GitHub repository and selecting `app.py` as the application entry point.

Ensure the dataset, trained model, and required dependencies are available in the repository.

## ⚠️ Limitations

- Predictions are estimates, not verified startup valuations.
- Dataset patterns may not represent the entire startup ecosystem.
- The model may produce inaccurate or negative predictions.
- Industry and regional averages describe the available dataset only.
- Correlation does not establish causation.

## 👨‍💻 Project Purpose

This project demonstrates practical skills in:

- Data analysis and visualization
- Exploratory Data Analysis (EDA)
- Machine Learning pipelines
- Regression modeling
- Business Intelligence
- Interactive dashboard development
- Data export and reporting
- Application deployment

---

**Built with Python, Machine Learning, and Streamlit.**