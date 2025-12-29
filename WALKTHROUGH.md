# 🧬 Bioinformatics Toolkit - Project Walkthrough

![DNA Logo](https://img.shields.io/badge/Bioinformatics-Toolkit-purple?style=for-the-badge&logo=dna)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-red?style=for-the-badge&logo=streamlit)

---

## 📋 Project Overview

An **interactive web application** for bioinformatics analysis built with Python and Streamlit. This project transforms traditional command-line bioinformatics tools into a modern, user-friendly web interface with real-time visualizations and community analytics.

**Course:** Digital Image Processing using Python  
**Author:** Hamza Ahmed Siddiqui (22FA-043-SE)  
**Live Demo:** [Your Streamlit Cloud URL]  
**Repository:** https://github.com/Hamza-Ahmed-S/DIP-PROJECT

---

## ✨ Features

### 🧪 ATP Hydrolysis Analysis
- Calculate Gibbs free energy (ΔG) for ATP hydrolysis
- Compare energy profiles across tissues (Liver, Muscle, Brain)
- Interactive sliders for metabolite concentrations
- Real-time thermodynamic calculations

### 🧬 DNA & Protein Sequence Analysis
- **DNA Analysis:**
  - GC content calculation
  - Open Reading Frame (ORF) detection
  - Nucleotide distribution visualization
  - Sequence validation
  
- **Protein Analysis:**
  - Amino acid frequency distribution
  - Hydrophobic residue analysis
  - Transmembrane protein prediction
  - Sequence coloring and visualization

### 🔬 Advanced Analysis Tools
- **Valid ORF Detection:** Find all reading frames with start/stop codons
- **Stop Codon Distance:** Calculate distances from start to stop codons
- **Hydrophobic Fragments:** Extract continuous hydrophobic regions
- **DNA→Protein Translation:** Translate sequences using genetic code

### 📊 N50 Genome Assembly Calculator
- Calculate N50/N90 assembly quality metrics
- Cumulative length distribution visualization
- Contig size analysis
- Assembly quality assessment

### 📈 Analytics Dashboard
- Real-time community statistics
- Feature usage tracking
- User ratings and feedback
- Popular feature insights

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

```bash
# Clone the repository
git clone https://github.com/Hamza-Ahmed-S/DIP-PROJECT.git
cd DIP-PROJECT

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`

---

## 📁 Project Structure

```
DIP-PROJECT/
├── app.py                          # Main application homepage
├── analytics.py                    # Analytics tracking system
├── codon_table.py                  # Genetic code definitions
├── pages/                          # Multi-page app structure
│   ├── 1_🧪_ATP_Hydrolysis.py    # ATP energy calculations
│   ├── 2_🧬_DNA_Analysis.py       # DNA/Protein sequence tools
│   ├── 3_🔬_Advanced_Analysis.py  # Advanced bioinformatics tools
│   ├── 4_📊_N50_Calculator.py     # Genome assembly metrics
│   └── 5_📈_Analytics_Dashboard.py # Community statistics
├── utils/
│   ├── visualizations.py          # Plotly chart generators
│   └── data_loader.py              # FASTA parsers & sample data
├── .streamlit/
│   └── config.toml                 # App theme configuration
├── requirements.txt                # Production dependencies
├── .gitignore                      # Git ignore rules
└── README.md                       # Project documentation
```

---

## 🎨 Design Features

### Modern UI/UX
- **Animated gradient background** with smooth color transitions
- **Glassmorphism effects** for modern, frosted glass appearance
- **3D card animations** with hover effects
- **Floating particle animations** for visual interest
- **Responsive design** that works on all screen sizes

### Interactive Elements
- Real-time chart updates with Plotly
- File upload support for custom sequences
- Sample data for quick demonstrations
- Expandable information sections
- Smooth transitions and micro-animations

### Premium Styling
- Custom **Poppins** font family
- Purple gradient theme (#667eea → #764ba2)
- Pulsing header with rotating DNA emoji 🧬
- Gradient text effects on key metrics
- Modern pill-shaped buttons

---

## 💻 Technology Stack

| Technology | Purpose |
|------------|---------|
| **Python 3.8+** | Core programming language |
| **Streamlit** | Web framework and UI |
| **Plotly** | Interactive visualizations |
| **Pandas** | Data structures and analysis |
| **Pure Python** | Bioinformatics algorithms (no heavy dependencies) |

---

## 📊 Key Capabilities

### Data Input Methods
1. **Sample Data:** Pre-loaded sequences for testing
2. **Manual Input:** Paste sequences directly
3. **File Upload:** Support for FASTA, TXT, CSV formats

### Visualization Types
- Bar charts (vertical & horizontal)
- Pie charts with percentages
- Line charts with markers
- Cumulative distribution plots
- Color-coded sequence displays

### Analytics Tracking
- Anonymous usage statistics
- Feature popularity metrics
- User ratings (1-5 stars)
- Feedback collection
- Public analytics dashboard

---

## 🌟 Unique Features

### Exit Feedback Integration
Automatically prompts users to fill feedback form when leaving the app:
- Exit intent detection
- Google Form integration
- Non-intrusive modal design

### Real-time Community Stats
- Total visits counter
- Analyses performed
- Average rating display
- Most popular feature tracking

### Educational Value
- Tooltips and explanations
- Sample datasets with context
- Result interpretations
- Scientific accuracy

---

## 🧪 Usage Examples

### Example 1: Analyze DNA Sequence
```python
1. Navigate to "DNA & Protein Analysis"
2. Select "Use Sample Data" (Topoisomerase gene)
3. Click "Analyze DNA Sequence"
4. View GC content, ORF detection, and visualizations
```

### Example 2: Calculate N50
```python
1. Go to "N50 Calculator"
2. Choose input method (sample/manual/file)
3. Click "Calculate N50 Metrics"
4. Explore cumulative distribution chart
```

### Example 3: Translate DNA to Protein
```python
1. Open "Advanced Analysis"
2. Select "DNA→Protein Translation" tab
3. Input or load DNA sequence
4. View side-by-side DNA and protein sequences
```

---

## 🔧 Configuration

### Streamlit Theme (`.streamlit/config.toml`)
```toml
[theme]
primaryColor = "#667eea"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"
font = "sans serif"
```

### Analytics Storage
Analytics data is stored in `data/analytics.json` (not committed to Git)

---

## 🚀 Deployment

### Streamlit Cloud (Recommended - FREE)
1. Push code to GitHub
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Deploy with one click!

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions.

---

## 📈 Performance

- ⚡ Fast load times (< 2 seconds)
- 🎯 Efficient pure Python implementations
- 📦 Minimal dependencies (3MB total)
- 🌐 Scales well on free hosting tiers

---

## 🎓 Educational Context

### Course Integration
This project fulfills requirements for:
- Digital Image Processing
- Bioinformatics algorithms
- Web application development
- Data visualization
- User experience design

### Learning Outcomes
- Python programming
- Algorithm implementation
- Web framework usage
- Data visualization
- Project deployment

---

## 🤝 Contributing

Contributions are welcome! This is an educational project, perfect for learning:
- Bioinformatics algorithms
- Streamlit web development
- Data visualization
- Python best practices

---

## 📝 License

This project is created for educational purposes as part of a Digital Image Processing course.

---

## 🌟 Acknowledgments

- **Course:** Digital Image Processing using Python
- **Institution:** [Your University Name]
- **Instructor:** [Instructor Name]
- **Tools:** Streamlit, Plotly, Python

---

## 📞 Contact

**Hamza Ahmed Siddiqui**  
📧 Email: [Your Email]  
🐙 GitHub: [@Hamza-Ahmed-S](https://github.com/Hamza-Ahmed-S)  
🔗 LinkedIn: [Your LinkedIn]

---

## 🎉 Try It Out!

**Live Demo:** [Your Streamlit Cloud URL]

Experience modern bioinformatics analysis in your browser - no installation required!

---

<div align="center">

Made with ❤️ for Bioinformatics Education

⭐ **Star this repo if you found it helpful!** ⭐

</div>
