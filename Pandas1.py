import pandas as pd # data frames in tabular format
import numpy as np # array or multi dimensional data


data = np.array([10,20,50,21,45])
data1 = {'name':'abc','no':'1234','sal':12000}
out = pd.Series(data1)
print(out)