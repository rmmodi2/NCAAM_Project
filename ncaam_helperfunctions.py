#helper functions for ncaam_analysis
import pandas as pd 
import numpy as np


dtype_dict = {'Id':float,'Date':str,'Schl':str,'Location':str,'Opp':str,"Result":str,'MP':float,'FG':float,'FGA':float,'FG%':float,'2P':float,'2PA':float,'2P%':float,'3P':float,'3PA':float,'3P%':float,'FT':float,"FTA":float,'FT%':float,'PTS':float}
skiprows_list = []
for i in range(100000):
    skiprows_list.append(22*i)
    skiprows_list.append(22*i+1)
na_values_list = ["School","Id","Date","Schl","Location","Opp","Result","MP","FG","FGA","FG%","2P",'2PA',"2P%","3P","3PA","3P%","FT","FTA","FT%","PTS"]

#todo: read_csv into a seperate data frame for each year

# allGames_1011_1718 = pd.read_csv("/Users/ronakmodi/Desktop/NCAAM_Data/Data/NCAAM_AllGames_1011_1718.csv", names=dtype_dict.keys(),skiprows=skiprows_list, dtype=dtype_dict,na_values=na_values_list)
tournamentGames_1011_1718 = pd.read_csv("Data/NCAAM_TournamentGames_1011_1718.csv", header=0,na_values=na_values_list)

tournamentGames_1011_1718 = tournamentGames_1011_1718.dropna()
# print(tournamentGames_1011_1718)

allGames_1011 = pd.read_csv("Data/AllGames/NCAAM_AllGames_1011.csv", names=dtype_dict.keys(),skiprows=skiprows_list, dtype=dtype_dict,na_values=na_values_list)
allGames_1112 = pd.read_csv("Data/AllGames/NCAAM_AllGames_1112.csv", names=dtype_dict.keys(),skiprows=skiprows_list, dtype=dtype_dict,na_values=na_values_list)
allGames_1213 = pd.read_csv("Data/AllGames/NCAAM_AllGames_1213.csv", names=dtype_dict.keys(),skiprows=skiprows_list, dtype=dtype_dict,na_values=na_values_list)
allGames_1314 = pd.read_csv("Data/AllGames/NCAAM_AllGames_1314.csv", names=dtype_dict.keys(),skiprows=skiprows_list, dtype=dtype_dict,na_values=na_values_list)
allGames_1415 = pd.read_csv("Data/AllGames/NCAAM_AllGames_1415.csv", names=dtype_dict.keys(),skiprows=skiprows_list, dtype=dtype_dict,na_values=na_values_list)
allGames_1516 = pd.read_csv("Data/AllGames/NCAAM_AllGames_1516.csv", names=dtype_dict.keys(),skiprows=skiprows_list, dtype=dtype_dict,na_values=na_values_list)
allGames_1617 = pd.read_csv("Data/AllGames/NCAAM_AllGames_1617.csv", names=dtype_dict.keys(),skiprows=skiprows_list, dtype=dtype_dict,na_values=na_values_list)
allGames_1718 = pd.read_csv("Data/AllGames/NCAAM_AllGames_1718.csv", names=dtype_dict.keys(),skiprows=skiprows_list, dtype=dtype_dict,na_values=na_values_list)

tournamentGames_1011 = pd.read_csv("Data/TournamentGames/NCAAM_TournamentGames_1011.csv", names=dtype_dict.keys(),skiprows=skiprows_list, dtype=dtype_dict,na_values=na_values_list)
tournamentGames_1112 = pd.read_csv("Data/TournamentGames/NCAAM_TournamentGames_1112.csv", names=dtype_dict.keys(),skiprows=skiprows_list, dtype=dtype_dict,na_values=na_values_list)
tournamentGames_1213 = pd.read_csv("Data/TournamentGames/NCAAM_TournamentGames_1213.csv", names=dtype_dict.keys(),skiprows=skiprows_list, dtype=dtype_dict,na_values=na_values_list)
tournamentGames_1314 = pd.read_csv("Data/TournamentGames/NCAAM_TournamentGames_1314.csv", names=dtype_dict.keys(),skiprows=skiprows_list, dtype=dtype_dict,na_values=na_values_list)
tournamentGames_1415 = pd.read_csv("Data/TournamentGames/NCAAM_TournamentGames_1415.csv", names=dtype_dict.keys(),skiprows=skiprows_list, dtype=dtype_dict,na_values=na_values_list)
tournamentGames_1516 = pd.read_csv("Data/TournamentGames/NCAAM_TournamentGames_1516.csv", names=dtype_dict.keys(),skiprows=skiprows_list, dtype=dtype_dict,na_values=na_values_list)
tournamentGames_1617 = pd.read_csv("Data/TournamentGames/NCAAM_TournamentGames_1617.csv", names=dtype_dict.keys(),skiprows=skiprows_list, dtype=dtype_dict,na_values=na_values_list)
tournamentGames_1718 = pd.read_csv("Data/TournamentGames/NCAAM_TournamentGames_1718.csv", names=dtype_dict.keys(),skiprows=skiprows_list, dtype=dtype_dict,na_values=na_values_list)

kenpomUseCols = [0,1,4,5,6]
kenpomDTypeDict= {'Rk':float,'Team':str,'AdjEM':float,'AdjO':float,'AdjD':float}
skiprows_list_kenpom = []
# for i in range(400):
#     skiprows_list_kenpom.append(41 + 42*i)
kenpom_na_values_list = list(kenpomDTypeDict.keys())

