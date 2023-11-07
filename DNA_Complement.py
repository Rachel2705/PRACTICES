def complement(dna_sequence):
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement_dict[base] for base in dna_sequence)

# Example usage:
dna_sequence = "ATCG"
complement_seq = complement(dna_sequence)
print(complement_seq)  # Output: "TAGC"
