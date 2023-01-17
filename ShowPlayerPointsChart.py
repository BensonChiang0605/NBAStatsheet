# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# fetching teams data

from nba_api.stats.static import teams
import numpy
from nba_api.stats.endpoints import playergamelog
# fetching players data
from nba_api.stats.static import players
# get_players returns a list of dictionaries, each representing a player.
nba_players = players.get_players()
import matplotlib.pyplot as plt
import pandas as pd

players_interested = input("Welcome to Benson's Sportsbetting Assistant. Which players' points per games are you interested in examining?"
      " Separate player's names with commas: \n")
# get_teams returns a list of 30 dictionaries, each an NBA team.

# To search for an individual team or player by its name (or other attribute), dictionary comprehensions are your friend.
for interested_player in players_interested.split(","):
    print(interested_player)
    for player in nba_players:
        if player['full_name'] == interested_player:
            playerid = player['id']
            player_name = player['full_name']
        pass

    # https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/endpoints/playergamelog.md

    # career = boxscore.BoxScore(game_id='1610612763')
    player_and_season = playergamelog.PlayerGameLog(player_id = playerid, season_type_all_star = 'Regular Season', season = '2022-23')
    player_dataframe = player_and_season.get_data_frames()[0]

    points = player_dataframe['PTS']
    print(f"Player games played = {len(player_dataframe)}")

    plt.title(f"Points per Game Distribution")
    plt.xlabel('Points per Games')
    plt.ylabel('Frequency')
    bins = numpy.linspace(-10, 10, 100)
    # plt.legend(loc='upper right')
    plt.hist(points, range = (0, points.max()), alpha=0.5, label= player_name)

plt.legend(players_interested.split(","))
plt.show()
# show games played

#bins = [0, 10, 20, 30, 40, 50, points.max()]

# player stats without another player

print(player_dataframe.Game_ID)