kenpom_1011 = pd.read_csv("Data/KenpomStats/NCAAM_Kenpom_1011.csv",names=kenpomDTypeDict.keys(),skiprows=skiprows_list_kenpom,dtype=kenpomDTypeDict,na_values=kenpom_na_values_list,usecols=kenpomUseCols)
kenpom_1112 = pd.read_csv("Data/KenpomStats/NCAAM_Kenpom_1112.csv",names=kenpomDTypeDict.keys(),skiprows=skiprows_list_kenpom,dtype=kenpomDTypeDict,na_values=kenpom_na_values_list,usecols=kenpomUseCols)
kenpom_1213 = pd.read_csv("Data/KenpomStats/NCAAM_Kenpom_1213.csv",names=kenpomDTypeDict.keys(),skiprows=skiprows_list_kenpom,dtype=kenpomDTypeDict,na_values=kenpom_na_values_list,usecols=kenpomUseCols)
kenpom_1314 = pd.read_csv("Data/KenpomStats/NCAAM_Kenpom_1314.csv",names=kenpomDTypeDict.keys(),skiprows=skiprows_list_kenpom,dtype=kenpomDTypeDict,na_values=kenpom_na_values_list,usecols=kenpomUseCols)
kenpom_1415 = pd.read_csv("Data/KenpomStats/NCAAM_Kenpom_1415.csv",names=kenpomDTypeDict.keys(),skiprows=skiprows_list_kenpom,dtype=kenpomDTypeDict,na_values=kenpom_na_values_list,usecols=kenpomUseCols)
kenpom_1516 = pd.read_csv("Data/KenpomStats/NCAAM_Kenpom_1516.csv",names=kenpomDTypeDict.keys(),skiprows=skiprows_list_kenpom,dtype=kenpomDTypeDict,na_values=kenpom_na_values_list,usecols=kenpomUseCols)
kenpom_1617 = pd.read_csv("Data/KenpomStats/NCAAM_Kenpom_1617.csv",names=kenpomDTypeDict.keys(),skiprows=skiprows_list_kenpom,dtype=kenpomDTypeDict,na_values=kenpom_na_values_list,usecols=kenpomUseCols)
kenpom_1718 = pd.read_csv("Data/KenpomStats/NCAAM_Kenpom_1718.csv",names=kenpomDTypeDict.keys(),skiprows=skiprows_list_kenpom,dtype=kenpomDTypeDict,na_values=kenpom_na_values_list,usecols=kenpomUseCols)


teamStatsUseCols = [0,1,3,4,6,8,9,16,17,21,25,26,28]
teamStatsDTypeDict={'Rk':float,'School':str,'TotalW':float,'TotalL':float,'SRS':float, 'ConfW':float,'ConfL':float,'Pace':float,'ORtg':float,'TRB%':float,'eFG%':float,'TOV%':float,'FT/FGA':float,}
# skiprows_list_teamStats = skiprows_list
skiprows_list_teamStats = []
teamStats_na_values_list = list(teamStatsDTypeDict.keys()) + ["School Advanced","Opponent Advanced",'Overall','Conf.','W','L','SRS']

teamStats_1011 = pd.read_csv("Data/TeamStats/NCAAM_TeamStats_1011.csv",names=teamStatsDTypeDict.keys(),skiprows=skiprows_list_teamStats,dtype=teamStatsDTypeDict,na_values=teamStats_na_values_list,usecols=teamStatsUseCols)
teamStats_1112 = pd.read_csv("Data/TeamStats/NCAAM_TeamStats_1112.csv",names=teamStatsDTypeDict.keys(),skiprows=skiprows_list_teamStats,dtype=teamStatsDTypeDict,na_values=teamStats_na_values_list,usecols=teamStatsUseCols)
teamStats_1213 = pd.read_csv("Data/TeamStats/NCAAM_TeamStats_1213.csv",names=teamStatsDTypeDict.keys(),skiprows=skiprows_list_teamStats,dtype=teamStatsDTypeDict,na_values=teamStats_na_values_list,usecols=teamStatsUseCols)
teamStats_1314 = pd.read_csv("Data/TeamStats/NCAAM_TeamStats_1314.csv",names=teamStatsDTypeDict.keys(),skiprows=skiprows_list_teamStats,dtype=teamStatsDTypeDict,na_values=teamStats_na_values_list,usecols=teamStatsUseCols)
teamStats_1415 = pd.read_csv("Data/TeamStats/NCAAM_TeamStats_1415.csv",names=teamStatsDTypeDict.keys(),skiprows=skiprows_list_teamStats,dtype=teamStatsDTypeDict,na_values=teamStats_na_values_list,usecols=teamStatsUseCols)
teamStats_1516 = pd.read_csv("Data/TeamStats/NCAAM_TeamStats_1516.csv",names=teamStatsDTypeDict.keys(),skiprows=skiprows_list_teamStats,dtype=teamStatsDTypeDict,na_values=teamStats_na_values_list,usecols=teamStatsUseCols)
teamStats_1617 = pd.read_csv("Data/TeamStats/NCAAM_TeamStats_1617.csv",names=teamStatsDTypeDict.keys(),skiprows=skiprows_list_teamStats,dtype=teamStatsDTypeDict,na_values=teamStats_na_values_list,usecols=teamStatsUseCols)
teamStats_1718 = pd.read_csv("Data/TeamStats/NCAAM_TeamStats_1718.csv",names=teamStatsDTypeDict.keys(),skiprows=skiprows_list_teamStats,dtype=teamStatsDTypeDict,na_values=teamStats_na_values_list,usecols=teamStatsUseCols)

