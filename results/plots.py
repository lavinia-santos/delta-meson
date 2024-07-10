import matplotlib.pyplot as plt
#import numpy as np
import pandas as pd

#### Plots

#input_dir = "tov-outputs"
# num_lines = 5506
#colors=['mediumpurple', 'darkviolet', 'deeppink', 'navy', 'deeppink', 'springgreen']
#colors=['deepskyblue', 'deeppink', 'darkviolet']
# colors=['blueviolet','mediumvioletred','royalblue','mediumvioletred']
colors=['blue','red','green']
eos_number=[8,20,21]
font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 26}

plt.rc('font', **font)

# df = pd.read_csv(f'../../big-results/tov-data20-tovinp6.dat', sep='\s+', engine='python')
# df = df.rename(columns={df.columns[0]: 'label', df.columns[1]: 'energy_density', df.columns[2]: 'mass', df.columns[3]: 'radius', df.columns[4]: 'baryonic_masses', df.columns[5]: 'density'})
# # df = df[df['radius'] < 14.5]
# # df=df[df['radius'] > 10.0]
# # df = df[df['mass'] > 0.5]

# print(df)
# #input_file = f"{input_dir}/tov{i}.txt"
# #df = pd.read_csv(input_file, sep="   ", header=None, on_bad_lines='skip')
# #df = df.rename(columns={df.columns[0]: 'e0', df.columns[1]: 'M', df.columns[2]: 'R', df.columns[3]: 'Mb', df.columns[4]: 'rc'})
# labels = df['label'].unique()
# #print(f"labels:{labels}")
# for label in labels:
#         temp_df = df[df['label'] == label]
#         xi=temp_df['radius'].to_numpy()
#         yi=temp_df['mass'].to_numpy()
#         #needs to convert df to numpy because pandas and matplotlib doesn't get along with well
#         plt.plot(xi, yi)
#         #plt.plot(xi,yi)
# #plt.rcParams['font.size'] = 12
# # plt.xlabel('Radius')
# # plt.ylabel('Mass')
# # plt.title('EOS21')
# #plt.legend()
# plt.show()

i=0
plt.figure(figsize=(20,20))
for num in eos_number:
    
#     mass=[]
    proton_fraction=[]
    q1=[]
    q3=[]
    #plt.clf()
    #print(f"EOS{num}")
    quartiles = f"test-quartile-proton{num}.txt"
    #quartiles = f"EOS{num}/output-quartile-CI90_{num}.txt"
    
    #no_delta = f"EOS{num}/old_eos{num}_neutron.dat"
#     # no_delta2 = f"fsu2h.out"
    df = pd.read_csv(quartiles, sep=" ", header=None, on_bad_lines='skip')
    df = df.rename(columns={df.columns[0]: 'density', df.columns[1]: 'q1', df.columns[2]: 'q3'})
   #df = df.rename(columns={df.columns[0]: 'mass', df.columns[1]: 'q1', df.columns[2]: 'q3'})

#     df = df[df['mass'] >0.5]
#     # print(df)
    dens=df['density'].to_numpy()
    q1=df['q1'].to_numpy()
    #plt.plot(q1, mass, color='black' , linestyle='dashed', label=f'with delta CI90')
    plt.plot(dens, q1, color=colors[i%3] , linestyle='dashed', label=f'EOS {num}')
    q3=df['q3'].to_numpy()
    #print(len(q3))
    plt.plot(dens, q3, color=colors[i%3], linestyle='dashed')
    plt.fill_between(dens, q1, q3, color=colors[i%3], alpha=0.2)
#     df_nodelta = pd.read_csv(no_delta, sep="   ", header=None, on_bad_lines='skip')
#     df_nodelta = df_nodelta.rename(columns={df_nodelta.columns[0]: 'e0', df_nodelta.columns[1]: 'M', df_nodelta.columns[2]: 'R', df_nodelta.columns[3]: 'Mb', df_nodelta.columns[4]: 'rc'})
#     max_mass = df_nodelta['M'].max()
#     radius_max_mass = df_nodelta[df_nodelta['M'] == max_mass]['R'].values[0]
#     df_nodelta = df_nodelta[df_nodelta['R'] > radius_max_mass]
#     df_nodelta = df_nodelta[df_nodelta['M'] > 0.5]
#     df_nodelta = df_nodelta[df_nodelta['R'] < 16.5]
#     xi=df_nodelta['R'].to_numpy()
#     yi=df_nodelta['M'].to_numpy()
#     plt.plot(xi, yi, color=colors[i], label=f'EOS {num}', linewidth=7.0)
    # df_nodelta2 = pd.read_csv(no_delta2, sep="   ", header=None, on_bad_lines='skip')
    # df_nodelta2 = df_nodelta2.rename(columns={df_nodelta2.columns[0]: 'e0', df_nodelta2.columns[1]: 'M', df_nodelta2.columns[2]: 'R', df_nodelta2.columns[3]: 'Mb', df_nodelta2.columns[4]: 'rc'})
    # df_nodelta2 = df_nodelta2[df_nodelta2['M'] > 0.5]
    # df_nodelta2 = df_nodelta2[df_nodelta2['R'] < 16.5]
    # xi=df_nodelta2['R'].to_numpy()
    # yi=df_nodelta2['M'].to_numpy()
    # plt.plot(xi, yi, color='red', label='wo delta FSU2H')
    #plt.legend()
#     #plt.xlim(11, 15)
    # plt.xlabel('Radius')
    # plt.ylabel('Mass')
    #plt.title(f"EOS{num}")
    #plt.savefig(f"EOS{num}/with-without-delta.png")
    #plt.show()
    #plt.savefig(f"EOS{num}/mr-q-compare.png")
    proton_fraction=[]
    i+=1
 
plt.legend()
# #     #plt.xlim(11, 15)
# plt.xlabel('Radius')
# plt.ylabel('Mass')
plt.title(f"Proton fraction")
plt.savefig(f"proton-fraction-quartiles.png")
plt.show()