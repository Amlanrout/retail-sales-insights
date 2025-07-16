# scripts/data_cleaning.py

import pandas as pd

def load_and_clean_data(filepath):
    # Load CSV data
    df = pd.read_csv(filepath)

    # Convert the 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'])

    # Standardize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

    # Fill missing values if any
    if df.isnull().sum().sum() > 0:
        df = df.fillna({
            'sales_volume': 0,
            'revenue': 0.0,
            'discount': 0.0
        })

    # Create a new 'profit' column
    df['profit'] = df['revenue'] - df['discount']

    print("✅ Data loaded and cleaned successfully.")
    return df

