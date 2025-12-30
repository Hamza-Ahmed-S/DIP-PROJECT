"""
🧪 ATP Hydrolysis Analysis
Interactive thermodynamic calculations
"""

import streamlit as st
import sys
import os
from analytics import Analytics
from utils.visualizations import create_bar_chart

# Add parent directory to path to import requirement1
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# Apply shared styling
from utils.shared_styling import apply_common_styling
apply_common_styling()


# Initialize analytics
if 'analytics' not in st.session_state:
    st.session_state.analytics = Analytics()

st.set_page_config(page_title="ATP Hydrolysis Analysis", page_icon="🧪", layout="wide")

# Header
st.title("🧪 ATP Hydrolysis Analysis")
st.markdown("Calculate Gibbs free energy (ΔG) for ATP hydrolysis in different tissues")

# Track feature usage
if 'atp_analysis_tracked' not in st.session_state:
    st.session_state.analytics.track_feature_usage("atp_hydrolysis")
    st.session_state.atp_analysis_tracked = True

# Educational information
with st.expander("ℹ️ About ATP Hydrolysis"):
    st.markdown("""
    ### What is ATP Hydrolysis?
    
    ATP (Adenosine Triphosphate) is the primary energy currency of cells. When ATP is hydrolyzed 
    to ADP (Adenosine Diphosphate) and inorganic phosphate (Pi), energy is released.
    
    **Reaction:** ATP + H₂O → ADP + Pi + Energy
    
    ### Gibbs Free Energy (ΔG)
    
    The Gibbs free energy change (ΔG) determines whether a reaction is spontaneous:
    - **ΔG < 0**: Reaction is spontaneous (exergonic) - releases energy
    - **ΔG > 0**: Reaction is non-spontaneous (endergonic) - requires energy
    - **ΔG = 0**: Reaction is at equilibrium
    
    **Formula:** ΔG = ΔG° + RT ln(Q)
    
    Where:
    - ΔG° = Standard free energy change
    - R = Gas constant (8.314 J/mol·K)
    - T = Temperature (Kelvin)
    - Q = Reaction quotient ([ADP][Pi]/[ATP])
    """)

st.markdown("---")

# Constants
R = 8.314  # J/(mol·K)
delta_G_standard = -30500  # J/mol
T_celsius = 37
T_kelvin = T_celsius + 273.15

# Tissue data
st.markdown("## 🔬 Tissue Analysis")
st.info("Analyze ATP hydrolysis in different tissue types with varying metabolite concentrations")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🔴 Liver Tissue")
    liver_atp = st.slider("ATP (mM)", 0.5, 10.0, 3.5, 0.1, key="liver_atp")
    liver_adp = st.slider("ADP (mM)", 0.1, 5.0, 1.8, 0.1, key="liver_adp")
    liver_pi = st.slider("Pi (mM)", 1.0, 10.0, 5.0, 0.1, key="liver_pi")

with col2:
    st.markdown("### 💪 Muscle Tissue")
    muscle_atp = st.slider("ATP (mM)", 0.5, 10.0, 8.0, 0.1, key="muscle_atp")
    muscle_adp = st.slider("ADP (mM)", 0.1, 5.0, 0.9, 0.1, key="muscle_adp")
    muscle_pi = st.slider("Pi (mM)", 1.0, 10.0, 8.0, 0.1, key="muscle_pi")

with col3:
    st.markdown("### 🧠 Brain Tissue")
    brain_atp = st.slider("ATP (mM)", 0.5, 10.0, 2.6, 0.1, key="brain_atp")
    brain_adp = st.slider("ADP (mM)", 0.1, 5.0, 0.7, 0.1, key="brain_adp")
    brain_pi = st.slider("Pi (mM)", 1.0, 10.0, 2.7, 0.1, key="brain_pi")

