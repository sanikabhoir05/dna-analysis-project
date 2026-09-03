from Bio.Seq import Seq
dna = input("Enter DNA sequence: ").upper()
dna_seq = Seq(dna)
rna = dna_seq.transcribe()
protein = dna_seq.translate()
print("\nDNA:", dna)
print("RNA:", rna)
print("Protein:", protein)
