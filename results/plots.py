import matplotlib.pyplot as plt
#import numpy as np
import pandas as pd

#### Plots

input_dir = "tov-outputs"
num_lines = 500
#colors=['mediumpurple', 'darkviolet', 'deeppink', 'navy', 'deeppink', 'springgreen']

eos_number=[8,20,21]

#for i in range (1, num_lines + 1):
#for i in range(12,13):
#if i!=12:
df = pd.read_csv(f'../../big-results/tov-data20.dat', sep='\s+', engine='python')
df = df.rename(columns={df.columns[0]: 'label', df.columns[1]: 'energy_density', df.columns[2]: 'mass', df.columns[3]: 'radius', df.columns[4]: 'baryonic_masses', df.columns[5]: 'density'})
df = df[df['radius'] < 13.5]
df=df[df['radius'] > 11.0]
#input_file = f"{input_dir}/tov{i}.txt"
#df = pd.read_csv(input_file, sep="   ", header=None, on_bad_lines='skip')
#df = df.rename(columns={df.columns[0]: 'e0', df.columns[1]: 'M', df.columns[2]: 'R', df.columns[3]: 'Mb', df.columns[4]: 'rc'})
labels = df['label'].unique()
print(f"labels:{labels}")
for label in labels:
    # xi=[]
    # yi=[]
    # Filter data by label
    temp_df = df[df['label'] == label]
    # max_mass=max(temp_df['mass'])
    # max_radius=temp_df['radius'][temp_df['mass']==max_mass]
    # temp_df = temp_df[temp_df['radius'] > max_radius.values[0]]
    #print(temp_df)
    #print(f"temp_df:{temp_df}")
    xi=temp_df['radius'].to_numpy()
    yi=temp_df['mass'].to_numpy()
    #needs to convert df to numpy because pandas and matplotlib doesn't get along with well
    plt.plot(xi, yi)
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
#     print(df)
#     mass=df['mass'].to_numpy()
#     q1=df['q1'].to_numpy()
#     plt.plot(q1, mass, color='black', linestyle='dashed')
#     q3=df['q3'].to_numpy()
#     print(len(q3))
#     plt.plot(q3, mass, color='black', linestyle='dashed')
#     plt.legend()
#     #plt.show()
#     plt.savefig(f"quartile-plot{num}.png")
#     mass=[]
#     q1=[]
#     q3=[]