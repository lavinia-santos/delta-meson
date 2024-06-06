import matplotlib.pyplot as plt
#import numpy as np
import pandas as pd

#### Plots

input_dir = "tov-outputs"
num_lines = 1000
colors=['mediumpurple', 'darkviolet', 'deeppink', 'navy', 'deeppink', 'springgreen']

eos_number=[21]


df = pd.read_csv(f'../../big-results/tov-data21.dat', sep='\s+', engine='python')
df = df.rename(columns={df.columns[0]: 'label', df.columns[1]: 'energy_density', df.columns[2]: 'mass', df.columns[3]: 'radius', df.columns[4]: 'baryonic_masses', df.columns[5]: 'density'})
df = df[df['radius'] < 14.5]
df=df[df['radius'] > 10.0]
df = df[df['mass'] > 0.5]

print(df)
#input_file = f"{input_dir}/tov{i}.txt"
#df = pd.read_csv(input_file, sep="   ", header=None, on_bad_lines='skip')
#df = df.rename(columns={df.columns[0]: 'e0', df.columns[1]: 'M', df.columns[2]: 'R', df.columns[3]: 'Mb', df.columns[4]: 'rc'})
labels = df['label'].unique()
print(f"labels:{labels}")
for label in labels:
        temp_df = df[df['label'] == label]
        xi=temp_df['radius'].to_numpy()
        yi=temp_df['mass'].to_numpy()
        #needs to convert df to numpy because pandas and matplotlib doesn't get along with well
        plt.plot(xi, yi, color=colors[label%6])
plt.xlabel('Radius')
plt.ylabel('Mass')
plt.title('EOS21')
plt.legend()
plt.show()


# for num in eos_number:
#     mass=[]
#     q1=[]
#     q3=[]
#     plt.clf()
#     quartiles = f"EOS{num}/output-quartile.txt"
#     df = pd.read_csv(quartiles, sep=" ", header=None, on_bad_lines='skip')
#     df = df.rename(columns={df.columns[0]: 'mass', df.columns[1]: 'q1', df.columns[2]: 'q3'})
#     df = df[df['mass'] >0.5]
#     # print(df)
#     mass=df['mass'].to_numpy()
#     q1=df['q1'].to_numpy()
#     plt.plot(q1, mass, color='black', linestyle='dashed')
#     q3=df['q3'].to_numpy()
#     print(len(q3))
#     plt.plot(q3, mass, color='black', linestyle='dashed')
#     plt.legend()
#     #plt.xlim(11, 15)
#     plt.title(f"EOS{num}")
#     plt.show()
#     plt.savefig(f"quartile-plot{num}.png")
#     mass=[]
 
