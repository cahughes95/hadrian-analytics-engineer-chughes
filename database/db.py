import pandas as pd
import duckdb
from .games import Game
from .teams import Team

con = duckdb.connect(database='nba_data.db')  # Use a file path for persistent storage

def save_data(con, data, endpoint, data_class):

    flattened_data = [data_class(item).to_dict() for item in data]
    df = pd.DataFrame(flattened_data)

    table = f'stg_{endpoint}'
    # Print DataFrame for debugging
    print("DataFrame shape:", df.shape)
    print("DataFrame columns:", df.columns)
    print("DataFrame head:", df.head())

    con.execute(f"DROP TABLE IF EXISTS {table}")
    con.execute(f"CREATE TABLE {table} AS SELECT * FROM df")

    # Verify data in DuckDB
    print(con.execute(f"SELECT * FROM {table} LIMIT 5").fetchall())

def transform_teams_data(con):
    # Drop the final table if it exists
    con.execute("DROP TABLE IF EXISTS nba_teams")

    # Create the final table with the specified column types
    con.execute("""
    CREATE TABLE nba_teams (
        team_id INT,
        team_name VARCHAR,
        conference VARCHAR,
        division VARCHAR
    )
    """)

    # Insert the transformed data into the final table
    con.execute("""
    INSERT INTO nba_teams
    SELECT
        team_id,
        team_name,
        conference,
        division
    FROM
        stg_teams
    WHERE
        nba_franchise = True AND
        all_star = False
    """)

def transform_games_data(con):
    # Drop the final table if it exists
    con.execute("DROP TABLE IF EXISTS nba_games")

    # Create the final table with the specified column types
    con.execute("""
    CREATE TABLE nba_games (
        game_id INT,
        season INT,
        date DATE,
        home_team VARCHAR,
        home_score INT,
        away_team VARCHAR,
        away_score INT
    )
    """)

    # Insert the transformed data into the final table
    con.execute("""
    INSERT INTO nba_games
    SELECT
        game_id,
        season,
        CAST(SUBSTR(date_start, 1, 10) AS DATE) AS date,
        home_team_name AS home_team,
        home_team_points AS home_score,
        visitor_team_name AS away_team,
        visitor_team_points AS away_score
    FROM
        stg_games
    WHERE
        date_start IS NOT NULL
    """)
