import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

# colors = ['red', 'blue', 'green']
colors=['deepskyblue', 'deeppink', 'darkviolet']
font = {'family' : 'normal',
        'size'   : 26}

plt.rc('font', **font)
plt.figure(figsize=(20,20))


for num in [8,20,21]:
    N_points = 100
    df = pd.read_csv(f"../../big-results/props-new-{num}.dat", sep=",", header=None, on_bad_lines='skip')
    # Renaming columns for easier reference
    df.rename(columns={4: "Density", 9: "Symmetry Energy"}, inplace=True)
    print(df)
    # Ensure that we are only working with the necessary columns
    df = df[["Density", "Symmetry Energy"]]
    
    # Convert columns to numpy arrays
    density = df["Density"].to_numpy()
    symmetry_energy = df["Symmetry Energy"].to_numpy()
    
    # Determine the number of curves to plot
    num_curves = len(density) // 100

    # Generate proton fraction points
    dx = np.linspace(df['Density'].min(), df['Density'].max(), N_points)

    esym_i = []
    dens_i = []

    for label in range(1, num_curves+1):
        #let's get a temporary dataframe for each 100 lines
        temp_df = df[(label-1)*100:label*100]
        if not temp_df.empty:  
            dens_df = temp_df['Density']
            esym_df = temp_df['Symmetry Energy']
            # print(f"proton_df: {proton_df}")

            if not dens_df.empty:
                tck = interp1d(dens_df, esym_df, bounds_error=False, kind='linear', fill_value=(np.nan, np.nan))
                interpolated_esym = tck(dx)
                dens_i.extend(dx)
                esym_i.extend(interpolated_esym)
                print(f"Interpolated esym: {interpolated_esym}")

    eos = pd.DataFrame({'density': dens_i, 'e_sym': esym_i})
    print(eos.head())  # Print the first few rows to check the dataframe

    q1 = []
    q3 = []
    dens = []

    for d_value in dx:
        df_temp = eos[eos['density'] == d_value]
        if len(df_temp) > 1:
            q1_temp, q3_temp = np.nanquantile(df_temp['e_sym'], [0.05, 0.95])
        else:
            q1_temp = q3_temp = np.nan
        q1.append(q1_temp)
        q3.append(q3_temp)
        dens.append(d_value)
    
    print(f"dens {num}: {dens}")
    print(f"q1: {q1}")
    print(f"q3: {q3}")
    
    output_file = f"quantile-esym-eos{num}.txt"
    with open(output_file, 'w') as f:
        for d_value, q1_val, q3_val in zip(dens, q1, q3):
            f.write(f"{d_value} {q1_val} {q3_val}\n")
    
    if num == 8:
        plt.plot(dens, q1, color=colors[0], linestyle='dashed')
        plt.plot(dens, q3, color=colors[0], linestyle='dashed')
        plt.fill_between(dens, q1, q3, color=colors[0], alpha=0.3, label=f'EOS {num}')

    elif num==20:
        plt.plot(dens, q1, color=colors[1], linestyle='dashed')
        plt.plot(dens, q3, color=colors[1], linestyle='dashed')
        plt.fill_between(dens, q1, q3, color=colors[1], alpha=0.3, label=f'EOS {num}')

    else:
        plt.plot(dens, q1, color=colors[2], linestyle='dashed')
        plt.plot(dens, q3, color=colors[2], linestyle='dashed')
        plt.fill_between(dens, q1, q3, color=colors[2], alpha=0.3, label=f'EOS {num}')


# plt.title('Symmetry energy vs density - all')
plt.ylabel('Symmetry energy/MeV')
plt.xlabel('Density/fm-3')
plt.legend()
plt.savefig('esym-vs-density-all.png')
plt.show()
