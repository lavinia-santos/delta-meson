import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

colors=['blue', 'red', 'green']
# Read data
for num in [8]:
    df = pd.read_csv(f"../../big-results/props-new-{num}.dat", sep=",", header=None, on_bad_lines='skip')
    # Renaming columns for easier reference
    df.rename(columns={3: "Density", 13: "Symmetry Energy"}, inplace=True)
    print(df)
    # Ensure that we are only working with the necessary columns
    df = df[["Density", "Symmetry Energy"]]
    
    # Convert columns to numpy arrays
    density = df["Density"].to_numpy()
    symmetry_energy = df["Symmetry Energy"].to_numpy()
    
    # Determine the number of curves to plot
    num_curves = len(density) // 100
    
    # Plot each curve
    for i in range(num_curves):
        start = i * 100
        end = (i + 1) * 100
        if num==8:
            plt.plot(density[start:end], symmetry_energy[start:end], color=colors[0])
        elif num==20:
            plt.plot(density[start:end], symmetry_energy[start:end], color=colors[1])
        elif num==21:
            plt.plot(density[start:end], symmetry_energy[start:end], color=colors[2])
        #plt.plot(density[start:end], symmetry_energy[start:end])
    #let's write the data to a file
    # output_file = f"symmetry-energy-eos{num}.txt"
    # with open(output_file, 'w') as f:
    #     for d_value, s_value in zip(density, symmetry_energy):
    #         f.write(f"{d_value} {s_value}\n")

plt.xticks(np.linspace(min(density), max(density), 10))
plt.yticks(np.linspace(min(symmetry_energy), max(symmetry_energy), 10))
plt.legend()
plt.xlabel("Density")
plt.ylabel("Symmetry Energy")
plt.title("Symmetry Energy vs Density for EOS")
plt.show()
