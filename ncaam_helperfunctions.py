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
# tournamentGames_1011_1718 = pd.read_csv("Data/NCAAM_TournamentGames_1011_1718.csv", header=0,na_values=na_values_list)

# tournamentGames_1011_1718 = tournamentGames_1011_1718.dropna()
# print(tournamentGames_1011_1718)

allGames_1011 = pd.read_csv("Data/AllGames/NCAAM_AllGames_1011.csv", names=dtype_dict.keys(),skiprows=skiprows_list, dtype=dtype_dict,na_values=na_values_list)
allGames_1112 = pd.read_csv("Data/AllGames/NCAAM_AllGames_1112.csv", names=dtype_dict.keys(),skiprows=skiprows_list, dtype=dtype_dict,na_values=na_values_list)
allGames_1213 = pd.read_csv("Data/AllGames/NCAAM_AllGames_1213.csv", names=dtype_dict.keys(),skiprows=skiprows_list, dtype=dtype_dict,na_values=na_values_list)
allGames_1314 = pd.read_csv("Data/AllGames/NCAAM_AllGames_1314.csv", names=dtype_dict.keys(),skiprows=skiprows_list, dtype=dtype_dict,na_values=na_values_list)
allGames_1415 = pd.read_csv("Data/AllGames/NCAAM_AllGames_1415.csv", names=dtype_dict.keys(),skiprows=skiprows_list, dtype=dtype_dict,na_values=na_values_list)
allGames_1516 = pd.read_csv("Data/AllGames/NCAAM_AllGames_1516.csv", names=dtype_dict.keys(),skiprows=skiprows_list, dtype=dtype_dict,na_values=na_values_list)
allGames_1617 = pd.read_csv("Data/AllGames/NCAAM_AllGames_1617.csv", names=dtype_dict.keys(),skiprows=skiprows_list, dtype=dtype_dict,na_values=na_values_list)
allGames_1718 = pd.read_csv("Data/AllGames/NCAAM_AllGames_1718.csv", names=dtype_dict.keys(),skiprows=skiprows_list, dtype=dtype_dict,na_values=na_values_list)

#remaking tournament games from Kaggle's Data

tournamentGames = pd.read_csv("Data/KaggleData/DataFiles/NCAATourneyCompactResults.csv",header=0)
# print(tournamentGames)
tournamentGames = tournamentGames.loc[tournamentGames['Season']>=2010]

def getTournamentGames():
    return tournamentGames

tournamentGames_0910 = tournamentGames.loc[tournamentGames['Season']==2010]
tournamentGames_1011 = tournamentGames.loc[tournamentGames['Season']==2011]
tournamentGames_1112 = tournamentGames.loc[tournamentGames['Season']==2012]
tournamentGames_1213 = tournamentGames.loc[tournamentGames['Season']==2013]
tournamentGames_1314 = tournamentGames.loc[tournamentGames['Season']==2014]
tournamentGames_1415 = tournamentGames.loc[tournamentGames['Season']==2015]
tournamentGames_1516 = tournamentGames.loc[tournamentGames['Season']==2016]
tournamentGames_1617 = tournamentGames.loc[tournamentGames['Season']==2017]
tournamentGames_1718 = tournamentGames.loc[tournamentGames['Season']==2018]



# tournamentGames_1011 = pd.read_csv("Data/TournamentGames/NCAAM_TournamentGames_1011.csv", names=dtype_dict.keys(),skiprows=skiprows_list, dtype=dtype_dict,na_values=na_values_list)
# tournamentGames_1112 = pd.read_csv("Data/TournamentGames/NCAAM_TournamentGames_1112.csv", names=dtype_dict.keys(),skiprows=skiprows_list, dtype=dtype_dict,na_values=na_values_list)
# tournamentGames_1213 = pd.read_csv("Data/TournamentGames/NCAAM_TournamentGames_1213.csv", names=dtype_dict.keys(),skiprows=skiprows_list, dtype=dtype_dict,na_values=na_values_list)
# tournamentGames_1314 = pd.read_csv("Data/TournamentGames/NCAAM_TournamentGames_1314.csv", names=dtype_dict.keys(),skiprows=skiprows_list, dtype=dtype_dict,na_values=na_values_list)
# tournamentGames_1415 = pd.read_csv("Data/TournamentGames/NCAAM_TournamentGames_1415.csv", names=dtype_dict.keys(),skiprows=skiprows_list, dtype=dtype_dict,na_values=na_values_list)
# tournamentGames_1516 = pd.read_csv("Data/TournamentGames/NCAAM_TournamentGames_1516.csv", names=dtype_dict.keys(),skiprows=skiprows_list, dtype=dtype_dict,na_values=na_values_list)
# tournamentGames_1617 = pd.read_csv("Data/TournamentGames/NCAAM_TournamentGames_1617.csv", names=dtype_dict.keys(),skiprows=skiprows_list, dtype=dtype_dict,na_values=na_values_list)
# tournamentGames_1718 = pd.read_csv("Data/TournamentGames/NCAAM_TournamentGames_1718.csv", names=dtype_dict.keys(),skiprows=skiprows_list, dtype=dtype_dict,na_values=na_values_list)

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


