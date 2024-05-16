


def add_crust():
    num_lines= 5
    core_dir = "beta-outputs/"
    output_dir = "beta-outputs/with-crust"

    for i in range(1, num_lines + 1):
        core_file_path = f"{core_dir}beta-eq-eos{i}.txt"
        output_file = f"{output_dir}/beta-crust{i}.txt"
    
        with open(output_file, "w"):
            pass
        with open("bps_nl3wr_crust.dat", "r") as crust, open(output_file, "a") as outfile:
            outfile.write(crust.read())
   
        with open(core_file_path, "r") as core_file, open(output_file, "a") as outfile:
            outfile.write(core_file.read())

add_crust()

    