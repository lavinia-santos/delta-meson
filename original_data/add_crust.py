


def add_crust():
    num_lines= 2
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

    
        # with open(output_file, "w"):
        #     pass
        with open("bps_nl3wr_crust.dat", "r") as crust, open(output_file, "w") as outfile:
            outfile.write(crust.read())
   
        with open(core_new_file_path, "r") as core_file, open(output_file, "a") as outfile:
            outfile.write(core_file.read())

add_crust()

    