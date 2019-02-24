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


#dict mapping year to team stats dict for that year - teamStatistics.keys() - "1011"
#team stats dict is dict mapping team name to  teamStatisics.keys().keys() - "Kansas State"
#dict mapping statname to stat - teamStatisics.keys().keys().keys() - "eFG%"
#list of stats are as follows: ConfWinPct,NonConfWinPct,eFG%,eFG%Against,netEFG%,'TOV%'..
teamStatistics = helper.createTeamStatistics(tournamentWinsAllYears)

# print(teamStatistics["1718"]["Villanova"]["OverallWinPct"])

stat = 'kenpomRk'

#todo: convert into a X NP Array -> roadWinPct and a Y NP Array -> tournamentTeamWins
statdict,tournamentWins = helper.createXYArraysStats(teamStatistics,tournamentWinsAllYears,stat)
# print(tournamentWins)
statList = np.asarray(list(statdict.values()),dtype=float)
tournamentWinsList = np.asarray(list(tournamentWins.values()),dtype=int)

#todo: plot tournamentTeamWins vs roadWinPct
plt.plot(statList,tournamentWinsList,"ro")
plt.xlabel(stat)
plt.ylabel("tournamentWins")
statdictkeys = list(statdict.keys())
statdictvals = list(statdict.values())

#todo: apply Kendall Tau Correlation for x=road win% and y=# of NCAA Tournament Wins
kendallTau,p = stats.kendalltau(statList,tournamentWinsList)
print("The Kendall Tau Correlation between "+stat+" and ncaa tournament wins is:" +str(kendallTau))

plt.show()




