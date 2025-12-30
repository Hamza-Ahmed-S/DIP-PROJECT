"""
🔬 Advanced DNA/Protein Analysis
Deep-dive sequence analysis tools
"""

import streamlit as st
import sys
import os
from analytics import Analytics
from utils.data_loader import get_sample_dna, get_sample_protein, validate_dna_sequence, clean_sequence
from utils.visualizations import visualize_dna_sequence, visualize_protein_sequence

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from codon_table import CODON_TABLE

# Initialize analytics
if 'analytics' not in st.session_state:
    st.session_state.analytics = Analytics()


# Apply shared styling
from utils.shared_styling import apply_common_styling
apply_common_styling()

st.set_page_config(page_title="Advanced Analysis", page_icon="🔬", layout="wide")

# Header
st.title("🔬 Advanced DNA/Protein Analysis")
st.markdown("Deep-dive analysis: ORF detection, codon analysis, and protein translation")

# Track feature usage
if 'advanced_analysis_tracked' not in st.session_state:
    st.session_state.analytics.track_feature_usage("advanced_analysis")
    st.session_state.advanced_analysis_tracked = True

# Analysis tabs
tab1, tab2, tab3, tab4 = st.tabs(["🔍 Valid ORF Detection", "📏 Stop Codon Distance", "💧 Hydrophobic Fragments", "🧬 DNA→Protein Translation"])

# ============= TAB 1: VALID ORF DETECTION =============
with tab1:
    st.markdown("### Valid Open Reading Frame (ORF) Detection")
    st.info("Find all valid ORFs with start codons (ATG) and in-frame stop codons")
    
    # Input
    input_method = st.radio("Choose input method:", ["Use Sample Data", "Paste Sequence"], key="orf_input")
    
    if input_method == "Use Sample Data":
        dna_seq = get_sample_dna("topoisomerase")
        st.code(dna_seq[:200] + "..." if len(dna_seq) > 200 else dna_seq)
    else:
        dna_seq = st.text_area("Enter DNA sequence:", height=150, key="orf_paste")
        dna_seq = clean_sequence(dna_seq)
    
    if st.button("🔍 Find Valid ORFs", type="primary", key="find_orfs"):
        if not dna_seq:
            st.error("⚠️ Please provide a DNA sequence")
        else:
            is_valid, error_msg = validate_dna_sequence(dna_seq)
            if not is_valid:
                st.error(f"⚠️ Invalid DNA sequence: {error_msg}")
            else:
                st.success(f"✅ Analyzing sequence ({len(dna_seq)} bases)")
                
                # Find all ORFs
                start_codon = "ATG"
                stop_codons = ["TAA", "TAG", "TGA"]
                orfs_found = []
                
                # Search for all start codons
                for i in range(len(dna_seq) - 2):
                    if dna_seq[i:i+3] == start_codon:
                        # Look for stop codon in frame
                        for j in range(i + 3, len(dna_seq) - 2, 3):
                            codon = dna_seq[j:j+3]
                            if codon in stop_codons:
                                orf_seq = dna_seq[i:j+3]
                                orfs_found.append({
                                    "start": i,
                                    "stop": j,
                                    "length": len(orf_seq),
                                    "sequence": orf_seq,
                                    "stop_codon": codon
                                })
                                break
                
                if orfs_found:
                    st.success(f"✅ Found {len(orfs_found)} valid ORF(s)")
                    
                    for idx, orf in enumerate(orfs_found, 1):
                        with st.expander(f"ORF #{idx} - Position {orf['start']} to {orf['stop']} ({orf['length']} bp)"):
                            col1, col2 = st.columns(2)
                            with col1:
                                st.write(f"**Start Position:** {orf['start']}")
                                st.write(f"**Stop Position:** {orf['stop']}")
                                st.write(f"**Length:** {orf['length']} bases")
                            with col2:
                                st.write(f"**Stop Codon:** {orf['stop_codon']}")
                                st.write(f"**Codons:** {orf['length'] // 3}")
                            
                            st.markdown("**Sequence:**")
                            st.code(orf['sequence'], language="text")
                else:
                    st.warning("⚠️ No valid ORFs found in this sequence")

