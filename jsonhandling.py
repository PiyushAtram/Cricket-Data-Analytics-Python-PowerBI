import pandas as pd
import json
# #Batting Summary
with open('D:/Projects/2nd Project/data-analytics-project-for-beginners/t20_json_files/t20_json_files/t20_wc_batting_summary.json') as f:
    data=json.load(f)
    load_data=[]
    for rec in data:
        load_data.extend(rec['battingSummary'])
df1=pd.DataFrame(load_data)
df1["Out/Not Out"]=df1.dismissal.apply(lambda x:"out" if len(x)>0 else "Not out")
df1.drop(columns=["dismissal"],inplace=True)
df1['batsmanName'] = df1['batsmanName'].apply(lambda x: x.replace('â€', ''))

df1['batsmanName'] = df1['batsmanName'].apply(lambda x: x.replace('\xa0', ''))


# Match Summary
with open('D:/Projects/2nd Project/data-analytics-project-for-beginners/t20_json_files/t20_json_files/t20_wc_match_results.json') as f:
    data=json.load(f)
# print(data[0]["matchSummary"])
df2=pd.DataFrame(data[0]["matchSummary"])
df2.rename(columns={"scorecard":"Match id"},inplace=True)
print(df2)

# Adding Match Id in Batting Summary
match_id_dict={}
for index,row in df2.iterrows():
    key1=row['team1'] + " Vs " + row['team2']
    key2=row['team2'] + " Vs " + row['team1']
    match_id_dict[key1]=row['Match id']
    match_id_dict[key2]=row['Match id']
print(match_id_dict)

df1["Match id"]=df1["match"].map(match_id_dict)
df1.to_csv('D:/Projects/2nd Project/data-analytics-project-for-beginners/t20_json_files/t20_json_files/Batting_summary.csv', index = False)
print(df1)
df2.to_csv('D:/Projects/2nd Project/data-analytics-project-for-beginners/t20_json_files/t20_json_files/Match_summary.csv', index = False)
print(df1)


# Bowling Summary
with open('D:/Projects/2nd Project/data-analytics-project-for-beginners/t20_json_files/t20_json_files/t20_wc_bowling_summary.json') as f:
    data=json.load(f)
    load_data=[]
    for rec in data:
        load_data.extend(rec['bowlingSummary'])
df3=pd.DataFrame(load_data)
df3['Match id']=df3['match'].map(match_id_dict)
print(df3)
df3.to_csv('D:/Projects/2nd Project/data-analytics-project-for-beginners/t20_json_files/t20_json_files/bowling_summary.csv', index = False)
# Player Info

with open('D:/Projects/2nd Project/data-analytics-project-for-beginners/t20_json_files/t20_json_files/t20_wc_player_info.json') as f:
    data=json.load(f)
    df4=pd.DataFrame(data)
df4['name'] = df4['name'].apply(lambda x: x.replace('â€', ''))
df4['name'] = df4['name'].apply(lambda x: x.replace('†', ''))
df4['name'] = df4['name'].apply(lambda x: x.replace('\xa0', ''))
df4.head(10)
print(df4[df4['team']=='India'])
df4.to_csv('D:/Projects/2nd Project/data-analytics-project-for-beginners/t20_json_files/t20_json_files/players_summary.csv', index = False)



