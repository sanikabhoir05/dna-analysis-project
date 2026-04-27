def calculate_gc_content(sequence):
    gc_count = 0
    for base in sequence:
        if base == "G" or base == "C":
            gc_count += 1

    if len(sequence) == 0:
        return 0

    return (gc_count / len(sequence)) * 100