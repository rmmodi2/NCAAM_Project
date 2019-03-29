import sys
from scipy import stats
import pandas as pd 
import numpy as np
import ncaam_helperfunctions as helper
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
import random


tournamentWinsAllYears,tournament_dates = helper.createTournamentWinsAllYears()

teamStatistics = helper.createTeamStatistics(tournamentWinsAllYears)

#first we need to normalize 
teams = pd.read_csv("Data/KaggleData/Teams.csv",header=0)

conferences = pd.read_csv("Data/KaggleData/TeamConferences.csv",header=0)

# print(teamStatistics["1011"]["Notre Dame"])
#normalized = (old - mean) / (sdev)

teamStatisticsMatrix = helper.createCorrelationMatrix(teamStatistics)
print(teamStatisticsMatrix.corr())


def normalizeByYear(teamStatisticsYear):
    statsDicts = list(teamStatisticsYear.values())
    # meanNonConfWinPct = sum(item['NonConfWinPct'] for item in statsDicts) / len(statsDicts)
    # meanOverallWinPct = sum(item['OverallWinPct'] for item in statsDicts) / len(statsDicts)
    # meanRoadWinPct = sum(item['RoadWinPct'] for item in statsDicts) / len(statsDicts)
    meanNetEFG = sum([item['netEFG%'] for item in statsDicts]) / len(statsDicts)
    # meanKenpom = sum(item['kenpomRk'] for item in statsDicts) / len(statsDicts)
    meanNetTRB = sum([item['netTRB%'] for item in statsDicts]) / len(statsDicts)
    meanNetTOV = sum([item['netTOV%'] for item in statsDicts]) / len(statsDicts)
    meanNetBLK = sum([item['netBLK%'] for item in statsDicts]) / len(statsDicts)
    meanPreseason = sum([item['preseasonRk'] for item in statsDicts]) / len(statsDicts)
    meanDiffRk = sum([item['diffRk'] for item in statsDicts]) / len(statsDicts)
    meanTS = sum([item['netTS%'] for item in statsDicts]) / len(statsDicts)
#     meanNCAAWinPct = sum([item['winPctNCAA'] for item in statsDicts]) / len(statsDicts)
    meanTop50WinPct = sum([item['winPctTop50'] for item in statsDicts]) / len(statsDicts)
    meanTop100WinPct = sum([item['winPctTop100'] for item in statsDicts]) / len(statsDicts)
#     meanSOS = sum(item['SOS'] for item in statsDicts) / len(statsDicts)
#     meanConfWinPct = sum(item['ConfWinPct'] for item in statsDicts) / len(statsDicts)
    # sdevNonConfWinPct = np.std([item['NonConfWinPct'] for item in statsDicts]) 
    # sdevOverallWinPct = np.std([item['OverallWinPct'] for item in statsDicts]) 
    # sdevRoadWinPct = np.std([item['RoadWinPct'] for item in statsDicts]) 
    sdevNetEFG = np.std([item['netEFG%'] for item in statsDicts]) 
    # sdevKenpom = np.std([item['kenpomRk'] for item in statsDicts])
    sdevPreseason = np.std([item['preseasonRk'] for item in statsDicts])
    sdevNetTRB = np.std([item['netTRB%'] for item in statsDicts])
    sdevNetTOV = np.std([item['netTOV%'] for item in statsDicts]) 
    sdevNetBLK = np.std([item['netBLK%'] for item in statsDicts]) 
    sdevDiffRk = np.std([item['diffRk'] for item in statsDicts])
    sdevTS = np.std([item['netTS%'] for item in statsDicts])
#     sdevNCAAWinPct = np.std([item['winPctNCAA'] for item in statsDicts])
    sdevTop50WinPct = np.std([item['winPctTop50'] for item in statsDicts])
    sdevTop100WinPct = np.std([item['winPctTop100'] for item in statsDicts])
