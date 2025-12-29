"""
🧬 DNA & Protein Sequence Analysis
Fundamental bioinformatics analysis
"""

import streamlit as st
import sys
import os
from analytics import Analytics
from utils.visualizations import create_pie_chart, create_horizontal_bar_chart, visualize_dna_sequence, visualize_protein_sequence
from utils.data_loader import get_sample_dna, get_sample_protein, validate_dna_sequence, validate_protein_sequence, clean_sequence

# Initialize analytics
if 'analytics' not in st.session_state:
    st.session_state.analytics = Analytics()

st.set_page_config(page_title="DNA & Protein Analysis", page_icon="🧬", layout="wide")

# Header
st.title("🧬 DNA & Protein Sequence Analysis")
st.markdown("Fundamental sequence analysis tools for DNA and proteins")

# Track feature usage
if 'dna_analysis_tracked' not in st.session_state:
    st.session_state.analytics.track_feature_usage("dna_analysis")
    st.session_state.dna_analysis_tracked = True

# Tabs for DNA and Protein analysis
tab1, tab2 = st.tabs(["🧬 DNA Analysis", "🔬 Protein Analysis"])

# ============= DNA ANALYSIS TAB =============
with tab1:
    st.markdown("### DNA Sequence Analysis")
    st.info("Analyze DNA sequences for GC content and Open Reading Frames (ORFs)")
    
    # Input methods
    input_method = st.radio("Choose input method:", ["Use Sample Data", "Paste Sequence", "Upload File"], key="dna_input")
    
    dna_sequence = ""
    
    if input_method == "Use Sample Data":
        sample_type = st.selectbox("Select sample:", ["Topoisomerase Gene (Long)", "Short DNA Sequence"], key="dna_sample")
        if sample_type.startswith("Topoisomerase"):
            dna_sequence = get_sample_dna("topoisomerase")
        else:
            dna_sequence = get_sample_dna("short")
        st.code(dna_sequence, language="text")
    
    elif input_method == "Paste Sequence":
        dna_sequence = st.text_area("Enter DNA sequence (A, T, G, C):", height=150, key="dna_paste")
        dna_sequence = clean_sequence(dna_sequence)
    
    else:  # Upload File
        uploaded_file = st.file_uploader("Upload DNA sequence file:", type=["txt", "fasta"], key="dna_upload")
        if uploaded_file:
            dna_sequence = uploaded_file.read().decode("utf-8")
            dna_sequence = clean_sequence(dna_sequence)
            st.code(dna_sequence[:200] + "..." if len(dna_sequence) > 200 else dna_sequence)
    
    # Analyze button
    if st.button("🔬 Analyze DNA Sequence", type="primary", key="analyze_dna"):
        if not dna_sequence:
            st.error("⚠️ Please provide a DNA sequence")
        else:
            # Validate sequence
            is_valid, error_msg = validate_dna_sequence(dna_sequence)
            if not is_valid:
                st.error(f"⚠️ Invalid DNA sequence: {error_msg}")
            else:
                st.success(f"✅ Valid DNA sequence ({len(dna_sequence)} bases)")
                
                # Visualize sequence
                st.markdown("#### 🎨 Sequence Visualization")
                st.markdown(visualize_dna_sequence(dna_sequence, max_length=100), unsafe_allow_html=True)
                
                # 1. GC Content
                st.markdown("---")
                st.markdown("### 📊 GC Content Analysis")
                
                g_count = dna_sequence.count('G')
                c_count = dna_sequence.count('C')
                a_count = dna_sequence.count('A')
                t_count = dna_sequence.count('T')
                total = len(dna_sequence)
                
                gc_content = ((g_count + c_count) / total) * 100 if total > 0 else 0
                
                col1, col2 = st.columns([1, 2])
                
                with col1:
                    st.metric("GC Content", f"{gc_content:.2f}%")
                    st.metric("Sequence Length", f"{total} bp")
                    
                    st.markdown("**Base Composition:**")
                    st.write(f"- A: {a_count} ({(a_count/total*100):.1f}%)")
                    st.write(f"- T: {t_count} ({(t_count/total*100):.1f}%)")
                    st.write(f"- G: {g_count} ({(g_count/total*100):.1f}%)")
                    st.write(f"- C: {c_count} ({(c_count/total*100):.1f}%)")
                
                with col2:
                    nucleotide_data = {"A": a_count, "T": t_count, "G": g_count, "C": c_count}
                    fig = create_pie_chart(nucleotide_data, "Nucleotide Distribution")
                    st.plotly_chart(fig, use_container_width=True)
                
                # 2. ORF Detection
                st.markdown("---")
                st.markdown("### 🔍 Open Reading Frame (ORF) Detection")
                
                start_codon = "ATG"
                stop_codons = ["TAA", "TAG", "TGA"]
                
                start_pos = dna_sequence.find(start_codon)
                
                if start_pos != -1:
                    st.success(f"✅ Start codon (ATG) found at position {start_pos}")
                    
                    # Find stop codon
                    stop_pos = -1
                    for i in range(start_pos + 3, len(dna_sequence) - 2, 3):
                        codon = dna_sequence[i:i+3]
                        if codon in stop_codons:
                            stop_pos = i
                            stop_codon_found = codon
                            break
                    
                    if stop_pos != -1:
                        orf_sequence = dna_sequence[start_pos:stop_pos + 3]
                        st.success(f"✅ Stop codon ({stop_codon_found}) found at position {stop_pos}")
                        st.info(f"**ORF Length:** {len(orf_sequence)} bases ({len(orf_sequence)//3} codons)")
                        
                        with st.expander("View ORF Sequence"):
                            st.code(orf_sequence, language="text")
                    else:
                        st.warning("⚠️ No stop codon found in frame after start codon")
                else:
                    st.warning("⚠️ No start codon (ATG) found in sequence")
                
                # Interpretation
                with st.expander("📖 Understanding GC Content"):
                    st.markdown("""
                    ### What is GC Content?
                    
                    GC content is the percentage of bases in a DNA sequence that are either **Guanine (G)** or **Cytosine (C)**.
                    
                    **Significance:**
                    - **High GC content** (>60%): More stable DNA (3 hydrogen bonds)
                    - **Low GC content** (<40%): Less stable (2 hydrogen bonds for A-T)
                    - **Typical range**: 40-60% in most organisms
                    
                    **ORF (Open Reading Frame):**
                    - Starts with **ATG** (start codon)
                    - Ends with **TAA, TAG, or TGA** (stop codons)
                    - Represents a potential protein-coding region
                    """)

