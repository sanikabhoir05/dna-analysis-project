from src.gc_content import calculate_gc_content
from src.necleotide_frequemcy import count_nucleotides

with open("data/sample_dna.txt", "r") as file:
    sequence = file.read()

sequence = sequence.upper().replace("\n", "")

print("Nucleotide Frequency:")
print(count_nucleotides(sequence))

print("\nGC Content:")
print(calculate_gc_content(sequence))