def sort_eos18():
    input_file = r"C:\Users\lavin\OneDrive\Desktop\Lavinia\UT3\M1\Stage\delta-meson\original_data\delta.dat"
    output_file = r"C:\Users\lavin\OneDrive\Desktop\Lavinia\UT3\M1\Stage\delta-meson\original_data\delta_sorted.dat"
    
    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            columns = line.split()
            if len(columns) < 4:
                continue
            col2, col3, col4 = float(columns[1]), float(columns[2]), float(columns[3])
            if 9.33 <= col2 <= 10.63 and 0.27 <= col3 <= 1.96 and 2.35 <= col4 <= 3.38:
                outfile.write(line)

sort_eos18()
