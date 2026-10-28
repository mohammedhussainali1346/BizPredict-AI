import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import plotly.io as pio

# --------------------------------------------------
# CUSTOM PLOTLY THEME
# --------------------------------------------------

pio.templates.default = "plotly_dark"

CHART_COLORS = [
    "#38BDF8",
    "#818CF8",
    "#34D399",
    "#FBBF24",
    "#FB7185",
    "#A78BFA",
    "#22D3EE",
    "#F472B6",
]

px.defaults.color_discrete_sequence = CHART_COLORS
px.defaults.template = "plotly_dark"

# --------------------------------------------------
# REUSABLE CHART DISPLAY FUNCTION
# --------------------------------------------------


def display_chart(fig):

    fig.update_layout(
        paper_bgcolor="#111827",
        plot_bgcolor="#111827",
        font=dict(color="#E2E8F0"),
        title_font=dict(size=18, color="#F8FAFC"),
        margin=dict(l=20, r=20, t=60, b=20),
    )

    st.plotly_chart(fig, use_container_width=True)


from pathlib import Path

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="BizPredict AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)
# --------------------------------------------------
# PROFESSIONAL DASHBOARD STYLING
# --------------------------------------------------

st.markdown(
    """
<style>

/* Main application background */
.stApp {
    background-color: #0B1120;
    color: #E2E8F0;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111827;
    border-right: 1px solid #1E293B;
}

/* Headings */
h1, h2, h3 {
    color: #F8FAFC !important;
    font-family: 'Segoe UI', sans-serif;
}

/* Main title */
h1 {
    font-size: 2.3rem !important;
    font-weight: 700 !important;
}

/* Metric cards */
div[data-testid="stMetric"] {
    background: linear-gradient(135deg, #172554, #1E293B);
    padding: 22px;
    border-radius: 14px;
    border: 1px solid #334155;
}

/* Metric values */
div[data-testid="stMetricValue"] {
    color: #38BDF8;
    font-weight: 700;
}

/* Buttons */
.stButton > button,
.stFormSubmitButton > button {
    background: linear-gradient(90deg, #2563EB, #0891B2);
    color: white;
    border: none;
    border-radius: 10px;
    font-weight: 600;
    padding: 10px 20px;
}

.stButton > button:hover,
.stFormSubmitButton > button:hover {
    background: #1D4ED8;
    color: white;
}

/* Input fields */
div[data-baseweb="input"] {
    border-radius: 10px;
}

/* Horizontal dividers */
hr {
    border-color: #334155;
}

/* Plotly chart containers */
div[data-testid="stPlotlyChart"] {
    background-color: #111827;
    border-radius: 14px;
    padding: 10px;
}

/* Dataframe */
div[data-testid="stDataFrame"] {
    border-radius: 12px;
    overflow: hidden;
}

/* Footer */
.stCaption {
    color: #94A3B8;
}

</style>
""",
    unsafe_allow_html=True,
)

# --------------------------------------------------
# FILE PATHS
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

DATA_PATH = BASE_DIR / "startup_data_india.csv"
MODEL_PATH = BASE_DIR / "models" / "startup_valuation_model_india.pkl"

# --------------------------------------------------
# LOAD DATA AND MODEL
# --------------------------------------------------


@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)


@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


try:
    df = load_data()
    model = load_model()

except Exception as e:
    st.error(f"Error loading project files: {e}")
    st.stop()

# --------------------------------------------------
# PREDICTION HISTORY INITIALIZATION
# --------------------------------------------------

if "prediction_history" not in st.session_state:
    st.session_state.prediction_history = []

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("🚀 Startup Intelligence")

st.sidebar.markdown(
    "Global Startup Valuation Prediction & Business Intelligence System"
)

page = st.sidebar.radio(
    "Navigation",
    [
        "Overview Dashboard",
        "Business Intelligence",
        "Valuation Prediction",
        "Model Performance",
    ],
)

st.sidebar.divider()
st.sidebar.caption("Powered by Machine Learning & Streamlit")
st.sidebar.caption("Financial values shown in ₹ Crores")

# --------------------------------------------------
# PAGE 1: OVERVIEW DASHBOARD
# --------------------------------------------------

