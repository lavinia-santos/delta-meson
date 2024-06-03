import corner
import numpy as np
import pandas as pd



props="properties-outputs/props.dat"
corner_plot="corner.dat"
with open( props, 'r') as r, open(corner_plot, 'w') as o: 
    for line in r: 
        #strip() function 
        if line.strip(): 
            o.write(line) 
df=pd.read_csv(corner_plot, sep="\t", header=None, skip_blank_lines=True, on_bad_lines='skip')
props1 = df.to_numpy()

good_columns=props1[:,1:4]

figure = corner.corner(good_columns, labels=["grho", "gdel", "gwr"], show_titles=True)
figure.show()
figure.savefig("corner-test.png")