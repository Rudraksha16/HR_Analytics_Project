# Enterprise HR Analytics Dashboard
### End-to-End Data Analytics Portfolio Project (Excel, Python, MySQL, Power BI)

---

## Project Overview
This project presents a comprehensive, data-driven investigation into corporate workforce dynamics. Utilizing a synthetic pipeline of **500 employee records** injected with real-world anomalies (inconsistent text string cases, broken date patterns, missing termination records), this repository demonstrates a robust engineering workflow to clean, warehouse, analyze, and visualize corporate HR metrics.

The operational goal is to diagnose employee attrition drivers, highlight retention risks among top-performing staff, evaluate department-level pay equity, and deliver an interactive executive dashboard for HR decision-makers.

---

## Repository Structure
```text
HR_Analytics_Project/
│
├── data/
│   ├── raw_hr_data.csv          # Source data with anomalies and mixed date formats
│   └── clean_hr_data.csv        # Production-ready data optimized for SQL ETL
│
├── scripts/
│   ├── data_generator.py        # Python engine constructing the messy dataset
│   └── data_cleaning.py         # Pandas pipeline handling text & date normalization
│
├── sql/
│   └── hr_queries.sql           # Database DDL schema and analytical business queries
│
└── README.md                    # Professional documentation & execution roadmap# HR_Analytics_Project
# HR_Analytics_Project