#     sdevSOS = np.std([item['SOS'] for item in statsDicts])
#     sdevConfWinPct = np.std([item['ConfWinPct'] for item in statsDicts])
    for k in teamStatisticsYear.keys():
        # teamStatisticsYear[k]['NonConfWinPct'] = (teamStatisticsYear[k]['NonConfWinPct']-meanNonConfWinPct)/sdevNonConfWinPct
        # teamStatisticsYear[k]['OverallWinPct'] = (teamStatisticsYear[k]['OverallWinPct']-meanOverallWinPct)/sdevOverallWinPct
        # teamStatisticsYear[k]['RoadWinPct'] = (teamStatisticsYear[k]['RoadWinPct']-meanRoadWinPct)/sdevRoadWinPct
        teamStatisticsYear[k]['netEFG%'] = (teamStatisticsYear[k]['netEFG%']-meanNetEFG)/sdevNetEFG
        # teamStatisticsYear[k]['kenpomRk'] = (teamStatisticsYear[k]['kenpomRk']-meanKenpom)/sdevKenpom
        teamStatisticsYear[k]['preseasonRk'] = (teamStatisticsYear[k]['preseasonRk']-meanPreseason)/sdevPreseason
        teamStatisticsYear[k]['netTRB%'] = (teamStatisticsYear[k]['netTRB%']-meanNetTRB)/sdevNetTRB
        teamStatisticsYear[k]['netTOV%'] = (teamStatisticsYear[k]['netTOV%']-meanNetTOV)/sdevNetTOV
        teamStatisticsYear[k]['netBLK%'] = (teamStatisticsYear[k]['netBLK%']-meanNetBLK)/sdevNetBLK
        teamStatisticsYear[k]['diffRk'] = (teamStatisticsYear[k]['diffRk']-meanDiffRk)/sdevDiffRk
        teamStatisticsYear[k]['netTS%'] = (teamStatisticsYear[k]['netTS%']-meanTS)/sdevTS
        # teamStatisticsYear[k]['winPctNCAA'] = (teamStatisticsYear[k]['winPctNCAA']-meanNCAAWinPct)/sdevNCAAWinPct
        teamStatisticsYear[k]['winPctTop50'] = (teamStatisticsYear[k]['winPctTop50']-meanTop50WinPct)/sdevTop50WinPct
        teamStatisticsYear[k]['winPctTop100'] = (teamStatisticsYear[k]['winPctTop100']-meanTop100WinPct)/sdevTop100WinPct
        # teamStatisticsYear[k]['SOS'] = (teamStatisticsYear[k]['SOS']-meanSOS)/sdevSOS
        # teamStatisticsYear[k]['ConfWinPct'] = (teamStatisticsYear[k]['ConfWinPct']-meanConfWinPct)/sdevConfWinPct

print("now we are normalizing by year")
normalizeByYear(teamStatistics[2010])
normalizeByYear(teamStatistics[2011])
normalizeByYear(teamStatistics[2012])
normalizeByYear(teamStatistics[2013])
normalizeByYear(teamStatistics[2014])
normalizeByYear(teamStatistics[2015])
normalizeByYear(teamStatistics[2016])
normalizeByYear(teamStatistics[2017])
normalizeByYear(teamStatistics[2018])
normalizeByYear(teamStatistics[2019])
# print(teamStatistics["1011"]["Notre Dame"])

