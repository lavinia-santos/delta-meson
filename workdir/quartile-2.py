import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys
from scipy.interpolate import interp1d

original_stdout = sys.stdout


############################################
#2nd try
#Let's try with matrices instead of lists
#############################################




def plot_mr_curve():
    M=[]
    R=[]
    q1=[]
    q3=[]
    Mass=[]
    output_file = "output-quartile.txt"
    # Load data from file
    N_points=200
    df = pd.read_csv('tov-data-ex.dat', sep='   ')
    df = df.rename(columns={df.columns[0]: 'label', df.columns[1]: 'energy density', df.columns[2]: 'mass', df.columns[3]: 'radius', df.columns[4]: 'baryonic masses', df.columns[5]: 'density'})
    M_x=np.linspace(min(df.mass), max(df.mass), N_points)
    print(df)

    labels = np.asarray(df['label'])
    labels = np.unique(labels)
    #print(f"labels:{labels}")

    N_models = len(labels)

    for x in range(5001,N_models+5001):
        print(x)

        M_Temp = np.asarray(df.mass[df.label == x])
        #M_Temp = np.sort(M_Temp)
        
        #print(f"M_Temp:{M_Temp}")
        R_Temp = np.asarray(df.radius[df.label == x])
        #R_Temp = np.sort(R_Temp)
        #print(f"R_Temp:{R_Temp}")
        
        #index=M_Temp.argmax()
        # print(f"index:{index}")
        # M_df=M_Temp[index:]
        # R_df=R_Temp[index:]
        # print(f"M_df:{M_df}, R_df:{R_df}")
        #if x !=1:
        tck = interp1d(M_Temp, R_Temp, bounds_error=False, kind='linear', fill_value=(np.nan, np.nan))

        for k in range(N_points):
            R_Temp=tck(M_x[k])
            M.append(M_x[k])
            R.append(R_Temp)
    eos=pd.DataFrame({'M':M, 'R':R})

    #print(eos)
    count=0
    for mass in eos['M']:
        #print(count, len(eos['M']))
        #print(f"{count}/{len(eos['M'])}")
        #count+=1
        df_temp=eos.query(f'M=={mass}')

        q1_temp,q3_temp=np.nanquantile(df_temp['R'], [0.25, 0.75])
        q1.append(q1_temp)
        q3.append(q3_temp)
        Mass.append(mass)

    with open(output_file, 'a') as f:
        for i in range(len(Mass)):
            f.write(f"{Mass[i]} {q1[i]} {q3[i]}\n")
    
    # print(f"q1:{q1}")
    # print(f"q3:{q3}")
    # print(f"mass:{Mass}")

    plt.plot(q1, Mass, 'r-')
    plt.plot(q3, Mass, 'b-')
    plt.show()



plot_mr_curve()