oppTeamStats_1011 = pd.read_csv("Data/TeamStats/NCAAM_OppTeamStats_1011.csv",names=teamStatsDTypeDict.keys(),skiprows=skiprows_list_teamStats,dtype=teamStatsDTypeDict,na_values=teamStats_na_values_list,usecols=teamStatsUseCols)
oppTeamStats_1112 = pd.read_csv("Data/TeamStats/NCAAM_OppTeamStats_1112.csv",names=teamStatsDTypeDict.keys(),skiprows=skiprows_list_teamStats,dtype=teamStatsDTypeDict,na_values=teamStats_na_values_list,usecols=teamStatsUseCols)
oppTeamStats_1213 = pd.read_csv("Data/TeamStats/NCAAM_OppTeamStats_1213.csv",names=teamStatsDTypeDict.keys(),skiprows=skiprows_list_teamStats,dtype=teamStatsDTypeDict,na_values=teamStats_na_values_list,usecols=teamStatsUseCols)
oppTeamStats_1314 = pd.read_csv("Data/TeamStats/NCAAM_OppTeamStats_1314.csv",names=teamStatsDTypeDict.keys(),skiprows=skiprows_list_teamStats,dtype=teamStatsDTypeDict,na_values=teamStats_na_values_list,usecols=teamStatsUseCols)
oppTeamStats_1415 = pd.read_csv("Data/TeamStats/NCAAM_OppTeamStats_1415.csv",names=teamStatsDTypeDict.keys(),skiprows=skiprows_list_teamStats,dtype=teamStatsDTypeDict,na_values=teamStats_na_values_list,usecols=teamStatsUseCols)
oppTeamStats_1516 = pd.read_csv("Data/TeamStats/NCAAM_OppTeamStats_1516.csv",names=teamStatsDTypeDict.keys(),skiprows=skiprows_list_teamStats,dtype=teamStatsDTypeDict,na_values=teamStats_na_values_list,usecols=teamStatsUseCols)
oppTeamStats_1617 = pd.read_csv("Data/TeamStats/NCAAM_OppTeamStats_1617.csv",names=teamStatsDTypeDict.keys(),skiprows=skiprows_list_teamStats,dtype=teamStatsDTypeDict,na_values=teamStats_na_values_list,usecols=teamStatsUseCols)
oppTeamStats_1718 = pd.read_csv("Data/TeamStats/NCAAM_OppTeamStats_1718.csv",names=teamStatsDTypeDict.keys(),skiprows=skiprows_list_teamStats,dtype=teamStatsDTypeDict,na_values=teamStats_na_values_list,usecols=teamStatsUseCols)


