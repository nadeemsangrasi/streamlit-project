import streamlit as st
import pandas as pd
import time

# Page Configuration
st.set_page_config(page_title="Data Sweeper App", page_icon="🧹")

# App Title and Description
st.title("🧹 Data Sweeper App")
st.write("Upload your CSV file below and choose your cleaning options to get started.")

# File Uploader Widget
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the uploaded CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)
    
    st.subheader("Original Data Preview")
    st.dataframe(df.head())

    # Cleaning Options
    st.subheader("Cleaning Options")
    remove_duplicates = st.checkbox("Remove Duplicate Rows", value=True)
    fill_na = st.checkbox("Fill Missing Values", value=True)

    # When the user clicks the "Clean Data" button
    if st.button("Clean Data"):
        # Simulate processing with a progress bar
        progress_bar = st.progress(0)
        cleaned_df = df.copy()
        for percent in range(100):
            time.sleep(0.01)  # Simulate a time-consuming process
            progress_bar.progress(percent + 1)

        # Remove duplicate rows if selected
        if remove_duplicates:
            cleaned_df = cleaned_df.drop_duplicates()

        # Fill missing values if selected
        if fill_na:
            for col in cleaned_df.columns:
                if pd.api.types.is_numeric_dtype(cleaned_df[col]):
                    # Fill numeric columns with the mean value
                    cleaned_df[col].fillna(cleaned_df[col].mean(), inplace=True)
                else:
                    # Fill non-numeric columns with the mode or a default value
                    if not cleaned_df[col].mode().empty:
                        cleaned_df[col].fillna(cleaned_df[col].mode()[0], inplace=True)
                    else:
                        cleaned_df[col].fillna("N/A", inplace=True)

        st.success("Data cleaning complete!")
        st.subheader("Cleaned Data Preview")
        st.dataframe(cleaned_df.head())

        # Provide an option to download the cleaned data as a CSV file
        csv = cleaned_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Cleaned Data",
            data=csv,
            file_name='cleaned_data.csv',
            mime='text/csv'
        )

# Footer
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        text-align: center;
        color: gray;
        font-size: 12px;
        padding: 10px;
        background-color: #f9f9f9;
    }
    </style>
    <div class="footer">
        Created by Nadeem Khan
    </div>
    """,
    unsafe_allow_html=True,
)
