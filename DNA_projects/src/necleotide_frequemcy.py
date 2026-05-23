def count_nucleotides(sequence):
    freq = {
        "A": 0,
        "T": 0,
        "G": 0,
        "C": 0
    }

    for base in sequence:
        if base in freq:
            freq[base] += 1

    return freq