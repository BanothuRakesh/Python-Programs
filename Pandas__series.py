import numpy as np
import pandas as pd

#ser=pd.Series(np.random.rand(10))
#print(ser)

#dataframe 
#newdf=pd.DataFrame(np.random.rand(10,5))
#print(newdf)
#index=np.arange(10)
#print(newdf.head(5))
#print(newdf.tail(5))
#rint(newdf.describe)

#newdf[0][0]='samp'
#print(newdf)
#print(newdf.index)
#print(newdf.columns)
#print(newdf.to_numpy)

#newdf[1][0]='rks'
#print(newdf)
#print(newdf.T)

#newdf2=newdf
#newdf2[1][1]='kee'
#print(newdf)

#newdf.loc[2,2]='sra'
#print(newdf)
#print(newdf.head(3))

#newdf.columns=list('ABCDE')
#print(newdf.head(2))

#newdf.loc[2,'B']='some'
#print(newdf)
#print(newdf.head())

#newdf4=newdf.drop('A',axis=1)
#print(newdf4)

#newdf3=newdf.loc[[1,2],['C','D']]
#print(newdf3)

#newdf.loc[newdf['D']<0.8]
#print(newdf)
#print(newdf.head())

#newdf5=newdf.iloc[1,4]
#print(newdf5)

#newdf6=newdf.drop(['A','C'],axis=1) 
#print(newdf6)

#newdf.reset_index(drop=True,inplace=True)
#print(newdf.head(3))

#newdf8=newdf['B'].isnull()
#print(newdf8)
#newdf['B']=None

#print(newdf)

df=pd.DataFrame({
    'nam':['sam','rak','roh','sam'],
    'age':[np.nan,56,89,24],
    'bor':[3,14,20,28]
    })
#print(df)
#print(df.head())
#print(df.shape)
#print(df.info)

#df1=df.dropna()
#print(df1)  #np.nan is remove 

#df2=df.dropna(how='all')
#print(df2)  #np.nan is come

#df3=df.dropna(how='all',axis=1)
#print(df3)  #np.nan is rempove

#df4=df.drop_duplicates(subset=['nam'],keep=False)
#print(df4)  #same namis remove

#df5=df['age'].value_counts(dropna=False)
#print(df5)

df6=df.notnull()#isnull=reverse of notnull
print(df6)
