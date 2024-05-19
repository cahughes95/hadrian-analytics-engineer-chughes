
class Team:
    def __init__(self, team_data):
        self.id = team_data['id']
        self.name = team_data['name']
        self.all_star = team_data['allStar']
        self.nba_franchise = team_data['nbaFranchise']
        self.conference = team_data['leagues']['standard']['conference']
        self.division = team_data['leagues']['standard']['division']

    def to_dict(self):
        return {
            'team_id': self.id,
            'team_name': self.name,
            'all_star': self.all_star,
            'nba_franchise': self.nba_franchise,
            'conference': self.conference,
            'division': self.division
        }