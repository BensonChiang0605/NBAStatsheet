from nba_api.stats.static import teams
import numpy
from nba_api.stats.endpoints import playergamelog
# fetching players data
from nba_api.stats.static import players
# get_players returns a list of dictionaries, each representing a player.
nba_players = players.get_players()
import matplotlib.pyplot as plt
import pandas as pd

interested_player = input("Welcome to Benson's Sportsbetting Assistant. Which players' points per games are you interested in examining?"
      "\n")
absent_player = input("Who's his teammate not playing")

for player in nba_players:
    if player['full_name'] == interested_player:
        playerid = player['id']
        player_name = player['full_name']
    if player['full_name'] == absent_player:
        absent_playerid = player['id']
        absent_player_name = player['full_name']

# https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/endpoints/playergamelog.md

# Get season  stats for main player
player_and_season = playergamelog.PlayerGameLog(player_id=playerid, season_type_all_star='Regular Season',
                                                season='2022-23')
player_dataframe = player_and_season.get_data_frames()[0]

player_games_played = list(player_dataframe.Game_ID)

# Get season stats for absent player
absent_player_and_season = playergamelog.PlayerGameLog(player_id=absent_playerid, season_type_all_star='Regular Season',
                                                season='2022-23')
absent_player_dataframe = absent_player_and_season.get_data_frames()[0]

absent_player_games_played = list(absent_player_dataframe.Game_ID)

print(absent_player_games_played)

filt = (player_dataframe["Game_ID"] not in absent_player_games_played)
print(player_dataframe[filt])
# rslt_df = player_dataframe.loc[player_dataframe['Game_ID'] not in absent_player_games_played]
# print(rslt_df)