teamStatsUseCols = [0,1,3,4,6,7,8,9,12,13,16,17,21,22,24,25,26,28]
teamStatsDTypeDict={'Rk':float,'School':str,'TotalW':float,'TotalL':float,'SRS':float,'SOS':float, 'ConfW':float,'ConfL':float,'RoadW':float,'RoadL':float,'Pace':float,'ORtg':float,'TRB%':float,'AST%':float,'BLK%':float,'eFG%':float,'TOV%':float,'FT/FGA':float,}
# skiprows_list_teamStats = skiprows_list
skiprows_list_teamStats = []
teamStats_na_values_list = list(teamStatsDTypeDict.keys()) + ["School Advanced","Opponent Advanced",'Overall','Conf.','W','L','SRS','SOS','Away']

teamStats_0910 = pd.read_csv("Data/TeamStats/NCAAM_TeamStats_0910.csv",names=teamStatsDTypeDict.keys(),skiprows=skiprows_list_teamStats,dtype=teamStatsDTypeDict,na_values=teamStats_na_values_list,usecols=teamStatsUseCols)
teamStats_1011 = pd.read_csv("Data/TeamStats/NCAAM_TeamStats_1011.csv",names=teamStatsDTypeDict.keys(),skiprows=skiprows_list_teamStats,dtype=teamStatsDTypeDict,na_values=teamStats_na_values_list,usecols=teamStatsUseCols)
teamStats_1112 = pd.read_csv("Data/TeamStats/NCAAM_TeamStats_1112.csv",names=teamStatsDTypeDict.keys(),skiprows=skiprows_list_teamStats,dtype=teamStatsDTypeDict,na_values=teamStats_na_values_list,usecols=teamStatsUseCols)
teamStats_1213 = pd.read_csv("Data/TeamStats/NCAAM_TeamStats_1213.csv",names=teamStatsDTypeDict.keys(),skiprows=skiprows_list_teamStats,dtype=teamStatsDTypeDict,na_values=teamStats_na_values_list,usecols=teamStatsUseCols)
teamStats_1314 = pd.read_csv("Data/TeamStats/NCAAM_TeamStats_1314.csv",names=teamStatsDTypeDict.keys(),skiprows=skiprows_list_teamStats,dtype=teamStatsDTypeDict,na_values=teamStats_na_values_list,usecols=teamStatsUseCols)
teamStats_1415 = pd.read_csv("Data/TeamStats/NCAAM_TeamStats_1415.csv",names=teamStatsDTypeDict.keys(),skiprows=skiprows_list_teamStats,dtype=teamStatsDTypeDict,na_values=teamStats_na_values_list,usecols=teamStatsUseCols)
teamStats_1516 = pd.read_csv("Data/TeamStats/NCAAM_TeamStats_1516.csv",names=teamStatsDTypeDict.keys(),skiprows=skiprows_list_teamStats,dtype=teamStatsDTypeDict,na_values=teamStats_na_values_list,usecols=teamStatsUseCols)
teamStats_1617 = pd.read_csv("Data/TeamStats/NCAAM_TeamStats_1617.csv",names=teamStatsDTypeDict.keys(),skiprows=skiprows_list_teamStats,dtype=teamStatsDTypeDict,na_values=teamStats_na_values_list,usecols=teamStatsUseCols)
teamStats_1718 = pd.read_csv("Data/TeamStats/NCAAM_TeamStats_1718.csv",names=teamStatsDTypeDict.keys(),skiprows=skiprows_list_teamStats,dtype=teamStatsDTypeDict,na_values=teamStats_na_values_list,usecols=teamStatsUseCols)

