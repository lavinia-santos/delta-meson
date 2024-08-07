import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#import sys
from scipy.interpolate import interp1d

#original_stdout = sys.stdout


############################################
#2nd try
#Let's try with matrices instead of lists
#############################################
eos_number=[8,20,21]


def plot_mr_curve():
    for i in eos_number:
        N_points = 100
        output_file = f"EOS{i}/output-quartile-2-CI90_{i}.txt"
    
        # Load data from file
        df = pd.read_csv(f'../../big-results/tov-data{i}.dat', sep='\s+', engine='python')
        df = df.rename(columns={df.columns[0]: 'label', df.columns[1]: 'energy_density', df.columns[2]: 'mass', df.columns[3]: 'radius', df.columns[4]: 'baryonic_masses', df.columns[5]: 'density'})
        
        # Sort and filter data
        #df = df.sort_values(by='radius')
        df = df[df['radius'] < 14.5]
        # df=df[df['radius'] > 10.0]
        df = df[df['mass'] > 0.5]
        print(f"df:{df}")
        # Generate mass points
        M_x = np.linspace(df['mass'].min(), df['mass'].max(), N_points)
        
        # Get unique labels
        labels = df['label'].unique()
        print(f"labels:{labels}")
        #N_models = len(labels)
        
        # Initialize lists for M and R
        M = []
        R = []

        for label in labels:
            # Filter data by label
            temp_df = df[df['label'] == label]

            # If the filtered data is not empty
            if not temp_df.empty:

                
                # Slice the data from the index of maximum mass
                mass_df = temp_df['mass']
                radius_df = temp_df['radius']
                # print(f"mass_df:{mass_df }, radius_df:{radius_df}")

                if not mass_df.empty:
                # Interpolation
                    tck = interp1d(mass_df, radius_df, bounds_error=False, kind='linear', fill_value=(np.nan, np.nan))
                
                    # Append interpolated values to M and R lists
                    R.extend(tck(M_x))
                    M.extend(M_x)

        
        # Create a DataFrame for interpolated values
        eos = pd.DataFrame({'M': M, 'R': R})
    
        
        # Initialize lists for quartiles and mass
        q1 = []
        q3 = []
        Mass = []
        # Compute quartiles
        for mass in M_x:
            df_temp = eos[eos['M'] == mass]
            if len(df_temp) > 1:  # Ensure there are enough points to calculate quantiles
                q1_temp, q3_temp = np.nanquantile(df_temp['R'], [0.05, 0.95])
            else:
                q1_temp, q3_temp = np.nan, np.nan  # Handle cases with insufficient data
            q1.append(q1_temp)
            q3.append(q3_temp)
            Mass.append(mass)

        # Write results to file
        with open(output_file, 'w') as f:
            for mass, q1_val, q3_val in zip(Mass, q1, q3):
                f.write(f"{mass} {q1_val} {q3_val}\n")
        
        # Plot the results
        plt.clf()
        plt.plot(q1, Mass, linestyle='dashed', color='black')
        plt.plot(q3, Mass, linestyle='dashed', color='black')
        plt.xlabel('Radius')
        plt.ylabel('Mass')
        plt.title(f"EOS{i}")
        plt.legend()
        #plt.savefig(f"mr-q-90CI-plot{i}.png")
        plt.show()

plot_mr_curve()

