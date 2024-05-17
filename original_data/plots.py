import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#### Plots

input_dir = "tov-outputs"
num_lines = 5


for i in range (1, num_lines + 1):
    input_file = f"{input_dir}/tov{i}.txt"
    df = pd.read_csv(input_file, sep="   ", header=None, on_bad_lines='skip')
    df = df.rename(columns={df.columns[0]: 'e0', df.columns[1]: 'M', df.columns[2]: 'R', df.columns[3]: 'Mb', df.columns[4]: 'rc'})
    #print(input_file)
    xi=[]
    yi=[]
    xi=df['R'].to_numpy()
    yi=df['M'].to_numpy()
    #needs to convert df to numpy because pandas and matplotlib doesn't get along with well
    plt.plot(xi, yi, label=f'file {i}')
#plt.plot(df['x'],df['y1'], label='file {i}')
plt.legend()
plt.show()

# x1=[0,1,2,3,4,5,6,7,8,9,10]
# x2=[0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5]
# y1 = np.sin(x1)
# y2 = np.cos(x2)
# plt.plot(x1, y1)
# plt.plot(x2, y2)
# plt.show()


# input_file = f"{input_dir}/tov1.txt"
# df = pd.read_csv(input_file, sep="   ", on_bad_lines='skip')
#plt.plot(df['a'].to_numpy(), df['b'].to_numpy())
#df = pd.DataFrame(columns=['a','b','c','d','e'])
#df = df.rename(columns={df.columns[0]: 'a', df.columns[1]: 'b', df.columns[2]: 'c', df.columns[3]: 'd', df.columns[4]: 'e'})
#print(input_file)
#print(df)
#df.plot(x='a',y='b',kind='scatter')
# df.columns.get_loc('a')
# df.columns.get_loc('b')
#df.plot(kind='scatter', x='a',y='b')
#plt.plot(df['c'].to_numpy(), df['b'].to_numpy())
# plt.legend()
#plt.show()