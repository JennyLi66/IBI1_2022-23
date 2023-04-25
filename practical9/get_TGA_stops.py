Python 3.11.2 (v3.11.2:878ead1ac1, Feb  7 2023, 10:02:41) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
with open('/Users/jenny/Desktop/IBI 1/week9/1.fa','r')as input_file, open('/Users/jenny/Desktop/IBI 1/week9/TGA_genes.fa', 'w') as output_file:
    current_gene = ''
    current_sequence = ''
    for line in input_file:
        if line.startswith('>'):
            if current_sequence.endswith('TGA'):
                output_file.write(current_gene + '\n')
                output_file.write(current_sequence + '\n')
            current_gene = line.strip()
            current_sequence = ''
        else:
            current_sequence += line.strip()
    if current_sequence.endswith('TGA'):
        output_file.write(current_gene +'\n')
        output_file.write(current_sequence + '\n')
