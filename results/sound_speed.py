
import pandas as pd



eos_number=[8,20,21]


def get_sound_speed():
    for i in eos_number:
        output_file = f"sound-speed-eos{i}.dat"
    
        # Load data from file
        df = pd.read_csv(f'../../big-results/beta-data{i}.dat', sep='\s+', engine='python')
        df = df.rename(columns={df.columns[0]: 'label', df.columns[1]: 'density', df.columns[2]: 'energy_density', df.columns[3]: 'pressure'})
        
        # Sort and filter data
        #df = df.sort_values(by='radius')
        # df = df[df['radius'] < 14.5]
        # df=df[df['radius'] > 10.0]
        # df = df[df['mass'] > 0.5]
        
        # Get unique labels
        labels = df['label'].unique()
        print(f"labels:{labels}")
        with open(output_file, 'w') as f:
                    f.write(f"#label dp/de dp/de^2 rho\n")


        # Initialize lists for dp and de


        for label in labels:
            # Filter data by label
            
            dp = []
            de = []
            temp_df = df[df['label'] == label]
            #print(f"temp_df:{temp_df}")
            # If the filtered data is not empty
            if not temp_df.empty:
                rho=temp_df['density']
                temp_df2 = temp_df.diff()
                #print(f"temp_df2:{temp_df2}")
                dp=temp_df2['pressure']
                de=temp_df2['energy_density']
                #print(f"len dp:{len(dp)} \n de:{len(de)} \n rho:{len(rho)}")

                # Calculate dp and de
                #print(f"label: {label} \n dp:{dp} \n de:{de} \n rho:{rho}")
                #print(f"len dp:{len(dp)} \n de:{len(de)}")
                dp_de=[]
                dp= dp.dropna()
                de = de.dropna()
                #print(f"label: {label} \n dp:{dp} \n de:{de} \n rho:{rho}")

                dp=dp.to_numpy()
                de=de.to_numpy()
                rho=rho.to_numpy()
                #print(f"label: {label} \n dp:{dp} \n de:{de} \n rho:{rho}")
                for k in range(len(dp)):
                    # print(f"dp:{dp[k]} \n de:{de[k]} \n rho:{rho[k]}")
                    
                    dp_de.append(dp[k]/de[k])

                # Write results to file
                #print(f"label: {label} \n len(dp_de): {len(dp_de)} k: {k}")
                with open(output_file, 'a') as f:
                    for i in range(len(dp_de)):
                        f.write(f"{label} {dp_de[i]} {(dp_de[i])**2} {(rho[i]+rho[i+1])/2}\n")


get_sound_speed()
