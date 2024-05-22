import subprocess, os
def do_tov_delta():
    input_dir = "beta-outputs/with-crust"
    output_dir = "tov-outputs"
    temp_input_file = "tov.dat"
    num_lines = 7734


    #output_file = f"{output_dir}/tov-data.txt" ### uncomment for merged file


    for i in range(0, num_lines):
        input_file = f"{input_dir}/beta-crust{i+1}.txt"
        
    
        with open(output_file, "w"), open(temp_input_file, "w"):
            pass

        with open(input_file, "r") as infile, open(temp_input_file, "a") as tempfile:   
            tempfile.write(infile.read())
        
        #print(tempfile)
        output_file = f"{output_dir}/tov{i+1}.txt"

        with open(temp_input_file, "a") as tempfile:
            tempfile.write("-1. -1. -1.")

        result = subprocess.run("./tov", shell=True)
        result
        #result = subprocess.run("./beta-eq", shell=True)

        with open("tov.out", "r") as tov_file, open(output_file, "w") as outfile:
            outfile.write(tov_file.read())

            #outfile.write(f"{i+1}"+tov_file.read() + '\n') ### uncomment for merged file
        
        if os.path.exists(temp_input_file):
            os.remove(temp_input_file)

        print(f"tov {i+1} done")
        
        # with open(temp_input_file, "w") as tempfile:
        #     pass

do_tov_delta()