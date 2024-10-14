import random
import clickhouse_connect

# Connect to ClickHouse
client = clickhouse_connect.get_client(host='192.168.100.217', port=8123)


table_name = 'project_assignments'

# Create table project_assignments
client.command(f'''
CREATE TABLE IF NOT EXISTS {table_name} (
    ID Int32,
    Project_Name String
) ENGINE = MergeTree()
ORDER BY (ID)
''')

# Define project names
project_names = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta", "Eta", "Theta"]

# list of data with common project name for 50 ID
data = []

for id in range(1, 51):  
    project = random.choice(project_names)  # choose random project name from list
    data.append((id, project))


client.insert(table_name, data, column_names=['ID', 'Project_Name'])

print("Data inserted successfully into ClickHouse!")

