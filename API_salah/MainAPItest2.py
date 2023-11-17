import FootballAPIClient as ftb
import pandas as pd





# Exemple d'utilisation
api_key = "447225a4d6mshb59b87af2b61952p1a82c6jsnb05af10a2871"
football_api = ftb(api_key=api_key)

#------------- Exemple pour obtenir les saisons
# seasons = football_api.get_seasons()
# print("Saisons disponibles :", seasons)

#------------- Exemple pour obtenir les ligues
leagues = football_api.get_leagues()
# leagues = pd.json_normalize(leagues, max_level=9)
leagues = pd.DataFrame(leagues)
leagues
# columns = leagues.columns

# print("Ligues disponibles :", columns)
# print("Ligues disponibles :", leagues.head())

# # Exemple pour obtenir les événements des fixtures
# fixtures_events = football_api.get_fixtures_events("2022", "Premier League")
# print("Événements des fixtures :", fixtures_events)

# # Exemple pour obtenir les statistiques des fixtures
# fixtures_statistics = football_api.get_fixtures_statistics("2022", "Premier League")
# print("Statistiques des fixtures :", fixtures_statistics)

# ... Ajoutez d'autres exemples selon vos besoins
