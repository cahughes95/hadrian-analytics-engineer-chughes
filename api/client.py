import requests
import json
from lib import API_KEY
import pandas as pd

class Client:
    def __init__(self):
        # Initialize the Client with API authentication details
        self.base_url = "https://v2.nba.api-sports.io"
        self.headers = {
            'x-rapidapi-host': "v2.nba.api-sports.io",
            'x-rapidapi-key': API_KEY
        }

    def get_basketball_data(self, endpoint, query_params=None):
        # Make a GET request to the API for a given endpoint and optional query parameters, then return a JSON response.
        url = f"{self.base_url}/{endpoint}"      
        response = requests.get(url, headers=self.headers, params=query_params)
        response_json = response.json()
        return response_json['response'], endpoint

    def get_games_data(self, num_seasons, endpoint, query_params=None):
        # Retrieve games data for a specified number of seasons by making repeated API requests, then aggregate and return the data.
        current_year = pd.Timestamp.now().year
        years = range(current_year - num_seasons, current_year + 1)
        all_games = []

        for year in years:
            query_params['season'] = year
            print(f"Requesting data for season: {year}")
            # Calls the get_basketball_data() function from above to make the API request, looping through seasons.
            year_data, _ = self.get_basketball_data(endpoint, query_params)
            all_games.extend(year_data)

        return all_games, 'games'
