import numpy as np
import pandas as pd

eos_number = [8, 20, 21]
props = {}
medians = {}
CI90 = {}
CI95 = {}

for i in eos_number:
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

    props[i] = df.to_numpy()

    # Calculate the median values for each parameter, as well as 90% and 95% CI
    medians[i] = np.median(props[i], axis=0)
    CI90[i] = np.percentile(props[i], [5, 95], axis=0)
    CI95[i] = np.percentile(props[i], [2.5, 97.5], axis=0)
print(props[8][:,9])
# Prepare data for CSV
data = {
    "EOS": [],
    "Parameter": [],
    "Median": [],
    "CI90_Lower": [],
    "CI90_Upper": [],
    "CI95_Lower": [],
    "CI95_Upper": []
}

parameters = ['gr', 'gdel', 'gwr', 'rho0', 'm_eff', 'EB', 'K0', 'Q0', 'Esym', 'L', 'Ksym', 'Qsym']

# for i in eos_number:
#     for idx, param in enumerate(parameters):
#         data["EOS"].append(i)
#         data["Parameter"].append(param)
#         data["Median"].append(medians[i][idx])
#         data["CI90_Lower"].append(CI90[i][0, idx])
#         data["CI90_Upper"].append(CI90[i][1, idx])
#         data["CI95_Lower"].append(CI95[i][0, idx])
#         data["CI95_Upper"].append(CI95[i][1, idx])

# df_output = pd.DataFrame(data)
# df_output.to_csv('eos_statistics.csv', index=False)
