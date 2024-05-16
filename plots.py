import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#### Plots

input_dir = "tov-outputs"
num_lines = 3


for i in range (1, num_lines + 1):
    input_file = f"{input_dir}/tov{i}.txt"
    df = pd.read_csv(input_file, sep=" ", header=None, on_bad_lines='skip')
    df.columns = ["e0", "M", "R", "Mb","rc"]
    #print(df)
    #fig, ax = plt.subplots()
    plt.plot(df['R'],df['M'], label='file {i}')
    plt.legend()
    plt.show()
