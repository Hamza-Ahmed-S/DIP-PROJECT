"""
Data loading utilities for the Bioinformatics Web App
"""

import io
from typing import Optional


def parse_fasta(file_content: str) -> dict:
    """Parse FASTA format content"""
    sequences = {}
    current_id = None
    current_seq = []
    
    lines = file_content.strip().split('\n')
    
    for line in lines:
        line = line.strip()
        if line.startswith('>'):
            # Save previous sequence
            if current_id is not None:
                sequences[current_id] = ''.join(current_seq)
            
            # Start new sequence
            current_id = line[1:].strip()
            current_seq = []
        else:
            current_seq.append(line)
    
    # Save last sequence
    if current_id is not None:
        sequences[current_id] = ''.join(current_seq)
    
    return sequences


def validate_dna_sequence(sequence: str) -> tuple[bool, str]:
    """Validate DNA sequence - returns (is_valid, error_message)"""
    if not sequence:
        return False, "Sequence is empty"
    
    valid_bases = set('ATGCN')
    sequence_upper = sequence.upper()
    
    invalid_chars = set(sequence_upper) - valid_bases
    if invalid_chars:
        return False, f"Invalid characters found: {', '.join(invalid_chars)}"
    
    return True, ""


def validate_protein_sequence(sequence: str) -> tuple[bool, str]:
    """Validate protein sequence - returns (is_valid, error_message)"""
    if not sequence:
        return False, "Sequence is empty"
    
    valid_amino_acids = set('ACDEFGHIKLMNPQRSTVWY*')
    sequence_upper = sequence.upper()
    
    invalid_chars = set(sequence_upper) - valid_amino_acids
    if invalid_chars:
        return False, f"Invalid characters found: {', '.join(invalid_chars)}"
    
    return True, ""


def clean_sequence(sequence: str) -> str:
    """Remove whitespace and newlines from sequence"""
    return ''.join(sequence.split()).upper()


def parse_contig_lengths(file_content: str) -> list:
    """Parse contig lengths from file content"""
    lengths = []
    
    lines = file_content.strip().split('\n')
    for line in lines:
        line = line.strip()
        if line and not line.startswith('#'):
            try:
                length = int(line)
                if length > 0:
                    lengths.append(length)
            except ValueError:
                continue
    
    return lengths


# Sample DNA sequences
SAMPLE_DNA_TOPOISOMERASE = """ATGGCGATGAAACAAAAAGTATTTTTGATCATCCGCCTGACCCCGATCGAGCCGATGAAAATGTCGATCGTGGTCGTGTCGGGTCGGATCGTATTCCGGCCGGCGTTCAATTACAGGCAGAAGACACGGCAAAAGCTGAAATGTTTGATAGCCGCGCTGGCGTTGAACAGGACACCGCTCGCCGCGATGAAACCCGTCGCGCCGCTGATGAACTTTGTCATCGCGATGCGCGTGGTGGCGGTGAGCCGGAACAAAAAGGGGATAGTAACCCGTGGGAATGTTCCCATCTTTGATGGTATTGA"""

SAMPLE_DNA_SHORT = """ATGTCGATTAAGGCTAGATGACTAGCTGA"""

# Sample protein sequences
SAMPLE_PROTEIN_TMEM222 = """MKVLWAALLVTFLAGCQAKVVLTQESSGGLVQPGGSLRLSCAASEFTFSGYAMHWVRQAPGKGLEWVAVISYNGDTKYLDSVKGRFTISRDNSKNMLYLQMNSLRAEDTAVYYCAKVLWAALLVTFLAGCQ"""

SAMPLE_PROTEIN_SHORT = """MVILAILMFWYVAAILMFWYVAIL"""


def get_sample_dna(sample_type: str = "topoisomerase") -> str:
    """Get sample DNA sequence"""
    if sample_type == "topoisomerase":
        return SAMPLE_DNA_TOPOISOMERASE
    elif sample_type == "short":
        return SAMPLE_DNA_SHORT
    else:
        return SAMPLE_DNA_TOPOISOMERASE


def get_sample_protein(sample_type: str = "tmem222") -> str:
    """Get sample protein sequence"""
    if sample_type == "tmem222":
        return SAMPLE_PROTEIN_TMEM222
    elif sample_type == "short":
        return SAMPLE_PROTEIN_SHORT
    else:
        return SAMPLE_PROTEIN_TMEM222


def get_sample_contigs() -> list:
    """Get sample contig lengths for N50 calculation"""
    return [2000, 2000, 1800, 1800, 1500, 1500, 1200, 1000, 1000, 900, 900, 900, 800, 800, 700, 600, 500, 500, 400, 300]