# def normalizeByConference(teamStatisticsYear,teams,conferences,year):
#     statsDicts = list(teamStatisticsYear.values())
#     conferenceToStats = {}
#     #first create the conference stats
#     for k in teamStatisticsYear.keys():
#         teamId = teams.loc[teams['TeamName']==k]['TeamID'].array[0]
#         team_conference = conferences.loc[conferences['TeamID']==teamId]
#         team_conference = team_conference.loc[team_conference['Season']==year]['ConfAbbrev'].array[0]
#         if (team_conference in conferenceToStats.keys()):
#             conferenceToStats[team_conference]['NonConfWinPct'].append(teamStatisticsYear[k]['NonConfWinPct'])
#             conferenceToStats[team_conference]['netEFG%'].append(teamStatisticsYear[k]['netEFG%'])
#             conferenceToStats[team_conference]['kenpomRk'].append(teamStatisticsYear[k]['kenpomRk'])
#             conferenceToStats[team_conference]['netTRB%'].append(teamStatisticsYear[k]['netTRB%'])
#             conferenceToStats[team_conference]['netTOV%'].append(teamStatisticsYear[k]['netTOV%'])
#         else:
#             conferenceToStats[team_conference] = {'NonConfWinPct': [teamStatisticsYear[k]['NonConfWinPct']]}
#             conferenceToStats[team_conference]['netEFG%'] = [teamStatisticsYear[k]['netEFG%']]
#             conferenceToStats[team_conference]['kenpomRk'] = [teamStatisticsYear[k]['kenpomRk']]
#             conferenceToStats[team_conference]['netTRB%'] = [teamStatisticsYear[k]['netTRB%']]
#             conferenceToStats[team_conference]['netTOV%'] = [teamStatisticsYear[k]['netTOV%']]
#     for conf in conferenceToStats:
#         # if (conf == 'acc'):
#         #     print(conferenceToStats[conf])
#         ncwinpct = conferenceToStats[conf]['NonConfWinPct']
#         netefg = conferenceToStats[conf]['netEFG%']
#         kenpomrk = conferenceToStats[conf]['kenpomRk']
#         nettrb = conferenceToStats[conf]['netTRB%']
#         nettov = conferenceToStats[conf]['netTOV%']
#         conferenceToStats[conf]['NonConfWinPct'] = [sum(ncwinpct)/len(ncwinpct),np.std(ncwinpct)]
#         conferenceToStats[conf]['netEFG%'] = [sum(netefg)/len(netefg),np.std(netefg)]
#         conferenceToStats[conf]['kenpomRk'] = [sum(kenpomrk)/len(kenpomrk),np.std(kenpomrk)]
#         conferenceToStats[conf]['netTRB%'] = [sum(nettrb)/len(nettrb),np.std(nettrb)]
#         conferenceToStats[conf]['netTOV%'] = [sum(nettov)/len(nettov),np.std(nettov)]
#     for k in teamStatisticsYear.keys():
#         teamId = teams.loc[teams['TeamName']==k]['TeamID'].array[0]
#         team_conference = conferences.loc[conferences['TeamID']==teamId]
#         team_conference = team_conference.loc[team_conference['Season']==year]['ConfAbbrev'].array[0]
#         if (conferenceToStats[team_conference]['NonConfWinPct'][1]) != 0:
#             teamStatisticsYear[k]['NonConfWinPct'] = (teamStatisticsYear[k]['NonConfWinPct'] - conferenceToStats[team_conference]['NonConfWinPct'][0]) / conferenceToStats[team_conference]['NonConfWinPct'][1]
#         if (conferenceToStats[team_conference]['netEFG%'][1] != 0):
#             teamStatisticsYear[k]['netEFG%'] = (teamStatisticsYear[k]['netEFG%'] - conferenceToStats[team_conference]['netEFG%'][0]) / conferenceToStats[team_conference]['netEFG%'][1]
#         if (conferenceToStats[team_conference]['kenpomRk'][1] != 0):    
#             teamStatisticsYear[k]['kenpomRk'] = (teamStatisticsYear[k]['kenpomRk'] - conferenceToStats[team_conference]['kenpomRk'][0]) / conferenceToStats[team_conference]['kenpomRk'][1]
#         if (conferenceToStats[team_conference]['netTRB%'][1] != 0):    
#             teamStatisticsYear[k]['netTRB%'] = (teamStatisticsYear[k]['netTRB%'] - conferenceToStats[team_conference]['netTRB%'][0]) / conferenceToStats[team_conference]['netTRB%'][1]
#         if (conferenceToStats[team_conference]['netTOV%'][1] != 0):    
#             teamStatisticsYear[k]['netTOV%'] = (teamStatisticsYear[k]['netTOV%'] - conferenceToStats[team_conference]['netTOV%'][0]) / conferenceToStats[team_conference]['netTOV%'][1]

