def number_negatives(seq):
    """Number of negative residues a protein sequence"""
    # Convert sequence to upper case
    seq = seq.upper()

    # Count E's and D's, since these are the negative residues
    return seq.count('E') + seq.count('D')