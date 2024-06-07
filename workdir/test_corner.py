import corner
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



props="../results/EOS8/props.dat"
corner_plot="corner.dat"
with open( props, 'r') as r, open(corner_plot, 'w') as o: 
    for line in r: 
        #strip() function 
        if line.strip(): 
            o.write(line) 
df=pd.read_csv(corner_plot, sep=",", header=None, skip_blank_lines=True, on_bad_lines='skip')
props1 = df.to_numpy()
# print(df)
good_columns=props1[:,9:13]
# print(good_columns)

figure = corner.corner(good_columns, labels=["Esym", "L", "Ksym", "Qsym"], show_titles=True, cmap=plt.cm.get_cmap('viridis'))
figure.show()
figure.savefig("corner-test.png")