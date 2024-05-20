def sort_eos18():
    # input_file = r"C:\Users\lavin\OneDrive\Desktop\Lavinia\UT3\M1\Stage\delta-meson\original_data\delta.dat"
    # output_file = r"C:\Users\lavin\OneDrive\Desktop\Lavinia\UT3\M1\Stage\delta-meson\original_data\delta_sorted.dat"
#no need to filter
    input_file = "delta.dat"
    output_file = "delta_sorted.dat"
    
    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            columns = line.split()
            if len(columns) < 4:
                continue
            col2, col3, col4 = float(columns[1]), float(columns[2]), float(columns[3])
            if 11.2 <= col2 <= 11.54 and 0.55 <= col3 <= 4.02 and 3.49 <= col4 <= 9.42:
                outfile.write(line)

sort_eos18()
