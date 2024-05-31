import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('tov-test.dat', sep='   ')
df = df.rename(columns={df.columns[0]: 'label', df.columns[1]: 'energy density', df.columns[2]: 'mass', df.columns[3]: 'radius', df.columns[4]: 'baryonic masses', df.columns[5]: 'density'})
#df=df.sort_values(by = ['radius'])
df = df[df['radius'] < 14.0]
R_Temp = np.asarray(df.radius[df.label == 6348])
M_Temp = np.asarray(df.mass[df.label == 6348])
print(f"R size:{R_Temp.size}, M size:{M_Temp.size}")
print(f"R:{R_Temp}, M:{M_Temp}")
plt.plot(R_Temp, M_Temp)
plt.show()