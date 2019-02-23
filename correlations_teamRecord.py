from scipy import stats
import pandas as pd 
import numpy as np
import ncaam_helperfunctions as helper
import matplotlib.pyplot as plt




#dict mapping a String identifier (year) to the tournamentWins dict for that year
#tournamentWins dict is team name -> tournament wins
tournamentWinsAllYears,tournament_dates = helper.createTournamentWinsAllYears()

# #dict mapping a String identifier (year) to the teamRoadWins dict for that year
#teamRoadWins dict is team name -> team road win pct
roadWinPctAllYears = helper.createRoadWinPctAllYears()

#todo: convert into a X NP Array -> roadWinPct and a Y NP Array -> tournamentTeamWins
roadWinPct,tournamentWins = helper.createXYArrays(roadWinPctAllYears,tournamentWinsAllYears)
roadWinPct = np.asarray(roadWinPct,dtype=float)
tournamentWins = np.asarray(tournamentWins,dtype=int)

#todo: plot tournamentTeamWins vs roadWinPct
plt.plot(roadWinPct,tournamentWins,"ro")
plt.xlabel("roadWinPct")
plt.ylabel("tournamentWins")

#todo: apply Kendall Tau Correlation for x=road win% and y=# of NCAA Tournament Wins
kendallTau,p = stats.kendalltau(roadWinPct,tournamentWins)
print("The Kendall Tau Correlation between road win pct and ncaa tournament wins is: "+str(kendallTau))

plt.show()

# tournament_dates = helper.createTournamentDateList(seenGames_1011,seenGames_1112,seenGames_1213,seenGames_1314,seenGames_1415,seenGames_1516,seenGames_1617,seenGames_1718)

# #dict mapping a String identifier (year) to the teamRoadWins dict for that year
# teamWinPctAllYears = {}

# #dict mapping teamName str to road winning % 
# teamWinPctAllYears["1011"] = helper.teamWinPct(allGames_1011,tournament_dates)
# teamWinPctAllYears["1112"] = helper.teamWinPct(allGames_1112,tournament_dates)
# teamWinPctAllYears["1213"] = helper.teamWinPct(allGames_1213,tournament_dates)
# teamWinPctAllYears["1314"] = helper.teamWinPct(allGames_1314,tournament_dates)
# teamWinPctAllYears["1415"] = helper.teamWinPct(allGames_1415,tournament_dates)
# teamWinPctAllYears["1516"] = helper.teamWinPct(allGames_1516,tournament_dates)
# teamWinPctAllYears["1617"] = helper.teamWinPct(allGames_1617,tournament_dates)
# teamWinPctAllYears["1718"] = helper.teamWinPct(allGames_1718,tournament_dates)

# #todo: convert into a X NP Array -> roadWinPct and a Y NP Array -> tournamentTeamWins
# teamWinPct,tournamentWins = helper.createXYArrays(teamWinPctAllYears,tournamentWinsAllYears)
# teamWinPct = np.asarray(teamWinPct,dtype=float)
# tournamentWins = np.asarray(tournamentWins,dtype=int)

# #todo: plot tournamentTeamWins vs roadWinPct
# plt.plot(teamWinPct,tournamentWins,"ro")
# plt.xlabel("teamWinPct")
# plt.ylabel("tournamentWins")

# #todo: apply Kendall Tau Correlation for x=road win% and y=# of NCAA Tournament Wins
# kendallTau,p = stats.kendalltau(teamWinPct,tournamentWins)
# print("The Kendall Tau Correlation between team overall win pct and ncaa tournament wins is: "+str(kendallTau))

# plt.show()

#dict mapping a String identifier (year) to the teamRoadWins dict for that year
# homeWinPctAllYears = {}

# #dict mapping teamName str to road winning % 
# homeWinPctAllYears["1011"] = helper.homeWinPct(allGames_1011)
# homeWinPctAllYears["1112"] = helper.homeWinPct(allGames_1112)
# homeWinPctAllYears["1213"] = helper.homeWinPct(allGames_1213)
# homeWinPctAllYears["1314"] = helper.homeWinPct(allGames_1314)
# homeWinPctAllYears["1415"] = helper.homeWinPct(allGames_1415)
# homeWinPctAllYears["1516"] = helper.homeWinPct(allGames_1516)
# homeWinPctAllYears["1617"] = helper.homeWinPct(allGames_1617)
# homeWinPctAllYears["1718"] = helper.homeWinPct(allGames_1718)

# #todo: convert into a X NP Array -> roadWinPct and a Y NP Array -> tournamentTeamWins
# homeWinPct,tournamentWins = helper.createXYArrays(homeWinPctAllYears,tournamentWinsAllYears)
# homeWinPct = np.asarray(homeWinPct,dtype=float)
# tournamentWins = np.asarray(tournamentWins,dtype=int)

# #todo: plot tournamentTeamWins vs roadWinPct
# plt.plot(homeWinPct,tournamentWins,"ro")
# plt.xlabel("homeWinPct")
# plt.ylabel("tournamentWins")

# #todo: apply Kendall Tau Correlation for x=road win% and y=# of NCAA Tournament Wins
# kendallTau,p = stats.kendalltau(homeWinPct,tournamentWins)
# print("The Kendall Tau Correlation between team home win pct and ncaa tournament wins is: "+str(kendallTau))

# plt.show()

# neutralWinPctAllYears = {}

# #dict mapping teamName str to road winning % 
# neutralWinPctAllYears["1011"] = helper.neutralWinPct(allGames_1011,tournament_dates)
# neutralWinPctAllYears["1112"] = helper.neutralWinPct(allGames_1112,tournament_dates)
# neutralWinPctAllYears["1213"] = helper.neutralWinPct(allGames_1213,tournament_dates)
# neutralWinPctAllYears["1314"] = helper.neutralWinPct(allGames_1314,tournament_dates)
# neutralWinPctAllYears["1415"] = helper.neutralWinPct(allGames_1415,tournament_dates)
# neutralWinPctAllYears["1516"] = helper.neutralWinPct(allGames_1516,tournament_dates)
# neutralWinPctAllYears["1617"] = helper.neutralWinPct(allGames_1617,tournament_dates)
# neutralWinPctAllYears["1718"] = helper.neutralWinPct(allGames_1718,tournament_dates)

# #todo: convert into a X NP Array -> roadWinPct and a Y NP Array -> tournamentTeamWins
# neutralWinPct,tournamentWins = helper.createXYArrays(neutralWinPctAllYears,tournamentWinsAllYears)
# neutralWinPct = np.asarray(neutralWinPct,dtype=float)
# tournamentWins = np.asarray(tournamentWins,dtype=int)

# #todo: plot tournamentTeamWins vs roadWinPct
# plt.plot(neutralWinPct,tournamentWins,"ro")
# plt.xlabel("neutralWinPct")
# plt.ylabel("tournamentWins")

# #todo: apply Kendall Tau Correlation for x=road win% and y=# of NCAA Tournament Wins
# kendallTau,p = stats.kendalltau(neutralWinPct,tournamentWins)
# print("The Kendall Tau Correlation between team neutral win pct and ncaa tournament wins is: "+str(kendallTau))

# plt.show()