#helper function to convert kenpom into correct format
#kenpomToSRef = {"IncorrectKenPomTeamName":"CorrectSRefTeamName"}
#^^^^^^use for hardcoding names that don't match the "St." / "State" pattern
def convertTeamNames(kenpom,kenpomflag):
    tournamentSeeds = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
    
    def createKenpomTeamName(team,numberFlag,stateFlag):
        # print('we are editing the name') 
        name = team[0]
        for i in range(1,len(team)):
            if (numberFlag and stateFlag and i == (len(team)-2)):
                name+=' State'
                return name
            if ((not numberFlag) and stateFlag and i == (len(team)-1)):
                name+=' State'
                return name
            if ((not stateFlag) and numberFlag and i == (len(team)-1)):
                return name
            name+=" "+team[i]
        return name

    if (kenpomflag):        
        for index,row in kenpom.iterrows():
            if (not pd.isnull(row['Team'])):
                # first check if there's a number in the name, get rid of it
                #then if there's a St. at the end of the string, change the St. to State
                if (row['Team'] == 'George Mason 8'):
                    kenpom.at[index,'Team'] = 'George Mason'
                    continue
                if (row['Team'] == 'VCU 11'):
                    kenpom.at[index,'Team'] = 'VCU'
                    continue
                if (row['Team'] == 'Arkansas Little Rock 16' or row['Team'] == 'Arkansas Little Rock 12'):
                    kenpom.at[index,'Team'] = 'Little Rock'
                    continue
                if (row['Team'] == 'UC Santa Barbara 15'):
                    kenpom.at[index,'Team'] = 'UCSB'
                    continue    
                team = str.split(row['Team'])
                if (team[0] == 'Connecticut'):
                    # print("did we find uconn?")
                    kenpom.at[index,'Team'] = 'UConn'
                    continue
                if (team[0] == 'Albany'):
                    # print("did we find uconn?")
                    kenpom.at[index,'Team'] = 'Albany (NY)'
                    continue
                if (team[0] == 'Pittsburgh'):
                    # print("did we find uconn?")
                    kenpom.at[index,'Team'] = 'Pitt'
                    continue
                if (team[0] == 'UC' and team[1] == 'Irvine'):
                    # print("did we find uconn?")
                    kenpom.at[index,'Team'] = 'UC-Irvine'
                    continue
                if (team[0] == 'UC' and team[1] == 'Davis'):
                    # print("did we find uconn?")
                    kenpom.at[index,'Team'] = 'UC-Davis'
                    continue
                if (team[0] == 'LIU' and team[1] == 'Brooklyn'):
                    kenpom.at[index,'Team'] = 'LIU-Brooklyn'
                    continue
                if (team[0] == 'St.' and team[1] == "John's"):
                    kenpom.at[index,'Team'] = "St. John's (NY)"
                    continue
                if (team[0] == 'Boston' and team[1] == "University"):
                    kenpom.at[index,'Team'] = "Boston U."
                    continue
                if (team[0] == 'Loyola' and team[1] == 'MD'):
                    kenpom.at[index,'Team'] = "Loyola (MD)"
                    continue
                if (team[0] == 'Loyola' and team[1] == 'Chicago'):
                    kenpom.at[index,'Team'] = "Loyola (IL)"
                    continue
                if (team[0] == 'Miami' and team[1] == "FL"):
                    kenpom.at[index,'Team'] = "Miami (FL)"
                    continue
                if (team[0] == 'Louisiana' and team[1] == "Lafayette"):
                    kenpom.at[index,'Team'] = "Louisiana"
                    continue
                # print("old name is "+row['Team'])
                if team[-1] in tournamentSeeds:
                    # print("seeded in ncaa tournament we're removing that")
                    if team[-2] == 'St.':
                        # print("ends in st. instead of state we're fixing that")
                        kenpom.at[index,'Team'] = createKenpomTeamName(team,True,True)
                    else:
                        kenpom.at[index,'Team'] = createKenpomTeamName(team,True,False)
                if team[-1] == 'St.':
                    # print("ends in st. instead of state we're fixing that")
                    kenpom.at[index,'Team'] = createKenpomTeamName(team,False,True)
                # print("new name is "+row['Team'])
    else:
        for index,row in kenpom.iterrows():
            if (not pd.isnull(row['School'])):
                # first check if there's a number in the name, get rid of it
                #then if there's a St. at the end of the string, change the St. to State
                if row['School'] == 'Virginia Commonwealth':
                    kenpom.at[index,'School'] = 'VCU'
                    continue
                if row['School'] == 'Pennsylvania':
                    kenpom.at[index,'School'] = 'Penn'
                    continue
                if row['School'] == 'Cal State Fullerton':
                    kenpom.at[index,'School'] = 'Cal St. Fullerton'
                    continue
                if (row['School'] == 'Long Island University'):
                    kenpom.at[index,'School'] = 'LIU-Brooklyn'
                    continue
                if (row['School'] == 'Brigham Young'):
                    kenpom.at[index,'School'] = 'BYU'
                    continue
                if (row['School'] == 'North Carolina-Asheville'):
                    kenpom.at[index,'School'] = 'UNC Asheville'
                    continue
                if (row['School'] == 'Connecticut'):
                    kenpom.at[index,'School'] = 'UConn'
                    continue
                if (row['School'] == 'UC-Santa Barbara'):
                    kenpom.at[index,'School'] = 'UCSB'
                    continue
                if (row['School'] == 'Texas-San Antonio'):
                    kenpom.at[index,'School'] = 'UTSA'
                    continue
                if (row['School'] == 'Pittsburgh'):
                    kenpom.at[index,'School'] = 'Pitt'
                    continue
                if (row['School'] == 'Nevada-Las Vegas'):
                    kenpom.at[index,'School'] = 'UNLV'
                    continue
                if (row['School'] == 'Boston University'):
                    kenpom.at[index,'School'] = 'Boston U.'
                    continue
                if (row['School'] == 'Alabama-Birmingham'):
                    kenpom.at[index,'School'] = 'UAB'
                    continue
                if (row['School'] == 'Southern California'):
                    kenpom.at[index,'School'] = 'USC'
                    continue
                if (row['School'] == "Saint Mary's (CA)"):
                    kenpom.at[index,'School'] = "Saint Mary's"
                    continue
                if (row['School'] == 'Southern Mississippi'):
                    kenpom.at[index,'School'] = 'Southern Miss'
                    continue
                if (row['School'] == 'University of California'):
                    kenpom.at[index,'School'] = 'California'
                    continue
                if (row['School'] == 'Detroit Mercy'):
                    kenpom.at[index,'School'] = 'Detroit'
                    continue
                if (row['School'] == 'Louisiana State'):
                    kenpom.at[index,'School'] = 'LSU'
                    continue
                if (row['School'] == 'Southern Methodist'):
                    kenpom.at[index,'School'] = 'SMU'
                    continue
                if (row['School'] == 'North Carolina-Wilmington'):
                    kenpom.at[index,'School'] = 'UNC Wilmington'
                    continue
                if (row['School'] == 'Cal State Bakersfield'):
                    kenpom.at[index,'School'] = 'Cal St. Bakersfield'
                    continue
                if (row['School'] == 'Maryland-Baltimore County'):
                    kenpom.at[index,'School'] = 'UMBC'
                    continue
                if (row['School'] == 'North Carolina-Greensboro'):
                    kenpom.at[index,'School'] = 'UNC Greensboro'
                    continue
                if (row['School'] == 'Texas Christian'):
                    kenpom.at[index,'School'] = 'TCU'
                    continue

# print(kenpom_1314.loc[kenpom_1314['Team']=='Louisiana Lafayette 14'])

convertTeamNames(kenpom_1011,True)
convertTeamNames(kenpom_1112,True)
convertTeamNames(kenpom_1213,True)
convertTeamNames(kenpom_1314,True)
convertTeamNames(kenpom_1415,True)
convertTeamNames(kenpom_1516,True)
convertTeamNames(kenpom_1617,True)
convertTeamNames(kenpom_1718,True)
convertTeamNames(teamStats_1011,False)
convertTeamNames(teamStats_1112,False)
convertTeamNames(teamStats_1213,False)
convertTeamNames(teamStats_1314,False)
convertTeamNames(teamStats_1415,False)
convertTeamNames(teamStats_1516,False)
convertTeamNames(teamStats_1617,False)
convertTeamNames(teamStats_1718,False)
convertTeamNames(oppTeamStats_1011,False)
convertTeamNames(oppTeamStats_1112,False)
convertTeamNames(oppTeamStats_1213,False)
convertTeamNames(oppTeamStats_1314,False)
convertTeamNames(oppTeamStats_1415,False)
convertTeamNames(oppTeamStats_1516,False)
convertTeamNames(oppTeamStats_1617,False)
convertTeamNames(oppTeamStats_1718,False)

