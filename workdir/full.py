import os, subprocess
import matplotlib.pyplot as plt
import pandas as pd

num_lines = 5

def do_eos_delta():
    input_file = "delta.dat"
    output_dir = "beta-outputs"
    temp_input_file = "delta.inp"
    
    # Open the input file
    with open(input_file, "r") as infile:
        lines = infile.readlines()
    
    for i in range(0 , num_lines):
       with open(temp_input_file, "w") as tempfile:
        pass
       
        with open(temp_input_file, "w") as tempfile:
            tempfile.write(lines[i].strip()+"\n")
        
        output_file = f"{output_dir}/beta-eq-eos{i+1}.txt"
        # Execute the external command
        result = subprocess.run("./beta-eq", shell=True)
        result
        # Write (overwrite!) the contents of fort.7 to the output file
        with open("fort.7", "r") as fort_file, open(output_file, "w") as outfile:
            outfile.write(fort_file.read())
        # Remove the temporary input file
        if os.path.exists(temp_input_file):
            os.remove(temp_input_file)
def add_crust():
    core_dir = "beta-outputs/"
    output_dir = "beta-outputs/with-crust"

    for i in range(0, num_lines):
        core_old_file_path = f"{core_dir}beta-eq-eos{i+1}.txt"
        core_new_file_path = f"{core_dir}beta-eq-eos-new{i+1}.txt"
        output_file = f"{output_dir}/beta-crust{i+1}.txt"
        
        with open (core_new_file_path, "w"):
            pass

        with open (core_old_file_path, "r") as core_old_file, open(core_new_file_path, "w") as core_new_file:
            for line in core_old_file:
                if line.strip():
                    core_new_file.write("  ".join(line.split()[:3]) + "\n")


        with open("bps_nl3wr_crust.dat", "r") as crust, open(output_file, "w") as outfile:
            outfile.write(crust.read())
   
        with open(core_new_file_path, "r") as core_file, open(output_file, "a") as outfile:
            outfile.write(core_file.read())
def do_tov_delta():
    input_dir = "beta-outputs/with-crust"
    output_dir = "tov-outputs"
    temp_input_file = "tov.dat"

    for i in range(0, num_lines):
        input_file = f"{input_dir}/beta-crust{i+1}.txt"
        output_file = f"{output_dir}/tov{i+1}.txt"
    
        with open(output_file, "w"), open(temp_input_file, "w"):
            pass
        with open(input_file, "r") as infile, open(temp_input_file, "a") as tempfile:   
            tempfile.write(infile.read())

        with open(temp_input_file, "a") as tempfile:
            tempfile.write("-1. -1. -1.")

        result = subprocess.run("./tov", shell=True)
        result

        with open("tov.out", "r") as tov_file, open(output_file, "w") as outfile:
            outfile.write(tov_file.read())
        
        print(f"tov {i+1} done")

        if os.path.exists(temp_input_file):
            os.remove(temp_input_file)
def do_properties_delta():
    input_file = "delta.dat"
    output_dir = "properties-outputs"
    temp_input_file = "delta.inp"
    
    # Open the input file
    with open(input_file, "r") as infile:
        lines = infile.readlines()
    
    output_file = f"{output_dir}/props.txt"

    with open(output_file, "w"):
        pass
    
    for i in range(0, num_lines):
       with open(temp_input_file, "w") as tempfile:
        pass
       
    
        with open(temp_input_file, "w") as tempfile:
            tempfile.write(lines[i].strip()+"\n")
        
        
        # Execute the external command
        result = subprocess.run("./properties", shell=True)
        result

        #Write (overwrite!) the contents of fort.60 to the output file
        with open("fort.60", "r") as fort_file, open(output_file, "a") as outfile:
            outfile.write(f"{i+1}"+fort_file.read() + '\n')
            #### test carefully #####
            # if lines.strip():
            #     columns = lines.split()
            #     del columns[1]
            #     for i in range(len(columns)):
            #         outfile.write( columns[i] + " ")
            #     outfile.write("\n")
            ####### otherwise use the fix_values() function #####
        # Remove the temporary input file
        if os.path.exists(temp_input_file):
            os.remove(temp_input_file)

###### uncomment if the util inside the function is not working ######
# def fix_columns():
#     input_file = "properties-outputs/props.txt"
#     output_file = "properties-outputs/props_1.txt"
    
#     with open(input_file, "r") as infile, open(output_file, "w") as outfile:
#         for line in infile:
            
#             if line.strip():
#                 columns = line.split()
#                 del columns[1]
#                 for i in range(len(columns)):
#                     outfile.write( columns[i] + " ")
#                 outfile.write("\n")
######################################################################             


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
        plt.plot(xi, yi)
    plt.legend()
    plt.show()
def plot_pressure_vs_energy_density():
    input_dir = "beta-outputs/with-crust"
    for i in range (1, num_lines + 1):
        fm4_file = f"{input_dir}/beta-crust{i}.txt"
        input_file = f"{input_dir}/beta-crust-Mevfm3-{i}.txt"
        with open(fm4_file, "r") as prevfile, open(input_file, "w") as infile:
            infile.write(prevfile.read())
        df = pd.read_csv(input_file, sep="  ", header=None, on_bad_lines='skip')
        print(df)
        df = df.rename(columns={df.columns[0]: 'density', df.columns[1]: 'energy', df.columns[2]: 'pressure'})
        df=df.mul({'density':1, 'energy': 197.26, 'pressure': 197.26})
        # df.columns[1] = df.columns[1]*197.26
        # df.columns[2] = df.columns[2]*197.26
        #print (df)
        xi=[]
        yi=[]
        #needs to convert df to numpy because pandas and matplotlib doesn't get along with well
        xi=df['energy'].to_numpy()
        yi=df['pressure'].to_numpy()
        plt.yscale("log")
        plt.plot(xi, yi)
    plt.legend()
    plt.show()

    
def main():
    do_properties_delta()
    do_eos_delta()
    add_crust()
    do_tov_delta()
    plot_mass_radius()
    #check on corner plots


main()