
import FootballAPI as fa
import pandas as pd 

api_key = "447225a4d6mshb59b87af2b61952p1a82c6jsnb05af10a2871"
football_api = fa.FootballAPI(api_key=api_key)

leagues = football_api.get_leagues()
seasons = [entry['league'] for entry in leagues]
seasons= pd.json_normalize(leagues, max_level=9)
seasons = pd.DataFrame(leagues)

print(seasons.columns)