# print(kenpom_1314.loc[kenpom_1314['Team']=='Louisiana'])
# print(kenpom_1011)
# print(kenpom_1011.loc[kenpom_1011['Team']=='Oakland'])
# print(teamStats_1011.loc[teamStats_1011['School']=='North Carolina State'])

teams = pd.read_csv("Data/KaggleData/Teams.csv",header=0)

masseyOrdinals = pd.read_csv("Data/KaggleData/MasseyOrdinals.csv",header=0)
masseyOrdinals = masseyOrdinals[masseyOrdinals['SystemName']=='POM']
masseyOrdinals = masseyOrdinals[masseyOrdinals['RankingDayNum']==133]

masseyOrdinals_0910 = masseyOrdinals[masseyOrdinals['Season']==2010]
masseyOrdinals_1011 = masseyOrdinals[masseyOrdinals['Season']==2011]
masseyOrdinals_1112 = masseyOrdinals[masseyOrdinals['Season']==2012]
masseyOrdinals_1213 = masseyOrdinals[masseyOrdinals['Season']==2013]
masseyOrdinals_1314 = masseyOrdinals[masseyOrdinals['Season']==2014]
masseyOrdinals_1415 = masseyOrdinals[masseyOrdinals['Season']==2015]
masseyOrdinals_1516 = masseyOrdinals[masseyOrdinals['Season']==2016]
masseyOrdinals_1617 = masseyOrdinals[masseyOrdinals['Season']==2017]
masseyOrdinals_1718 = masseyOrdinals[masseyOrdinals['Season']==2018]

def createTeamStatistics(tournamentWinsAllYears):
    teamStatistics = {}
    teamStatistics["1011"] = teamStats(teamStats_1011,oppTeamStats_1011,kenpom_1011,masseyOrdinals_1011,tournamentWinsAllYears["1011"],teams)
    teamStatistics["1112"] = teamStats(teamStats_1112,oppTeamStats_1112,kenpom_1112,masseyOrdinals_1112,tournamentWinsAllYears["1112"],teams)
    teamStatistics["1213"] = teamStats(teamStats_1213,oppTeamStats_1213,kenpom_1213,masseyOrdinals_1213,tournamentWinsAllYears["1213"],teams)
    teamStatistics["1314"] = teamStats(teamStats_1314,oppTeamStats_1314,kenpom_1314,masseyOrdinals_1314,tournamentWinsAllYears["1314"],teams)
    teamStatistics["1415"] = teamStats(teamStats_1415,oppTeamStats_1415,kenpom_1415,masseyOrdinals_1415,tournamentWinsAllYears["1415"],teams)
    teamStatistics["1516"] = teamStats(teamStats_1516,oppTeamStats_1516,kenpom_1516,masseyOrdinals_1516,tournamentWinsAllYears["1516"],teams)
    teamStatistics["1617"] = teamStats(teamStats_1617,oppTeamStats_1617,kenpom_1617,masseyOrdinals_1617,tournamentWinsAllYears["1617"],teams)
    teamStatistics["1718"] = teamStats(teamStats_1718,oppTeamStats_1718,kenpom_1718,masseyOrdinals_1718,tournamentWinsAllYears["1718"],teams)
    return teamStatistics

#####TO DO######
#helper function to generate needed teamStats for a given year
def teamStats(statsFor,statsAgainst,kenpom,massey,tournamentWins,teams):
    teamStats = {}
    statsFor = statsFor.dropna()
    list_of_teams = statsFor['School']
    # print(list_of_teams)
    for k in list_of_teams:
        # print(k)
        statsForRow = statsFor.loc[statsFor['School'] == k]
        statsAgainstRow = statsAgainst.loc[statsAgainst['School'] == k]
        kenpomRow = kenpom.loc[kenpom['Team'] == k]
        teamId = teams.loc[teams['TeamName']==k]['TeamID'].array[0]
        masseyRk = massey.loc[massey['TeamID']==teamId]['OrdinalRank'].array[0]
        statDict = {}
        statDict['kenpomRk'] = masseyRk
        if k in tournamentWins.keys():
            tourneywins = tournamentWins[k]
            if tourneywins == 6:
                tourneylosses = 0
            else:
                tourneylosses = 1
        else:
            tourneywins = 0
            tourneylosses = 0
        statDict['OverallWinPct'] = (statsForRow['TotalW'].array[0] - tourneywins)/(statsForRow['TotalL'].array[0]-tourneylosses + statsForRow['TotalW'].array[0] - tourneywins)
        statDict['NonConfWinPct'] = (statsForRow['TotalW'].array[0]-statsForRow['ConfW'].array[0]-tourneywins)/((statsForRow['TotalL'].array[0]-statsForRow['ConfL'].array[0]-tourneylosses) + (statsForRow['TotalW'].array[0]-statsForRow['ConfW'].array[0]-tourneywins))
        if (statsForRow['ConfL'].array[0] + statsForRow['ConfW'].array[0] == 0):
            statDict['ConfWinPct'] = statDict['NonConfWinPct']
        else:
            statDict['ConfWinPct'] = statsForRow['ConfW'].array[0] / (statsForRow['ConfL'].array[0] + statsForRow['ConfW'].array[0])
        statDict['eFG%'] = statsForRow['eFG%'].array[0]
        # print(statDict['eFG%'])
        statDict['eFG%Against'] = statsAgainstRow['eFG%'].array[0]
        statDict['netEFG%'] = statDict['eFG%'] - statDict['eFG%Against']
        statDict['TOV%'] = statsForRow['TOV%'].array[0]
        statDict['TOV%Against'] = statsAgainstRow['TOV%'].array[0]
        statDict['netTOV%'] = statDict['TOV%Against'] - statDict['TOV%']
        statDict['TRB%'] = statsForRow['TRB%'].array[0]
        statDict['TRB%Against'] = statsAgainstRow['TRB%'].array[0]
        statDict['netTRB%'] = statDict['TRB%'] - statDict['TRB%Against']
        statDict['FTRate'] = statsForRow['FT/FGA'].array[0]
        statDict['FTRateAgainst'] = statsAgainstRow['FT/FGA'].array[0]
        statDict['netFTRate'] = statDict['FTRate'] - statDict['FTRateAgainst']
        statDict['ORtg'] = statsForRow['ORtg'].array[0]
        statDict['DRtg'] = statsAgainstRow['ORtg'].array[0]
        statDict['netRtg'] = statDict['ORtg'] - statDict['DRtg']
        statDict['pace'] = statsForRow['Pace'].array[0]
        teamStats[k] = statDict
    return teamStats        


