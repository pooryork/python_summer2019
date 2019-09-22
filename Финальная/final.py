# -*- coding: utf-8 -*-

import pandas as pd
import sys
import matplotlib.pyplot as plt
import pylab

#1
sys.stdout = open('output.txt', 'w')
df = pd.read_csv('results.csv', delimiter=',')

#2
print('Median score:')
print(df[['home_score', 'away_score']].median())
print()

print('Mode score:')
print(df[['home_score', 'away_score']].mode())
print()

print('Average score:')
print(df[['home_score', 'away_score']].mean())
print()

print('Min score:')
print(df[['home_score', 'away_score']].min())
print()

print('Max score:')
print(df[['home_score', 'away_score']].max())
print()

#3
df_rus = df.query("home_team == 'Russia' or away_team == 'Russia'")
df_rus.to_csv('Russia.csv')
df_eng = df.query("home_team == 'England' or away_team == 'England'")
df_eng.to_csv('England.csv')
df_ger = df.query("home_team == 'Germany' or away_team == 'Germany'")
df_ger.to_csv('Germany.csv')

#4
data = [df_rus.shape[0], df_eng.shape[0], df_ger.shape[0]]
labels = ["Matches with Russia", "Matches with England", "Matches with Germany"]

#5
pylab.pie(data, labels=labels)
plt.savefig('pic1.png')
pylab.show()

#6
plt.hist(df_rus["city"])
plt.savefig('pic2.png')
plt.show()

plt.hist(df_eng['away_score'])
plt.savefig('pic3.png')
plt.show()

plt.plot(df_ger['city'], df_ger['tournament'])
plt.savefig('pic4.png')
plt.show()

dfgroup = df.groupby('city')[['home_score', 'away_score']].sum()
dfgroup.to_csv('city_groupby.csv')
