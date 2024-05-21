import subprocess
def do_tov_delta():
    input_dir = "beta-outputs/with-crust"
    output_dir = "tov-outputs"
    temp_input_file = "tov.dat"
    num_lines = 7734

    for i in range(6400, 7734):
        input_file = f"{input_dir}/beta-crust{i+1}.txt"
        output_file = f"{output_dir}/tov{i+1}.txt"
    
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
        
        print(f"tov {i+1} done")
        
        # with open(temp_input_file, "w") as tempfile:
        #     pass

do_tov_delta()