def createTournamentWinsAllYears():
    tournamentWinsAllYears = {}
    seenGames = {}
    tournamentWinsAllYears["1011"],seenGames["1011"] = tournamentTeamWins(tournamentGames_1011)
    tournamentWinsAllYears["1112"],seenGames["1112"] = tournamentTeamWins(tournamentGames_1112)
    tournamentWinsAllYears["1213"],seenGames["1213"] = tournamentTeamWins(tournamentGames_1213)
    tournamentWinsAllYears["1314"],seenGames["1314"] = tournamentTeamWins(tournamentGames_1314)
    tournamentWinsAllYears["1415"],seenGames["1415"] = tournamentTeamWins(tournamentGames_1415)
    tournamentWinsAllYears["1516"],seenGames["1516"] = tournamentTeamWins(tournamentGames_1516)
    tournamentWinsAllYears["1617"],seenGames["1617"] = tournamentTeamWins(tournamentGames_1617)
    tournamentWinsAllYears["1718"],seenGames["1718"] = tournamentTeamWins(tournamentGames_1718)
    return tournamentWinsAllYears,createTournamentDateList(seenGames)

def createRoadWinPctAllYears(tournamentDates):
    roadWinPctAllYears = {}
    roadWinPctAllYears["1011"] = roadWinPct(allGames_1011,tournamentDates)
    roadWinPctAllYears["1112"] = roadWinPct(allGames_1112,tournamentDates)
    roadWinPctAllYears["1213"] = roadWinPct(allGames_1213,tournamentDates)
    roadWinPctAllYears["1314"] = roadWinPct(allGames_1314,tournamentDates)
    roadWinPctAllYears["1415"] = roadWinPct(allGames_1415,tournamentDates)
    roadWinPctAllYears["1516"] = roadWinPct(allGames_1516,tournamentDates)
    roadWinPctAllYears["1617"] = roadWinPct(allGames_1617,tournamentDates)
    roadWinPctAllYears["1718"] = roadWinPct(allGames_1718,tournamentDates)
    return roadWinPctAllYears

def createTeamWinPctAllYears(tournamentDates):
    roadWinPctAllYears = {}
    roadWinPctAllYears["1011"] = teamWinPct(allGames_1011,tournamentDates)
    roadWinPctAllYears["1112"] = teamWinPct(allGames_1112,tournamentDates)
    roadWinPctAllYears["1213"] = teamWinPct(allGames_1213,tournamentDates)
    roadWinPctAllYears["1314"] = teamWinPct(allGames_1314,tournamentDates)
    roadWinPctAllYears["1415"] = teamWinPct(allGames_1415,tournamentDates)
    roadWinPctAllYears["1516"] = teamWinPct(allGames_1516,tournamentDates)
    roadWinPctAllYears["1617"] = teamWinPct(allGames_1617,tournamentDates)
    roadWinPctAllYears["1718"] = teamWinPct(allGames_1718,tournamentDates)
    return roadWinPctAllYears

