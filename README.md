<div align="center">

# 🧬 Bioinformatics Using Python

### Digital Image Processing Course Project

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Complete-success.svg)](https://github.com/Hamza-Ahmed-S/DIP-PROJECT)

*A comprehensive bioinformatics toolkit for DNA/protein analysis and biochemical calculations*

</div>

---

## 📋 Table of Contents

- [About](#-about)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Usage](#-usage)
- [Detailed Requirements](#-detailed-requirements)
- [Author](#-author)

---

## 🔬 About

This project implements **4 comprehensive bioinformatics requirements** combining molecular biology, biochemistry, and genomics. It provides tools for analyzing DNA sequences, protein structures, ATP hydrolysis thermodynamics, and genome assembly quality metrics.

**Course:** Digital Image Processing  
**Project Type:** Bioinformatics Analysis Suite  
**Language:** Python 3.x (Pure Python - No External Dependencies)

---

## ✨ Features

🧪 **Biochemical Analysis**
- ATP hydrolysis Gibbs free energy (ΔG) calculations
- Tissue-specific metabolic analysis
- Energy unit conversions (kJ ↔ kcal)

🧬 **DNA Sequence Analysis**
- Open Reading Frame (ORF) detection
- GC content calculation
- Start/Stop codon identification
- DNA to protein translation

🔬 **Protein Analysis**
- Amino acid frequency distribution
- Hydrophobic residue analysis
- Transmembrane domain detection
- Sequence composition statistics

📊 **Genome Assembly Metrics**
- N50/N90 quality statistics
- Contig length analysis
- Assembly quality assessment

---

## 📁 Project Structure

```
DIP-PROJECT/
│
├── 🚀 main.py                    # Interactive menu runner
├── 📚 codon_table.py            # Genetic code & amino acid definitions
│
├── 🧪 requirement1.py           # ATP Hydrolysis Thermodynamics
├── 🧬 requirement2.py           # DNA & Protein Sequence Analysis
├── 🔬 requirement3.py           # Advanced DNA/Protein Analysis
├── 📊 requirement4.py           # N50 Genome Assembly Statistics
│
├── 📖 README.md                 # Project documentation (this file)
└── 🔒 .gitignore               # Git exclusions
```

---

## 🎯 Requirements

| Requirement | Description |
|-------------|-------------|
| **Python Version** | 3.x or higher |
| **External Libraries** | None (uses only standard library) |
| **Operating System** | Windows, macOS, Linux |
| **Storage** | Minimal (~50 KB) |

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/Hamza-Ahmed-S/DIP-PROJECT.git
cd DIP-PROJECT
```

### Verify Python Installation

```bash
python --version
# Should show Python 3.x or higher
```

**That's it!** No additional dependencies needed. ✅

---

## 💻 Usage

### Option 1: Interactive Menu (Recommended)

Run the main script to access an interactive menu:

```bash
python main.py
```

**Menu Options:**
```
1. Requirement 1: ATP Hydrolysis Analysis
2. Requirement 2: DNA and Protein Sequence Analysis
3. Requirement 3: Advanced DNA/Protein Analysis
4. Requirement 4: N50 Calculation
5. Run ALL requirements
0. Exit
```

### Option 2: Run Individual Requirements

Execute specific requirement scripts directly:

```bash
# ATP Hydrolysis Analysis
python requirement1.py

# DNA/Protein Sequence Analysis
python requirement2.py

# Advanced DNA/Protein Analysis
python requirement3.py

# N50 Genome Assembly Statistics
python requirement4.py
```

---

## 📊 Detailed Requirements

### 🧪 Requirement 1: ATP Hydrolysis Thermodynamics

**Objective:** Calculate Gibbs free energy for ATP hydrolysis across different tissues

**What It Does:**
- ✅ Calculates ΔG using thermodynamic equation: `ΔG = ΔG° + RT ln(Q)`
- ✅ Analyzes three tissue types (Liver, Muscle, Brain)
- ✅ Identifies most exothermic reaction
- ✅ Converts energy units (kJ/mol ↔ kcal/mol)

**Key Concepts:**
- Cellular energy metabolism
- Gibbs free energy
- Reaction spontaneity

---

### 🧬 Requirement 2: DNA & Protein Sequence Analysis

**Objective:** Fundamental sequence analysis on biological data

**What It Does:**

| Task | Method | Output |
|------|--------|--------|
| **ORF Finding** | `find()` + slice functions | Open Reading Frame sequence |
| **GC Content** | Nucleotide counting | Percentage of G+C bases |
| **Amino Acid Frequency** | Character counting | Distribution of 20 amino acids |
| **Hydrophobic Analysis** | Pattern matching | % of hydrophobic residues |

**Datasets Used:**
- Topoisomerase gene sequence (DNA)
- Transmembrane protein 222 (protein)

---

### 🔬 Requirement 3: Advanced DNA/Protein Analysis

**Objective:** Complex sequence manipulation and translation

**What It Does:**

1. **Valid ORF Detection**
   - Finds all start codons (ATG)
   - Validates stop codons in reading frame
   - Reports complete ORF coordinates

2. **Stop Codon Distance Analysis**
   - Locates TAA, TAG, TGA codons
   - Calculates distance from start
   - Identifies nearest terminator

3. **Hydrophobic Fragment Extraction**
   - Finds continuous hydrophobic regions
   - Filters by minimum length (≥3 aa)
   - Identifies transmembrane domains

4. **DNA → Protein Translation**
   - Uses genetic code dictionary
   - Translates codons to amino acids
   - Handles start/stop signals

**Technologies:**
- List comprehensions
- Dictionary lookups
- Conditional filtering
- Range-based iteration

---

### 📊 Requirement 4: N50 Genome Assembly Statistics

**Objective:** Calculate assembly quality metrics

**What It Does:**
- ✅ Sorts contigs by length (longest → shortest)
- ✅ Calculates cumulative genome length
- ✅ Identifies N50 threshold (50% of total)
- ✅ Provides additional stats (N90, L-max, L-min, mean, median)

**Why N50 Matters:**
> Higher N50 = Better assembly quality (longer, more contiguous sequences)

---

## 👨‍💻 Author

<div align="center">

### **MADE BY HAMZA AHMED SIDDIQUI**
**Roll Number:** 22FA-043-SE

**Project Group:** Group-12  
**Course:** Digital Image Processing using Python

---

📧 Contact: [GitHub Profile](https://github.com/Hamza-Ahmed-S)

</div>

---

<div align="center">

### 🌟 If you find this project helpful, please give it a star! ⭐

**Made with ❤️ for Bioinformatics Education**

</div>
