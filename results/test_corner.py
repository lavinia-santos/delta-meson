import corner
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


eos_number=[20,21,8]

for i in eos_number:
    props=f"EOS{i}/props.dat"
    corner_plot="corner.dat"
    with open( props, 'r') as r, open(corner_plot, 'w') as o: 
        for line in r: 
            #strip() function 
            if line.strip(): 
                o.write(line) 
    df=pd.read_csv(corner_plot, sep=",", header=None, skip_blank_lines=True, on_bad_lines='skip')
    df=df.rename(columns={df.columns[9]: 'Esym', df.columns[10]: 'L', df.columns[11]: 'Ksym', df.columns[12]: 'Qsym'})
    print(df)
    df=df[df['L'] < 100]
    df=df[df['L'] > -100]
    df=df[df['Ksym'] > -200]
    df=df[df['Ksym'] < 200]
    props1 = df.to_numpy()
    print(df)
    good_columns=props1[:,9:13]
    print(good_columns)

    # print(good_columns)
    
    
    figure = corner.corner(good_columns, labels=["Esym", "L", "Ksym", "Qsym"], show_titles=True)
    # figure.show()
    # plt.show()
    figure.suptitle(f"EOS{i}", fontsize=16)
    figure.savefig(f"corner-test-props{i}.png")