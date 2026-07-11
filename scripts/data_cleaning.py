# scripts/data_cleaning.py
import pandas as pd
import numpy as np

# Load messy data
df = pd.read_csv('data/raw_hr_data.csv')

print("Starting Data Cleaning Process...")

# 1. Standardize Department Names
dept_mapping = {
    'Dev': 'Engineering',
    'Software Eng': 'Engineering',
    'Engineering': 'Engineering',
    'SALES': 'Sales',
    'Sales': 'Sales',
    'HR': 'Human Resources',
    'Human Resources': 'Human Resources',
    'Marketing': 'Marketing'
}
df['department'] = df['department'].map(dept_mapping)

# 2. Standardize Date Columns (Handling mixed formats gracefully)
df['hire_date'] = pd.to_datetime(df['hire_date'], errors='coerce', format='mixed').dt.strftime('%Y-%m-%d')
df['termination_date'] = pd.to_datetime(df['termination_date'], errors='coerce', format='mixed').dt.strftime('%Y-%m-%d')

# 3. Feature Engineering: Calculate Tenure
today = pd.to_datetime('2026-07-11')
end_dates = pd.to_datetime(df['termination_date']).fillna(today)
start_dates = pd.to_datetime(df['hire_date'])

df['tenure_years'] = round((end_dates - start_dates).dt.days / 365.25, 2)

# Save Cleaned Data
df.to_csv('data/clean_hr_data.csv', index=False)
print("Cleaned dataset saved at data/clean_hr_data.csv ready for MySQL import!")