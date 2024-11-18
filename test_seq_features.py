import seq_features
import pytest
def test_number_negatives_for_invalid_amino_acid():
    with pytest.raises(RuntimeError) as excinfo:
        seq_features.number_negatives('Z')
    excinfo.match("Z is not a valid amino acid")

def test_number_negatives_single_E_or_D():
    """Perform unit tests on number_negative for single AA"""
    assert seq_features.number_negatives('E') == 1
    assert seq_features.number_negatives('D') == 1


def test_number_negatives_for_empty():
    """Perform unit tests on number_negative for empty entry"""
    assert seq_features.number_negatives('') == 0


def test_number_negatives_for_short_sequences():
    """Perform unit tests on number_negative for short sequence"""
    assert seq_features.number_negatives('ACKLWTTAE') == 1
    assert seq_features.number_negatives('DDDDEEEE') == 8


def test_number_negatives_for_lowercase():
    """Perform unit tests on number_negative for lowercase"""
    assert seq_features.number_negatives('acklwttae') == 1

def test_number_positives_single_R_K_or_H():
    """Perform unit tests on number_positives for single AA"""
    assert seq_features.number_positives('R') == 1
    assert seq_features.number_positives('K') == 1
    assert seq_features.number_positives('H') == 1

def test_number_positives_for_empty():
    """Perform unit tests on number_positives for empty entry"""
    assert seq_features.number_positives('') == 0


def test_number_positives_for_short_sequences():
    """Perform unit tests on number_positives for short sequence"""
    assert seq_features.number_positives('RCKLWTTRE') == 3
    assert seq_features.number_positives('DDDDEEEE') == 0


def test_number_positives_for_lowercase():
    """Perform unit tests on number_positives for lowercase"""
    assert seq_features.number_positives('rcklwttre') == 3


def test_number_positives_for_invalid_amino_acid():
    with pytest.raises(RuntimeError) as excinfo:
        seq_features.number_positives('Z')
    excinfo.match("Z is not a valid amino acid")