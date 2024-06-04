import matplotlib.pyplot as plt
#import numpy as np
import pandas as pd

#### Plots

input_dir = "tov-outputs"
num_lines = 500
colors=['mediumpurple', 'darkviolet', 'deeppink', 'navy', 'deeppink', 'springgreen']

for i in range (1, num_lines + 1):
#for i in range(12,13):
#if i!=12:
    input_file = f"{input_dir}/tov{i}.txt"
    df = pd.read_csv(input_file, sep="   ", header=None, on_bad_lines='skip')
    df = df.rename(columns={df.columns[0]: 'e0', df.columns[1]: 'M', df.columns[2]: 'R', df.columns[3]: 'Mb', df.columns[4]: 'rc'})
    xi=[]
    yi=[]
    xi=df['R'].to_numpy()
    yi=df['M'].to_numpy()
    #needs to convert df to numpy because pandas and matplotlib doesn't get along with well
    plt.plot(xi, yi, color=colors[i%6])
plt.legend()
plt.show()