#helper function to get every team's win total from a certain ncaa tournament
def tournamentTeamWins(tournamentGames):
    team_tournamentWins_1011 = {}
    seenGames_1011 = {}
    for index, row in tournamentGames.iterrows():
        if (not pd.isnull(row['Id'])):
            #gather relevant info from game
            team = row['Schl']
            result = row['Result'][0]
            oppTeam = row['Opp']
            #you have to comment this out if you are doing anything based on RECORD ##########
            if (team == "UMass"):
                team = "Massachusetts"
            if (team == 'Northern Colo.'):
                # print("found northern colo")
                team = 'Northern Colorado'
            if (team == "St. Peter's"):
                team = "Saint Peter's"
            if (team == "Western Ky."):
                team = "Western Kentucky"
            if (team == "New Mexico St."):
                team = "New Mexico State"
            if (team == "NC State"):
                team = "North Carolina State"
            if (team == "UNC"):
                team = "North Carolina"
            if (team == "Long Beach St."):
                team = "Long Beach State"
            if (team == "S Dakota St."):
                team = "South Dakota State"
            if (team == "Miss Val St"):
                team = "Mississippi Valley State"
            if (team == "Fla. Gulf Coast"):
                team = "Florida Gulf Coast"
            if (team == "N.C. A&T"):
                team = "North Carolina A&T"
            if (team == "NW St."):
                team = "Northwestern State"
            if (team == "Ole Miss"):
                team = "Mississippi"
            if (team == "Middle Tenn."):
                team = "Middle Tennessee"
            if (team == "Mt. St. Mary's"):
                team = "Mount St. Mary's"
            if (oppTeam == "Mt. St. Mary's"):
                oppTeam = "Mount St. Mary's"
            if (team == "Cal St Bakersfield"):
                team = "Cal St. Bakersfield"
            if (oppTeam == "Cal St Bakersfield"):
                oppTeam = "Cal St. Bakersfield"
            if (team == "Coastal Caro."):
                team = "Coastal Carolina"
            if (oppTeam == "Coastal Caro."):
                oppTeam = "Coastal Carolina"
            if (team == "Eastern Wash."):
                team = "Eastern Washington"
            if (oppTeam == "Eastern Wash."):
                oppTeam = "Eastern Washington"
            if (team == "Cal St Fullerton"):
                team = "Cal St. Fullerton"
            if (oppTeam == "Cal St Fullerton"):
                oppTeam = "Cal St. Fullerton"
            if (team == "Fairl. Dickinson"):
                team = "Fairleigh Dickinson"
            if (oppTeam == "Fairl. Dickinson"):
                oppTeam = "Fairleigh Dickinson"
            if (team == "ETSU"):
                team = "East Tennessee State"
            if (oppTeam == "ETSU"):
                oppTeam = "East Tennessee State"
            if (team == "Middle Tenn."):
                team = "Middle Tennessee"
            if (oppTeam == "Middle Tenn."):
                oppTeam = "Middle Tennessee"
            if (team == "Northern Ky."):
                team = "Northern Kentucky"
            if (oppTeam == "Northern Ky."):
                oppTeam = "Northern Kentucky"
            if (team == "N.C. Central"):
                team = "North Carolina Central"
            if (oppTeam == "Jacksonville St."):
                oppTeam = "Jacksonville State"
            if (team == "Jacksonville St."):
                team = "Jacksonville State"
            if (team == "Western Mich."):
                team = "Western Michigan"
            if (oppTeam == "Western Mich."):
                oppTeam = "Western Michigan"
            if (team == "St. Joseph's"):
                team = "Saint Joseph's"
            if (team == "North Dakota St."):
                team = "North Dakota State"
            if (team == "Eastern Ky."):
                team = "Eastern Kentucky"
            if (oppTeam == 'Northern Colo.'):
                oppTeam = "Northern Colorado"
            if (team == "Charleston"):
                team = "College of Charleston"
            if (oppTeam == 'Charleston'):
                oppTeam = "College of Charleston"
            if (oppTeam == "St. Peter's"):
                oppTeam = "Saint Peter's"
            if (oppTeam == "Western Ky."):
                oppTeam = "Western Kentucky"
            if (oppTeam == "New Mexico St."):
                oppTeam = "New Mexico State"
            if (oppTeam == "NC State"):
                oppTeam = "North Carolina State"
            if (oppTeam == "UNC"):
                oppTeam = "North Carolina"
            if (oppTeam == "Long Beach St."):
                oppTeam = "Long Beach State"
            if (oppTeam == "S Dakota St."):
                oppTeam = "South Dakota State"
            if (oppTeam == "Miss Val St"):
                oppTeam = "Mississippi Valley State"
            if (oppTeam == "Fla. Gulf Coast"):
                oppTeam = "Florida Gulf Coast"
            if (oppTeam == "N.C. A&T"):
                oppTeam = "North Carolina A&T"
            if (oppTeam == "NW St."):
                oppTeam = "Northwestern State"  
            if (oppTeam == "Ole Miss"):
                oppTeam = "Mississippi"  
            if (oppTeam == "Middle Tenn."):
                oppTeam = "Middle Tennessee"
            if (oppTeam == "N.C. Central"):
                oppTeam = "North Carolina Central"
            if (oppTeam == "St. Joseph's"):
                oppTeam = "Saint Joseph's"
            if (oppTeam == "UMass"):
                oppTeam = "Massachusetts"
            if (oppTeam == "North Dakota St."):
                oppTeam = "North Dakota State"
            if (oppTeam == "Eastern Ky."):
                oppTeam = "Eastern Kentucky"

            date = row['Date']
            #check if this game has been scanned already - important to check for tuple of (oppTeam,team) since that is the other copy of this game
            if (oppTeam,team) in seenGames_1011 and (seenGames_1011[(oppTeam,team)] == date):
                continue
            #game hasn't been seen before, add it to seenGames
            seenGames_1011[(team,oppTeam)] = date
            #add result to our tournamentWins dict
            if result == 'W':
                if (team in team_tournamentWins_1011.keys()):
                    team_tournamentWins_1011[team]+=1
                else:
                    team_tournamentWins_1011[team] = 1
                if (oppTeam in team_tournamentWins_1011.keys()):
                    team_tournamentWins_1011[oppTeam]+=0
                else:
                    team_tournamentWins_1011[oppTeam] = 0
            if result == 'L':
                if (oppTeam in team_tournamentWins_1011.keys()):
                    team_tournamentWins_1011[oppTeam]+=1
                else:
                    team_tournamentWins_1011[oppTeam] = 1
                if (team in team_tournamentWins_1011.keys()):
                    team_tournamentWins_1011[team]+=0
                else:
                    team_tournamentWins_1011[team] = 0
    return (team_tournamentWins_1011,seenGames_1011)

#helper function to get every team's road winning % for a given season
def roadWinPct(allGames):
    #team_roadWinPct is a dict of team : (#roadwins,#roadgames)
    team_roadWinPct = {}
    for index,row in allGames.iterrows():
        if (not pd.isnull(row['Id'])):
        #gather relevant info from game
            team = row['Schl']
            result = row['Result'][0]
            oppTeam = row['Opp']
            date = row['Date']
            location = row['Location']
            #check if this is a road game
            if location == '@':
                if result == 'W':
                    if (team in team_roadWinPct.keys()):
                        before = team_roadWinPct[team]
                        after = (before[0]+1,before[1]+1)
                        team_roadWinPct[team] = after
                    else:
                        team_roadWinPct[team] = (1,1)
                if result == 'L':
                    if (team in team_roadWinPct.keys()):
                        before = team_roadWinPct[team]
                        after = (before[0],before[1]+1)
                        team_roadWinPct[team] = after
                    else:
                        team_roadWinPct[team] = (0,1)
    for k in team_roadWinPct.keys():
        roadwins = team_roadWinPct[k][0]
        roadgames = team_roadWinPct[k][1]
        team_roadWinPct[k] = float(roadwins/roadgames)
    return team_roadWinPct

