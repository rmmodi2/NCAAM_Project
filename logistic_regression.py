from scipy import stats
import pandas as pd 
import numpy as np
import ncaam_helperfunctions as helper
import matplotlib.pyplot as plt


tournamentWinsAllYears,tournament_dates = helper.createTournamentWinsAllYears()

teamStatistics = helper.createTeamStatistics(tournamentWinsAllYears)

#first we need to normalize 
teams = pd.read_csv("Data/KaggleData/Teams.csv",header=0)

conferences = pd.read_csv("Data/KaggleData/TeamConferences.csv",header=0)

# print(teamStatistics["1011"]["North Carolina"])
#normalized = (old - mean) / (sdev)

def normalizeByYear(teamStatisticsYear):
    statsDicts = list(teamStatisticsYear.values())
    meanNonConfWinPct = sum(item['NonConfWinPct'] for item in statsDicts) / len(statsDicts)
    meanNetEFG = sum(item['netEFG%'] for item in statsDicts) / len(statsDicts)
    meanKenpom = sum(item['kenpomRk'] for item in statsDicts) / len(statsDicts)
    sdevNonConfWinPct = np.std([item['NonConfWinPct'] for item in statsDicts]) 
    sdevNetEFG = np.std([item['netEFG%'] for item in statsDicts]) 
    sdevKenpom = np.std([item['kenpomRk'] for item in statsDicts]) 
    for k in teamStatisticsYear.keys():
        teamStatisticsYear[k]['NonConfWinPct'] = (teamStatisticsYear[k]['NonConfWinPct']-meanNonConfWinPct)/sdevNonConfWinPct
        teamStatisticsYear[k]['netEFG%'] = (teamStatisticsYear[k]['netEFG%']-meanNetEFG)/sdevNetEFG
        teamStatisticsYear[k]['kenpomRk'] = (teamStatisticsYear[k]['kenpomRk']-meanKenpom)/sdevKenpom

normalizeByYear(teamStatistics["1011"])
normalizeByYear(teamStatistics["1112"])
normalizeByYear(teamStatistics["1213"])
normalizeByYear(teamStatistics["1314"])
normalizeByYear(teamStatistics["1415"])
normalizeByYear(teamStatistics["1516"])
normalizeByYear(teamStatistics["1617"])
normalizeByYear(teamStatistics["1718"])
# print(teamStatistics["1011"]["North Carolina"])

def normalizeByConference(teamStatisticsYear,teams,conferences):
    statsDicts = list(teamStatisticsYear.values())
    conferenceToStats = {}
    #first create the conference stats
    for k in teamStatisticsYear.keys():
        teamId = teams.loc[teams['TeamName']==k]['TeamID'].array[0]
        team_conference = conferences.loc[conferences['TeamID']==teamId]['ConfAbbrev'].array[0]
        if (team_conference in conferenceToStats.keys()):
            conferenceToStats[team_conference]['NonConfWinPct'].append(teamStatisticsYear[k]['NonConfWinPct'])
            conferenceToStats[team_conference]['netEFG%'].append(teamStatisticsYear[k]['netEFG%'])
            conferenceToStats[team_conference]['kenpomRk'].append(teamStatisticsYear[k]['kenpomRk'])
        else:
            conferenceToStats[team_conference] = {'NonConfWinPct': [teamStatisticsYear[k]['NonConfWinPct']]}
            conferenceToStats[team_conference]['netEFG%'] = [teamStatisticsYear[k]['netEFG%']]
            conferenceToStats[team_conference]['kenpomRk'] = [teamStatisticsYear[k]['kenpomRk']]
    for conf in conferenceToStats:
        ncwinpct = conferenceToStats[conf]['NonConfWinPct']
        netefg = conferenceToStats[conf]['netEFG%']
        kenpomrk = conferenceToStats[conf]['kenpomRk']
        conferenceToStats[conf]['NonConfWinPct'] = [sum(ncwinpct)/len(ncwinpct),np.std(ncwinpct)]
        conferenceToStats[conf]['netEFG%'] = [sum(netefg)/len(netefg),np.std(netefg)]
        conferenceToStats[conf]['kenpomRk'] = [sum(kenpomrk)/len(kenpomrk),np.std(kenpomrk)]
    for k in teamStatisticsYear.keys():
        teamId = teams.loc[teams['TeamName']==k]['TeamID'].array[0]
        team_conference = conferences.loc[conferences['TeamID']==teamId]['ConfAbbrev'].array[0]
        teamStatisticsYear[k]['NonConfWinPct'] = (teamStatisticsYear[k]['NonConfWinPct'] - conferenceToStats[team_conference]['NonConfWinPct'][0]) / conferenceToStats[team_conference]['NonConfWinPct'][1]
        teamStatisticsYear[k]['netEFG%'] = (teamStatisticsYear[k]['netEFG%'] - conferenceToStats[team_conference]['netEFG%'][0]) / conferenceToStats[team_conference]['netEFG%'][1]
        teamStatisticsYear[k]['kenpomRk'] = (teamStatisticsYear[k]['kenpomRk'] - conferenceToStats[team_conference]['kenpomRk'][0]) / conferenceToStats[team_conference]['kenpomRk'][1]


normalizeByConference(teamStatistics["1011"],teams,conferences)
# normalizeByConference(teamStatistics["1112"],teams,conferences)
# normalizeByConference(teamStatistics["1213"],teams,conferences)
# normalizeByConference(teamStatistics["1314"],teams,conferences)
# normalizeByConference(teamStatistics["1415"],teams,conferences)
# normalizeByConference(teamStatistics["1516"],teams,conferences)
# normalizeByConference(teamStatistics["1617"],teams,conferences)
# normalizeByConference(teamStatistics["1718"],teams,conferences)
# print(teamStatistics["1011"]["North Carolina"])