# ============= PROTEIN ANALYSIS TAB =============
with tab2:
    st.markdown("### Protein Sequence Analysis")
    st.info("Analyze protein sequences for amino acid composition and hydrophobic regions")
    
    # Input methods
    input_method_protein = st.radio("Choose input method:", ["Use Sample Data", "Paste Sequence", "Upload File"], key="protein_input")
    
    protein_sequence = ""
    
    if input_method_protein == "Use Sample Data":
        sample_type_protein = st.selectbox("Select sample:", ["TMEM222 Protein", "Short Hydrophobic Sequence"], key="protein_sample")
        if sample_type_protein.startswith("TMEM222"):
            protein_sequence = get_sample_protein("tmem222")
        else:
            protein_sequence = get_sample_protein("short")
        st.code(protein_sequence, language="text")
    
    elif input_method_protein == "Paste Sequence":
        protein_sequence = st.text_area("Enter protein sequence (single letter amino acids):", height=150, key="protein_paste")
        protein_sequence = clean_sequence(protein_sequence)
    
    else:  # Upload File
        uploaded_file_protein = st.file_uploader("Upload protein sequence file:", type=["txt", "fasta"], key="protein_upload")
        if uploaded_file_protein:
            protein_sequence = uploaded_file_protein.read().decode("utf-8")
            protein_sequence = clean_sequence(protein_sequence)
            st.code(protein_sequence[:200] + "..." if len(protein_sequence) > 200 else protein_sequence)
    
    # Analyze button
    if st.button("🔬 Analyze Protein Sequence", type="primary", key="analyze_protein"):
        if not protein_sequence:
            st.error("⚠️ Please provide a protein sequence")
        else:
            # Validate sequence
            is_valid, error_msg = validate_protein_sequence(protein_sequence)
            if not is_valid:
                st.error(f"⚠️ Invalid protein sequence: {error_msg}")
            else:
                st.success(f"✅ Valid protein sequence ({len(protein_sequence)} residues)")
                
                # Visualize sequence
                st.markdown("#### 🎨 Sequence Visualization")
                st.markdown(visualize_protein_sequence(protein_sequence, max_length=100), unsafe_allow_html=True)
                
                # 1. Amino Acid Frequency
                st.markdown("---")
                st.markdown("### 📊 Amino Acid Frequency Analysis")
                
                amino_acids = "ACDEFGHIKLMNPQRSTVWY"
                aa_counts = {aa: protein_sequence.count(aa) for aa in amino_acids}
                total_aa = len(protein_sequence)
                aa_frequencies = {aa: (count / total_aa * 100) for aa, count in aa_counts.items() if count > 0}
                
                col1, col2 = st.columns([1, 2])
                
                with col1:
                    st.metric("Sequence Length", f"{total_aa} aa")
                    st.metric("Unique Amino Acids", len(aa_frequencies))
                    
                    # Show top 5
                    st.markdown("**Top 5 Amino Acids:**")
                    sorted_aa = sorted(aa_frequencies.items(), key=lambda x: x[1], reverse=True)
                    for aa, freq in sorted_aa[:5]:
                        st.write(f"- **{aa}**: {freq:.1f}%")
                
                with col2:
                    if aa_frequencies:
                        fig = create_horizontal_bar_chart(aa_frequencies, "Amino Acid Frequency Distribution")
                        st.plotly_chart(fig, use_container_width=True)
                
                # 2. Hydrophobic Analysis
                st.markdown("---")
                st.markdown("### 💧 Hydrophobic Residue Analysis")
                
                hydrophobic_residues = "AILMFWYV"
                hydrophobic_count = sum(1 for aa in protein_sequence if aa in hydrophobic_residues)
                hydrophobic_percentage = (hydrophobic_count / total_aa * 100) if total_aa > 0 else 0
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.metric("Hydrophobic Residues", f"{hydrophobic_count}/{total_aa}")
                    st.metric("Hydrophobic Percentage", f"{hydrophobic_percentage:.2f}%")
                    
                    if hydrophobic_percentage > 50:
                        st.success("🔸 High hydrophobicity - likely transmembrane protein!")
                    elif hydrophobic_percentage > 30:
                        st.info("🔸 Moderate hydrophobicity")
                    else:
                        st.info("🔸 Low hydrophobicity - likely soluble protein")
                
                with col2:
                    # Create pie chart for hydrophobic vs hydrophilic
                    hydro_data = {
                        "Hydrophobic": hydrophobic_count,
                        "Hydrophilic": total_aa - hydrophobic_count
                    }
                    fig = create_pie_chart(hydro_data, "Hydrophobic vs Hydrophilic")
                    st.plotly_chart(fig, use_container_width=True)
                
                # Interpretation
                with st.expander("📖 Understanding Amino Acid Properties"):
                    st.markdown("""
                    ### Amino Acid Classification
                    
                    **Hydrophobic (Water-repelling):** A, I, L, M, F, W, Y, V
                    - Found in protein cores and transmembrane regions
                    - Important for protein folding and membrane spanning
                    
                    **Hydrophilic (Water-loving):** All others
                    - Found on protein surfaces
                    - Interact with aqueous environment
                    
                    **Transmembrane Proteins:**
                    - Typically have >50% hydrophobic residues
                    - Contain stretches of hydrophobic amino acids
                    - Span cell membranes
                    """)

st.markdown("---")

# Rating section
st.markdown("## ⭐ Rate This Feature")
rating = st.slider("How useful was this analysis?", 1, 5, 5, key="dna_prot_rating")
feedback = st.text_area("Share your feedback (optional):", key="dna_prot_feedback")

if st.button("Submit Rating"):
    st.session_state.analytics.add_rating("dna_analysis", rating, feedback)
    st.success("✅ Thank you for your feedback!")
    st.balloons()
