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
eos_number=[8]


def get_sound_speed():
    for i in eos_number:
        output_file = f"sound-speed-eos{i}.dat"
    
        # Load data from file
        df = pd.read_csv(f'../../big-results/beta-data{i}', sep='\s+', engine='python')
        df = df.rename(columns={df.columns[0]: 'label', df.columns[1]: 'density', df.columns[2]: 'energy_density', df.columns[3]: 'pressure'})
        
        # Sort and filter data
        #df = df.sort_values(by='radius')
        # df = df[df['radius'] < 14.5]
        # df=df[df['radius'] > 10.0]
        # df = df[df['mass'] > 0.5]
        
        # Get unique labels
        labels = df['label'].unique()
        print(f"labels:{labels}")
        


        # Initialize lists for dp and de
        dp = []
        de = []

        for label in labels:
            # Filter data by label
            temp_df = df[df['label'] == label]

            # If the filtered data is not empty
            if not temp_df.empty:
                p=temp_df['pressure']
                e=temp_df['energy_density']
                rho=temp_df['density']
                # Calculate dp and de
                dp.append(p.diff())
                de.append(e.diff())
            dp_de=[]
            for i in range(len(dp)):
                dp[i] = dp[i].dropna()
                de[i] = de[i].dropna()
                dp_de.append(dp[i]/de[i])
            # Write results to file
            with open(output_file, 'w') as f:
                for i in range(len(dp_de)):
                    f.write(f"{dp_de[i]} {(dp_de[i])**2} {(rho[i]+rho[i+1])/2}\n")


get_sound_speed()
