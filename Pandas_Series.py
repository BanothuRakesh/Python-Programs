import numpy as np
import pandas as pd 
data=pd.read_excel("data.xlsx")
data=pd.read_excel("data.xlsx",sheet_name=1 or 2 )
data.to_excel("data.xslx",sheet_name='keerthana2')
print(data)