tournamentGamesData = helper.getTournamentGames()
# train, validation = train_test_split(tournamentGamesData, test_size=0.1)
train = tournamentGamesData[tournamentGamesData['Season']!=2019]
validation = tournamentGamesData[tournamentGamesData['Season']==2019]
x,y,gamesInfo = helper.createXYLogisticRegression(teamStatistics,tournamentGamesData,False)


######### FOR LOGISTIC REGRESSION ###########

# logRegModel = GridSearchCV(LogisticRegression(solver='lbfgs',penalty='l2'),param_grid={"C":[.0001,.001,.01,.1,1,10,100,1000]},cv=10).fit(x,y)

# print(logRegModel.best_params_)
# print(logRegModel.best_score_)
# # print(logRegModel.cv_results_)

######### FOR RANDOM FORESTS ##########

# rf = RandomForestClassifier()

# # n_estimators = [int(x) for x in np.linspace(start = 200, stop = 2000, num = 10)]
# # max_features = ['auto', 'sqrt']
# # max_depth = [int(x) for x in np.linspace(10, 110, num = 11)]
# # max_depth.append(None)
# # min_samples_split = [2, 5, 10]
# # min_samples_leaf = [1, 2, 4]
# # bootstrap = [True, False]

# param_tries={
#         "n_estimators":[100,200,300,400,500],
#         # "n_estimators":[300,400,500],
#         # "n_estimators":[300],
#         # "min_samples_split":[2,3,4,5,6,7,8,9,10],
#         'min_samples_split':[10,20,30,40,50,75,100,150,200],
#         # "min_samples_leaf":[1,2,3,4,5],
#         'min_samples_leaf':[10,15,20,30,50,75,100,150,200],
#         'max_features':[None],
#         'max_depth':[5,10,20,30,40,50,60,70],
#         'bootstrap':[True]}

# #helps narrow down to which hyperparameter options are best

# randomForestModel = RandomizedSearchCV(estimator = rf, param_distributions = param_tries, n_iter = 100, cv = 10, verbose=2, random_state=42, n_jobs = -1).fit(x,y)
# print(randomForestModel.best_score_)
# print(randomForestModel.best_params_)


###### THIS IS OUR ACTUAL TEST RUN #######


x,y,gamesInfo = helper.createXYLogisticRegression(teamStatistics,train,False)

model = RandomForestClassifier(n_estimators=200,min_samples_split=10,min_samples_leaf=10,max_features=None,max_depth=20,bootstrap=True).fit(x,y)

validation = helper.createallpossiblematchups(2019)

listofallgames=pd.read_csv("/Users/ronakmodi/Desktop/NCAAM_Project/Data/KaggleData/SampleSubmissionStage2.csv",header=0)

# x,y,gamesInfo = helper.createXYLogisticRegression(teamStatistics,validation,True)
x,gamesInfo = helper.create2019(teamStatistics[2019],listofallgames)

y = model.predict_proba(x)

print(y)

model_results = pd.DataFrame(y)

print(model_results)

gamesInfo.reset_index(drop=True, inplace=True)
model_results.reset_index(drop=True, inplace=True)
listofallgames.reset_index(drop=True,inplace=True)

forcsv = pd.concat([gamesInfo, model_results], axis=1)
forkaggle = pd.concat([listofallgames, model_results],axis=1)

print(forcsv)

# forcsv.to_csv("resultsofmodel.csv")
forkaggle.to_csv("pleasejesuschristsubmitproperlytokaggle.csv")






