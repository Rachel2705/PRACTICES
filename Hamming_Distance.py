def hamming_distance(seq1, seq2):
    if len(seq1) !=len(seq2):
        raise ValueError("sequences must have the same length")
    return sum(c1 != c2 for c1,c2 in zip(seq1,seq2))

# Example usage:
sequence1 = "ATCG"
sequence2 = "ATCA"
distance = hamming_distance(sequence1, sequence2)
print(distance)  #Output: 1
