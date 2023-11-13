import streamlit as st
import yfinance as yf
import os
import pandas as pd

def fetch_stock_data(ticker, statement_type):
    stock = yf.Ticker(ticker)
    if statement_type == "Balance Sheet":
        data = stock.balance_sheet
    elif statement_type == "Income Statement":
        data = stock.financials
    else:
        st.error("Invalid statement type. Please choose 'Balance Sheet' or 'Income Statement'")
        return None
    
    return data

def save_data_to_folder(data, folder_path, file_name):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_path = os.path.join(folder_path, file_name)
    data.to_csv(file_path)
    return file_path

def main():
    st.title("Stock Data Fetcher")

    # Sidebar
    st.sidebar.header("User Input")
    ticker = st.sidebar.text_input("Enter Stock Ticker", "AAPL")
    statement_type = st.sidebar.selectbox("Select Statement Type", ["Balance Sheet", "Income Statement"])

    # Fetch Data
    data = fetch_stock_data(ticker, statement_type)

    # Display Data
    if data is not None:
        st.subheader(f"{ticker} {statement_type}")
        st.write(data)

        # Save Data
        if st.button("Save Data"):
            folder_path = "stock_data"
            file_name = f"{ticker}_{statement_type.replace(' ', '_').lower()}_data.csv"
            saved_file_path = save_data_to_folder(data, folder_path, file_name)
            st.success(f"Data saved successfully at: {saved_file_path}")

if __name__ == "__main__":
    main()
