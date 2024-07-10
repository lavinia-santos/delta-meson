import time
import pandas as pd
import numpy as np
from scipy.interpolate import interp1d
import os
import matplotlib.pyplot as plt
import corner

start_time = time.time()
eos_number = [8, 20, 21]

full_arrays = {}
titles = {}
props = {}
sound = {}
proton_f={}

for i in eos_number:
    results = f"../../big-results/tov-data{i}.dat"
    corner_plot = "corner.dat"
    
    with open(results, 'r') as r, open(corner_plot, 'w') as o: 
        for line in r: 
            if line.strip(): 
                o.write(line)
    
    df_NS = pd.read_csv(corner_plot, sep='\s+', engine='python')
    df_NS = df_NS.rename(columns={
        df_NS.columns[0]: 'label', 
        df_NS.columns[1]: 'energy_density', 
        df_NS.columns[2]: 'mass', 
        df_NS.columns[3]: 'radius', 
        df_NS.columns[4]: 'baryonic_masses', 
        df_NS.columns[5]: 'density'
    })
    
    labels = df_NS['label'].unique()
    
    max_masses = []
    radii_max_masses = []

    for label in labels:
        temp_df = df_NS[df_NS['label'] == label]
        max_mass = temp_df['mass'].max()
        radius_max_mass = temp_df[temp_df['mass'] == max_mass]['radius'].values[0]
        #let's filter the data to avoid junk data
        # if max_mass < 2.5:
        max_masses.append(max_mass)
        radii_max_masses.append(radius_max_mass)

    masses_14 = []
    radii_masses_14 = []
    
    for label in labels:
        temp_df = df_NS[df_NS['label'] == label]
        if temp_df[temp_df['mass'] == 1.4].empty:
            tck = interp1d(temp_df['mass'], temp_df['radius'], bounds_error=False, kind='linear', fill_value=(np.nan, np.nan))
            radius = float(tck(1.4))
            radii_masses_14.append(radius)
            masses_14.append(1.4)
        else:
            radii_masses_14.append(temp_df[temp_df['mass'] == 1.4]['radius'].values[0])
            masses_14.append(1.4)

    masses_20 = []
    radii_masses_20 = []

    for label in labels:
        temp_df = df_NS[df_NS['label'] == label]
        if temp_df[temp_df['mass'] == 2.0].empty:
            tck = interp1d(temp_df['mass'], temp_df['radius'], bounds_error=False, kind='linear', fill_value=(np.nan, np.nan))
            radius = float(tck(2.0))
            radii_masses_20.append(radius)
            masses_20.append(2.0)
        else:
            radii_masses_20.append(temp_df[temp_df['mass'] == 2.0]['radius'].values[0])
            masses_20.append(2.0)

    properties = f"EOS{i}/props.dat"

    df = pd.read_csv(properties, sep=',', on_bad_lines='skip')
    df = df.rename(columns={
        df.columns[0]: 'label', df.columns[1]: 'gr', df.columns[2]: 'gdel', 
        df.columns[3]: 'gwr', df.columns[4]: 'rho0', df.columns[5]: 'm_eff', 
        df.columns[6]: 'EB', df.columns[7]: 'K0', df.columns[8]: 'Q0', 
        df.columns[9]: 'Esym', df.columns[10]: 'L', df.columns[11]: 'Ksym', 
        df.columns[12]: 'Qsym'
    })
    del df['label']
    
    #let's filter the data to avoid junk data
    df = df[df['Ksym'] > -300]
    df = df[df['L'] > 0]

    #now, let's include the sound speed data at Mmax
    df_sound_speed = pd.read_csv(f"../../big-results/sound-speed-tov-data-eos{i}.dat", sep='\s+', engine='python')
    df_sound_speed = df_sound_speed.rename(columns={df_sound_speed.columns[0]: 'label', df_sound_speed.columns[1]: 'Mmax', df_sound_speed.columns[2]: 'dp/de', df_sound_speed.columns[3]: 'dp/de**2', df_sound_speed.columns[4]: 'density_tov', df_sound_speed.columns[5]: 'density_sound_speed'})
    #filtering to dp/de < 1
    df_sound_speed = df_sound_speed[df_sound_speed['dp/de'] <= 1]
    df_sound_speed = df_sound_speed[df_sound_speed['dp/de'] > 0.35]

    #the same with yp
    df_proton_fraction = pd.read_csv(f"../../big-results/proton-fraction-tov-data-eos{i}.dat", sep='\s+', engine='python')
    df_proton_fraction = df_proton_fraction.rename(columns={df_proton_fraction.columns[0]: 'label', df_proton_fraction.columns[1]: 'Mmax', df_proton_fraction.columns[2]: 'Xi', df_proton_fraction.columns[3]: '1-Xi', df_proton_fraction.columns[4]: 'density_tov', df_proton_fraction.columns[5]: 'density_proton_fraction'})
    #filtering
    df_proton_fraction = df_proton_fraction[df_proton_fraction['1-Xi'] <= 0.16]
    df_proton_fraction = df_proton_fraction[df_proton_fraction['1-Xi'] >= 0.1]
    
    # Convert properties dataframe to numpy array
    props[i] = df.to_numpy()
    sound[i] = df_sound_speed['dp/de'].to_numpy()
    proton_f[i] = df_proton_fraction['1-Xi'].to_numpy()


    # Ensure props and sound have compatible shapes with radii_masses_14
    target_length = len(radii_masses_14)
    
    # Adjust props[i] shape
    if props[i].shape[0] < target_length:
        while props[i].shape[0] < target_length:
            props[i] = np.vstack([props[i], np.full((1, props[i].shape[1]), np.nan)])
    elif props[i].shape[0] > target_length:
        props[i] = props[i][:target_length]
    
    # Adjust sound[i] shape
    if sound[i].shape[0] < target_length:
        while sound[i].shape[0] < target_length:
            sound[i] = np.append(sound[i], np.nan)
    elif sound[i].shape[0] > target_length:
        sound[i] = sound[i][:target_length]

    #Adjust proton_f[i] shape
    if proton_f[i].shape[0] < target_length:
        while proton_f[i].shape[0] < target_length:
            proton_f[i] = np.append(proton_f[i], np.nan)
    elif proton_f[i].shape[0] > target_length:
        proton_f[i] = proton_f[i][:target_length]
    
    
    
    # Combine arrays into full_array
    full_arrays[i] = np.column_stack((
        radii_masses_14, 
        radii_masses_20, 
        max_masses, 
        radii_max_masses, 
        props[i][:,8], 
        props[i][:,9], 
        props[i][:,10], 
        sound[i],
        proton_f[i]
    ))
    
    full_arrays[i] = full_arrays[i][~np.isnan(full_arrays[i]).any(axis=1)]
    os.remove(corner_plot)