oppTeamStats_0910 = pd.read_csv("Data/TeamStats/NCAAM_OppTeamStats_0910.csv",names=teamStatsDTypeDict.keys(),skiprows=skiprows_list_teamStats,dtype=teamStatsDTypeDict,na_values=teamStats_na_values_list,usecols=teamStatsUseCols)
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
convertTeamNames(teamStats_0910,False)
convertTeamNames(teamStats_1011,False)
convertTeamNames(teamStats_1112,False)
convertTeamNames(teamStats_1213,False)
convertTeamNames(teamStats_1314,False)
convertTeamNames(teamStats_1415,False)
convertTeamNames(teamStats_1516,False)
convertTeamNames(teamStats_1617,False)
convertTeamNames(teamStats_1718,False)
convertTeamNames(oppTeamStats_0910,False)
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
# masseyOrdinals = masseyOrdinals[(masseyOrdinals['SystemName']=='POM')]

preseasonMassey_0910 = masseyOrdinals[(masseyOrdinals['Season']==2010) & (masseyOrdinals['RankingDayNum']<15)]
preseasonMassey_1011 = masseyOrdinals[(masseyOrdinals['Season']==2011) & (masseyOrdinals['RankingDayNum']<14)]
preseasonMassey_1112 = masseyOrdinals[(masseyOrdinals['Season']==2012) & (masseyOrdinals['RankingDayNum']<14)]
preseasonMassey_1213 = masseyOrdinals[(masseyOrdinals['Season']==2013) & (masseyOrdinals['RankingDayNum']<9)]
preseasonMassey_1314 = masseyOrdinals[(masseyOrdinals['Season']==2014) & (masseyOrdinals['RankingDayNum']==9)]
preseasonMassey_1415 = masseyOrdinals[(masseyOrdinals['Season']==2015) & (masseyOrdinals['RankingDayNum']==16)]
preseasonMassey_1516 = masseyOrdinals[(masseyOrdinals['Season']==2016) & (masseyOrdinals['RankingDayNum']==16)]
preseasonMassey_1617 = masseyOrdinals[(masseyOrdinals['Season']==2017) & (masseyOrdinals['RankingDayNum']==16)]
preseasonMassey_1718 = masseyOrdinals[(masseyOrdinals['Season']==2018) & (masseyOrdinals['RankingDayNum']==16)]

# preseasonMassey_1213.to_csv("helpermassey.csv")

masseyOrdinals = masseyOrdinals[(masseyOrdinals['SystemName']=='POM')]
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

# print(masseyOrdinals_0910.loc[masseyOrdinals_0910['TeamID']==1434]['OrdinalRank'].mean())

def createTeamStatistics(tournamentWinsAllYears):
    teamStatistics = {}
    teamStatistics[2010] = teamStats(teamStats_0910,oppTeamStats_0910,kenpom_1011,masseyOrdinals_0910,preseasonMassey_0910,tournamentWinsAllYears[2010],teams)
    teamStatistics[2011] = teamStats(teamStats_1011,oppTeamStats_1011,kenpom_1011,masseyOrdinals_1011,preseasonMassey_1011,tournamentWinsAllYears[2011],teams)
    teamStatistics[2012] = teamStats(teamStats_1112,oppTeamStats_1112,kenpom_1112,masseyOrdinals_1112,preseasonMassey_1112,tournamentWinsAllYears[2012],teams)
    teamStatistics[2013] = teamStats(teamStats_1213,oppTeamStats_1213,kenpom_1213,masseyOrdinals_1213,preseasonMassey_1213,tournamentWinsAllYears[2013],teams)
    teamStatistics[2014] = teamStats(teamStats_1314,oppTeamStats_1314,kenpom_1314,masseyOrdinals_1314,preseasonMassey_1314,tournamentWinsAllYears[2014],teams)
    teamStatistics[2015] = teamStats(teamStats_1415,oppTeamStats_1415,kenpom_1415,masseyOrdinals_1415,preseasonMassey_1415,tournamentWinsAllYears[2015],teams)
    teamStatistics[2016] = teamStats(teamStats_1516,oppTeamStats_1516,kenpom_1516,masseyOrdinals_1516,preseasonMassey_1516,tournamentWinsAllYears[2016],teams)
    teamStatistics[2017] = teamStats(teamStats_1617,oppTeamStats_1617,kenpom_1617,masseyOrdinals_1617,preseasonMassey_1617,tournamentWinsAllYears[2017],teams)
    teamStatistics[2018] = teamStats(teamStats_1718,oppTeamStats_1718,kenpom_1718,masseyOrdinals_1718,preseasonMassey_1718,tournamentWinsAllYears[2018],teams)
    return teamStatistics

