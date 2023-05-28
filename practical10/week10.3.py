def protein_coding(sequence):
    sequence = sequence.upper()
    atg = sequence.find('ATG')
    tga = sequence.find('TGA')
    if  atg == -1 or tga == -1:
        return'unclear', 0
    coding = sequence[atg:tga+3]
    coding_percentage = len(coding) / len(sequence)*100
    if coding_percentage > 50:
        return 'protein-coding', coding_percentage
    elif coding_percentage < 10:
        return ' non-coding', coding_percentage
    else:
        return ' unclear', coding_percentage

    
sequence = 'ATGCGGAGGAGTGA'
result, percentage = protein_coding(sequence)
print(f"Result: {result}\nCoding DNA percentage: {percentage}")
Result: protein-coding
Coding DNA percentage: 100.0
