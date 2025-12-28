"""
Requirement 3: Advanced DNA and Protein Analysis

1. Print valid ORF from DNA sequence
2. Find nearest stop codon to start codon using list functions
3. Find and print hydrophobic fragments from transmembrane protein
4. Translate DNA sequence to protein sequence using dictionary
"""

from codon_table import CODON_TABLE, START_CODON, STOP_CODONS, HYDROPHOBIC_AMINO_ACIDS

print("=" * 80)
print("REQUIREMENT 3: ADVANCED DNA AND PROTEIN ANALYSIS")
print("=" * 80)
print()

# Dataset
DNA = "tgagggggggctgttttgcccgcaagagttggagcattttatgcacattggctccatagttgcctccggctctagaccaggaattaggctcctaacgcataccaactccggttaacagggtgtctctgtgtacccccacagaattcgtagccaacgtctgacggactgagtatagcgataacttaccagttactaacccgaggcggcatttcaatggcgtagacacggcgattaacccctgattgctaaaggctcgaattgtagcatcctggcagagcgggggtcattttgcactaatcaatgccagtagacccaactgctcacccccactttccccgtgttggcattataggctcgattcgttgatgcaactggactggtggcccgacagtaacgtacgtacacggctgtacgaccctgaaggctggtacctccgcatatttgaggacactgaccgaaaaacatgtatactagtaacagtttgtaagattaagacgttgtataatctgcagattcgtcacaga"

TRANSMEMBRANE_PROTEIN = "MAEAEGSSLLLLPPPPPPPRMAEVEAPTAAETDMKQYQGSGGVAMDVERSRFPYCVVWTPIPVLTWFFPIIGHMGICTSTGVIRDFAGPYFVSEDNMAFGKPAKYWKLDPAQVYASGPNAWDTAVHDASEEYKHRMHNLCCDNCHSHVALALNLMRYNNSTNWNMVTLCFFCLLYGKYVSVGAFVKTWLPFILLLGIILTVSLVFNLR"

# ============================================================================
# TASK 1: Print Valid ORF from DNA Sequence
# ============================================================================
print("TASK 1: Finding Valid ORF from DNA Sequence")
print("-" * 80)

# Convert to uppercase for consistency
DNA = DNA.upper()

# Find all start codons positions using list comprehension
start_positions = [i for i in range(len(DNA) - 2) if DNA[i:i+3] == START_CODON]

print(f"DNA Sequence Length: {len(DNA)} bp")
print(f"Start codons (ATG) found at positions: {start_positions}")
print()

# Find valid ORFs (start to stop codon in same reading frame)
valid_orfs = []

for start_pos in start_positions:
    # Check from this start position for a stop codon
    for i in range(start_pos, len(DNA) - 2, 3):
        codon = DNA[i:i+3]
        if codon in STOP_CODONS:
            # Found a valid ORF
            orf_seq = DNA[start_pos:i+3]
            valid_orfs.append({
                'start': start_pos,
                'stop': i,
                'stop_codon': codon,
                'length': len(orf_seq),
                'sequence': orf_seq
            })
            break

if valid_orfs:
    print(f"Found {len(valid_orfs)} valid ORF(s):\n")
    for idx, orf in enumerate(valid_orfs, 1):
        print(f"ORF #{idx}:")
        print(f"  Start position: {orf['start']}")
        print(f"  Stop position: {orf['stop']}")
        print(f"  Stop codon: {orf['stop_codon']}")
        print(f"  Length: {orf['length']} bp")
        print(f"  Sequence: {orf['sequence']}")
        print()
else:
    print("No valid ORF found (start codon with stop codon in same frame)")
    print()

# ============================================================================
# TASK 2: Find Nearest Stop Codon to Start Codon
# ============================================================================
print("TASK 2: Finding Nearest Stop Codon to Start Codon")
print("-" * 80)

