# app.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="NeuroSync Dashboard", layout="wide")

st.title("🧠 NeuroSync: A Closed-Loop Bioadaptive Framework")
st.subheader("Predicting Learning Retention Using Multi-Modal Physiological Signals in African Undergraduates")

st.markdown("""
Upload your Excel/CSV file with student physiological and learning data.  
The system will:
1. Draw bar graphs for all numeric features.  
2. Calculate descriptive statistics (mean, median, std, etc.).  
3. Display an analytics dashboard.  
""")

# File uploader
uploaded_file = st.file_uploader("📂 Upload Excel/CSV file", type=["xlsx", "csv"])

if uploaded_file is not None:
    # Load data
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.success("File uploaded successfully!")

    st.subheader("📊 Complete Dataset")
    st.dataframe(df)   # 👈 shows ALL rows

    # Descriptive statistics
    st.subheader("📈 Descriptive Statistics")
    st.write(df.describe(include="all").T)

    # Individual statistics
    st.subheader("🔎 Key Metrics")
    for col in df.select_dtypes(include="number").columns:
        st.markdown(f"**{col}**")
        st.write({
            "Mean": df[col].mean(),
            "Median": df[col].median(),
            "Mode": df[col].mode()[0] if not df[col].mode().empty else "N/A",
            "Standard Deviation": df[col].std(),
            "Variance": df[col].var(),
            "Minimum": df[col].min(),
            "Maximum": df[col].max(),
            "25th Percentile": df[col].quantile(0.25),
            "75th Percentile": df[col].quantile(0.75)
        })

    # Bar graphs
    st.subheader("📊 Bar Graphs")
    numeric_cols = df.select_dtypes(include="number").columns
    for col in numeric_cols:
        st.markdown(f"**Distribution of {col}**")
        fig, ax = plt.subplots()
        sns.histplot(df[col], kde=True, ax=ax)
        st.pyplot(fig)

    st.success("✅ Analysis complete! Dashboard generated successfully.")

