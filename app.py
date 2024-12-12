import os
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def load_data(file):
    df = pd.read_csv(file)
    return df

def main():
    st.title("Sales Data Analyzer")
    st.write("Upload a CSV file to analyze sales data")

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        df = load_data(uploaded_file)
        st.write("Data Preview:")
        st.write(df.head())

        st.write("Basic Statistics:")
        st.write(df.describe())

        st.write("Total Sales by Product Category:")
        category_sales = df.groupby('Product Category')['Sales'].sum().sort_values(ascending=False)
        st.bar_chart(category_sales)

        st.write("Monthly Sales Trend:")
        df['Date'] = pd.to_datetime(df['Date'])
        monthly_sales = df.resample('M', on='Date')['Sales'].sum()
        st.line_chart(monthly_sales)

        st.write("Top 10 Products by Sales:")
        top_products = df.groupby('Product')['Sales'].sum().sort_values(ascending=False).head(10)
        fig, ax = plt.subplots()
        ax.pie(top_products.values, labels=top_products.index, autopct='%1.1f%%')
        st.pyplot(fig)

if __name__ == "__main__":
    main()