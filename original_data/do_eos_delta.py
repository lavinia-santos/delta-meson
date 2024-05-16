import os, subprocess

def do_eos_delta():
    input_file = "delta_sorted.dat"
    output_dir = "/beta-outputs"
    temp_input_file = "delta.inp"
    
    #beta=r"C:/Users/lavin/OneDrive/Desktop/Lavinia/UT3/M1/Stage/delta-meson/original_data/beta-eq"
    beta=r"C:/Users/lavin/OneDrive/Desktop/Lavinia/UT3/M1/Stage/delta-meson/original_data/beta-eq"
    num_lines = 5

    # Open the input file
    with open(input_file, "r") as infile:
        lines = infile.readlines()
    
    for i in range(1, num_lines + 1):
        # Write the i-th line to the temporary input file
        with open(temp_input_file, "w") as tempfile:
            tempfile.write(lines[i - 1])
        
        print(i)
        with open(temp_input_file, "r") as tempfile:
            print(tempfile.read())
        
        output_file = f"{output_dir}/beta-eq-eos{i}`.dat"
        if os.path.exists(output_file):
            os.remove(output_file)
        
        # Execute the external command
        "./beta-eq"
        
        # Append the contents of fort.7 to the output file
        with open("fort.7", "r") as fort_file, open(output_file, "a") as outfile:
            outfile.write(fort_file.read())
        
        # Remove the temporary input file
        if os.path.exists(temp_input_file):
            os.remove(temp_input_file)

do_eos_delta()
