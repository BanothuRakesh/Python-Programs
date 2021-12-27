import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from mlxtend.plotting import plot_decision_regions
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
iris=datasets.load_iris()
x=iris.data[:,2:]
y=iris.target
X_train,x_test,Y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1,stratify=y)
forest=RandomForestClassifier(criterion='gini',n_estimators=5,random_state=1,n_jobs=2)
forest.fit(X_train,Y_train)
y_pred=forest.predict(x_test)
print('Accuracy:%.3f'%accuracy_score(y_test,y_pred))
X_combined=np.vstack((X_train,x_test))
Y_combined=np.hstack((Y_train,y_test))
fig,ax=plt.subplots(figsize=(7,7))
plot_decision_regions(X_combined,Y_combined,clf=forest)
plt.xlabel('petal length[cm]')
plt.legend(loc=' upper left')
plt.tight_layout()
print(plt.show())
