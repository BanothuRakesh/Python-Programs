import numpy as np
import pandas as pd
r1={
    'name':['p','s','k'],
    'mar':[23,67,90],
    'cty':['bodi','puram','karra']
}
#df=pd.DataFrame(r1)
#print(df)

#print(df.to_csv('friends.csv'))

#print (df.to_csv('friends_index_false.csv', index = False ))
#print(df. head(1))
#print(df. tail(1))

#print(df. describe())
keerthana=pd.read_csv('keerthana.csv')
#print(keerthana['spd'])

keerthana['spd'][0]=150
print(keerthana)



