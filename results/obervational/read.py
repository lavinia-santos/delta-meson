import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(16,8), sharey=True)
#fig,ax=plt.subplots()
# ax[0]: MxR, ax[1]: MxLambda

colors=['navy', 'deeppink', 'darkviolet']

eos_number=[8,20,21]
font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 26}

plt.rc('font', **font)

i=0
plt.figure(figsize=(20,20))
for num in eos_number:
    
    mass=[]
    q1=[]
    q3=[]
    #plt.clf()
    #print(f"EOS{num}")
    quartiles = f"../EOS{num}/output-quartile-CI90_{num}.txt"
    no_delta = f"../EOS{num}/old_eos{num}_neutron.dat"
    # no_delta2 = f"fsu2h.out"
    df = pd.read_csv(quartiles, sep=" ", header=None, on_bad_lines='skip')
    df = df.rename(columns={df.columns[0]: 'mass', df.columns[1]: 'q1', df.columns[2]: 'q3'})
    df = df[df['mass'] >0.5]
    # print(df)
    mass=df['mass'].to_numpy()
    q1=df['q1'].to_numpy()
    plt.plot(q1, mass, color=colors[i] , linestyle='dashed')
    q3=df['q3'].to_numpy()
    #print(len(q3))
    plt.plot(q3, mass, color=colors[i], linestyle='dashed')
    df_nodelta = pd.read_csv(no_delta, sep="   ", header=None, on_bad_lines='skip')
    df_nodelta = df_nodelta.rename(columns={df_nodelta.columns[0]: 'e0', df_nodelta.columns[1]: 'M', df_nodelta.columns[2]: 'R', df_nodelta.columns[3]: 'Mb', df_nodelta.columns[4]: 'rc'})
    max_mass = df_nodelta['M'].max()
    radius_max_mass = df_nodelta[df_nodelta['M'] == max_mass]['R'].values[0]
    df_nodelta = df_nodelta[df_nodelta['R'] > radius_max_mass]
    df_nodelta = df_nodelta[df_nodelta['M'] > 0.5]
    df_nodelta = df_nodelta[df_nodelta['R'] < 16.5]
    xi=df_nodelta['R'].to_numpy()
    yi=df_nodelta['M'].to_numpy()
    plt.plot(xi, yi, color=colors[i], label=f'EOS{num}', linewidth=7.0)
    mass=[]
    i+=1
plt.ylim(0.5, 2.75)
plt.legend()
plt.xlabel(r'$R [km]$')
plt.ylabel(r'$M [M_{\odot}]$')

## NICER DATA
DIR = './' # colocar o diretório dos dados
Miller14_68=np.loadtxt(DIR+"NICER/Miller_68_3_J0030_0451.csv",dtype= 'float', comments="#", delimiter=",", converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0)
Miller14_95=np.loadtxt(DIR+"NICER/Miller_95_4_J0030_0451.csv",dtype= 'float', comments="#", delimiter=",", converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0)

Riley14_68=np.loadtxt(DIR+"NICER/Riley_68_3_J0030_0451.csv",dtype= 'float', comments="#", delimiter=",", converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0)
Riley14_95=np.loadtxt(DIR+"NICER/Riley_95_4_J0030_0451.csv",dtype= 'float', comments="#", delimiter=",", converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0)

Riley20_68=np.loadtxt(DIR+"NICER/Riley_68_J0740_6620.csv",dtype= 'float', comments="#", delimiter=",", converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0)


GW_90=np.loadtxt(DIR+"bounds/GW170817_90.csv",dtype= 'float', comments="#", delimiter=",", converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0)
GW_50=np.loadtxt(DIR+"bounds/GW170817_50.csv",dtype= 'float', comments="#", delimiter=",", converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0)

## HES DATA
HESS_68=np.loadtxt(DIR+"bounds/HESS_68.csv",dtype= 'float', comments="#", delimiter=",", converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0)
HESS_95=np.loadtxt(DIR+"bounds/HESS_95.csv",dtype= 'float', comments="#", delimiter=",", converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0)


## TOV DATA Input for few RMF Models
#bigapple,IUFSU,FSU2,FSU2R,nl3wr,tm1_2,tm1_2wr, tm1wr
# mr_bigapple=np.loadtxt(DIR+"nlwtov/tovbigapple.out",dtype= 'float', comments="#", delimiter=None, converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0)
# mr_IUFSU=np.loadtxt(DIR+"nlwtov/toviufsu_bpspas.out",dtype= 'float', comments="#", delimiter=None, converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0)
# mr_FSU2=np.loadtxt(DIR+"nlwtov/tov_FSU2.out",dtype= 'float', comments="#", delimiter=None, converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0)
# mr_FSU2R=np.loadtxt(DIR+"nlwtov/tov_FSU2R.out",dtype= 'float', comments="#", delimiter=None, converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0)
mr_nl3wr=np.loadtxt(DIR+"nlwtov/tovnl3wr_pn.out",dtype= 'float', comments="#", delimiter=None, converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0)
# mr_tm1_2=np.loadtxt(DIR+"nlwtov/tovtm1-2.out",dtype= 'float', comments="#", delimiter=None, converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0)
# mr_tm1_2wr=np.loadtxt(DIR+"nlwtov/tovtm1-2wr.out",dtype= 'float', comments="#", delimiter=None, converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0)
# mr_tm1wr=np.loadtxt(DIR+"nlwtov/tov_TM1wr.out",dtype= 'float', comments="#", delimiter=None, converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0)

##plot##
plt.errorbar(12.6,2.075,xerr=0.8,capsize=10, linewidth=10, color="blue", alpha=0.5,zorder=12)
plt.errorbar(13.11,1.445, xerr=1.15,yerr=0.145, capsize=4, linewidth=3, color="seagreen", alpha=0.9,zorder=12)
plt.errorbar(12.685,1.335, xerr=1.165,yerr=0.155, capsize=4, linewidth=3, color="lightseagreen", alpha=0.9,zorder=12)
plt.fill(Miller14_68[:,0],Miller14_68[:,1],color="#b1e1e1",hatch="x",linewidth=3.0, alpha=0.4,linestyle="dashed",zorder=10)
plt.fill(Riley14_68[:,0],Riley14_68[:,1],color="#cfb2ec",linewidth=3.0, alpha=0.7,linestyle="dashed",zorder=10)
plt.errorbar(12.55,2.0725, xerr=1.14,yerr=0.0665, capsize=4, linewidth=3, color="teal", alpha=0.9,zorder=12)
plt.fill(Riley20_68[:,0],Riley20_68[:,1],color="#f6d6b4",linewidth=3.0, alpha=0.4,linestyle="dotted",zorder=10)
plt.fill(GW_90[:,0], GW_90[:,1],color="k",linestyle="-", linewidth=2, alpha=0.1,zorder=10)
plt.fill(GW_50[:,0], GW_50[:,1],color="k",linestyle="dashed", linewidth=2, alpha=0.1,zorder=10)


#ax[1].errorbar(395, 1.36, xerr=325,capsize=6, linewidth=4, color="blue", alpha=0.5, zorder=10)

#plt.show()
plt.savefig("../obs-compare.png")