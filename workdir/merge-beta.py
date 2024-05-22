num_lines= 3


def merge_beta_delta():
    core_dir = "beta-outputs/"
    #output_dir = "beta-outputs/with-crust"
    output_file = "beta-data.txt"

    with open (output_file, "w"):
            pass
    
    for i in range(0, num_lines):
        input_file = f"{core_dir}beta-eq-eos-new{i+1}.txt"
        
        with open(input_file, "r") as infile, open(output_file, "a") as outfile:
            for line in infile:
                # Escreve o número do arquivo de entrada e a linha no arquivo de saída
                outfile.write(f"{i+1} {line}")
        print(f"beta {i+1} done")

def merge_tov_delta():
    core_dir = "tov-outputs/"
    #output_dir = "beta-outputs/with-crust"
    output_file = "tov-data.txt"

    with open (output_file, "w"):
            pass
    
    for i in range(0, num_lines):
        input_file = f"{core_dir}tov{i+1}.txt"
        
        with open(input_file, "r") as infile, open(output_file, "a") as outfile:
            for line in infile:
                # Escreve o número do arquivo de entrada e a linha no arquivo de saída
                outfile.write(f"{i+1} {line}")
        print(f"tov {i+1} done")

merge_beta_delta()
merge_tov_delta()