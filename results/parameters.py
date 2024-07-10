import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import corner
import matplotlib.lines as mlines
import matplotlib.transforms as mtransforms
from types import MethodType
from scipy.interpolate import interp1d
import os


eos_number=[8,20,21]
params={}
medians={}
CI90={}
CI95={}

for i in eos_number:

    couplings=f"../../../../../../../../Downloads/para_eos{i}.csv"

    df=pd.read_csv(couplings, sep=',', on_bad_lines='skip')
    df=df.rename(columns={df.columns[0]:'label', df.columns[1]: 'gr', df.columns[2]: 'gdel', df.columns[3]: 'lambda_gr2'})
    del df['label']
    #print(df)
    if i in [8,20,21]:
        params[i]=df.to_numpy()
        #params[i]=params[i][~np.isnan(params[i]).any(axis=1)]
    print(f"{params[i]}")
    #print(f"EOS{i} {params[i].shape})")

#now, let's calculate the median values for each parameter, as well as 90% and 95% CI

    medians[i]=np.median(params[i], axis=0)
    CI90[i]=np.percentile(params[i], [5,95], axis=0)
    CI95[i]=np.percentile(params[i], [2.5,97.5], axis=0)

print(f"medians: \n EOS8: {medians[8]} \n EOS20: {medians[20]} \n EOS21: {medians[21]}")
print(f"CI90: \n EOS8: {CI90[8]} \n EOS20: {CI90[20]} \n EOS21: {CI90[21]}")
print(f"CI95: \n EOS8: {CI95[8]} \n EOS20: {CI95[20]} \n EOS21: {CI95[21]}")
    
    



