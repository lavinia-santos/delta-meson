import os, subprocess

def do_properties_delta():
    input_file = "delta.dat"
    output_dir = "properties-outputs"
    temp_input_file = "delta.inp"
    
    num_lines = 7734

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
        
        #print(i)
        #with open(temp_input_file, "r") as tempfile:
        #its not necessary to remove the old files because it overwrites them (w)
        
        # Execute the external command
        result = subprocess.run("./properties", shell=True)
            #result
            # Write (overwrite!) the contents of fort.7 to the output file
        with open("fort.60", "r") as fort_file, open(output_file, "a") as outfile:
            outfile.write(f"{i+1}"+fort_file.read() + '\n')
                
        # Remove the temporary input file
        if os.path.exists(temp_input_file):
            os.remove(temp_input_file)
        
        print(f"properties {i+1} done")

do_properties_delta()
