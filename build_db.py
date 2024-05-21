import pandas as pd
from elt import Client
from elt import Team, Game, save_data, transform_teams_data, transform_games_data, con

def build_db():
    """
    Orchestrates the process of building the NBA database by fetching data from the API,
    saving it to staging tables, and transforming it into the final schema.
    """
    # Initialize the API client and define query parameters fro the requests
    client = Client()
    query_params = {'league': 'standard'}
    
    # Fetch and save the NBA teams data
    teams_endpoint = 'teams'
    teams_data = client.get_basketball_data(endpoint=teams_endpoint, query_params=query_params)
    save_data(con, data=teams_data, endpoint=teams_endpoint, data_class=Team)
    transform_teams_data(con)

    # Fetch and save the NBA games data
    games_endpoint = 'games'
    games_data = client.get_games_data(num_seasons=10, endpoint=games_endpoint, query_params=query_params)
    save_data(con, data=games_data, endpoint=games_endpoint, data_class=Game)
    transform_games_data(con)

if __name__ == "__main__":
    # Build the database by executing this script directly.
    build_db()