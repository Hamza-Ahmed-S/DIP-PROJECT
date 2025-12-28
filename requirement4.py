"""
Requirement 4: N50 Calculation

N50 is a statistic used in genomics to assess assembly quality.
It is defined as the sequence length of the shortest contig at 50% 
of the total genome length when contigs are ordered from longest to shortest.
"""

print("=" * 80)
print("REQUIREMENT 4: N50 CALCULATION")
print("=" * 80)
print()

# Dataset: Multiple sequences (contigs) for N50 calculation
# For this example, we'll split the provided sequences into fragments
# In a real scenario, you would have multiple assembled contigs

sequences = [
    "ATGACCGCCCTCCCCCGCTACGCCGTTTTCGGCAACCCCGTCGCCCACAGCAAATCGCCGCAAATTCATC",
    "AACAATTTGCCCTTCAGGAAGGCGTTGACATTGAATACGAACGCATTTGCGCCGACATCGGCGGTTTCGC",
    "GCAGGCGGTTTCGACATTTTTTGAAACAGGCGGTTGCGGGGCAAACGTTACCGTACCGTTCAAACAGGAA",
    "GCGTTTCATCTGGCGGACGAGCATTCCGAACGCGCATTGGCGGCAGGTGCGGTCAATACGCTGATTCCGT",
    "TGAAAAACGGCAAGCTGCGTGGCGACAACACCGACGGTATCGGTTTGACCAACGACATCACGCAGGTCAA",
    "AAATATTGCCATCGAGGGCAAAACCATTTTGCTTTTGGGCGCAGGCGGCGCGGTGCGCGGCGTGATTCCT",
    "GTTTTGAAAGAACACCGTCCTGCCCGTATCGTCATTGCCAACCGTACCCGCGCCAAAGCCGAGGAATTGG",
    "CGCAGCTTTTCGGCATTGAAGCCGTCCCGATGGCGGACGTGAACGGCGGTTTTGATATCATCATCAACGG",
    "CACGTCGGGCGGTCTAAACGGTCAGATTCCCGATATTCCGCCCGATATTTTTCAAAACTGCGCGCTTGCC",
    "TACGATATGGTGTACGGCTGCGCGGCAAAACCGTTTTTAGATTTTGCACGACAATCGGGTGCGAAAAAAA",
    "CTGCCGACGGACTGGGTATGCTAGTCGGTCAAGCGGCGGCTTCCTACGCCCTCTGGCGCGGATTTACGCC",
    "CGATATCCGCCCCGTTATCGAATACATGAAAGCCCTATAA"
]

print("N50 Statistic Calculation for Genome Assembly")
print("-" * 80)
print()

# Calculate length of each sequence
sequence_lengths = [len(seq) for seq in sequences]

print(f"Number of sequences (contigs): {len(sequences)}")
print(f"\nSequence lengths:")
for i, length in enumerate(sequence_lengths, 1):
    print(f"  Sequence {i}: {length} bp")

# Calculate total length
total_length = sum(sequence_lengths)
print(f"\nTotal genome length: {total_length} bp")

# Sort sequences by length in descending order
sorted_lengths = sorted(sequence_lengths, reverse=True)

print(f"\nSorted lengths (longest to shortest):")
print(f"  {sorted_lengths}")

# Calculate N50
# N50 is the length where the cumulative sum reaches 50% of total length
half_length = total_length / 2
cumulative_length = 0
n50 = 0

print(f"\nCalculating N50 (50% threshold = {half_length} bp):")
print()

for i, length in enumerate(sorted_lengths, 1):
    cumulative_length += length
    percentage = (cumulative_length / total_length) * 100
    print(f"  Position {i}: Length = {length} bp, Cumulative = {cumulative_length} bp ({percentage:.1f}%)")
    
    if cumulative_length >= half_length and n50 == 0:
        n50 = length
        n50_position = i
        print(f"  >>> N50 reached! <<<")

print()
print("-" * 80)
print(f"\nN50 Result:")
print(f"  N50 = {n50} bp")
print(f"  Position in sorted list: {n50_position}")
print(f"\nInterpretation:")
print(f"  At least 50% of the assembled genome consists of sequences")
print(f"  that are {n50} bp or longer.")
print()

# Additional statistics
print("-" * 80)
print("\nAdditional Assembly Statistics:")
print(f"  Longest sequence (L-max): {sorted_lengths[0]} bp")
print(f"  Shortest sequence (L-min): {sorted_lengths[-1]} bp")
print(f"  Mean sequence length: {total_length / len(sequences):.1f} bp")
print(f"  Median sequence length: {sorted_lengths[len(sorted_lengths)//2]} bp")

# Calculate N90 as well (90% threshold)
ninety_percent = total_length * 0.9
cumulative = 0
n90 = 0
for length in sorted_lengths:
    cumulative += length
    if cumulative >= ninety_percent:
        n90 = length
        break

print(f"  N90 (90% threshold): {n90} bp")
print()

print("=" * 80)
print("REQUIREMENT 4 COMPLETED")
print("=" * 80)
