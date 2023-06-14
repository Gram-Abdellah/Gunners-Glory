#!/usr/bin/env python
# coding: utf-8

# In[155]:


import pandas as ps 
from datetime import datetime
import matplotlib.pyplot as plt
df = ps.read_csv(r'C:\Users\HP\OneDrive\Documents\Analytics projects topics\Arsenal 2023\Arsenal 23 dataset\epl_results_2022-23.csv')
import requests
df


# In[6]:


# fillter  only arsenal matches
arsenal_matches = df[(df['HomeTeam'] == 'Arsenal') | (df['AwayTeam'] == 'Arsenal')]
arsenal_matches


# In[36]:


# Performance Analysis :
#  What is Arsenal's win-loss record for the season?
Ars_win = arsenal_matches[((arsenal_matches['HomeTeam'] == 'Arsenal') & (arsenal_matches['FTR'] == 'H')) | ((arsenal_matches['AwayTeam'] == 'Arsenal') & (arsenal_matches['FTR'] == 'A'))  ]
Ars_win['Date'].size


# In[47]:


# How many goals did Arsenal score in home matches versus away matches?
Away_score= Ars_win[(Ars_win['AwayTeam'] == 'Arsenal') ]
Home_score= Ars_win[(Ars_win['HomeTeam'] == 'Arsenal') ]
print('Away :',sum(Away_score['FTAG']),'\n')
print('Home :',sum(Home_score['FTAG']))


# In[70]:


# Which player has the highest number of assists for Arsenal?
# get data from this website :
# https://theathletic.com/football/team/arsenal/stats/


# In[ ]:


url=('https://theathletic.com/football/team/arsenal/stats/')
response = requests.get(url)
table_data = ps.read_html(response.text)
Players = table_data[1]
GKs = table_data[0]
print(table)
Players.to_csv(r'C:\Users\HP\OneDrive\Documents\Analytics projects topics\Arsenal 2023\Players.csv')
GKs.to_csv(r'C:\Users\HP\OneDrive\Documents\Analytics projects topics\Arsenal 2023\GoalKappers.csv')


# In[79]:


players=ps.read_csv(r'C:\Users\HP\OneDrive\Documents\Analytics projects topics\Arsenal 2023\Players.csv')
GKs=ps.read_csv(r'C:\Users\HP\OneDrive\Documents\Analytics projects topics\Arsenal 2023\GoalKappers.csv')
players


# In[92]:


highest_Nassist = players[(players['A'] == max(players['A']))]
highest_Nassist


# In[93]:


highest_NGoal = players[(players['G'] == max(players['G']))]
highest_NGoal


# In[100]:


# What is the average number of yellow cards per game for Arsenal?
Avg_YC = players['YC'].mean()
Avg_YC


# In[122]:


#How does Arsenal's goal difference compare to other teams in the Premier League?
man_city_matches = _matches = df[(df['HomeTeam'] == 'Man City') | (df['AwayTeam'] == 'Man City')]
mc_Away_score = man_city_matches[(man_city_matches['AwayTeam'] == 'Man City') ]
mc_Home_score = man_city_matches[(man_city_matches['HomeTeam'] == 'Man City') ]

ar_sum_goal = sum(Away_score['FTAG']) + sum(Home_score['FTHG'])
ar_avg_goal_away = Away_score['FTAG'].mean() 
ar_avg_goal_home = Home_score['FTHG'].mean()
ar_max_goal_away =Away_score['FTAG'].max()
ar_max_goal_home =Home_score['FTHG'].max()


mc_sum_goal = sum(mc_Away_score['FTAG']) + sum(mc_Home_score['FTHG'])
mc_avg_goal_away = mc_Away_score['FTAG'].mean() 
mc_avg_goal_home = mc_Home_score['FTHG'].mean()
mc_max_goal_away =mc_Away_score['FTAG'].max()
mc_max_goal_home =mc_Home_score['FTHG'].max()

print('Arsenal Goals sum :', ar_sum_goal ,' , Man City Goals sum :',mc_sum_goal ,'\n')
print('Arsenal Away Goals avg :', ar_avg_goal_away ,' , Man City Away Goals avg :',mc_avg_goal_away ,'\n')
print('Arsenal Home Goals avg :', ar_avg_goal_home ,' , Man City Home Goals avg:',mc_avg_goal_home ,'\n')
print('Arsenal Away Goals max :', ar_max_goal_away ,' , Man CityAway Goals max :',mc_max_goal_away ,'\n')
print('Arsenal Home Goals max :', ar_max_goal_home ,' , Man City Home Goals max :',mc_max_goal_home ,'\n')


# In[132]:


# Which team did Arsenal have the most victories against this season?
Goals_df_Away = Away_score
Away_score['difference'] = Away_score['FTAG'] - Away_score['FTHG']
Goals_df_Home = Home_score
Goals_df_Home['difference'] = Home_score['FTHG'] - Home_score['FTAG']


# In[141]:


