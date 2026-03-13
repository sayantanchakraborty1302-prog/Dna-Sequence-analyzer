from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction

def is_valid_dna(sequence):
    valid = set("ATGC")
    return all(base in valid for base in sequence)

def analyze_sequence(sequence):

    seq = Seq(sequence)

    print("\nOriginal Sequence:")
    print(seq)

    gc = gc_fraction(seq) * 100
    print("\nGC Content:")
    print(f"{gc:.2f}%")

    print("\nComplement:")
    print(seq.complement())

    print("\nReverse Complement:")
    print(seq.reverse_complement())

    rna = seq.transcribe()
    print("\nRNA Transcription:")
    print(rna)

    protein = rna.translate()
    print("\nProtein Translation:")
    print(protein)


if __name__ == "__main__":

    sequence = input("Enter DNA sequence: ").upper()

    if is_valid_dna(sequence):
        analyze_sequence(sequence)
    else:
        print("Invalid DNA sequence! Only A, T, G, C allowed.")