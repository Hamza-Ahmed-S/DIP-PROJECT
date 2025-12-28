# Bioinformatics Using Python - Project

This project implements 4 bioinformatics requirements for digital image processing course.

## Project Structure

```
DIP PROJECT/
├── main.py                    # Main runner script with menu
├── codon_table.py            # Codon table and amino acid definitions
├── requirement1.py           # ATP Hydrolysis Analysis
├── requirement2.py           # DNA and Protein Sequence Analysis
├── requirement3.py           # Advanced DNA/Protein Analysis
├── requirement4.py           # N50 Calculation
├── requirements.txt          # Extracted project requirements
├── datasets.txt              # Extracted datasets
└── README.md                 # This file
```

## Requirements Overview

### Requirement 1: ATP Hydrolysis Thermodynamics
- Calculate ΔG (Gibbs free energy) for ATP hydrolysis in three tissues
- Identify the most exothermic reaction
- Convert energy values from kJ to kcal

### Requirement 2: DNA and Protein Sequence Analysis
- Find and print ORF (Open Reading Frame) from topoisomerase gene
- Calculate GC content in DNA sequences
- Calculate amino acid frequency in transmembrane protein 222
- Calculate percentage of hydrophobic amino acids

### Requirement 3: Advanced DNA/Protein Analysis
- Print valid ORF from DNA sequence
- Find nearest stop codon to start codon
- Extract hydrophobic fragments from transmembrane protein
- Translate DNA sequences to protein sequences

### Requirement 4: Genome Assembly Quality
- Calculate N50 statistic for genome assembly quality assessment

## How to Run

### Option 1: Run the main menu (Recommended)
```bash
python main.py
```

This will display a menu where you can:
- Run individual requirements (1-4)
- Run all requirements at once (option 5)

### Option 2: Run individual requirements
```bash
python requirement1.py
python requirement2.py
python requirement3.py
python requirement4.py
```

## Requirements

- Python 3.x
- No external libraries needed (uses only standard library)

## Datasets

All datasets are extracted from the provided Word documents:
- Topoisomerase gene sequences
- Transmembrane protein sequences
- Various DNA sequences for analysis

## Author

Project Group-12
Digital Image Processing Course
