import pandas as pd
import sys

sys.stdout = open('output.txt', 'w')

df1 = pd.read_csv('input1.csv', delimiter=',')
df2 = pd.read_csv('input2.csv', delimiter=',')

df1 = df1.append(df2)

#1
print(df1[(df1['number'] < 10) & (df1['country'] == 'Germany')].shape[0] / df1[df1['country'] == 'Germany'].shape[0])
#2
#print(df1)
#df1 = df1.drop((df1['in refrigerator'] == "Yes") & (df1['fragility'] == "Yes"))
#print(df1)
