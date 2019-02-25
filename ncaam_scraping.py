from bs4 import BeautifulSoup
import pandas as pd 
import requests as requests

base_url_all_games="https://www.sports-reference.com/cbb/play-index/tgl_finder.cgi?request=1&player=&match=game&year_min=2018&year_max=2018&school_id=&opp_id=&game_type=A&is_range=N&best_of=&game_num_type=&game_num_min=&game_num_max=&game_month=&game_location=&game_result=&is_overtime=&comp_schl_rk=eq&comp_opp_rk=eq&val_schl_rk=ANY&val_opp_rk=ANY&c1stat=&c1comp=&c1val=&c2stat=&c2comp=&c2val=&c3stat=&c3comp=&c3val=&c4stat=&c4comp=&c4val=&order_by=pts&order_by_asc=&offset={}"
base_url_tourney_games="https://www.sports-reference.com/cbb/play-index/tgl_finder.cgi?request=1&player=&match=game&year_min=2018&year_max=2018&school_id=&opp_id=&game_type=N&is_range=N&best_of=&game_num_type=&game_num_min=&game_num_max=&game_month=&game_location=&game_result=&is_overtime=&comp_schl_rk=eq&comp_opp_rk=eq&val_schl_rk=ANY&val_opp_rk=ANY&c1stat=&c1comp=&c1val=&c2stat=&c2comp=&c2val=&c3stat=&c3comp=&c3val=&c4stat=&c4comp=&c4val=&order_by=pts&order_by_asc=&offset={}"
base_url_teamstatsforyear = "https://www.sports-reference.com/cbb/seasons/2010-advanced-school-stats.html"
base_url_oppteamstatsforyear = "https://www.sports-reference.com/cbb/seasons/2010-advanced-opponent-stats.html"
base_url_kenpomforyear = "https://kenpom.com/index.php?y=2018"
base_url_alltournamentgames = "https://www.sports-reference.com/cbb/play-index/tgl_finder.cgi?request=1&match=game&comp_schl_rk=eq&val_schl_rk=ANY&comp_opp_rk=eq&val_opp_rk=ANY&game_type=N&is_range=N&order_by=pts&offset={}"

baseurl = base_url_oppteamstatsforyear

df = pd.DataFrame()

length=100
offset=0

# while length>=100:
try:
	# print("processing rows {} to {}".format(offset+1,(offset+1)+100))
	# request = requests.get(baseurl.format(offset))
	request=requests.get(baseurl)
	content=request.content
	soup = BeautifulSoup(content)
	data = pd.read_html(str(soup.find_all("table")[0]))[0]
	df = pd.concat([df,data])
	length = data.shape[0]
	# print("processed rows {} to {}".format(offset+1,(offset+1)+100))
except Exception as e:
	print(e)
	# print("could not process rows {} to {}".format(offset+1,(offset+1)+100))
	# continue

	# offset=offset+100

df.to_csv('Data/TeamStats/NCAAM_OppTeamStats_0910.csv',index=False)







