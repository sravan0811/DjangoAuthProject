import pandas as pd
import numpy as np
empno = [101,102,103,104]
ename = ['abc','bcd','cde','def']

ename_series = pd.Series(ename)
empno_series = pd.Series(empno)
frame = {'empno':empno_series,'ename':ename_series}
out = pd.DataFrame(frame)
mydf = pd.read_csv('emp.csv')

print(mydf.duplicated())