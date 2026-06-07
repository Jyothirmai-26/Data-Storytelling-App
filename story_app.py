import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.title("📖 Data Storytelling: Advertising Analysis")

# Load dataset
df = pd.read_csv("Advertising.csv")

# -----------------------------
# 1. Dataset Introduction
# -----------------------------
st.header("📌 Dataset Introduction")

st.write("""
This dataset contains information about advertising spending on TV, Radio, and Newspaper.
The goal is to understand how these factors influence product sales.
""")

st.write(df.head())

# -----------------------------
# 2. Data Overview (EDA)
# -----------------------------
st.header("🔍 Exploratory Data Analysis")

st.write("Dataset Summary:")
st.write(df.describe())

st.write("Missing Values:")
st.write(df.isnull().sum())

# -----------------------------
# 3. Visualizations
# -----------------------------
st.header("📊 Visualizations")

# Scatter plots
fig1 = px.scatter(df, x="TV", y="Sales", title="TV vs Sales")
st.plotly_chart(fig1)

fig2 = px.scatter(df, x="Radio", y="Sales", title="Radio vs Sales")
st.plotly_chart(fig2)

fig3 = px.scatter(df, x="Newspaper", y="Sales", title="Newspaper vs Sales")
st.plotly_chart(fig3)

# Correlation Heatmap
corr = df.corr()
fig4 = px.imshow(corr, text_auto=True, title="Correlation Matrix")
st.plotly_chart(fig4)

# -----------------------------
# 4. Insights
# -----------------------------
st.header("📈 Insights and Findings")

st.write("""
- TV advertising shows a strong positive relationship with sales.
- Radio advertising has a moderate impact on sales.
- Newspaper advertising has very little impact.
- Investing more in TV ads can increase sales significantly.
""")

# -----------------------------
# 5. Conclusion
# -----------------------------
st.header("✅ Conclusion & Recommendations")

st.write("""
Based on the analysis, companies should prioritize TV advertising as it gives the best return.
Radio can be used as a secondary channel, while Newspaper ads are less effective.
""")