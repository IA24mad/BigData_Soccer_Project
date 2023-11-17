
import FootballAPI as fa
import pandas as pd 

api_key = "447225a4d6mshb59b87af2b61952p1a82c6jsnb05af10a2871"
football_api = fa.FootballAPI(api_key=api_key)

#leagues = football_api.get_leagues()
#seasons = [entry['league'] for entry in leagues]
#seasons= pd.json_normalize(leagues, max_level=9)
#seasons = pd.DataFrame(leagues)
#print(seasons.columns)

leagues = football_api.get_leagues_test()
leagues = pd.json_normalize(leagues, max_level=9)
leagues = pd.DataFrame(leagues)
Leagues_names = ["UEFA Champions League"]
league_ids = []
for index, row in leagues.iterrows():
    # Check if the lowercase version of the league name is in Leagues_names
    if row['name'].lower() in [name.lower() for name in Leagues_names]:
        # Append the league ID and name to league_ids
        league_ids.append({'id': row['id'], 'name': row['name'], 'logo': row['logo']})

result_df = pd.DataFrame(league_ids)
result_df.to_csv('football_leagues2.csv', index=False)

print(league_ids)
