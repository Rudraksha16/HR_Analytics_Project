# scripts/data_generator.py
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set seed for reproducibility
np.random.seed(42)
n_records = 500

# Generate base data
emp_ids = range(1001, 1001 + n_records)
first_names = np.random.choice(['John', 'Jane', 'Alex', 'Emily', 'Michael', 'Sarah', 'David', 'Jessica', 'James', 'Amanda'], n_records)
last_names = np.random.choice(['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Miller', 'Davis', 'Garcia', 'Rodriguez', 'Wilson'], n_records)
genders = np.random.choice(['Male', 'Female', 'Non-Binary'], n_records, p=[0.48, 0.48, 0.04])

# Messy departments (deliberate inconsistencies for cleaning phase)
dept_pool = ['Engineering', 'Dev', 'Software Eng', 'Sales', 'SALES', 'Human Resources', 'HR', 'Marketing']
departments = np.random.choice(dept_pool, n_records)

# Dates
start_date = datetime(2018, 1, 1)
hire_dates = [start_date + timedelta(days=int(np.random.randint(0, 2500))) for _ in range(n_records)]

# Create Attrition and Termination Dates
attrition = np.random.choice(['Yes', 'No'], n_records, p=[0.16, 0.84])
termination_dates = []

for i in range(n_records):
    if attrition[i] == 'Yes':
        # Terminated somewhere between 6 months and 3 years after hire
        term_days = np.random.randint(180, 1095)
        t_date = hire_dates[i] + timedelta(days=term_days)
        # Randomly mix date formats to simulate real-world messy pipelines
        if np.random.rand() > 0.5:
            termination_dates.append(t_date.strftime('%Y-%m-%d'))
        else:
            termination_dates.append(t_date.strftime('%d/%m/%Y'))
    else:
        termination_dates.append(np.nan) # Active employees have no term date

# Format hire dates messily too
hire_dates_formatted = [d.strftime('%Y-%m-%d') if np.random.rand() > 0.5 else d.strftime('%m-%d-%Y') for d in hire_dates]

salaries = np.random.randint(45000, 145000, n_records)
performance_ratings = np.random.choice([1, 2, 3, 4, 5], n_records, p=[0.05, 0.15, 0.50, 0.20, 0.10])

# Construct DataFrame
df = pd.DataFrame({
    'employee_id': emp_ids,
    'first_name': first_names,
    'last_name': last_names,
    'gender': genders,
    'department': departments,
    'hire_date': hire_dates_formatted,
    'termination_date': termination_dates,
    'salary': salaries,
    'performance_rating': performance_ratings,
    'attrition': attrition
})

# Save to raw
df.to_csv('data/raw_hr_data.csv', index=False)
print("Messy raw dataset created at data/raw_hr_data.csv")