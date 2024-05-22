import os, subprocess

def do_eos_delta():
    ######################## MERGED FILES ############################

    # input_file = "delta.dat"
    # output_dir = "beta-outputs"
    # temp_input_file = "delta.inp"
    
    # num_lines = 2

    # # Open the input file
    # with open(input_file, "r") as infile:
    #     lines = infile.readlines()
    # output_file = f"{output_dir}/eos-data.txt"

    # for i in range(0 , num_lines):
    #    with open(temp_input_file, "w") as tempfile:
    #     pass
       
    
    #     with open(temp_input_file, "w") as tempfile:
    #         tempfile.write(lines[i].strip()+"\n")
        
    #     #print(i)
    #     #with open(temp_input_file, "r") as tempfile:
    #     #its not necessary to remove the old files because it overwrites them (w)
    #     # Execute the external command
    #     result = subprocess.run("./beta-eq", shell=True)
    #         #result
    #         # Write (overwrite!) the contents of fort.7 to the output file
    #     with open("fort.7", "r") as fort_file, open(output_file, "w") as outfile:
    #         outfile.write(f"{i+1}"+fort_file.read() + '\n')
                
    #     # Remove the temporary input file
    #     if os.path.exists(temp_input_file):
    #         os.remove(temp_input_file)
        
    #     print(f"beta eos {i+1} done")

    ########################## SEPARATE FILES - USE MERGE-BETA.PY TO MERGE THEM ############################

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
            #result
            # Write (overwrite!) the contents of fort.7 to the output file
        with open("fort.7", "r") as fort_file, open(output_file, "w") as outfile:
            outfile.write(fort_file.read())
                
        # Remove the temporary input file
        if os.path.exists(temp_input_file):
            os.remove(temp_input_file)


do_eos_delta()
