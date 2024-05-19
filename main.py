import duckdb

con = duckdb.connect('nba_data.db')

# Read the .sql file
with open('sql_queries.sql', 'r') as file:
    sql_script = file.read()

# Split the script into individual queries
queries = sql_script.split(';')

# List of custom messages for each query
messages = [
    "The top 10 highest-scoring games in the last decade are: ",
    "The win-loss record for each team over the last decade is: ",
    "The average points scored by each team per season over the last decade is: ",
    "The conference with the most wins in the last decade is: ",
    "The team with the highest average margin of victory in the last decade is: ",
    "For each team, here are the average points scored per game and average points allowed per game for each season: "
]

# Execute each query and print the corresponding message and result
for message, query in zip(messages, queries):
    if query:  # Ignore empty queries
        try:
            result = con.execute(query).fetchall()
            print(message)
            for row in result:
                print(row)
            print()  # Add a blank line for better readability
        except duckdb.Error as e:
            print(f"Error executing query: {e}")
