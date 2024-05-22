
def sort_values():
    input_file = "props.txt"
    output_file = "test.txt"
    
    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            
            if line.strip():
                columns = line.split()
                #print(columns[1])
                del columns[1]
                col9, col10 = float(columns[9]), float(columns[10])
                if col9 > 0 and col10 > 0:
                    for i in range(len(columns)):
                        outfile.write( columns[i] + " ")
                    outfile.write("\n")
                   
sort_values()