import bootcamp_utils

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
    # Convert sequence to upper case
    seq = seq.upper()

    # Check for a valid sequence
    for aa in seq:
        if aa not in bootcamp_utils.aa.keys():
            raise RuntimeError(aa + ' is not a valid amino acid.')

    return seq.count('R') + seq.count('K') + seq.count('H')