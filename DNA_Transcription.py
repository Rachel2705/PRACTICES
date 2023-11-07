def transcribe(dna_sequence):
    return dna_sequence.replace('T', 'U')

# Example usage:
dna_sequence = "ATCG"
rna_sequence = transcribe(dna_sequence)
print(rna_sequence)  #output: "AUCG"