end_time = time.time()
execution_time = end_time - start_time
print(f"Tempo de execução: {execution_time} segundos")

# Verificação se os arrays foram preenchidos corretamente antes de fazer os plots
if all(key in full_arrays for key in [8, 20, 21]):
    figure = corner.corner(
        full_arrays[8], color='teal', quantiles=[0.16, 0.5, 0.84], 
        labels=["R1.4", "R2.0", "Mmax", "R_Mmax", "Esym", "L", "Ksym", "sound speed", "proton fraction"], 
        label='EOS8', show_titles=False, smooth=True, smooth1d=True, 
        label_kwargs=dict(fontsize=20), title_kwargs=dict(fontsize=10, color='teal', horizontalalignment='left', verticalalignment='top')
    )
    corner.corner(
        full_arrays[20], fig=figure, color='orangered', quantiles=[0.16, 0.5, 0.84], 
        label='EOS20', show_titles=False, smooth=True, smooth1d=True, 
        label_kwargs=dict(fontsize=20), title_kwargs=dict(fontsize=10, color='orangered', horizontalalignment='right', verticalalignment='center')
    )
    corner.corner(
        full_arrays[21], fig=figure, color='yellowgreen', quantiles=[0.16, 0.5, 0.84], 
        label='EOS21', show_titles=False, smooth=True, smooth1d=True, 
        label_kwargs=dict(fontsize=20), title_kwargs=dict(fontsize=10, color='yellowgreen', horizontalalignment='center', verticalalignment='bottom')
    )
    figure.legend(['EOS 8','_','_','_','EOS 20','_','_','_','EOS 21'], fontsize=30, frameon=False, loc='upper right')
    plt.savefig("corner_NS.png")
    plt.show()
else:
    print("Erro: Um ou mais arrays não foram preenchidos corretamente.")
