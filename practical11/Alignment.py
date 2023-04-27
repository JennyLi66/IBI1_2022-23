Python 3.11.2 (v3.11.2:878ead1ac1, Feb  7 2023, 10:02:41) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
blosum62 = {}
with open("/Users/jenny/Desktop/IBI 1/week 11/BLOSUM.xlsx", "rb") as f:
    amino_acids = f.readline().decode('latin-1').split()
    for line in f:
        values = line.decode('latin-1').split()
        key = values.pop(0)
        blosum62[key] = {amino_acids[i]: int(values[i]) for i in range(len(values))}
with open("/Users/jenny/Desktop/IBI 1/week 11/sequences.txt", "r") as f:
    seq1_name = f.readline().strip()
    seq1 = f.readline().strip()
    seq2_name = f.readline().strip()
    seq2 = f.readline().strip()
score = 0
identical = 0
alignment = ""
for i in range(len(seq1)):
    aa1 = seq1[i]
    aa2 = seq2[i]

    if aa1 == aa2:
        identical += 1
        alignment += "|"
    else:
        alignment += " "

    score += blosum62[aa1][aa2]
identity_percent = identical / len(seq1) * 100
print(seq1_name)
print(seq1)
print(seq2_name)
print(seq2)
print("Alignment: ", alignment)
print("Score: ", score)
print("Identity percent: ", "{:.2f}%".format(identity_percent))blosum62 = {}
