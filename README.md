# 🚀 BizPredict AI
### Startup Valuation & Business Intelligence Platform

**Predict Smarter. Analyze Better.**

BizPredict AI is a machine learning-powered web application designed to analyze startup performance, explore financial trends, and predict startup valuations using financial and operational characteristics.

The platform combines data analytics, interactive visualizations, business intelligence, and machine learning in a Streamlit dashboard.

## 🌐 Live Demo

🚀 **Try BizPredict AI:**

[Launch Application](https://bizpredict-ai.streamlit.app/)

## ✨ Key Features

### 📊 1. Interactive Overview Dashboard

- Analyze startup funding, valuation, and revenue.
- Explore startup distributions by industry and region.
- Filter startups by industry, region, and profitability.
- Visualize funding and valuation relationships.
- Compare revenue and valuation trends.
- Identify the highest-valued startups.
- Download filtered startup datasets as CSV files.

### 📈 2. Business Intelligence

- Analyze funding across industries.
- Compare average valuations across regions.
- Explore revenue and valuation relationships.
- Analyze industry and regional performance.
- Study startup founding-year trends.
- Examine profitability across industries and regions.
- Explore financial correlations using interactive heatmaps.
- Export industry and regional performance reports.

### 🤖 3. Machine Learning Valuation Prediction

- Predict startup valuations using Linear Regression.
- Accept financial and operational inputs.
- Automatically preprocess input features.
- Validate inputs against observed dataset ranges.
- Compare predicted valuations with industry and regional averages.
- Maintain prediction history during the session.
- Download prediction history as a CSV file.
- Display warnings for negative predictions and unusual inputs.

### 🎯 4. Model Performance

- Display recorded model evaluation metrics.
- Explain R², Mean Absolute Error, and Root Mean Squared Error.
- Describe the preprocessing pipeline.
- Communicate model limitations and prediction reliability.

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Model Persistence | Joblib |
| Web Application | Streamlit |
| Interactive Visualization | Plotly |
| Data Visualization | Matplotlib, Seaborn |
| Version Control | Git, GitHub |
| Deployment | Streamlit Community Cloud |

## 🧠 Machine Learning Approach

BizPredict AI uses a trained **Linear Regression** model to estimate startup valuations based on financial and operational features.

### Data Preprocessing

The model pipeline includes:

- **One-Hot Encoding:** Converts categorical features into numerical representations.
- **Standard Scaling:** Standardizes numerical features.
- **Binary Feature Handling:** Represents profitability as 0 or 1.

### Input Features

The model uses the following nine features:

1. Industry
2. Funding Rounds
3. Funding Amount (Cr INR)
4. Revenue (Cr INR)
5. Number of Employees
6. Market Share (%)
7. Profitability
8. Year Founded
9. Region

### Model Evaluation

The model was evaluated using an 80/20 train-test split.

| Evaluation Metric | Test Result |
|---|---:|
| R² Score | 0.6715 |
| Mean Absolute Error (MAE) | ₹3,840.40 crore |
| Root Mean Squared Error (RMSE) | ₹5,111.06 crore |

**Understanding the Results**

- **R² Score:** The model explains approximately 67.15% of the variation in valuation within the held-out test dataset.
- **MAE:** The average absolute difference between predicted and actual valuations is approximately ₹3,840.40 crore.
- **RMSE:** The root mean squared prediction error is approximately ₹5,111.06 crore, with larger errors receiving greater weight.

These metrics are from the recorded evaluation of the trained model. They are not recalculated by the Streamlit application.

The prediction errors are substantial. The results should be treated as experimental performance on synthetic data, not evidence of real-world startup valuation accuracy.

## 📁 Project Structure

```text
BizPredict-AI/
│
├── app.py
├── startup_data_india.csv
├── requirements.txt
├── README.md
├── PROJECT.ipynb
├── convert_currency.py
│
└── models/
    └── startup_valuation_model_india.pkl
```

**Note:** This is the intended project structure. The files listed should match the files actually included in your published GitHub repository.

## ⚙️ Installation and Local Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/mohammedhussainali1346/BizPredict-AI.git
```

### Step 2: Navigate to the Project Directory

```bash
cd BizPredict-AI
```

### Step 3: Create a Virtual Environment

```bash
python -m venv bizpredictvenv
```

### Step 4: Activate the Environment

**Windows PowerShell:**

```powershell
.\bizpredictvenv\Scripts\Activate.ps1
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Run the Application

```bash
streamlit run app.py
```

The application should open in your browser.

## 📊 Dataset Information

The project uses a synthetic dataset containing 500 startup records.

The original financial columns were expressed in millions of US dollars. For the INR version, the financial values were converted to Indian rupee crores using an illustrative exchange rate of ₹90 per USD.

The conversion used the following relationship:

**INR Crores = USD Millions × 9**

The conversion changes the currency units and numerical scale. It does not transform the dataset into verified Indian startup data.

The records remain synthetic and global in nature. Consequently, the model's predictions should be interpreted as experimental estimates rather than verified business valuations.

## ⚠️ Model Limitations

- The dataset is synthetic and limited to 500 records.
- The dataset is not verified Indian startup market data.
- The currency conversion uses an illustrative exchange rate.
- Linear Regression may produce negative valuation estimates.
- Predictions outside the observed training ranges may be unreliable.
- The model does not account for every factor affecting startup valuation.
- The model's recorded performance does not establish real-world accuracy.
- Predictions should not be used as investment advice or as substitutes for professional business valuation.

## 🎯 Project Objectives

- Apply machine learning to a business analytics problem.
- Develop an interactive startup analytics dashboard.
- Explore financial patterns through data visualization.
- Build an end-to-end valuation prediction workflow.
- Implement data preprocessing and feature encoding.
- Evaluate model performance using regression metrics.
- Deploy a Python application using Streamlit.
- Integrate data analytics, machine learning, and web development.

## 🚀 Future Enhancements

- Compare additional regression algorithms.
- Perform systematic hyperparameter tuning.
- Integrate verified real-world startup datasets.
- Add feature importance and model explainability.
- Improve handling of negative valuation predictions.
- Introduce persistent prediction history.
- Generate downloadable PDF business intelligence reports.
- Evaluate model performance on independent real-world data.

## 👨‍💻 Author

Developed as a machine learning and business intelligence portfolio project.

**GitHub Repository:**

[BizPredict AI — GitHub](https://github.com/mohammedhussainali1346/BizPredict-AI)

**Live Application:**

[Launch BizPredict AI](https://bizpredict-ai.streamlit.app/)

## 📌 Disclaimer

BizPredict AI is an educational and experimental project.

Its predictions are statistical estimates based on a synthetic dataset. They are not verified market valuations, financial advice, or recommendations to invest in any business.

---

**BizPredict AI — Predict Smarter. Analyze Better.**