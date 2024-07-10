import pandas as pd
import numpy as np


eos_number=[8,20,21]

for num in eos_number:
    sound_speed_file = f"sound-speed-eos{num}.dat"
    tov_file = f"../../big-results/tov-data{num}.dat"

    output_file = f"sound-speed-tov-data-eos{num}.dat"


    df_tov = pd.read_csv(tov_file, sep='\s+', engine='python')
    df_tov = df_tov.rename(columns={df_tov.columns[0]: 'label', df_tov.columns[1]: 'energy density', df_tov.columns[2]: 'mass', df_tov.columns[3]: 'radius', df_tov.columns[4]: 'baryonic mass', df_tov.columns[5]: 'central density'})
    labels_tov=df_tov['label'].unique()

    df_sound_speed = pd.read_csv(sound_speed_file, sep='\s+', engine='python')
    df_sound_speed = df_sound_speed.rename(columns={df_sound_speed.columns[0]: 'label', df_sound_speed.columns[1]: 'dp/de', df_sound_speed.columns[2]: 'dp/de**2', df_sound_speed.columns[3]: 'density'})
    labels_sound_speed=df_sound_speed['label'].unique()
    with open(output_file, 'w') as f:
        f.write("label Mmax(tov) dp/de dp/de**2 density(tov) density(sound speed)  \n")
    for label in labels_tov:
        temp_df_tov = df_tov[df_tov['label'] == label]
        temp_df_sound_speed = df_sound_speed[df_sound_speed['label'] == label]
        #print(f"label: {label} temp_df_tov: {temp_df_tov} temp_df_sound_speed: {temp_df_sound_speed}")
        
        
        #now, let's match the sound speed data with the tov data through the density
        #for that, we get the Mmax from the tov data and find the corresponding sound speed through the density
        
        Mmax = temp_df_tov['mass'].max()
        
        density_Mmax = temp_df_tov[temp_df_tov['mass']==Mmax]['central density'].values[0]
        #radius_max_mass = df_nodelta[df_nodelta['M'] == max_mass]['R'].values[0]

        # print(f"label: {label} Mmax: {Mmax} density_Mmax: {density_Mmax}\n")
        s_speed_dens_max=temp_df_sound_speed.iloc[(temp_df_sound_speed['density']-density_Mmax).abs().argsort()[:3]]
        #now, let's get only the density values
        s_speed_dens_max = s_speed_dens_max['density'].to_numpy()
        #and now, let's get the density value that is closest to the density_Mmax
        
        density_Mmax_s_speed = s_speed_dens_max[np.abs(s_speed_dens_max-density_Mmax).argmin()]
        
        # #now, let's get the sound speed values for the density_Mmax
        # s_speed_dens_max = temp_df_sound_speed[temp_df_sound_speed['density'] == density_Mmax]
        # print(s_speed_dens_max)
        # print(s_speed_dens_max-density_Mmax)

        # print(f"label: {label} density_Mmax: {density_Mmax} density_Mmax_s_speed: {density_Mmax_s_speed} \n")
        
        #print(f"label: {label} density_Mmax: {density_Mmax} \ns_speed_dens_max: \n{s_speed_dens_max}")
        #temp_df_sound_speed = temp_df_sound_speed[temp_df_sound_speed['density'] == density_Mmax]
        
        #now, we write the data to a file, along with the Mmax, label, and density

        dpde=temp_df_sound_speed[temp_df_sound_speed['density']==density_Mmax_s_speed]['dp/de'].values[0]
        dpde2=temp_df_sound_speed[temp_df_sound_speed['density']==density_Mmax_s_speed]['dp/de**2'].values[0]
        # print(f"label: {label} Mmax: {Mmax} dp/de: {dpde} dp/de**2: {dpde2} density_Mmax: {density_Mmax} density_Mmax_s_speed: {density_Mmax_s_speed} \n")
        with open(output_file, 'a') as f:
            f.write(f"{label} {Mmax} {dpde} {dpde2} {density_Mmax} {density_Mmax_s_speed} \n")
