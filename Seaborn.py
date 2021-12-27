import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from seaborn.axisgrid import pairplot
from seaborn.distributions import kdeplot

S=sns.load_dataset('tips')
#print(S.head())
#print(S.tail())
#print(S.describe())

#dist univariate (kde+hist)
#sns.distplot(S['total_bill'])

#dist(hist))
#sns.distplot(S['total_bill'],kde=False)

#dist(kde)
#sns.distplot(S['total_bill'],hist=False)

#bivariate(joint=dot+graph)
#sns.jointplot(x="total_bill",y="tip",data=S)

#scatter()
#sns.scatterplot(x="total_bill",y="tip",data=S)

#pairwise with pairplot
#sns.set_style("ticks")
#sns.pairplot(S)

#strip
#sns.stripplot(x="day",y="total_bill",data=S)
#sns.stripplot(x="day",y="total_bill",data=S,jitter=False)

#swarm
#sns.swarmplot(x="day",y="total_bill",data=S)

#box
#sns.boxplot(x=S["total_bill"])
#sns.boxplot(x="day",y="total_bill",data=S)

#violin
#sns.violinplot(x=S["total_bill"])
#sns.violinplot(x="time",y="total_bill",data=S)

#bar
#sns.barplot(x="time",y="total_bill",data=S)

#point
#sns.pointplot(x="time",y="total_bill",data=S)
#sns.pointplot(x="time",y="total_bill",hue="smoker",data=S)

#linear(reg)
#sns.regplot(x="total_bill",y="tip",data=S)

#lm
#sns.lmplot(x="total_bill",y="tip",data=S)

#heat map
#uniform_data=np.random.rand(11,14)
#sns.heatmap(uniform_data)

#cluster
df1=S[["total_bill",'size']]
sns.clustermap(df1)
plt.show()