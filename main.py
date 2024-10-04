import pyodbc

# Define the connection string
conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=your_server_name;"
    "DATABASE=your_database_name;"
    "UID=your_username;"
    "PWD=your_password"
)

# Establish the connection
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Define the insert query
insert_query = """
INSERT INTO your_table_name (column1, column2, column3)
VALUES (?, ?, ?)
"""

# Define the data to be inserted
data = ('value1', 'value2', 'value3')

# Execute the insert query
cursor.execute(insert_query, data)

# Commit the transaction
conn.commit()

# Close the connection
cursor.close()
conn.close()

#added for testing

#added testing 2

#added testing 3

#added testing 4
