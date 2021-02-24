import requests
import json
import numpy as np
import pandas as pd
import datetime

# Make a get request to get the latest player data from the FPL API
response = requests.get("https://fantasy.premierleague.com/api/bootstrap-static/")

data = json.loads(response.text)

team_names = {team['id']: team['name'] for team in data['teams']}

players = {player['id']: f'{player["first_name"]} {player["second_name"]}' for player in data['elements']}

print('wtf')