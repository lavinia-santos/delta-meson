import os, subprocess
import matplotlib.pyplot as plt
import pandas as pd

num_lines = 5

def do_eos_delta():
    input_file = "delta_sorted.dat"
    output_dir = "beta-outputs"
    temp_input_file = "delta.inp"

    # Open the input file
    with open(input_file, "r") as infile:
        lines = infile.readlines()
    
    for i in range(1, num_lines + 1):
       with open(temp_input_file, "w") as tempfile:
        pass
       
    
        with open(temp_input_file, "w") as tempfile:
            tempfile.write(lines[i].strip()+"\n")
        
        #print(i)
        #with open(temp_input_file, "r") as tempfile:
        #its not necessary to remove the old files because it overwrites them (w)
        output_file = f"{output_dir}/beta-eq-eos{i}.txt"
        # Execute the external command
        result = subprocess.run("./beta-eq", shell=True)
            #result
            # Write (overwrite!) the contents of fort.7 to the output file
        with open("fort.7", "r") as fort_file, open(output_file, "w") as outfile:
            outfile.write(fort_file.read())
                
        # Remove the temporary input file
        if os.path.exists(temp_input_file):
            os.remove(temp_input_file)
def add_crust():
    core_dir = "beta-outputs/"
    output_dir = "beta-outputs/with-crust"

    for i in range(1, num_lines + 1):
        core_old_file_path = f"{core_dir}beta-eq-eos{i}.txt"
        core_new_file_path = f"{core_dir}beta-eq-eos-new{i}.txt"
        output_file = f"{output_dir}/beta-crust{i}.txt"
        
        with open (core_new_file_path, "w"):
            pass

        with open (core_old_file_path, "r") as core_old_file, open(core_new_file_path, "w") as core_new_file:
            for line in core_old_file:
                if line.strip():
                    core_new_file.write("\t".join(line.split()[:3]) + "\n")

    
        # with open(output_file, "w"):
        #     pass
        with open("bps_nl3wr_crust.dat", "r") as crust, open(output_file, "w") as outfile:
            outfile.write(crust.read())
   
        with open(core_new_file_path, "r") as core_file, open(output_file, "a") as outfile:
            outfile.write(core_file.read())
def do_tov_delta():
    input_dir = "beta-outputs/with-crust"
    output_dir = "tov-outputs"
    temp_input_file = "tov.dat"
    

    for i in range(1, num_lines + 1):
        input_file = f"{input_dir}/beta-crust{i}.txt"
        output_file = f"{output_dir}/tov{i}.txt"
    
        with open(output_file, "w"), open(temp_input_file, "w"):
            pass
        with open(input_file, "r") as infile, open(temp_input_file, "a") as tempfile:   
            tempfile.write(infile.read())
        
        #print(tempfile)
        
        with open(temp_input_file, "a") as tempfile:
            tempfile.write("-1. -1. -1.")

        result = subprocess.run("./tov", shell=True)
        result
        #result = subprocess.run("./beta-eq", shell=True)

        with open("tov.out", "r") as tov_file, open(output_file, "w") as outfile:
            outfile.write(tov_file.read())
        
        with open(temp_input_file, "r") as tempfile:
            pass
        print(f"tov {i} done")

def plot_mass_radius():
    input_dir = "tov-outputs"
    for i in range (1, num_lines + 1):
        input_file = f"{input_dir}/tov{i}.txt"
        df = pd.read_csv(input_file, sep="   ", header=None, on_bad_lines='skip')
        df = df.rename(columns={df.columns[0]: 'e0', df.columns[1]: 'M', df.columns[2]: 'R', df.columns[3]: 'Mb', df.columns[4]: 'rc'})
        xi=[]
        yi=[]
        #needs to convert df to numpy because pandas and matplotlib doesn't get along with well
        xi=df['R'].to_numpy()
        yi=df['M'].to_numpy()
        plt.plot(xi, yi, label=f'file {i}')
    plt.legend()
    plt.show()

def main():
    do_eos_delta()
    add_crust()
    do_tov_delta()
    plot_mass_radius() 

main()