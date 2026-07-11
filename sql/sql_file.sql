sudo mysql --local-infile=1 -u root HR_Analytics_DB -e "
LOAD DATA LOCAL INFILE 'data/clean_hr_data.csv'
INTO TABLE employees
FIELDS TERMINATED BY ',' 
ENCLOSED BY '\"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(employee_id, first_name, last_name, gender, department, hire_date, @v_term_date, salary, performance_rating, attrition, tenure_years)
SET termination_date = NULLIF(@v_term_date, '');"