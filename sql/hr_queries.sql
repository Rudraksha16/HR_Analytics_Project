-- sql/hr_queries.sql

-- 1. Setup Database
CREATE DATABASE IF NOT EXISTS HR_Analytics_DB;
USE HR_Analytics_DB;

-- 2. Setup Table Architecture
CREATE TABLE IF NOT EXISTS employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    gender VARCHAR(15),
    department VARCHAR(50),
    hire_date DATE,
    termination_date DATE NULL,
    salary INT,
    performance_rating INT,
    attrition VARCHAR(5),
    tenure_years DECIMAL(5,2)
);

-- ----------------------------------------------------------------------
-- PORTFOLIO INSIGHT QUERIES
-- Run these after importing data/clean_hr_data.csv into the table
-- ----------------------------------------------------------------------

-- Query A: Total Headcount and Overall Attrition Rate
SELECT 
    COUNT(*) as total_hires,
    COUNT(CASE WHEN attrition = 'Yes' THEN 1 END) as total_left,
    ROUND((COUNT(CASE WHEN attrition = 'Yes' THEN 1 END) / COUNT(*)) * 100, 2) as attrition_rate
FROM employees;

-- Query B: Department Breakdown of Retention Risks
SELECT 
    department,
    COUNT(*) as total_employees,
    COUNT(CASE WHEN attrition = 'Yes' THEN 1 END) as departures,
    ROUND(AVG(salary), 0) as avg_salary,
    ROUND(AVG(performance_rating), 2) as avg_performance
FROM employees
GROUP BY department
ORDER BY departures DESC;

-- Query C: High-Performer Brain Drain Analysis
-- Looks at individuals with top marks (4 or 5 rating) who still quit
SELECT 
    employee_id, department, salary, performance_rating, tenure_years
FROM employees
WHERE attrition = 'Yes' AND performance_rating >= 4
ORDER BY salary DESC;