# Calculate button
if st.button("🧮 Calculate ΔG for All Tissues", type="primary"):
    st.markdown("---")
    st.markdown("## 📊 Results")
    
    # Calculate for each tissue
    tissues = {
        "Liver": {"ATP": liver_atp, "ADP": liver_adp, "Pi": liver_pi},
        "Muscle": {"ATP": muscle_atp, "ADP": muscle_adp, "Pi": muscle_pi},
        "Brain": {"ATP": brain_atp, "ADP": brain_adp, "Pi": brain_pi}
    }
    
    results = {}
    
    for tissue, conc in tissues.items():
        # Convert mM to M
        atp_m = conc["ATP"] / 1000
        adp_m = conc["ADP"] / 1000
        pi_m = conc["Pi"] / 1000
        
        # Calculate Q
        Q = (adp_m * pi_m) / atp_m
        
        # Calculate ΔG
        delta_G = delta_G_standard + (R * T_kelvin * 2.303 * (-3))  # Using log10
        delta_G_actual = delta_G_standard + R * T_kelvin * 2.303 * (-3)
        
        # More accurate calculation
        import math
        ln_Q = math.log(Q)
        delta_G = delta_G_standard + (R * T_kelvin * ln_Q)
        
        # Convert to kJ/mol and kcal/mol
        delta_G_kJ = delta_G / 1000
        delta_G_kcal = delta_G_kJ / 4.184
        
        results[tissue] = {
            "ΔG (J/mol)": delta_G,
            "ΔG (kJ/mol)": delta_G_kJ,
            "ΔG (kcal/mol)": delta_G_kcal,
            "Q": Q
        }
    
    # Display results in columns
    col1, col2, col3 = st.columns(3)
    
    for idx, (tissue, data) in enumerate(results.items()):
        col = [col1, col2, col3][idx]
        with col:
            if tissue == "Liver":
                color = "🔴"
            elif tissue == "Muscle":
                color = "💪"
            else:
                color = "🧠"
            
            st.markdown(f"### {color} {tissue}")
            st.metric("ΔG (kJ/mol)", f"{data['ΔG (kJ/mol)']:.2f}")
            st.metric("ΔG (kcal/mol)", f"{data['ΔG (kcal/mol)']:.2f}")
            st.caption(f"Reaction Quotient (Q): {data['Q']:.6f}")
            
            if data['ΔG (kJ/mol)'] < 0:
                st.success("✅ Spontaneous (Exergonic)")
            else:
                st.error("❌ Non-spontaneous (Endergonic)")
    
    # Find most exothermic
    most_exothermic = min(results.items(), key=lambda x: x[1]['ΔG (kJ/mol)'])
    
    st.markdown("---")
    st.success(f"🏆 **Most Exothermic Reaction:** {most_exothermic[0]} tissue with ΔG = {most_exothermic[1]['ΔG (kJ/mol)']:.2f} kJ/mol")
    
    # Visualization
    st.markdown("### 📊 Comparison Chart")
    chart_data = {tissue: data['ΔG (kJ/mol)'] for tissue, data in results.items()}
    fig = create_bar_chart(chart_data, "Gibbs Free Energy by Tissue", "Tissue Type", "ΔG (kJ/mol)")
    st.plotly_chart(fig, width='stretch')
    
    # Interpretation
    with st.expander("📖 Understanding the Results"):
        st.markdown("""
        ### Interpretation Guide
        
        - **Negative ΔG values** indicate that ATP hydrolysis is **spontaneous** and releases energy
        - **More negative ΔG** means **more energy released** (more exothermic)
        - Different tissues have different metabolite concentrations based on their energy demands
        
        **Typical Patterns:**
        - **Muscle tissue** often shows high ATP/ADP ratio (high energy state)
        - **Brain tissue** maintains moderate ATP levels for consistent energy supply
        - **Liver tissue** balances energy production and storage
        """)

st.markdown("---")

# Rating section
st.markdown("## ⭐ Rate This Feature")
rating = st.slider("How useful was this analysis?", 1, 5, 5, key="atp_rating")
feedback = st.text_area("Share your feedback (optional):", key="atp_feedback")

if st.button("Submit Rating"):
    st.session_state.analytics.add_rating("atp_hydrolysis", rating, feedback)
    st.success("✅ Thank you for your feedback!")
    st.balloons()
