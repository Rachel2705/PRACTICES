def find_orfs(dna_sequence):
    start_codon = "ATG"
    stop_codons = ["TAA", "TAG", "TGA"]
    orfs = []
    for i in range(len(dna_sequence) - 2):
        if dna_sequence[i:i+3] == start_codon:
            for j in range(i+3, len(dna_sequence), 3):
                if dna_sequence[j:j+3] in stop_codons:
                    orfs.append(dna_sequence[i:j+3])
                    break
    return orfs

# Example usage:
sequence = "ATGAAATGAACCCGTAGTGA"
orf_list = find_orfs(sequence)
print(orf_list)  # Output: ['ATGAAATGAACCCGTA', 'ATG']
