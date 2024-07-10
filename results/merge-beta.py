

for num in [21]:
    with open(f"EOS{num}/delta.dat", "r") as infile:
        num_lines = len(infile.readlines())
    #num_lines=5104
     
    def merge_proton_delta():
        core_dir = f"EOS{num}/beta-outputs"
        #output_dir = "beta-outputs/with-crust"
        output_file = f"../../big-results/proton-fraction{num}.dat"
        #output_file = f"proton-fraction{num}.dat"

        with open (output_file, "w"):
                pass
        
        for i in range(0, num_lines):
            input_file = f"{core_dir}/beta-eq-fort2-{i+1}.dat"
            
            with open(input_file, "r") as infile, open(output_file, "a") as outfile:
                for line in infile:
                    # Escreve o número do arquivo de entrada e a linha no arquivo de saída
                    outfile.write(f"{i+1} {line}")
            print(f"proton fraction {i+1} EOS {num} done")
    
    def merge_beta_delta():
        core_dir = f"EOS{num}/beta-outputs/with-crust"
        #output_dir = "beta-outputs/with-crust"
        output_file = f"../../big-results/beta-data{num}.dat"

        with open (output_file, "w"):
                pass
        
        for i in range(0, num_lines):
            input_file = f"{core_dir}/beta-crust{i+1}.txt"
            
            with open(input_file, "r") as infile, open(output_file, "a") as outfile:
                for line in infile:
                    # Escreve o número do arquivo de entrada e a linha no arquivo de saída
                    outfile.write(f"{i+1} {line}")
            print(f"beta {i+1} EOS {num} done")
    ###### fix before running ########
    def merge_tov_delta():
        core_dir = f"EOS{num}/tov-outputs/"
        #output_dir = "beta-outputs/with-crust"
        output_file = f"../../big-results/tov-data{num}.dat"

        with open (output_file, "w"):
                pass
        
        for i in range(0, num_lines):
            input_file = f"{core_dir}tov{i+1}.txt"
            
            with open(input_file, "r") as infile, open(output_file, "a") as outfile:
                for line in infile:
                    # Escreve o número do arquivo de entrada e a linha no arquivo de saída
                    outfile.write(f"{i+1} {line}")
            print(f"tov {i+1} EOS {num} done")

    merge_proton_delta()
    # merge_beta_delta()
    # merge_tov_delta()