#####TO DO######
#helper function to generate needed teamStats for a given year
def teamStats(statsFor,statsAgainst,kenpom,massey,preseasonMassey,tournamentWins,teams):
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
        preseasonRk = preseasonMassey.loc[preseasonMassey['TeamID']==teamId]['OrdinalRank'].mean()
        # print(masseyRk)
        statDict = {}
        statDict['preseasonRk'] = preseasonRk
        if (pd.isnull(preseasonRk)):
            print("###errrororroorooror####")
        statDict['kenpomRk'] = masseyRk
        statDict['diffRk'] = masseyRk - preseasonRk
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
        # if (statsForRow['ConfL'].array[0] + statsForRow['ConfW'].array[0] == 0):
        #     statDict['ConfWinPct'] = statDict['NonConfWinPct']
        # else:
        #     statDict['ConfWinPct'] = statsForRow['ConfW'].array[0] / (statsForRow['ConfL'].array[0] + statsForRow['ConfW'].array[0])
        statDict['RoadWinPct'] = statsForRow['RoadW'].array[0] / (statsForRow['RoadL'].array[0] + statsForRow['RoadW'].array[0])
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
        statDict['BLK%'] = statsForRow['BLK%'].array[0]
        statDict['BLK%Against'] = statsAgainstRow['BLK%'].array[0]
        statDict['netBLK%'] = statDict['BLK%'] - statDict['BLK%Against']
        # statDict['AST%'] = statsForRow['AST%'].array[0]
        # statDict['AST%Against'] = statsAgainstRow['AST%'].array[0]
        # statDict['netAST%'] = statDict['AST%'] - statDict['AST%Against']
        # statDict['FTRate'] = statsForRow['FT/FGA'].array[0]
        # statDict['FTRateAgainst'] = statsAgainstRow['FT/FGA'].array[0]
        # statDict['netFTRate'] = statDict['FTRate'] - statDict['FTRateAgainst']
        # statDict['ORtg'] = statsForRow['ORtg'].array[0]
        # statDict['DRtg'] = statsAgainstRow['ORtg'].array[0]
        # statDict['netRtg'] = statDict['ORtg'] - statDict['DRtg']
        # statDict['pace'] = statsForRow['Pace'].array[0]
        # statDict['SOS'] = statsForRow['SOS'].array[0]
        teamStats[k] = statDict
    return teamStats        


def createTournamentWinsAllYears():
    tournamentWinsAllYears = {}
    seenGames = {}
    tournamentWinsAllYears[2010],seenGames["0910"] = tournamentTeamWins(tournamentGames_0910)
    tournamentWinsAllYears[2011],seenGames["1011"] = tournamentTeamWins(tournamentGames_1011)
    tournamentWinsAllYears[2012],seenGames["1112"] = tournamentTeamWins(tournamentGames_1112)
    tournamentWinsAllYears[2013],seenGames["1213"] = tournamentTeamWins(tournamentGames_1213)
    tournamentWinsAllYears[2014],seenGames["1314"] = tournamentTeamWins(tournamentGames_1314)
    tournamentWinsAllYears[2015],seenGames["1415"] = tournamentTeamWins(tournamentGames_1415)
    tournamentWinsAllYears[2016],seenGames["1516"] = tournamentTeamWins(tournamentGames_1516)
    tournamentWinsAllYears[2017],seenGames["1617"] = tournamentTeamWins(tournamentGames_1617)
    tournamentWinsAllYears[2018],seenGames["1718"] = tournamentTeamWins(tournamentGames_1718)
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
        winningTeamID = row['WTeamID']
        losingTeamID = row['LTeamID']
        winningTeam = teams.loc[teams['TeamID']==winningTeamID]['TeamName'].array[0]
        losingTeam = teams.loc[teams['TeamID']==losingTeamID]['TeamName'].array[0]
        if (winningTeam in team_tournamentWins_1011.keys()):
            team_tournamentWins_1011[winningTeam]+=1
        else:
            team_tournamentWins_1011[winningTeam] = 1
        if (losingTeam in team_tournamentWins_1011.keys()):
            team_tournamentWins_1011[losingTeam]+=0
        else:
            team_tournamentWins_1011[losingTeam] = 0
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
                x[team+str(year)]=(teamStatistics[year][team][stat])
                # print(tournamentWinsDict[year][team])
                y[team+str(year)]=(tournamentWinsDict[year][team])
                if x[team+str(year)] == 1 and y[team+str(year)] == 0:
                    print(team+str(year))

            else:
                print(team+" wasn't in both the tournament wins dict and the stats dict")
    return x,y

