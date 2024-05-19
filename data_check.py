import duckdb

# Connect to the DuckDB database
con = duckdb.connect('nba_data.db')

# Query to check the data types of the columns in nba_games table
schema_query = "PRAGMA table_info(nba_games);"

# Execute the schema query
schema_result = con.execute(schema_query).fetchall()

# Print the schema information
print("Schema of nba_games table:")
for column in schema_result:
    print(column)

# Close the connection
con.close()
