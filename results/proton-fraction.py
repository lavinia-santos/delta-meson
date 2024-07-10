import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

colors = ['red', 'blue', 'green']

for num in [8,20,21]:
    N_points = 50
    df = pd.read_csv(f'../../big-results/proton-fraction{num}.dat', sep='\s+', engine='python')
    df = df.rename(columns={df.columns[0]: 'label', df.columns[1]: 'density', df.columns[2]: 'proton_fraction'})
    # Add a new column to df with the value 1-xi
    df['1-Xi'] = df['proton_fraction'].apply(lambda x: 1 - x)
    labels = df['label'].unique()
    print(f"labels: {labels}")

    # Generate proton fraction points
    dx = np.linspace(df['density'].min(), df['density'].max(), N_points)

    p_i = []
    dens_i = []

    for label in labels:
        temp_df = df[df['label'] == label]
        if not temp_df.empty:  
            dens_df = temp_df['density']
            proton_df = temp_df['1-Xi']
            # print(f"proton_df: {proton_df}")

            if not dens_df.empty:
                tck = interp1d(dens_df, proton_df, bounds_error=False, kind='linear', fill_value=(np.nan, np.nan))
                interpolated_fraction = tck(dx)
                dens_i.extend(dx)
                p_i.extend(interpolated_fraction)
                print(f"Interpolated fractions: {interpolated_fraction}")

    eos = pd.DataFrame({'density': dens_i, 'proton_fraction': p_i})
    print(eos.head())  # Print the first few rows to check the dataframe

    q1 = []
    q3 = []
    dens = []

    for d_value in dx:
        df_temp = eos[eos['density'] == d_value]
        if len(df_temp) > 1:
            q1_temp, q3_temp = np.nanquantile(df_temp['proton_fraction'], [0.05, 0.95])
        else:
            q1_temp = q3_temp = np.nan
        q1.append(q1_temp)
        q3.append(q3_temp)
        dens.append(d_value)
    
    print(f"dens {num}: {dens}")
    print(f"q1: {q1}")
    print(f"q3: {q3}")
    
    output_file = f"test-quartile-proton{num}.txt"
    with open(output_file, 'w') as f:
        for d_value, q1_val, q3_val in zip(dens, q1, q3):
            f.write(f"{d_value} {q1_val} {q3_val}\n")
    
    #plt.fill_between(proton_f, q1, q3, color=colors[0], alpha=0.3, label=f'EOS {num}')
    if num == 8:
        plt.plot(dens, q1, color=colors[0], label=f'EOS {num}')
        plt.plot(dens, q3, color=colors[0])
    elif num==20:
        plt.plot(dens, q1, color=colors[1], label=f'EOS {num}')
        plt.plot(dens, q3, color=colors[1])
    else:
        plt.plot(dens, q1, color=colors[2])
        plt.plot(dens, q3, color=colors[2])

plt.title('Proton fraction vs density - all')
plt.ylabel('Proton Fraction')
plt.xlabel('Density')
plt.legend()
plt.show()
