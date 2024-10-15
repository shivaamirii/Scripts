This project consists of two Python scripts that insert sample data into different tables in ClickHouse. The scripts utilize the random and names modules for data generation, and the clickhouse_connect library to connect and interact with the ClickHouse database.

## Prerequisites
- Install and run ClickHouse
- Install Python
- Install the required packages:
  ```sh
  pip install clickhouse-connect names
  ```
## Project Assignments Script:
This script creates the project_assignments table and inserts data containing 50 IDs along with randomly assigned project names.

  ## Script Details:
  - Creates the project_assignments table with columns ID and Project_Name.
  - Generates 50 rows of data with randomly selected project names from a predefined list.

 ## Salary Script:
This script creates the company table and generates data with full names, departments, and salaries for 50 employees, and then inserts this data into ClickHouse.

  ## Script Details:
  - Creates the company1403 table with columns ID, NAME, DEPARTMENT, and SALARY.
  - Generates 50 rows of data with real names (using the names library), randomly assigned departments, and random salary amounts.

## How to Run
- Ensure that ClickHouse is running.
- Run each script as follows:
  ```sh
  python3 script_name.py
  ```

> After successful execution, the message "Data inserted successfully into ClickHouse!" will be displayed.

## Output
The output of both scripts is stored in their respective tables in ClickHouse, where they can be used for various data analyses.


