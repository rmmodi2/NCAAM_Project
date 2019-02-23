from scipy import stats
import pandas as pd 
import numpy as np
import ncaam_helperfunctions as helper
import matplotlib.pyplot as plt

#Get tournament games from teamRecord / helperFunctions instead
#dict mapping a String identifier (year) to the tournamentWins dict for that year
#tournamentWins dict is team name -> tournament wins
tournamentWinsAllYears,tournament_dates = helper.createTournamentWinsAllYears()

# skiprows_list = []
# for i in range(1,100000):
#     skiprows_list.append(22*i)
#     skiprows_list.append(22*i+1)


# print(kenpom_1011)
# print(teamStats_1011)
# print(oppTeamStats_1011)


#dict mapping year to team stats dict for that year
#team stats dict is dict mapping team name to 
#dict mapping statname to stat#
teamStatistics = helper.createTeamStatistics(tournamentWinsAllYears)

print(teamStatistics["1011"]["Kansas State"]['ConfWinPct'])

#dict mapping team name to team's stats