max_vic_away =Away_score[(Away_score['difference'])== (max(Away_score['difference']))]
max_vic_home =Home_score[(Home_score['difference'])== (max(Home_score['difference']))]
print('Maximum victory at home :\n')
max_vic
print('Maximum victory at away :\n')
max_vic_home
#print('Maximum victory at home :', max(Home_score['difference']))


# In[165]:


# How does Arsenal's home record compare to their away record?
home_matches = arsenal_matches[(arsenal_matches['HomeTeam']=='Arsenal')]
away_matches = arsenal_matches[(arsenal_matches['AwayTeam']=='Arsenal')]
home_matches['scored']=home_matches['FTHG']
away_matches['scored']=away_matches['FTAG']

plt.bar(home_matches['Date'], home_matches['scored'])
plt.xlabel('Date')
plt.ylabel('Home Goals')
plt.title('Home Goals per Date')
plt.show()



# In[166]:


# Away :
plt.bar(away_matches['Date'], away_matches['scored'])
plt.xlabel('Date')
plt.ylabel('Away Goals')
plt.title('Away Goals per Date')
plt.show()


# In[171]:


#  How many shots on target does Arsenal have on average per game?
SoT_home = (home_matches['HST']).mean()
SoT_away = (away_matches['AST']).mean()
print('Away :',SoT_away ,'Home : ',SoT_home )


# In[174]:


# Team Comparison :


# In[200]:


win_home =(home_matches[(home_matches['FTR'] == 'H')])['FTR'].count()
draw_home =(home_matches[(home_matches['FTR'] == 'D')])['FTR'].count()
win_away =(away_matches[(away_matches['FTR'] == 'A') ])['FTR'].count() 
draw_away =(away_matches[(away_matches['FTR'] == 'D') ])['FTR'].count() 

total_points = win_home*3 + draw_home* 1+ win_away*3 + draw_away*1
print ('-Total_points :', total_points ,'-Win :', win_home+win_away ,'-Draw :',draw_home+draw_away ,'-Lose :', 38-(win_home+ draw_home+ win_away + draw_away)  )
print ('Man City : 89')


# In[217]:


#  Which team has the highest number of goals scored in matches against Arsenal?
home_scored_ag_ars=arsenal_matches[(arsenal_matches['HomeTeam'] == 'Arsenal') & (arsenal_matches['FTHG'] == max(home_matches['FTHG'])) ]
home_scored_ag_ars
away_scored_ag_ars=arsenal_matches[(arsenal_matches['AwayTeam'] == 'Arsenal') & (arsenal_matches['FTAG'] == max(away_matches['FTAG'])) ]
away_scored_ag_ars


# In[230]:


#  Which teams have the best head-to-head record against Arsenal this season?
lose_home =home_matches[(home_matches['FTR'] == 'A' ) ]
lose_away =away_matches[(away_matches['FTR'] == 'H') ]

best_head_tohead_home =lose_home[lose_home['FTAG'] == max(lose_home['FTAG'])]
best_head_tohead_away =lose_away[lose_away['FTHG'] == max(lose_away['FTHG'])]
best_head_tohead_away


# In[237]:


# What is the average number of goals conceded by Arsenal compared to other teams?
avg_g_conceded=(sum(away_matches['FTHG']) + sum(home_matches['FTAG']))/38
avg_g_conceded


# In[249]:


# Which teams have the highest number of yellow or red cards when playing against Arsenal?
YCA_home =home_matches[(home_matches['AY'] == max(home_matches['AY'] & home_matches['AY']!= 0)) ]
YHC_away =away_matches[(away_matches['HY'] == max(away_matches['HY'] & away_matches['HY']!= 0) ) ]
RHC_home =home_matches[(home_matches['AR'] == max(home_matches['AR'])) & home_matches['AR']!= 0 ]
RAC_away =away_matches[(away_matches['HR'] == max(away_matches['HR']) ) & away_matches['HR']!= 0 ]
RHC_home


# In[260]:


# Tactical Analysis :
# What is the most common formation used by Arsenal in the Premier League matches?
# import data 
games_stats =ps.read_csv(r'C:\Users\HP\OneDrive\Documents\Analytics projects topics\Arsenal 2023\Games.csv')
def most_frequent(Array):
    counter = 0
    num = Array[0]
     
    for i in Array:
        curr_frequency = Array.count()
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num
 
print(most_frequent(games_stats['Formation']))


# In[266]:


# Which players have the highest pass completion rates for Arsenal?
players=ps.read_csv(r'C:\Users\HP\OneDrive\Documents\Analytics projects topics\Arsenal 2023\Players.csv')
h_pass_rate =players[(players['PAcc']==max(players['PAcc']))]
h_pass_rate


# In[269]:


# Are there any notable differences in Arsenal's tactical approach in home matches versus away matches?
# aggressivity
AFs=sum(home_matches['AF'])
HFs=sum(home_matches['HF'])
HFs
('-Number of fouls at home : ',HFs ,'-Number of fouls away :',AFs)


# In[ ]:




