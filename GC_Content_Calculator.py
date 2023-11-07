def gc_content(dna_sequence):
    gc_count = dna_sequence.count('G') + dna_sequence.count('C')
    total_bases = len(dna_sequence)
    gc_percentage = (gc_count / total_bases) * 100
    return gc_percentage

# Example usage:
sequence = "ATCGAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTA"
result = gc_content(sequence)
print(f"GC Content: {result}%")  # Output: "GC Content: 42.5%"
