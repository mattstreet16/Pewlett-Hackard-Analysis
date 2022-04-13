EMPLOYEE ERD CODE
#Deparment Schema
Departments
-
dept_no varchar pk
dept_name varchar

#Employee Schema
Employees
-
emp_no int pk
birth_date date 
first_name varchar
last_name varchar
gender varchar
hire_date date

#Manager Schema
Managers
-
dept_no varchar pk fk - Departments.dept_no
emp_no int fk - Employees.emp_no
from_date date
to_date date

#Dept Schema 
Dept_Emp
-
emp_no int pk fk -< Employees.emp_no
dept_no varchar fk -< Departments.dept_no
from_date date
to_date date

#Salary Schema
Salaries
-
emp_no varchar pk fk -< Employees.emp_no
salary int
from_date date
to_date date

#Title Schema 
Titles
-
emp_no varchar pk fk -< Employees.emp_no
title varchar
from_date date
to_date date
