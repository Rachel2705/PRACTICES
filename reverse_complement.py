def reverse_complement(dna_sequence):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reverse_seq = dna_sequence[::-1]
    reverse_complement_seq = ''.join(complement[base] for base in reverse_seq)
    return reverse_complement_seq

# Example usage:
sequence = "ATCG"
result = reverse_complement(sequence)
print(result)  # Output: "CGAT"
