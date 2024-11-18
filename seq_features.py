def number_negatives(seq):
    """Number of negative residues a protein sequence"""
    # Convert sequence to upper case
    seq = seq.upper()

    if seq == 'Z':
        raise RuntimeError('Z is not a valid amino acid.')

    # Count E's and D's, since these are the negative residues
    return seq.count('E') + seq.count('D')

def number_positives(seq):
    """Number of positive residues a protein sequence"""
    # Count R's, K's and H's, since these are the positive residues
    return seq.count('R') + seq.count('K') + seq.count('H')