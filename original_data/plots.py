import matplotlib.pyplot as plt
#import numpy as np
import pandas as pd

#### Plots



def plot_mass_radius():
    input_dir = "tov-outputs"
    num_lines = 50
    for i in range (1, num_lines + 1):
        input_file = f"{input_dir}/tov{i}.txt"
        df = pd.read_csv(input_file, sep="   ", header=None, on_bad_lines='skip')
        df = df.rename(columns={df.columns[0]: 'e0', df.columns[1]: 'M', df.columns[2]: 'R', df.columns[3]: 'Mb', df.columns[4]: 'rc'})
        xi=[]
        yi=[]
        #needs to convert df to numpy because pandas and matplotlib doesn't get along with well
        xi=df['R'].to_numpy()
        yi=df['M'].to_numpy()
        plt.plot(xi, yi, color="red")
        df_nodelta=pd.read_csv("18.out", sep="   ", header=None, on_bad_lines='skip')
        df_nodelta = df_nodelta.rename(columns={df_nodelta.columns[0]: 'e0', df_nodelta.columns[1]: 'M', df_nodelta.columns[2]: 'R', df_nodelta.columns[3]: 'Mb', df_nodelta.columns[4]: 'rc'})
        xi_nodelta=df_nodelta['R'].to_numpy()
        yi_nodelta=df_nodelta['M'].to_numpy()
        plt.plot(xi_nodelta, yi_nodelta, color="blue", linestyle='dashed')
    plt.legend()
    plt.show()


def plot_pressure_vs_energy_density():
    input_dir = "beta-outputs/with-crust"
    num_lines = 10
    for i in range (1, num_lines + 1):
        fm4_file = f"{input_dir}/beta-crust{i}.txt"
        input_file = f"{input_dir}/beta-crust-Mevfm3-{i}.txt"
        with open(fm4_file, "r") as prevfile, open(input_file, "w") as infile:
            infile.write(prevfile.read())
        df = pd.read_csv(input_file, sep="  ", header=None, on_bad_lines='skip')
        df = df.rename(columns={df.columns[0]: 'density', df.columns[1]: 'energy', df.columns[2]: 'pressure'})
        #print(df)
        df = df.mul({'density':1, 'energy': 197.26, 'pressure': 197.26})
        # df.columns[1] = df.columns[1]*197.26
        # df.columns[2] = df.columns[2]*197.26
        #print (df)
        xi=[]
        yi=[]
        #needs to convert df to numpy because pandas and matplotlib doesn't get along with well
        xi=df['energy'].to_numpy()
        yi=df['pressure'].to_numpy()
        plt.yscale("log")
        plt.plot(xi, yi, color="red")

        old_file = f"beta-eq-eos18.txt"
        new_file = f"beta-eq-eos18-new.dat"
        with open(old_file, "r") as prevfile, open(new_file, "w") as infile:
            infile.write(prevfile.read())

    df_nodelta=pd.read_csv(new_file, sep="  ", header=None, on_bad_lines='skip')
    print(df_nodelta)
    df_nodelta = df_nodelta.rename(columns={df_nodelta.columns[0]: 'density', df_nodelta.columns[1]: 'energy', df_nodelta.columns[2]: 'pressure'})
    #print(df_nodelta)
    df_nodelta = df_nodelta.mul({'density':1, 'energy': 197.26, 'pressure': 197.26})
    xi_nodelta=[]
    yi_nodelta=[]
    xi_nodelta=df_nodelta['energy'].to_numpy()
    yi_nodelta=df_nodelta['pressure'].to_numpy()
    plt.yscale("log")
    plt.plot(xi_nodelta, yi_nodelta, color="blue", linestyle='dashed')
    plt.legend()
    plt.show()

def plot_energy_vs_density():
    input_dir = "beta-outputs/with-crust"
    num_lines = 10
    for i in range (1, num_lines + 1):
        fm4_file = f"{input_dir}/beta-crust{i}.txt"
        input_file = f"{input_dir}/beta-crust-Mevfm3-{i}.txt"
        with open(fm4_file, "r") as prevfile, open(input_file, "w") as infile:
            infile.write(prevfile.read())
        df = pd.read_csv(input_file, sep="  ", header=None, on_bad_lines='skip')
        
        df = df.rename(columns={df.columns[0]: 'density', df.columns[1]: 'energy', df.columns[2]: 'pressure'})
        col = ['energy']
        df[col] = df[col].mul(df['density'], axis=0)
        xi=[]
        yi=[]
        #needs to convert df to numpy because pandas and matplotlib doesn't get along with well
        xi=df['density'].to_numpy()
        yi=df['energy'].to_numpy()
        plt.plot(xi, yi, label=f"file{i}")
    plt.legend()
    plt.show()

def plot_L_density():
    input_dir = "properties-outputs"
    num_lines = 50
    for i in range (1, num_lines + 1):
        input_file = f"{input_dir}/props.txt"
        df = pd.read_csv(input_file, sep=" ", header=None, on_bad_lines='skip')
        #print(df)
        df = df.rename(columns={df.columns[0]: 'id', df.columns[1]: 'r0', df.columns[2]: 'EB', df.columns[3]: 'E_dens', df.columns[4]: 'p', df.columns[5]: 'K0', df.columns[6]: 'Q0', df.columns[7]: 'Esym', df.columns[8]: 'L', df.columns[9]: 'Ksym', df.columns[10]: 'Qsym'})
        xi=[]
        yi=[]
        #needs to convert df to numpy because pandas and matplotlib doesn't get along with well
        xi=df['r0'].to_numpy()
        yi=df['Esym'].to_numpy()
        plt.plot(xi, yi, color="red")
        # df_nodelta=pd.read_csv("NM_properties18.dat", sep=" ", header=None, on_bad_lines='skip')
        # print(df_nodelta)
        # df_nodelta = df_nodelta.rename(columns={df.columns[0]: 'id', df_nodelta.columns[1]: 'r0', df_nodelta.columns[2]: 'EB', df_nodelta.columns[3]: 'K0', df_nodelta.columns[4]: 'Q0', df_nodelta.columns[5]: 'Esym', df_nodelta.columns[6]: 'L', df_nodelta.columns[7]: 'Ksym', df_nodelta.columns[8]: 'Qsym'})
        # xi_nodelta=df_nodelta['r0'].to_numpy()
        # yi_nodelta=df_nodelta['L'].to_numpy()
        # plt.plot(xi_nodelta, yi_nodelta, color="blue", linestyle='dashed')
    plt.legend()
    plt.show()

plot_pressure_vs_energy_density()