if start_positions:
    # Use the first start codon
    first_start = start_positions[0]
    print(f"First start codon at position: {first_start}")
    
    # Find positions of all three stop codons after the start
    stop_codon_positions = []
    
    for stop_codon in STOP_CODONS:
        # Search for stop codon after start position
        pos = first_start
        while pos < len(DNA) - 2:
            if DNA[pos:pos+3] == stop_codon:
                # Check if it's in the same reading frame
                if (pos - first_start) % 3 == 0:
                    stop_codon_positions.append({
                        'codon': stop_codon,
                        'position': pos,
                        'distance': pos - first_start
                    })
                    break
            pos += 1
    
    if stop_codon_positions:
        # Use list function to find the nearest (minimum distance)
        nearest_stop = min(stop_codon_positions, key=lambda x: x['distance'])
        
        print(f"\nStop codons found in reading frame:")
        for stop in stop_codon_positions:
            print(f"  {stop['codon']} at position {stop['position']} (distance: {stop['distance']} bp)")
        
        print(f"\nNearest stop codon: {nearest_stop['codon']}")
        print(f"Position: {nearest_stop['position']}")
        print(f"Distance from start: {nearest_stop['distance']} bp")
    else:
        print("No stop codons found in the same reading frame")
else:
    print("No start codon found")

print()

# ============================================================================
# TASK 3: Find and Print Hydrophobic Fragments
# ============================================================================
print("TASK 3: Finding Hydrophobic Fragments from Transmembrane Protein")
print("-" * 80)

print(f"Hydrophobic amino acids: {', '.join(HYDROPHOBIC_AMINO_ACIDS)}\n")

# Use conditional and list functions to find hydrophobic fragments
hydrophobic_fragments = []
current_fragment = []

for amino_acid in TRANSMEMBRANE_PROTEIN:
    if amino_acid in HYDROPHOBIC_AMINO_ACIDS:
        # Add to current fragment
        current_fragment.append(amino_acid)
    else:
        # End of hydrophobic fragment
        if len(current_fragment) >= 3:  # Only keep fragments of length 3 or more
            hydrophobic_fragments.append(''.join(current_fragment))
        current_fragment = []

# Don't forget the last fragment
if len(current_fragment) >= 3:
    hydrophobic_fragments.append(''.join(current_fragment))

print(f"Found {len(hydrophobic_fragments)} hydrophobic fragments (length ≥ 3):\n")
for idx, fragment in enumerate(hydrophobic_fragments, 1):
    print(f"Fragment {idx}: {fragment} (length: {len(fragment)})")

print()

# ============================================================================
# TASK 4: Translate DNA Sequence to Protein Sequence
# ============================================================================
print("TASK 4: Translating DNA to Protein Sequence")
print("-" * 80)

# Use the topoisomerase sequence for translation
TOPOISOMERASE = "CATATGCACTATATCATATCTCAATTACGGAACATATCAGCACACAATTGCCCATTATACGCGCGTATAATGGACTATTGTGTGCTGATAAGGAGAACATAAGCGCAGAACAATATGTATCTATTCCGGTGTTGTGTTCCTTTGTTATTCTGCTATTATGTTCTCTTATAGTGTGACGAAAGCAGCATAATTAATCGTCACTTGTTCTTT"

print(f"DNA Sequence: {TOPOISOMERASE[:60]}...")
print(f"DNA Length: {len(TOPOISOMERASE)} bp\n")

# Find start codon
start_index = TOPOISOMERASE.find(START_CODON)

if start_index != -1:
    # Extract coding sequence from start codon
    coding_sequence = TOPOISOMERASE[start_index:]
    
    # Translate using dictionary and range for codon specification
    protein_sequence = []
    
    # Use range to iterate through codons (every 3 nucleotides)
    for i in range(0, len(coding_sequence) - 2, 3):
        codon = coding_sequence[i:i+3]
        
        # Translate using codon table dictionary
        if codon in CODON_TABLE:
            amino_acid = CODON_TABLE[codon]
            
            # Stop at stop codon (represented as '_')
            if amino_acid == '_':
                print(f"Stop codon '{codon}' encountered at position {i}")
                break
            
            protein_sequence.append(amino_acid)
        else:
            print(f"Warning: Unknown codon '{codon}' at position {i}")
    
    # Join to create protein sequence
    protein = ''.join(protein_sequence)
    
    print(f"\nProtein Sequence ({len(protein)} amino acids):")
    print(protein)
    
    # Display in blocks for readability
    print("\nProtein Sequence (formatted):")
    block_size = 60
    for i in range(0, len(protein), block_size):
        print(f"{i+1:4d}: {protein[i:i+block_size]}")
else:
    print(f"No start codon '{START_CODON}' found in sequence")

print()
print("=" * 80)
print("REQUIREMENT 3 COMPLETED")
print("=" * 80)
