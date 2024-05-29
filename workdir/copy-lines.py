input_file = "../../tov-data.txt"
output_file = "tov-data-ex.txt"


def process_file(input_file, output_file, lines_to_copy=200, interval=6000):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        line_count = 0
        buffer = []
        
        for line in infile:
            buffer.append(line)
            line_count += 1
            
            # A cada 6000 linhas, copiar 200 linhas para o arquivo de saída
            if line_count % interval == 0:
                outfile.writelines(buffer[:lines_to_copy])
                buffer = []
        
        # Caso haja linhas restantes no buffer (menos de 6000 linhas)
        if buffer:
            outfile.writelines(buffer[:lines_to_copy])

# Uso da função
process_file(input_file, output_file)