# ============= TAB 2: STOP CODON DISTANCE =============
with tab2:
    st.markdown("### Stop Codon Distance Analysis")
    st.info("Calculate distances from start codon to all stop codons")
    
    # Input
    input_method2 = st.radio("Choose input method:", ["Use Sample Data", "Paste Sequence"], key="stop_input")
    
    if input_method2 == "Use Sample Data":
        dna_seq2 = get_sample_dna("topoisomerase")
        st.code(dna_seq2[:200] + "..." if len(dna_seq2) > 200 else dna_seq2)
    else:
        dna_seq2 = st.text_area("Enter DNA sequence:", height=150, key="stop_paste")
        dna_seq2 = clean_sequence(dna_seq2)
    
    if st.button("📏 Calculate Stop Codon Distances", type="primary", key="calc_stop"):
        if not dna_seq2:
            st.error("⚠️ Please provide a DNA sequence")
        else:
            is_valid, error_msg = validate_dna_sequence(dna_seq2)
            if not is_valid:
                st.error(f"⚠️ Invalid DNA sequence: {error_msg}")
            else:
                # Find start codon
                start_pos = dna_seq2.find("ATG")
                
                if start_pos == -1:
                    st.warning("⚠️ No start codon (ATG) found")
                else:
                    st.success(f"✅ Start codon found at position {start_pos}")
                    
                    # Find all stop codons after start
                    stop_codons = ["TAA", "TAG", "TGA"]
                    stops_found = []
                    
                    for stop_codon in stop_codons:
                        pos = start_pos + 3
                        while pos < len(dna_seq2) - 2:
                            idx = dna_seq2.find(stop_codon, pos)
                            if idx != -1:
                                distance = idx - start_pos
                                stops_found.append({
                                    "codon": stop_codon,
                                    "position": idx,
                                    "distance": distance
                                })
                                pos = idx + 1
                            else:
                                break
                    
                    if stops_found:
                        # Sort by distance
                        stops_found.sort(key=lambda x: x['distance'])
                        
                        st.success(f"✅ Found {len(stops_found)} stop codon(s) after start")
                        
                        # Show nearest
                        nearest = stops_found[0]
                        st.info(f"🎯 **Nearest Stop Codon:** {nearest['codon']} at position {nearest['position']} (distance: {nearest['distance']} bases)")
                        
                        # Table of all stops
                        st.markdown("#### All Stop Codons:")
                        
                        for stop in stops_found[:10]:  # Show first 10
                            col1, col2, col3 = st.columns(3)
                            with col1:
                                st.write(f"**Codon:** {stop['codon']}")
                            with col2:
                                st.write(f"**Position:** {stop['position']}")
                            with col3:
                                st.write(f"**Distance:** {stop['distance']} bases")
                            st.markdown("---")
                    else:
                        st.warning("⚠️ No stop codons found after start codon")

# ============= TAB 3: HYDROPHOBIC FRAGMENTS =============
with tab3:
    st.markdown("### Hydrophobic Fragment Extraction")
    st.info("Find continuous stretches of hydrophobic amino acids (≥3 residues)")
    
    # Input
    input_method3 = st.radio("Choose input method:", ["Use Sample Data", "Paste Sequence"], key="hydro_input")
    
    if input_method3 == "Use Sample Data":
        prot_seq = get_sample_protein("tmem222")
        st.code(prot_seq)
    else:
        prot_seq = st.text_area("Enter protein sequence:", height=150, key="hydro_paste")
        prot_seq = clean_sequence(prot_seq)
    
    min_length = st.slider("Minimum fragment length:", 3, 10, 3, key="min_hydro")
    
    if st.button("💧 Find Hydrophobic Fragments", type="primary", key="find_hydro"):
        if not prot_seq:
            st.error("⚠️ Please provide a protein sequence")
        else:
            st.success(f"✅ Analyzing sequence ({len(prot_seq)} residues)")
            
            # Find hydrophobic fragments
            hydrophobic = "AILMFWYV"
            fragments = []
            current_fragment = ""
            start_pos = -1
            
            for i, aa in enumerate(prot_seq):
                if aa in hydrophobic:
                    if not current_fragment:
                        start_pos = i
                    current_fragment += aa
                else:
                    if len(current_fragment) >= min_length:
                        fragments.append({
                            "sequence": current_fragment,
                            "start": start_pos,
                            "end": i - 1,
                            "length": len(current_fragment)
                        })
                    current_fragment = ""
            
            # Check last fragment
            if len(current_fragment) >= min_length:
                fragments.append({
                    "sequence": current_fragment,
                    "start": start_pos,
                    "end": len(prot_seq) - 1,
                    "length": len(current_fragment)
                })
            
            if fragments:
                st.success(f"✅ Found {len(fragments)} hydrophobic fragment(s)")
                
                for idx, frag in enumerate(fragments, 1):
                    with st.expander(f"Fragment #{idx} - {frag['sequence']} ({frag['length']} aa)"):
                        col1, col2 = st.columns(2)
                        with col1:
                            st.write(f"**Sequence:** {frag['sequence']}")
                            st.write(f"**Length:** {frag['length']} amino acids")
                        with col2:
                            st.write(f"**Start:** Position {frag['start']}")
                            st.write(f"**End:** Position {frag['end']}")
                        
                        if frag['length'] >= 7:
                            st.success("🔸 Potential transmembrane domain!")
            else:
                st.warning(f"⚠️ No hydrophobic fragments of length ≥{min_length} found")

