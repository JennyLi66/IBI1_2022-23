seq = 'ATGCAATCGACTACGATCTGAGGGCCTAA'
start_index = seq.find('ATG')
coding_seq_count = 0
while start_index < len(seq):
    stop_index = seq.find('TAA', start_index + 3)
    stop_index = min(stop_index, seq.find('TAG', start_index + 3))
    stop_index = min(stop_index, seq.find('TGA', start_index + 3))
    if stop_index != -1:
        coding_seq_count += 1
        start_index = seq.find('ATG', stop_index + 3)

    else:
        break

print('Total count of possible coding sequences:', coding_seq_count)
