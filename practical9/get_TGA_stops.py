Python 3.11.2 (v3.11.2:878ead1ac1, Feb  7 2023, 10:02:41) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
with open('/Users/jenny/Desktop/IBI 1/week9/1.fa') as f:
    nmae, seq = ", "
    for line in f:
        if line.startswith('>'):
            if seq.endswith('TGA'):
                with open('/Users/jenny/Desktop/IBI 1/week9/TGA_genes.fa', 'a') as output:
                    output.write(f'{name}\n{seq}\n')
                name, seq = line.strip(), ''
            else:
                seq += line.strip()
        if seq.endswith('TGA'):
            with open('/Users/jenny/Desktop/IBI 1/week9/TGA_genes.fa', 'a') as output:
                output.write(f'{name}\n{seq}\n')
