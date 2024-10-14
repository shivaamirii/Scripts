import random
import clickhouse_connect
import names

# Connect to ClickHouse
client = clickhouse_connect.get_client(host='192.168.100.217', port=8123)

# Create table
table_name = 'company'

client.command(f'''
CREATE TABLE IF NOT EXISTS {table_name} (
    ID Int32,
    NAME String,
    DEPARTMENT String,
    SALARY Int32
) ENGINE = MergeTree()
ORDER BY (ID)
''')

# Define the parameters
ids = range(1, 51)
DEPARTMENT_NAME = ['Support', 'Data', 'DevOps', 'Development', 'Accounting', 'SRE', 'HR']

# Function to generate data for each ID
def generate_data():
    rows = []

    for ID in ids:
        NAME = names.get_full_name()
        DEPARTMENT = random.choice(DEPARTMENT_NAME)
        SALARY = random.randint(18000000, 35000000)
        rows.append((ID, NAME, DEPARTMENT, SALARY))
    
    return rows

# Generate data and insert it into ClickHouse
data = generate_data()

# Insert data into the table
client.insert(table_name, data, column_names=['ID', 'NAME', 'DEPARTMENT', 'SALARY'])

print("Data inserted successfully into ClickHouse!")

