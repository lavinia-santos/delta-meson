import subprocess
def do_tov_delta():
    input_dir = "beta-outputs/with-crust"
    output_dir = "tov-outputs"
    temp_input_file = "tov.dat"
    num_lines = 5

    for i in range(1, num_lines + 1):
        input_file = f"{input_dir}/beta-crust{i}.txt"
        output_file = f"{output_dir}/tov{i}.txt"
    
        with open(output_file, "w"), open(temp_input_file, "w"):
            pass
        with open(input_file, "r") as infile, open(temp_input_file, "a") as tempfile:   
            tempfile.write(infile.read())
        
        print(tempfile)
        
        with open(temp_input_file, "a") as tempfile:
            tempfile.write("-1. -1. -1.")

        result = subprocess.run("./tov", shell=True)
        result
        #result = subprocess.run("./beta-eq", shell=True)

        with open("tov.out", "r") as tov_file, open(output_file, "w") as outfile:
            outfile.write(tov_file.read())
        
        with open(temp_input_file, "r") as tempfile:
            pass

do_tov_delta()