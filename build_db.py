import pandas as pd
from api import Client
from database import Team, Game, save_data, transform_teams_data, transform_games_data, con

def build_db():
    client = Client()

    query_params = {'league': 'standard'}
    
    # Get teams data
    teams_data, teams_endpoint = client.get_basketball_data(endpoint='teams', query_params=query_params)
    save_data(con, teams_data, teams_endpoint, Team)
    transform_teams_data(con)

    # Get games data
    games_data, games_endpoint = client.get_games_data(num_seasons=10, endpoint='games', query_params=query_params)
    save_data(con, games_data, games_endpoint, Game)
    transform_games_data(con)

if __name__ == "__main__":
    build_db()