def createXYMultipleStats(teamStatistics,stat1,stat2):
    x = {}
    y = {}
    for year in teamStatistics.keys():
        for team in teamStatistics[year]:
            x[team+str(year)]=teamStatistics[year][team][stat1]
            y[team+str(year)]=teamStatistics[year][team][stat2]
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

def createXYLogisticRegression(teamStatsByYear,trainingGames):
    #goal for x array [[wteamstats],[lteamstats]]
    #goal for y array = [1]
    y = []
    x = []
    i = 1
    def helperCreateLogRegXY(winningTeam,losingTeam,year,i):
        x_entry = []
        wNonConfWinPct = teamStatsByYear[year][winningTeam]['NonConfWinPct']
        # wConfWinPct = teamStatsByYear[year][winningTeam]['ConfWinPct']
        wOverallWinPct = teamStatsByYear[year][winningTeam]['OverallWinPct']
        wRoadWinPct = teamStatsByYear[year][winningTeam]['RoadWinPct']
        wNetEFG = teamStatsByYear[year][winningTeam]['netEFG%']
        wKenpomRk = teamStatsByYear[year][winningTeam]['kenpomRk']
        wDiffRk = teamStatsByYear[year][winningTeam]['diffRk']
        wPreseasonRk = teamStatsByYear[year][winningTeam]['preseasonRk']
        wNetTRB = teamStatsByYear[year][winningTeam]['netTRB%']
        wNetTOV = teamStatsByYear[year][winningTeam]['netTOV%']
        wNetBLK = teamStatsByYear[year][winningTeam]['netBLK%']
        # x_entry.append([wNonConfWinPct,wNetEFG,wKenpomRk])
        lNonConfWinPct = teamStatsByYear[year][losingTeam]['NonConfWinPct']
        lOverallWinPct = teamStatsByYear[year][losingTeam]['OverallWinPct']
        lRoadWinPct = teamStatsByYear[year][losingTeam]['RoadWinPct']
        # lConfWinPct = teamStatsByYear[year][losingTeam]['ConfWinPct']
        lNetEFG = teamStatsByYear[year][losingTeam]['netEFG%']
        lKenpomRk = teamStatsByYear[year][losingTeam]['kenpomRk']
        lDiffRk = teamStatsByYear[year][losingTeam]['diffRk']
        lPreseasonRk = teamStatsByYear[year][losingTeam]['preseasonRk']
        lNetTRB = teamStatsByYear[year][losingTeam]['netTRB%']
        lNetTOV = teamStatsByYear[year][losingTeam]['netTOV%']
        lNetBLK = teamStatsByYear[year][losingTeam]['netBLK%']
        # x_entry.append([lNonConfWinPct,lNetEFG,lKenpomRk]) 
        # x.append(x_entry)
        # y.append(1)
        if i % 2 == 0:
            t1=np.asarray([wNetEFG,wPreseasonRk,wNetTRB,wNetTOV,wNetBLK,wDiffRk])
            t2=np.asarray([lNetEFG,lPreseasonRk,lNetTRB,lNetTOV,lNetBLK,lDiffRk]) 
            return np.subtract(t1,t2),1
        else:
            t1=np.asarray([lNetEFG,lPreseasonRk,lNetTRB,lNetTOV,lNetBLK,lDiffRk])
            t2=np.asarray([wNetEFG,wPreseasonRk,wNetTRB,wNetTOV,wNetBLK,wDiffRk])
            return np.subtract(t1,t2),0
    
    for index,row in trainingGames.iterrows():
        WTeamID = row['WTeamID']
        LTeamID = row['LTeamID']
        year = row['Season']
        winningTeam = teams.loc[teams['TeamID']==WTeamID]['TeamName'].array[0]
        losingTeam = teams.loc[teams['TeamID']==LTeamID]['TeamName'].array[0]
        xtoapp,ytoapp = helperCreateLogRegXY(winningTeam,losingTeam,year,i)
        x.append(xtoapp)
        y.append(ytoapp)
        i=i+1
    return x,y

def createCorrelationMatrix(teamStatistics):
    outerArray = []
    for year in teamStatistics.keys():
        for team in teamStatistics[year].keys():
            outerArray.append(tuple(teamStatistics[year][team].values()))
    df = pd.DataFrame(outerArray,columns=teamStatistics[2010]['Kansas State'].keys())
    # print(df)
    return df