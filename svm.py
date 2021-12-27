import pandas as pd
import numpy as np
from pandas.core import tools
from sklearn.datasets import load_digits
from sklearn.metrics.pairwise import linear_kernel
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
digits=load_digits()
digits.target
dir(digits)
digits.target_names
df=pd.DataFrame(digits.data,digits.target)
df.head()
df['target']=digits.target
df.head(10)
X_train,X_test,y_train,y_test=train_test_split(df.drop('target',axis='columns'),df.target,test_size=0.3)
rbf_model=SVC(kernel='rbf')
len(X_train)
len(X_test)
rbf_model.fit(X_train,y_train)
SVC(C=1.0,cache_size=100,class_weight=None,coef0=0,decision_function_shape=None,degree=2,gamma='auto',kernel='rbf',
     max_iter=-1,probability=False,random_state=None,shrinking=True,tol=0.001, verbose=False)
print(rbf_model.score(X_test,y_test))
linear_model=SVC(kernel='linear')
linear_model.fit(X_train,y_train)     
SVC(C=1.0,cache_size=100,class_weight=None,coef0=0,decision_function_shape=None,degree=2,gamma='auto',kernel='rbf',
     max_iter=-1,probability=False,random_state=None,shrinking=True,tol=0.001, verbose=False)
print(linear_model.score(X_test,y_test))     