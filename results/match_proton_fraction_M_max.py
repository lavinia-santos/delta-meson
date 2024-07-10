import pandas as pd
import numpy as np


eos_number=[8,20,21]

for num in eos_number:
    proton_fraction_file = f"../../big-results/proton-fraction{num}.dat"
    tov_file = f"../../big-results/tov-data{num}.dat"

    output_file = f"proton-fraction-tov-data-eos{num}.dat"


    df_tov = pd.read_csv(tov_file, sep='\s+', engine='python')
    df_tov = df_tov.rename(columns={df_tov.columns[0]: 'label', df_tov.columns[1]: 'energy density', df_tov.columns[2]: 'mass', df_tov.columns[3]: 'radius', df_tov.columns[4]: 'baryonic mass', df_tov.columns[5]: 'central density'})
    labels_tov=df_tov['label'].unique()

    df_proton_fraction = pd.read_csv(proton_fraction_file, sep='\s+', engine='python')
    df_proton_fraction = df_proton_fraction.rename(columns={df_proton_fraction.columns[0]: 'label', df_proton_fraction.columns[1]: 'density', df_proton_fraction.columns[2]: 'proton fraction'})
    labels_sound_speed=df_proton_fraction['label'].unique()
    with open(output_file, 'w') as f:
        f.write("label Mmax(tov) Xi 1-Xi density(tov) density(proton fraction)  \n")
    for label in labels_tov:
        temp_df_tov = df_tov[df_tov['label'] == label]
        temp_df_proton_fraction = df_proton_fraction[df_proton_fraction['label'] == label]
        #print(f"label: {label} temp_df_tov: {temp_df_tov} temp_df_proton_fraction: {temp_df_proton_fraction}")
        
        
        #now, let's match the sound speed data with the tov data through the density
        #for that, we get the Mmax from the tov data and find the corresponding sound speed through the density
        
        Mmax = temp_df_tov['mass'].max()
        
        density_Mmax = temp_df_tov[temp_df_tov['mass']==Mmax]['central density'].values[0]
        #radius_max_mass = df_nodelta[df_nodelta['M'] == max_mass]['R'].values[0]

        # print(f"label: {label} Mmax: {Mmax} density_Mmax: {density_Mmax}\n")
        proton_dens_max=temp_df_proton_fraction.iloc[(temp_df_proton_fraction['density']-density_Mmax).abs().argsort()[:3]]
        #now, let's get only the density values
        proton_dens_max = proton_dens_max['density'].to_numpy()
        #and now, let's get the density value that is closest to the density_Mmax
        
        density_Mmax_proton = proton_dens_max[np.abs(proton_dens_max-density_Mmax).argmin()]
        
        # #now, let's get the sound speed values for the density_Mmax
        # proton_dens_max = temp_df_proton_fraction[temp_df_proton_fraction['density'] == density_Mmax]
        # print(proton_dens_max)
        # print(proton_dens_max-density_Mmax)

        # print(f"label: {label} density_Mmax: {density_Mmax} density_Mmax_proton: {density_Mmax_proton} \n")
        
        #print(f"label: {label} density_Mmax: {density_Mmax} \nproton_dens_max: \n{proton_dens_max}")
        #temp_df_proton_fraction = temp_df_proton_fraction[temp_df_proton_fraction['density'] == density_Mmax]
        
        #now, we write the data to a file, along with the Mmax, label, and density

        Xi=temp_df_proton_fraction[temp_df_proton_fraction['density']==density_Mmax_proton]['proton fraction'].values[0]
        # print(f"label: {label} Mmax: {Mmax} dp/de: {dpde} dp/de**2: {dpde2} density_Mmax: {density_Mmax} density_Mmax_proton: {density_Mmax_proton} \n")
        with open(output_file, 'a') as f:
            f.write(f"{label} {Mmax} {Xi} {1-Xi} {density_Mmax} {density_Mmax_proton} \n")