if page == "Overview Dashboard":

    st.title("🚀 Global Startup Intelligence Dashboard")

    st.markdown(
        "Explore startup funding, revenue, valuation, "
        "and global business performance."
    )

    st.divider()

    # --------------------------------------------------
    # DASHBOARD FILTERS
    # --------------------------------------------------

    st.subheader("🔎 Dashboard Filters")

    filter_col1, filter_col2, filter_col3 = st.columns(3)

    with filter_col1:
        selected_industries = st.multiselect(
            "Industry",
            options=sorted(df["Industry"].dropna().unique()),
            default=sorted(df["Industry"].dropna().unique()),
            key="overview_industry",
        )

    with filter_col2:
        selected_regions = st.multiselect(
            "Region",
            options=sorted(df["Region"].dropna().unique()),
            default=sorted(df["Region"].dropna().unique()),
            key="overview_region",
        )

    with filter_col3:
        profitability = st.selectbox(
            "Profitability", ["All Startups", "Profitable", "Not Profitable"]
        )

    dashboard_df = df[
        df["Industry"].isin(selected_industries) & df["Region"].isin(selected_regions)
    ].copy()

    if profitability == "Profitable":
        dashboard_df = dashboard_df[dashboard_df["Profitable"] == 1]

    elif profitability == "Not Profitable":
        dashboard_df = dashboard_df[dashboard_df["Profitable"] == 0]

    if dashboard_df.empty:
        st.warning("No startups match the selected filters.")
        st.stop()

    st.divider()

    total_startups = len(dashboard_df)
    total_funding = dashboard_df["Funding Amount (Cr INR)"].sum()
    average_valuation = dashboard_df["Valuation (Cr INR)"].mean()
    average_revenue = dashboard_df["Revenue (Cr INR)"].mean()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Startups", f"{total_startups:,}")
    col2.metric("Total Funding", f"₹{total_funding:,.2f} Cr")
    col3.metric("Average Valuation", f"₹{average_valuation:,.2f} Cr")
    col4.metric("Average Revenue", f"₹{average_revenue:,.2f} Cr")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Startups by Industry")

        industry_counts = dashboard_df["Industry"].value_counts().reset_index()

        industry_counts.columns = ["Industry", "Count"]

        fig = px.bar(
            industry_counts,
            x="Industry",
            y="Count",
            color="Industry",
            title="Industry Distribution",
        )

        fig.update_layout(
            paper_bgcolor="#111827",
            plot_bgcolor="#111827",
            font=dict(color="#E2E8F0"),
            title_font=dict(size=18, color="#F8FAFC"),
            margin=dict(l=20, r=20, t=60, b=20),
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:

        st.subheader("Startups by Region")

        region_counts = dashboard_df["Region"].value_counts().reset_index()

        region_counts.columns = ["Region", "Count"]

        fig = px.pie(
            region_counts,
            names="Region",
            values="Count",
            title="Regional Distribution",
            hole=0.4,
        )

        fig.update_layout(
            paper_bgcolor="#111827",
            plot_bgcolor="#111827",
            font=dict(color="#E2E8F0"),
            title_font=dict(size=18, color="#F8FAFC"),
            margin=dict(l=20, r=20, t=60, b=20),
        )

        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Startup Dataset")

    st.dataframe(dashboard_df, use_container_width=True, hide_index=True)

    # --------------------------------------------------
    # EXPORT FILTERED DASHBOARD DATA
    # --------------------------------------------------

    st.subheader("📥 Export Dashboard Data")

    csv_data = dashboard_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Filtered Startup Data",
        data=csv_data,
        file_name="filtered_startup_data_india.csv",
        mime="text/csv",
        use_container_width=True,
        key="download_dashboard_data",
    )

    # --------------------------------------------------
    # ADVANCED FINANCIAL ANALYTICS
    # --------------------------------------------------

    st.divider()

    st.header("💰 Advanced Financial Analytics")

    st.markdown(
        "Explore financial relationships, profitability, "
        "and the highest-valued startups."
    )

    # --------------------------------------------------
    # FUNDING VS VALUATION
    # --------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Funding vs Valuation")

        fig = px.scatter(
            dashboard_df,
            x="Funding Amount (Cr INR)",
            y="Valuation (Cr INR)",
            color="Industry",
            hover_name="Startup Name",
            title="Funding and Valuation Relationship",
        )

        display_chart(fig)

    # --------------------------------------------------
    # REVENUE VS VALUATION
    # --------------------------------------------------

    with col2:

        st.subheader("Revenue vs Valuation")

        fig = px.scatter(
            dashboard_df,
            x="Revenue (Cr INR)",
            y="Valuation (Cr INR)",
            color="Region",
            hover_name="Startup Name",
            title="Revenue and Valuation Relationship",
        )

        display_chart(fig)

    # --------------------------------------------------
    # PROFITABILITY DISTRIBUTION
    # --------------------------------------------------

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Profitability Distribution")

        profitability_data = (
            dashboard_df["Profitable"]
            .map({1: "Profitable", 0: "Not Profitable"})
            .value_counts()
            .reset_index()
        )

        profitability_data.columns = ["Profitability", "Count"]

        fig = px.pie(
            profitability_data,
            names="Profitability",
            values="Count",
            hole=0.5,
            title="Startup Profitability Distribution",
        )

        display_chart(fig)

    # --------------------------------------------------
    # TOP 10 STARTUPS
    # --------------------------------------------------

    with col2:

        st.subheader("Top 10 Startups by Valuation")

        top_startups = dashboard_df.nlargest(10, "Valuation (Cr INR)").sort_values(
            "Valuation (Cr INR)"
        )

        fig = px.bar(
            top_startups,
            x="Valuation (Cr INR)",
            y="Startup Name",
            orientation="h",
            color="Valuation (Cr INR)",
            color_continuous_scale="Blues",
            title="Highest-Valued Startups",
        )

        display_chart(fig)

