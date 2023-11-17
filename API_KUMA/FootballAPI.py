import requests

class FootballAPI:
    def __init__(self,api_key):
        self.api_key = api_key
        self.base_url = "https://api-football-beta.p.rapidapi.com"
        self.headers = {
            "X-RapidAPI-Key": api_key,
            "X-RapidAPI-Host": "api-football-beta.p.rapidapi.com"
        }


    def get_seasons(self):
        """
        Get all the available seasons within the api
        parametres : none
        """
        url = f"{self.base_url}/leagues/seasons"
        response = requests.get(url, headers=self.headers)
        return response.json()['response']

        
    def get_leagues(self):
        """
        Get all the available leagues within the api
        parametres : none
        """
        url = f"{self.base_url}/leagues"
        response = requests.get(url, headers=self.headers)
        return response.json()['response']
    

    def get_fixtures_events(self, season, league):
        url = f"{self.base_url}/fixtures/events"
        querystring = {"season": str(season), "league": str(league)}
        response = requests.get(url, headers=self.headers, params=querystring)
        return response.json()


    def get_fixtures_statistics(self, season, league):
        url = f"{self.base_url}/fixtures/statistics"
        querystring = {"season": str(season), "league": str(league)}
        response = requests.get(url, headers=self.headers, params=querystring)
        return response.json()
    

    def get_lineups(self, fixture_id):
        url = f"{self.base_url}/lineups"
        querystring = {"fixture": str(fixture_id)}
        response = requests.get(url, headers=self.headers, params=querystring)
        return response.json()
    
    
    def get_players(self, team_id):
        url = f"{self.base_url}/players"
        querystring = {"team": str(team_id)}
        response = requests.get(url, headers=self.headers, params=querystring)
        return response.json()


    def get_injuries(self, season, league):
        url = f"{self.base_url}/injuries"
        querystring = {"season": str(season), "league": str(league)}
        response = requests.get(url, headers=self.headers, params=querystring)
        return response.json()
    
    #testing area :

    def get_leagues_test(self):
        url = f"{self.base_url}/leagues"
        response = requests.get(url, headers=self.headers)
        # Extract only the 'league' column from the JSON response
        leagues = [entry['league'] for entry in response.json()['response']]
        return leagues

   # def save_csv_fixtures(self, Seasons, league):

        