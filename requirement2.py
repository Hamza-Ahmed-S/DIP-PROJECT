"""
Requirement 2: DNA and Protein Sequence Analysis

1. Find and print ORF (Open Reading Frame) from topoisomerase gene
2. Calculate total GC count in topoisomerase gene
3. Calculate amino acid frequency in transmembrane protein 222
4. Calculate percentage of hydrophobic amino acids
"""

from codon_table import CODON_TABLE, START_CODON, STOP_CODONS, HYDROPHOBIC_AMINO_ACIDS, ALL_AMINO_ACIDS

print("=" * 80)
print("REQUIREMENT 2: DNA AND PROTEIN SEQUENCE ANALYSIS")
print("=" * 80)
print()

# Dataset
TOPOISOMERASE = "CATATGCACTATATCATATCTCAATTACGGAACATATCAGCACACAATTGCCCATTATACGCGCGTATAATGGACTATTGTGTGCTGATAAGGAGAACATAAGCGCAGAACAATATGTATCTATTCCGGTGTTGTGTTCCTTTGTTATTCTGCTATTATGTTCTCTTATAGTGTGACGAAAGCAGCATAATTAATCGTCACTTGTTCTTT"

TRANSMEMBRANE_PROTEIN_222 = "MAEAEGSSLLLLPPPPPPPRMAEVEAPTAAETDMKQYQGSGGVAMDVERSRFPYCVVWTPIPVLTWFFPIIGHMGICTSTGVIRDFAGPYFVSEDNMAFGKPAKYWKLDPAQVYASGPNAWDTAVHDASEEYKHRMHNLCCDNCHSHVALALNLMRYNNSTNWNMVTLCFFCLLYGKYVSVGAFVKTWLPFILLLGIILTVSLVFNLR"

# ============================================================================
# TASK 1: Find and Print ORF from Topoisomerase Gene
# ============================================================================
print("TASK 1: Finding ORF (Open Reading Frame) from Topoisomerase Gene")
print("-" * 80)

# Find start codon (ATG) using find() method
start_pos = TOPOISOMERASE.find(START_CODON)

if start_pos != -1:
    print(f"Start codon '{START_CODON}' found at position: {start_pos}")
    
    # Extract sequence from start codon using slice function
    sequence_from_start = TOPOISOMERASE[start_pos:]
    
    # Find stop codon
    stop_pos = -1
    for i in range(0, len(sequence_from_start) - 2, 3):
        codon = sequence_from_start[i:i+3]
        if codon in STOP_CODONS:
            stop_pos = i
            stop_codon_found = codon
            break
    
    if stop_pos != -1:
        # Extract ORF (from start to stop codon, inclusive)
        orf = sequence_from_start[:stop_pos + 3]
        print(f"Stop codon '{stop_codon_found}' found at position: {stop_pos} (relative to start)")
        print(f"\nORF Length: {len(orf)} nucleotides")
        print(f"\nORF Sequence:")
        print(orf)
    else:
        print("No stop codon found in frame")
        orf = sequence_from_start
        print(f"\nPartial ORF (no stop codon):")
        print(orf)
else:
    print(f"No start codon '{START_CODON}' found")

print()

# ============================================================================
# TASK 2: Calculate Total GC Count in Topoisomerase Gene
# ============================================================================
print("TASK 2: Calculating GC Content in Topoisomerase Gene")
print("-" * 80)

# Count G and C nucleotides
g_count = TOPOISOMERASE.count('G')
c_count = TOPOISOMERASE.count('C')
total_gc = g_count + c_count
total_length = len(TOPOISOMERASE)
gc_percentage = (total_gc / total_length) * 100

print(f"Total Sequence Length: {total_length} bp")
print(f"G count: {g_count}")
print(f"C count: {c_count}")
print(f"Total GC count: {total_gc}")
print(f"GC percentage: {gc_percentage:.2f}%")
print()

# ============================================================================
# TASK 3 & 4: Amino Acid Frequency and Hydrophobic Percentage
# ============================================================================
print("TASK 3 & 4: Amino Acid Frequency in Transmembrane Protein 222")
print("-" * 80)

# Calculate frequency of each amino acid
amino_acid_counts = {}
total_amino_acids = len(TRANSMEMBRANE_PROTEIN_222)

for aa in ALL_AMINO_ACIDS:
    count = TRANSMEMBRANE_PROTEIN_222.count(aa)
    if count > 0:
        amino_acid_counts[aa] = count

# Display amino acid frequencies
print(f"\nTotal amino acids in protein: {total_amino_acids}\n")
print("Amino Acid Frequencies:")
print(f"{'Amino Acid':<15} {'Count':<10} {'Frequency (%)':<15}")
print("-" * 40)

for aa in sorted(amino_acid_counts.keys()):
    count = amino_acid_counts[aa]
    frequency = (count / total_amino_acids) * 100
    print(f"{aa:<15} {count:<10} {frequency:<15.2f}")

# Calculate percentage of hydrophobic amino acids
hydrophobic_count = sum(TRANSMEMBRANE_PROTEIN_222.count(aa) for aa in HYDROPHOBIC_AMINO_ACIDS)
hydrophobic_percentage = (hydrophobic_count / total_amino_acids) * 100

print()
print("-" * 80)
print(f"\nHydrophobic Amino Acids: {', '.join(HYDROPHOBIC_AMINO_ACIDS)}")
print(f"Total Hydrophobic Amino Acids: {hydrophobic_count}")
print(f"Percentage of Hydrophobic Amino Acids: {hydrophobic_percentage:.2f}%")
print()

print("=" * 80)
print("REQUIREMENT 2 COMPLETED")
print("=" * 80)
