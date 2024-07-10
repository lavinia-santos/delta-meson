import os, subprocess

# change num_lines to the number of lines in the input file
num_lines = 5104

input_file = "delta.dat"
output_dir = "beta-outputs"
temp_input_file = "delta.inp"

# Open the input file
with open(input_file, "r") as infile:
    lines = infile.readlines()

for i in range(0, num_lines):
   with open(temp_input_file, "w") as tempfile:
    pass
   

    with open(temp_input_file, "w") as tempfile:
        tempfile.write(lines[i].strip()+"\n")
    
    #print(i)
    #with open(temp_input_file, "r") as tempfile:
    #its not necessary to remove the old files because it overwrites them (w)
    #output_file1 = f"{output_dir}/beta-eq-eos{i+1}.txt"
    output_file2 = f"{output_dir}/beta-eq-fort2-{i+1}.dat"
    # Execute the external command
    result = subprocess.run("./beta-eq-eos8", shell=True)
        #result
        # Write (overwrite!) the contents of fort.7 to the output file
    # with open("fort.7", "r") as fort_file, open(output_file1, "w") as outfile:
    #     outfile.write(fort_file.read())
    with open("fort.2", "r") as fort_file, open(output_file2, "w") as outfile:
        outfile.write(fort_file.read())
            
    # Remove the temporary input file
    if os.path.exists(temp_input_file):
        os.remove(temp_input_file)
    print(f"beta-eq fort2 {i+1} done")