
class Game:
    def __init__(self, game_data):
        # Initialize a Game object with data from a single game.
        self.game_id = game_data['id']
        self.season = game_data['season']
        self.date_start = game_data['date']['start']
        self.home_team_name = game_data['teams']['home']['name']
        self.home_team_points = game_data['scores']['home']['points']
        self.visitor_team_name = game_data['teams']['visitors']['name']
        self.visitor_team_points = game_data['scores']['visitors']['points']

    def to_dict(self):
        # Convert the Game object to a dictionary for easier DataFrame conversion.
        return {
            'game_id': self.game_id,
            'season': self.season,
            'date_start': self.date_start,
            'home_team_name': self.home_team_name,
            'home_team_points': self.home_team_points,
            'visitor_team_name': self.visitor_team_name,
            'visitor_team_points': self.visitor_team_points
        }