# --------------------------------------------------
# PAGE 2: BUSINESS INTELLIGENCE
# --------------------------------------------------

elif page == "Business Intelligence":

    st.title("📊 Business Intelligence Analytics")

    st.markdown(
        "Analyze startup performance across industries and regions using the converted synthetic dataset."
    )

    st.divider()

    industries = sorted(df["Industry"].dropna().unique())
    regions = sorted(df["Region"].dropna().unique())

    col1, col2 = st.columns(2)

    with col1:
        selected_industries = st.multiselect(
            "Select Industries", industries, default=industries
        )

    with col2:
        selected_regions = st.multiselect("Select Regions", regions, default=regions)

    filtered_df = df[
        df["Industry"].isin(selected_industries) & df["Region"].isin(selected_regions)
    ]

    if filtered_df.empty:
        st.warning("No startups match the selected filters.")
        st.stop()

    st.metric("Filtered Startups", len(filtered_df))

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Funding by Industry")

        funding_data = filtered_df.groupby("Industry", as_index=False)[
            "Funding Amount (Cr INR)"
        ].sum()

        fig = px.bar(
            funding_data,
            x="Industry",
            y="Funding Amount (Cr INR)",
            color="Industry",
            title="Total Funding by Industry",
        )

        fig.update_layout(
            paper_bgcolor="#111827",
            plot_bgcolor="#111827",
            font=dict(color="#E2E8F0"),
            title_font=dict(size=18, color="#F8FAFC"),
            margin=dict(l=20, r=20, t=60, b=20),
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:

        st.subheader("Average Valuation by Region")

        valuation_data = filtered_df.groupby("Region", as_index=False)[
            "Valuation (Cr INR)"
        ].mean()

        fig = px.bar(
            valuation_data,
            x="Region",
            y="Valuation (Cr INR)",
            color="Region",
            title="Average Startup Valuation by Region",
        )

        fig.update_layout(
            paper_bgcolor="#111827",
            plot_bgcolor="#111827",
            font=dict(color="#E2E8F0"),
            title_font=dict(size=18, color="#F8FAFC"),
            margin=dict(l=20, r=20, t=60, b=20),
        )

        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Funding vs Valuation")

    fig = px.scatter(
        filtered_df,
        x="Funding Amount (Cr INR)",
        y="Valuation (Cr INR)",
        color="Industry",
        size="Revenue (Cr INR)",
        hover_name="Startup Name",
        title="Funding and Startup Valuation Relationship",
    )

    fig.update_layout(
        paper_bgcolor="#111827",
        plot_bgcolor="#111827",
        font=dict(color="#E2E8F0"),
        title_font=dict(size=18, color="#F8FAFC"),
        margin=dict(l=20, r=20, t=60, b=20),
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Revenue vs Valuation")

    fig = px.scatter(
        filtered_df,
        x="Revenue (Cr INR)",
        y="Valuation (Cr INR)",
        color="Region",
        hover_name="Startup Name",
        title="Revenue and Valuation Relationship",
    )

    fig.update_layout(
        paper_bgcolor="#111827",
        plot_bgcolor="#111827",
        font=dict(color="#E2E8F0"),
        title_font=dict(size=18, color="#F8FAFC"),
        margin=dict(l=20, r=20, t=60, b=20),
    )

    st.plotly_chart(fig, use_container_width=True)

    # --------------------------------------------------
    # INDUSTRY PERFORMANCE ANALYSIS
    # --------------------------------------------------

    st.divider()

    st.header("🏭 Industry Performance Analysis")

    industry_performance = filtered_df.groupby("Industry", as_index=False).agg(
        {
            "Funding Amount (Cr INR)": "mean",
            "Revenue (Cr INR)": "mean",
            "Valuation (Cr INR)": "mean",
        }
    )

    metric_options = {
        "Average Funding": "Funding Amount (Cr INR)",
        "Average Revenue": "Revenue (Cr INR)",
        "Average Valuation": "Valuation (Cr INR)",
    }

    selected_metric = st.selectbox(
        "Select Performance Metric",
        list(metric_options.keys()),
        key="industry_performance_metric",
    )

    metric_column = metric_options[selected_metric]

    fig = px.bar(
        industry_performance.sort_values(metric_column, ascending=False),
        x="Industry",
        y=metric_column,
        color="Industry",
        title=f"{selected_metric} by Industry",
        text_auto=".2f",
    )

    display_chart(fig)

    st.subheader("Industry Performance Summary")

    st.dataframe(
        industry_performance.round(2), use_container_width=True, hide_index=True
    )

    # --------------------------------------------------
    # REGIONAL PERFORMANCE ANALYSIS
    # --------------------------------------------------

    st.divider()

    st.header("🌍 Regional Performance Analysis")

    regional_performance = (
        filtered_df.groupby("Region", as_index=False)
        .agg(
            {
                "Startup Name": "count",
                "Funding Amount (Cr INR)": "mean",
                "Revenue (Cr INR)": "mean",
                "Valuation (Cr INR)": "mean",
            }
        )
        .rename(columns={"Startup Name": "Startup Count"})
    )

    regional_metric_options = {
        "Startup Count": "Startup Count",
        "Average Funding": "Funding Amount (Cr INR)",
        "Average Revenue": "Revenue (Cr INR)",
        "Average Valuation": "Valuation (Cr INR)",
    }

    selected_regional_metric = st.selectbox(
        "Select Regional Metric",
        list(regional_metric_options.keys()),
        key="regional_performance_metric",
    )

    regional_metric_column = regional_metric_options[selected_regional_metric]

    fig = px.bar(
        regional_performance.sort_values(regional_metric_column, ascending=False),
        x="Region",
        y=regional_metric_column,
        color="Region",
        title=f"{selected_regional_metric} by Region",
        text_auto=".2f",
    )

    display_chart(fig)

    st.subheader("Regional Performance Summary")

    st.dataframe(
        regional_performance.round(2), use_container_width=True, hide_index=True
    )

    # --------------------------------------------------
    # STARTUP GROWTH & FOUNDING-YEAR ANALYSIS
    # --------------------------------------------------

    st.divider()

    st.header("📈 Startup Growth & Founding-Year Analysis")

    st.markdown(
        "Explore startup formation trends, cumulative growth, "
        "and valuation patterns across founding years."
    )

    # Group startups by founding year
    yearly_growth = (
        filtered_df.groupby("Year Founded", as_index=False)
        .agg(
            Startup_Count=("Startup Name", "count"),
            Average_Valuation=("Valuation (Cr INR)", "mean"),
        )
        .sort_values("Year Founded")
    )

    # Calculate cumulative startup count
    yearly_growth["Cumulative_Startups"] = yearly_growth["Startup_Count"].cumsum()

    # --------------------------------------------------
    # CHART 1: STARTUPS FOUNDED BY YEAR
    # --------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Startups Founded by Year")

        fig = px.bar(
            yearly_growth,
            x="Year Founded",
            y="Startup_Count",
            title="Number of Startups Founded Each Year",
            labels={"Startup_Count": "Number of Startups"},
        )

        display_chart(fig)

    # --------------------------------------------------
    # CHART 2: CUMULATIVE STARTUP GROWTH
    # --------------------------------------------------

    with col2:

        st.subheader("Cumulative Startup Growth")

        fig = px.line(
            yearly_growth,
            x="Year Founded",
            y="Cumulative_Startups",
            markers=True,
            title="Cumulative Number of Startups",
            labels={"Cumulative_Startups": "Total Startups"},
        )

        display_chart(fig)

    # --------------------------------------------------
    # CHART 3: AVERAGE VALUATION BY FOUNDING YEAR
    # --------------------------------------------------

    st.subheader("Average Valuation by Founding Year")

    fig = px.line(
        yearly_growth,
        x="Year Founded",
        y="Average_Valuation",
        markers=True,
        title="Average Startup Valuation by Founding Year",
        labels={"Average_Valuation": "Average Valuation (Cr INR)"},
    )

    display_chart(fig)

    # --------------------------------------------------
    # YEARLY GROWTH SUMMARY TABLE
    # --------------------------------------------------

    st.subheader("Yearly Startup Growth Summary")

    st.dataframe(yearly_growth.round(2), use_container_width=True, hide_index=True)

    # --------------------------------------------------
    # ADVANCED PROFITABILITY ANALYSIS
    # --------------------------------------------------

    st.divider()

    st.header("💵 Advanced Profitability Analysis")

    st.markdown(
        "Compare the financial performance of profitable "
        "and non-profitable startups across industries and regions."
    )

    # Create a working copy of the filtered dataset
    profitability_df = filtered_df.copy()

    # Convert numeric profitability values into readable labels
    profitability_df["Profitability Status"] = profitability_df["Profitable"].map(
        {1: "Profitable", 0: "Not Profitable"}
    )

    # --------------------------------------------------
    # CHART 1: FINANCIAL PERFORMANCE BY PROFITABILITY
    # --------------------------------------------------

    st.subheader("Financial Performance by Profitability")

    profitability_performance = profitability_df.groupby(
        "Profitability Status", as_index=False
    ).agg(
        {
            "Funding Amount (Cr INR)": "mean",
            "Revenue (Cr INR)": "mean",
            "Valuation (Cr INR)": "mean",
        }
    )

    financial_metric_options = {
        "Average Funding": "Funding Amount (Cr INR)",
        "Average Revenue": "Revenue (Cr INR)",
        "Average Valuation": "Valuation (Cr INR)",
    }

    selected_financial_metric = st.selectbox(
        "Select Financial Metric",
        list(financial_metric_options.keys()),
        key="profitability_financial_metric",
    )

    financial_metric_column = financial_metric_options[selected_financial_metric]

    fig = px.bar(
        profitability_performance,
        x="Profitability Status",
        y=financial_metric_column,
        color="Profitability Status",
        title=f"{selected_financial_metric} by Profitability",
        text_auto=".2f",
    )

    display_chart(fig)

    # --------------------------------------------------
    # CHART 2: PROFITABILITY RATE BY INDUSTRY
    # --------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Profitability Rate by Industry")

        industry_profitability = profitability_df.groupby("Industry", as_index=False)[
            "Profitable"
        ].mean()

        industry_profitability["Profitability Rate (%)"] = (
            industry_profitability["Profitable"] * 100
        )

        fig = px.bar(
            industry_profitability.sort_values(
                "Profitability Rate (%)", ascending=False
            ),
            x="Industry",
            y="Profitability Rate (%)",
            color="Industry",
            title="Industry Profitability Rates",
            text_auto=".1f",
        )

        fig.update_yaxes(range=[0, 100])

        display_chart(fig)

    # --------------------------------------------------
    # CHART 3: PROFITABILITY RATE BY REGION
    # --------------------------------------------------

    with col2:

        st.subheader("Profitability Rate by Region")

        regional_profitability = profitability_df.groupby("Region", as_index=False)[
            "Profitable"
        ].mean()

        regional_profitability["Profitability Rate (%)"] = (
            regional_profitability["Profitable"] * 100
        )

        fig = px.bar(
            regional_profitability.sort_values(
                "Profitability Rate (%)", ascending=False
            ),
            x="Region",
            y="Profitability Rate (%)",
            color="Region",
            title="Regional Profitability Rates",
            text_auto=".1f",
        )

        fig.update_yaxes(range=[0, 100])

        display_chart(fig)

    # --------------------------------------------------
    # PROFITABILITY SUMMARY TABLE
    # --------------------------------------------------

    st.subheader("Profitability Performance Summary")

    st.dataframe(
        profitability_performance.round(2), use_container_width=True, hide_index=True
    )

    # --------------------------------------------------
    # FINANCIAL CORRELATION ANALYSIS
    # --------------------------------------------------

    st.divider()

    st.header("🔗 Financial Correlation Analysis")

    st.markdown(
        "Explore relationships between startup funding, "
        "revenue, valuation, market share, and other numerical features."
    )

    # Select numerical features for correlation analysis
    correlation_columns = [
        "Funding Rounds",
        "Funding Amount (Cr INR)",
        "Valuation (Cr INR)",
        "Revenue (Cr INR)",
        "Employees",
        "Market Share (%)",
        "Profitable",
        "Year Founded",
    ]

    # Let the user select the correlation method
    correlation_method = st.selectbox(
        "Select Correlation Method", ["Pearson", "Spearman"], key="correlation_method"
    )

    # Calculate correlation matrix
    correlation_matrix = filtered_df[correlation_columns].corr(
        method=correlation_method.lower()
    )

    # --------------------------------------------------
    # INTERACTIVE CORRELATION HEATMAP
    # --------------------------------------------------

    st.subheader("Correlation Heatmap")

    fig = px.imshow(
        correlation_matrix,
        text_auto=".2f",
        color_continuous_scale="RdBu_r",
        zmin=-1,
        zmax=1,
        aspect="auto",
        title=f"{correlation_method} Correlation Matrix",
    )

    fig.update_layout(height=650, xaxis_title="Features", yaxis_title="Features")

    display_chart(fig)

    # --------------------------------------------------
    # CORRELATION SUMMARY TABLE
    # --------------------------------------------------

    st.subheader("Correlation Matrix Table")

    st.dataframe(correlation_matrix.round(3), use_container_width=True)

    # --------------------------------------------------
    # VALUATION CORRELATION RANKING
    # --------------------------------------------------

    st.subheader("Features Correlated with Startup Valuation")

    valuation_correlations = (
        correlation_matrix["Valuation (Cr INR)"]
        .drop("Valuation (Cr INR)")
        .dropna()
        .sort_values(ascending=False)
        .reset_index()
    )

    valuation_correlations.columns = ["Feature", "Correlation"]

    fig = px.bar(
        valuation_correlations,
        x="Correlation",
        y="Feature",
        orientation="h",
        color="Correlation",
        color_continuous_scale="RdBu_r",
        range_color=[-1, 1],
        title="Feature Correlations with Valuation",
    )

    fig.update_xaxes(range=[-1, 1])

    display_chart(fig)

    # --------------------------------------------------
    # PAGE 3: VALUATION PREDICTION
    # --------------------------------------------------

    # --------------------------------------------------
    # BUSINESS INTELLIGENCE REPORT EXPORT
    # --------------------------------------------------

    st.divider()

    st.header("📥 Business Intelligence Report")

    st.markdown(
        "Generate and download a summary report of "
        "startup financial and business performance."
    )

    if not filtered_df.empty:

        # --------------------------------------------------
        # INDUSTRY SUMMARY
        # --------------------------------------------------

        industry_report = (
            filtered_df.groupby("Industry")
            .agg(
                Startup_Count=("Industry", "size"),
                Total_Funding=("Funding Amount (Cr INR)", "sum"),
                Average_Valuation=("Valuation (Cr INR)", "mean"),
                Average_Revenue=("Revenue (Cr INR)", "mean"),
                Profitability_Rate=("Profitable", "mean"),
            )
            .reset_index()
        )

        industry_report["Profitability_Rate"] *= 100

        # --------------------------------------------------
        # REGIONAL SUMMARY
        # --------------------------------------------------

        regional_report = (
            filtered_df.groupby("Region")
            .agg(
                Startup_Count=("Region", "size"),
                Total_Funding=("Funding Amount (Cr INR)", "sum"),
                Average_Valuation=("Valuation (Cr INR)", "mean"),
                Average_Revenue=("Revenue (Cr INR)", "mean"),
                Profitability_Rate=("Profitable", "mean"),
            )
            .reset_index()
        )

        regional_report["Profitability_Rate"] *= 100

        # --------------------------------------------------
        # DISPLAY REPORTS
        # --------------------------------------------------

        st.subheader("Industry Performance Report")

        st.dataframe(
            industry_report.round(2), use_container_width=True, hide_index=True
        )

        st.subheader("Regional Performance Report")

        st.dataframe(
            regional_report.round(2), use_container_width=True, hide_index=True
        )

        # --------------------------------------------------
        # DOWNLOAD REPORTS
        # --------------------------------------------------

        col1, col2 = st.columns(2)

        with col1:

            st.download_button(
                label="📥 Download Industry Report",
                data=industry_report.round(2).to_csv(index=False).encode("utf-8"),
                file_name="industry_performance_report.csv",
                mime="text/csv",
                use_container_width=True,
                key="download_industry_report",
            )

        with col2:

            st.download_button(
                label="📥 Download Regional Report",
                data=regional_report.round(2).to_csv(index=False).encode("utf-8"),
                file_name="regional_performance_report.csv",
                mime="text/csv",
                use_container_width=True,
                key="download_regional_report",
            )

    else:

        st.warning("No startup data is available for the selected filters.")

elif page == "Valuation Prediction":

    st.title("🤖 AI Startup Valuation Predictor")

    st.markdown(
        "Enter startup information to estimate its valuation "
        "using the trained machine learning model."
    )

    st.divider()

    industries = sorted(df["Industry"].dropna().unique())
    regions = sorted(df["Region"].dropna().unique())

    with st.form("prediction_form"):

        col1, col2 = st.columns(2)

        with col1:

            industry = st.selectbox("Industry", industries)

            funding_rounds = st.number_input(
                "Funding Rounds", min_value=0, value=2, step=1
            )

            funding_amount = st.number_input(
                "Funding Amount (Cr INR)", min_value=0.0, value=100.0
            )

            revenue = st.number_input("Revenue (Cr INR)", min_value=0.0, value=50.0)

            employees = st.number_input(
                "Number of Employees", min_value=0, value=500, step=1
            )

        with col2:

            market_share = st.number_input(
                "Market Share (%)", min_value=0.0, max_value=100.0, value=5.0
            )

            profitable = st.selectbox("Is the Startup Profitable?", ["Yes", "No"])

            year_founded = st.number_input(
                "Year Founded", min_value=1900, max_value=2026, value=2020, step=1
            )

            region = st.selectbox("Region", regions)

        submitted = st.form_submit_button(
            "🚀 Predict Startup Valuation", use_container_width=True
        )

    if submitted:

        input_data = pd.DataFrame(
            [
                {
                    "Industry": industry,
                    "Funding Rounds": funding_rounds,
                    "Funding Amount (Cr INR)": funding_amount,
                    "Revenue (Cr INR)": revenue,
                    "Employees": employees,
                    "Market Share (%)": market_share,
                    "Profitable": 1 if profitable == "Yes" else 0,
                    "Year Founded": year_founded,
                    "Region": region,
                }
            ]
        )

        # --------------------------------------------------
        # INPUT VALIDATION
        # --------------------------------------------------

        numeric_features = [
            "Funding Rounds",
            "Funding Amount (Cr INR)",
            "Revenue (Cr INR)",
            "Employees",
            "Market Share (%)",
            "Year Founded",
        ]

        unusual_inputs = []

        for feature in numeric_features:

            user_value = input_data[feature].iloc[0]

            minimum = df[feature].min()
            maximum = df[feature].max()

            if user_value < minimum or user_value > maximum:

                unusual_inputs.append(
                    f"{feature}: {user_value} " f"(Dataset range: {minimum}–{maximum})"
                )

        if unusual_inputs:

            st.warning(
                "⚠️ Some inputs are outside the ranges "
                "observed in the startup dataset."
            )

            for warning in unusual_inputs:
                st.write(f"• {warning}")

            st.info(
                "The model can still generate a prediction, "
                "but estimates outside the observed data ranges "
                "may be less reliable."
            )

        else:

            st.success(
                "✅ All numerical inputs are within " "the observed dataset ranges."
            )

        try:

            prediction = float(model.predict(input_data)[0])

            # --------------------------------------------------
            # SAVE PREDICTION TO SESSION HISTORY
            # --------------------------------------------------

            from datetime import datetime

            prediction_record = {
                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Industry": industry,
                "Region": region,
                "Funding Rounds": funding_rounds,
                "Funding Amount (Cr INR)": funding_amount,
                "Revenue (Cr INR)": revenue,
                "Employees": employees,
                "Market Share (%)": market_share,
                "Profitable": profitable,
                "Year Founded": year_founded,
                "Predicted Valuation (Cr INR)": round(prediction, 2),
            }

            st.session_state.prediction_history.append(prediction_record)

            st.divider()

            st.subheader("Prediction Result")

            if prediction >= 0:

                st.success("Valuation prediction completed successfully!")

                st.metric("Estimated Startup Valuation", f"₹{prediction:,.2f} Crores")

                st.caption(
                    f"Equivalent to approximately ₹{prediction / 100:,.2f} billion"
                )

                # --------------------------------------------------
                # VALUATION COMPARISON
                # --------------------------------------------------

                st.divider()

                st.subheader("📊 Valuation Comparison")

                # Calculate average valuation for selected industry
                industry_average = df.loc[
                    df["Industry"] == industry, "Valuation (Cr INR)"
                ].mean()

                # Calculate average valuation for selected region
                regional_average = df.loc[
                    df["Region"] == region, "Valuation (Cr INR)"
                ].mean()

                # Display comparison metrics
                col1, col2, col3 = st.columns(3)

                col1.metric("Predicted Valuation", f"₹{prediction:,.2f} Cr")

                col2.metric("Industry Average", f"₹{industry_average:,.2f} Cr")

                col3.metric("Regional Average", f"₹{regional_average:,.2f} Cr")

                # Create comparison dataset
                comparison_df = pd.DataFrame(
                    {
                        "Category": [
                            "Predicted Valuation",
                            "Industry Average",
                            "Regional Average",
                        ],
                        "Valuation (Cr INR)": [
                            prediction,
                            industry_average,
                            regional_average,
                        ],
                    }
                )

                # Create comparison chart
                fig = px.bar(
                    comparison_df,
                    x="Category",
                    y="Valuation (Cr INR)",
                    color="Category",
                    text_auto=".2f",
                    title="Startup Valuation Comparison",
                )

                display_chart(fig)

                # --------------------------------------------------
                # COMPARISON INSIGHTS
                # --------------------------------------------------

                st.subheader("💡 Valuation Insights")

                if industry_average > 0:

                    industry_difference = (
                        (prediction - industry_average) / industry_average
                    ) * 100

                    if industry_difference >= 0:
                        st.success(
                            f"Predicted valuation is "
                            f"{industry_difference:.2f}% higher "
                            f"than the industry average."
                        )
                    else:
                        st.info(
                            f"Predicted valuation is "
                            f"{abs(industry_difference):.2f}% lower "
                            f"than the industry average."
                        )

                if regional_average > 0:

                    regional_difference = (
                        (prediction - regional_average) / regional_average
                    ) * 100

                    if regional_difference >= 0:
                        st.success(
                            f"Predicted valuation is "
                            f"{regional_difference:.2f}% higher "
                            f"than the regional average."
                        )
                    else:
                        st.info(
                            f"Predicted valuation is "
                            f"{abs(regional_difference):.2f}% lower "
                            f"than the regional average."
                        )

            else:

                st.warning(
                    "The model produced a negative valuation estimate. "
                    "This is not a meaningful business valuation and "
                    "indicates a limitation of the linear regression model."
                )

            st.info(
                "This prediction is a statistical estimate based on the "
                "training dataset, not a verified market valuation."
            )

        except Exception as e:
            st.error(f"Prediction failed: {e}")

    # --------------------------------------------------
    # PAGE 4: MODEL PERFORMANCE
    # --------------------------------------------------

    # --------------------------------------------------
    # PREDICTION HISTORY
    # --------------------------------------------------

    st.divider()

    st.header("📜 Prediction History")

    if st.session_state.prediction_history:

        history_df = pd.DataFrame(st.session_state.prediction_history)

        st.metric("Total Predictions", len(history_df))

        st.dataframe(history_df, use_container_width=True, hide_index=True)

        # --------------------------------------------------
        # PREDICTION COMPARISON CHART
        # --------------------------------------------------

        st.subheader("Prediction Comparison")

        chart_df = history_df.copy()

        chart_df["Prediction Number"] = range(1, len(chart_df) + 1)

        fig = px.bar(
            chart_df,
            x="Prediction Number",
            y="Predicted Valuation (Cr INR)",
            color="Industry",
            hover_data=["Region", "Timestamp"],
            title="Historical Startup Valuation Predictions",
        )

        display_chart(fig)

        # --------------------------------------------------
        # DOWNLOAD PREDICTION HISTORY
        # --------------------------------------------------

        csv_data = history_df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="📥 Download Prediction History",
            data=csv_data,
            file_name="startup_prediction_history.csv",
            mime="text/csv",
            use_container_width=True,
        )

        # --------------------------------------------------
        # CLEAR PREDICTION HISTORY
        # --------------------------------------------------

        if st.button("🗑️ Clear Prediction History", use_container_width=True):

            st.session_state.prediction_history = []

            st.rerun()

    else:

        st.info(
            "No predictions recorded yet. " "Generate a valuation prediction to begin."
        )

    # --------------------------------------------------
    # MODEL TRANSPARENCY
    # --------------------------------------------------

    st.divider()

    st.header("🧠 How Does the AI Predict Valuation?")

    st.markdown(
        "The prediction system uses a trained Linear Regression "
        "model to estimate startup valuation in Indian rupee crores "
        "based on financial and operational characteristics."
    )

    with st.expander("🔍 View Prediction Process"):

        st.markdown("""
        ### Step 1: User Input

        The user provides nine startup characteristics:

        - Industry
        - Funding Rounds
        - Funding Amount
        - Revenue
        - Employees
        - Market Share
        - Profitability
        - Year Founded
        - Region

        ### Step 2: Data Preprocessing

        The machine learning pipeline applies:

        **One-Hot Encoding**
        - Converts Industry and Region into numerical features.

        **Standard Scaling**
        - Standardizes numerical features.

        **Binary Feature**
        - Profitability is represented as 0 or 1.

        ### Step 3: Machine Learning Prediction

        The Linear Regression model combines the transformed
        features using learned coefficients.

        ### Step 4: Valuation Output

        The application displays the estimated startup
        valuation in Indian rupee crores.
        """)

    with st.expander("⚠️ Model Limitations"):

        st.markdown("""
        - Predictions are estimates, not verified market valuations.
        - The model may produce negative predictions.
        - Predictions outside the observed data ranges may be unreliable.
        - The model does not consider every factor affecting valuation.
        - Correlation does not establish causation.
        - Model accuracy depends on the quality and representativeness
          of the training dataset.
        """)

elif page == "Model Performance":

    st.title("🎯 Machine Learning Model Performance")

    st.markdown(
        "Review the evaluation results of the trained "
        "startup valuation prediction model."
    )

    st.divider()

    st.subheader("Model Information")

    st.write("**Algorithm:** Linear Regression")
    st.write("**Preprocessing:** One-Hot Encoding + Standard Scaling")
    st.write("**Target:** Valuation (Cr INR)")
    st.write("**Dataset Size:** 500 Startups")

    st.divider()

    st.subheader("Previously Recorded Test Performance")

    col1, col2, col3 = st.columns(3)

    col1.metric("R² Score", "0.6715")
    col2.metric("MAE", "₹3,840.40 Cr")
    col3.metric("RMSE", "₹5,111.06 Cr")

    st.markdown("""
    **Understanding the metrics**

    - **R² Score:** Measures how much variation in valuation
      the model explains on the test dataset.

    - **MAE:** Average absolute prediction error.

    - **RMSE:** Measures prediction error while giving
      greater weight to large errors.
    """)

    st.divider()

    st.subheader("Model Limitations")

    st.warning(
        "The model was trained on a limited startup dataset. "
        "Predictions may be inaccurate for unusual startup profiles "
        "or inputs outside the training data range."
    )

    st.info(
        "The displayed performance values are from the earlier "
        "notebook evaluation. They are not newly calculated "
        "by this Streamlit application."
    )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption("Global Startup Valuation Prediction & Business Intelligence System")
