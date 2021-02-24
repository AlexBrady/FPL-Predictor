import requests
import os
import json
import numpy as np
import pandas as pd
import datetime

# Make a get request to get the latest player data from the FPL API
details_response = requests.get("https://fantasy.premierleague.com/api/bootstrap-static/")

data = json.loads(details_response.text)

# Store team names
team_names = {team['code']: team['name'] for team in data['teams']}

# Store player info
players = {
    player['id']: {
        'name': f'{player["first_name"]} {player["second_name"]}',
        'team_code': player['team_code'],
        'pos': player['element_type']
        } 
        for player in data['elements']
    }

# Convert to data frame
player_df = pd.DataFrame.from_dict(players, orient='index')

# Save the table of data as a CSV
player_df.to_csv(index=False, path_or_buf='../data/fpl_players.csv')
