seq = 'ATGCAATCGACTACGATCTGAGGGCCTAA'
start_codon = 'ATG'
stop_codons = ['TAA', 'TAG', 'TGA']
for i in range(len(seq)):
    if seq[i:i+3] == start_codon:
        for j in range(i+3,len(seq), 3):
            if seq[j:j+3] in stop_codons:
                if (j-i) % 3 == 0:
                    coding_seq_count += 1
                break

            
print('total count of possible coding sequences:' , coding_seq_count)
