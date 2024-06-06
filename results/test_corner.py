import corner
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#eos_number=[20,21,8]
eos_number=[21]
#plot coupling for 21


for i in eos_number:
    #props=f"EOS{i}/props.dat"
    couplings="../../../../../../../../Downloads/para_eos21.csv"
    corner_plot="corner.dat"
    with open( couplings, 'r') as r, open(corner_plot, 'w') as o: 
        for line in r: 
            #strip() function 
            if line.strip(): 
                o.write(line) 
    df=pd.read_csv(corner_plot, sep=",", header=None, skip_blank_lines=True, on_bad_lines='skip')
    #df=df.rename(columns={df.columns[9]: 'Esym', df.columns[10]: 'L', df.columns[11]: 'Ksym', df.columns[12]: 'Qsym'})
    df=df.rename(columns={df.columns[0]: 'label', df.columns[1]: 'gr', df.columns[2]: 'gdel', df.columns[3]: 'lambda'})
    # print(df)
    # df=df[df['L'] < 200]
    # df=df[df['L'] > 0]
    # df=df[df['Ksym'] > -200]
    # df=df[df['Ksym'] < 100]
    # df=df[df['Esym'] > 0]
    # df=df[df['Esym'] < 100]
    # df=df[df['Qsym'] > 1000]
    # df=df[df['Qsym'] < 4000]
    props1 = df.to_numpy()
    print(df)
    good_columns=props1[:,1:4]
    # print(good_columns)

    # print(good_columns)
    
    
    figure = corner.corner(good_columns, labels=["gr", "gdel", "lambda"], show_titles=True)
    # figure.show()
    # plt.show()
    figure.suptitle(f"EOS{i}", fontsize=16)
    figure.savefig(f"corner-couplings{i}.png")