# ============= TAB 4: DNA TO PROTEIN TRANSLATION =============
with tab4:
    st.markdown("### DNA to Protein Translation")
    st.info("Translate DNA sequence to protein using the genetic code")
    
    # Input
    input_method4 = st.radio("Choose input method:", ["Use Sample Data", "Paste Sequence"], key="trans_input")
    
    if input_method4 == "Use Sample Data":
        dna_seq4 = get_sample_dna("topoisomerase")
        st.code(dna_seq4[:200] + "..." if len(dna_seq4) > 200 else dna_seq4)
    else:
        dna_seq4 = st.text_area("Enter DNA sequence:", height=150, key="trans_paste")
        dna_seq4 = clean_sequence(dna_seq4)
    
    if st.button("🧬 Translate DNA to Protein", type="primary", key="translate"):
        if not dna_seq4:
            st.error("⚠️ Please provide a DNA sequence")
        else:
            is_valid, error_msg = validate_dna_sequence(dna_seq4)
            if not is_valid:
                st.error(f"⚠️ Invalid DNA sequence: {error_msg}")
            else:
                # Translate
                protein = ""
                for i in range(0, len(dna_seq4) - 2, 3):
                    codon = dna_seq4[i:i+3]
                    if len(codon) == 3:
                        aa = CODON_TABLE.get(codon, 'X')
                        if aa == '*' or aa == '_':  # Stop codon
                            break
                        protein += aa
                
                if protein:
                    st.success(f"✅ Translation successful! ({len(protein)} amino acids)")
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown("#### 🧬 DNA Sequence:")
                        st.markdown(visualize_dna_sequence(dna_seq4, max_length=100), unsafe_allow_html=True)
                    
                    with col2:
                        st.markdown("#### 🔬 Protein Sequence:")
                        st.markdown(visualize_protein_sequence(protein, max_length=100), unsafe_allow_html=True)
                    
                    st.markdown("---")
                    st.markdown("#### Full Protein Sequence:")
                    st.code(protein, language="text")
                    
                    # Stats
                    st.markdown("#### Statistics:")
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Codons Translated", len(protein))
                    with col2:
                        hydrophobic = sum(1 for aa in protein if aa in "AILMFWYV")
                        st.metric("Hydrophobic %", f"{(hydrophobic/len(protein)*100):.1f}%")
                    with col3:
                        st.metric("Unique Amino Acids", len(set(protein)))
                else:
                    st.warning("⚠️ Translation produced empty protein (immediate stop codon?)")

st.markdown("---")

# Rating section
st.markdown("## ⭐ Rate This Feature")
rating = st.slider("How useful was this analysis?", 1, 5, 5, key="advanced_rating")
feedback = st.text_area("Share your feedback (optional):", key="advanced_feedback")

if st.button("Submit Rating"):
    st.session_state.analytics.add_rating("advanced_analysis", rating, feedback)
    st.success("✅ Thank you for your feedback!")
    st.balloons()