#helper function to convert roadWinPct dict and tournamentWins dict into X and Y NP Arrays
def createXYArraysRecord(roadWinPctDict,tournamentWinsDict):
    x = []
    y = []
    for year in tournamentWinsDict.keys():
        for team in tournamentWinsDict[year].keys():
            if (team in roadWinPctDict[year].keys()):
                x.append(roadWinPctDict[year][team])
                y.append(tournamentWinsDict[year][team])
    return x,y

def createXYArraysStats(teamStatistics,tournamentWinsDict,stat):
    x = {}
    y = {}
    for year in tournamentWinsDict.keys():
        for team in tournamentWinsDict[year].keys():
            if (team in teamStatistics[year].keys()):
                x[team+year]=(teamStatistics[year][team][stat])
                # print(tournamentWinsDict[year][team])
                y[team+year]=(tournamentWinsDict[year][team])
                if x[team+year] == 1 and y[team+year] == 0:
                    print(team+year)

            else:
                print(team+" wasn't in both the tournament wins dict and the stats dict")
    return x,y

#helper function to get every team's overall winning % for a given season
def teamWinPct(allGames,tournamentGameDates):
    #team_roadWinPct is a dict of team : (#roadwins,#roadgames)
    team_roadWinPct = {}
    for index,row in allGames.iterrows():
        if (not pd.isnull(row['Id'])):
        #gather relevant info from game
            team = row['Schl']
            result = row['Result'][0]
            oppTeam = row['Opp']
            date = row['Date']
            print(date)
            location = row['Location']
            if (date not in tournamentGameDates):
                if result == 'W':
                    if (team in team_roadWinPct.keys()):
                        before = team_roadWinPct[team]
                        after = (before[0]+1,before[1]+1)
                        team_roadWinPct[team] = after
                    else:
                        team_roadWinPct[team] = (1,1)
                if result == 'L':
                    if (team in team_roadWinPct.keys()):
                        before = team_roadWinPct[team]
                        after = (before[0],before[1]+1)
                        team_roadWinPct[team] = after
                    else:
                        team_roadWinPct[team] = (0,1)
            else:
                print("the date was an ncaa tournament game!")
    for k in team_roadWinPct.keys():
        roadwins = team_roadWinPct[k][0]
        roadgames = team_roadWinPct[k][1]
        team_roadWinPct[k] = float(roadwins/roadgames)
    return team_roadWinPct

def homeWinPct(allGames):
    #team_roadWinPct is a dict of team : (#roadwins,#roadgames)
    team_roadWinPct = {}
    for index,row in allGames.iterrows():
        if (not pd.isnull(row['Id'])):
        #gather relevant info from game
            team = row['Schl']
            result = row['Result'][0]
            oppTeam = row['Opp']
            date = row['Date']
            location = row['Location']
            if (pd.isnull(location)):
                print("game is at home")
                if result == 'W':
                    if (team in team_roadWinPct.keys()):
                        before = team_roadWinPct[team]
                        after = (before[0]+1,before[1]+1)
                        team_roadWinPct[team] = after
                    else:
                        team_roadWinPct[team] = (1,1)
                if result == 'L':
                    if (team in team_roadWinPct.keys()):
                        before = team_roadWinPct[team]
                        after = (before[0],before[1]+1)
                        team_roadWinPct[team] = after
                    else:
                        team_roadWinPct[team] = (0,1)
            else:
                print("game is not at home")
    for k in team_roadWinPct.keys():
        roadwins = team_roadWinPct[k][0]
        roadgames = team_roadWinPct[k][1]
        team_roadWinPct[k] = float(roadwins/roadgames)
    return team_roadWinPct

def neutralWinPct(allGames,tournamentGameDates):
    #team_roadWinPct is a dict of team : (#roadwins,#roadgames)
    team_roadWinPct = {}
    for index,row in allGames.iterrows():
        if (not pd.isnull(row['Id'])):
        #gather relevant info from game
            team = row['Schl']
            result = row['Result'][0]
            oppTeam = row['Opp']
            date = row['Date']
            location = row['Location']
            if (location == 'N' and (date not in tournamentGameDates)):
                if result == 'W':
                    if (team in team_roadWinPct.keys()):
                        before = team_roadWinPct[team]
                        after = (before[0]+1,before[1]+1)
                        team_roadWinPct[team] = after
                    else:
                        team_roadWinPct[team] = (1,1)
                if result == 'L':
                    if (team in team_roadWinPct.keys()):
                        before = team_roadWinPct[team]
                        after = (before[0],before[1]+1)
                        team_roadWinPct[team] = after
                    else:
                        team_roadWinPct[team] = (0,1)
            else:
                if (location == 'N'): 
                    print("the date was an ncaa tournament game!")
    for k in team_roadWinPct.keys():
        roadwins = team_roadWinPct[k][0]
        roadgames = team_roadWinPct[k][1]
        team_roadWinPct[k] = float(roadwins/roadgames)
    return team_roadWinPct

#helper function to add all the tournament game dates to a list
def createTournamentDateList(seenGames):
    retList = []
    for k in seenGames.keys():
        retList.append(list(seenGames[k].values()))
    return retList

def tournamentWinsAllYears(year):
    return teamRecord.tournamentWinsAllYears(year)

def createXYLogisticRegression(teamStatsByYear):

