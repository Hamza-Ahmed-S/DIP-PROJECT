"""
🧬 Bioinformatics Toolkit - Interactive Web App
Main homepage and navigation
"""

import streamlit as st
from analytics import Analytics
import sys
import os

# Initialize analytics
if 'analytics' not in st.session_state:
    st.session_state.analytics = Analytics()
    st.session_state.analytics.increment_visit()

# Page configuration
st.set_page_config(
    page_title="Bioinformatics Toolkit",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Exit feedback feature - Shows Google Form prompt when user tries to leave
st.components.v1.html("""
<script>
    // Google Form URL - Replace with your actual Google Form link
    const GOOGLE_FORM_URL = "https://forms.gle/YUrEef7Gj3GNBKS66";
    
    // Track if user has already been prompted
    let hasPrompted = false;
    
    window.addEventListener('beforeunload', function (e) {
        if (!hasPrompted) {
            hasPrompted = true;
            
            // Standard way to show browser's own confirmation dialog
            e.preventDefault();
            e.returnValue = '';
            
            // Try to open Google Form in a new tab (may be blocked by popup blocker)
            setTimeout(() => {
                const userWantsToFeedback = confirm(
                    "⭐ Before you go!\\n\\n" +
                    "Would you like to share your feedback about this Bioinformatics Toolkit?\\n\\n" +
                    "Click OK to open our quick feedback form (takes 1 minute)"
                );
                
                if (userWantsToFeedback) {
                    window.open(GOOGLE_FORM_URL, '_blank');
                }
            }, 100);
            
            return '';
        }
    });
    
    // Alternative: Show a custom modal when user moves cursor to close button
    let exitIntentShown = false;
    
    document.addEventListener('mouseleave', function(e) {
        if (e.clientY < 10 && !exitIntentShown) {
            exitIntentShown = true;
            
            // Create custom modal
            const modal = document.createElement('div');
            modal.style.cssText = `
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(0,0,0,0.8);
                display: flex;
                justify-content: center;
                align-items: center;
                z-index: 10000;
            `;
            
            modal.innerHTML = `
                <div style="
                    background: white;
                    padding: 2rem;
                    border-radius: 15px;
                    max-width: 500px;
                    text-align: center;
                    box-shadow: 0 10px 40px rgba(0,0,0,0.3);
                ">
                    <h2 style="color: #667eea; margin-bottom: 1rem;">⭐ Wait! Before You Go...</h2>
                    <p style="margin-bottom: 1.5rem; color: #333; font-size: 1.1rem;">
                        Help us improve by sharing your experience! 
                        It takes less than 1 minute.
                    </p>
                    <a href="${GOOGLE_FORM_URL}" 
                       target="_blank" 
                       style="
                           display: inline-block;
                           background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                           color: white;
                           padding: 12px 30px;
                           border-radius: 8px;
                           text-decoration: none;
                           font-weight: bold;
                           margin-right: 10px;
                       "
                       onclick="this.parentElement.parentElement.remove()">
                        📝 Fill Feedback Form
                    </a>
                    <button 
                        onclick="this.parentElement.parentElement.remove()" 
                        style="
                            background: #f0f0f0;
                            border: none;
                            padding: 12px 30px;
                            border-radius: 8px;
                            cursor: pointer;
                            font-weight: bold;
                        ">
                        Maybe Later
                    </button>
                </div>
            `;
            
            document.body.appendChild(modal);
            
            // Remove modal after 10 seconds if no action
            setTimeout(() => {
                if (modal.parentElement) {
                    modal.remove();
                }
            }, 10000);
        }
    });
</script>
""", height=0)

# Custom CSS for stunning eye-catching design
st.markdown("""
<style>
    /* Import Premium Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&family=Fira+Code:wght@400;500&display=swap');
    
    /* Global Font */
    * {
        font-family: 'Poppins', sans-serif !important;
    }
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Animated Gradient Background */
    .stApp {
        background: linear-gradient(-45deg, #667eea, #764ba2, #f093fb, #4facfe);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Floating Particles */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(circle at 20% 50%, rgba(255, 255, 255, 0.1) 2px, transparent 2px),
            radial-gradient(circle at 80% 80%, rgba(255, 255, 255, 0.1) 2px, transparent 2px),
            radial-gradient(circle at 40% 20%, rgba(255, 255, 255, 0.1) 2px, transparent 2px);
        background-size: 200px 200px, 150px 150px, 250px 250px;
        animation: particles 20s linear infinite;
        pointer-events: none;
        z-index: 0;
    }
    
    @keyframes particles {
        0% { transform: translateY(0) translateX(0); }
        100% { transform: translateY(-50px) translateX(50px); }
    }
    
    /* Main Content - Glassmorphism */
    .main .block-container {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-radius: 25px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 25px 45px rgba(0, 0, 0, 0.2);
       padding: 3rem !important;
        margin-top: 2rem;
        position: relative;
        z-index: 1;
    }
    
    /* Header with Pulse Animation */
    .main-header {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.95) 0%, rgba(118, 75, 162, 0.95) 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 15px 35px rgba(102, 126, 234, 0.4);
        position: relative;
        overflow: hidden;
        border: 2px solid rgba(255, 255, 255, 0.3);
        animation: headerPulse 4s ease-in-out infinite;
    }
    
    @keyframes headerPulse {
        0%, 100% { transform: scale(1); box-shadow: 0 15px 35px rgba(102, 126, 234, 0.4); }
        50% { transform: scale(1.02); box-shadow: 0 20px 45px rgba(102, 126, 234, 0.6); }
    }
    
    .main-header::before {
        content: "🧬";
        position: absolute;
        font-size: 15rem;
        opacity: 0.08;
        top: -3rem;
        right: -3rem;
        animation: rotate 10s linear infinite;
    }
    
    @keyframes rotate {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    
    .main-header h1 {
        color: white;
        font-size: 3.5rem;
        font-weight: 800;
        margin: 0;
        text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.3);
        animation: titleGlow 2s ease-in-out infinite alternate;
        letter-spacing: 1px;
    }
    
    @keyframes titleGlow {
        from { text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.3); }
        to { text-shadow: 0 0 25px rgba(255, 255, 255, 0.7), 3px 3px 6px rgba(0, 0, 0, 0.3); }
    }
    
    .main-header p {
        color: rgba(255, 255, 255, 0.95);
        font-size: 1.3rem;
        margin-top: 0.8rem;
        font-weight: 400;
    }
    
    /* Stat Cards with 3D Effect */
    .stat-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(255, 255, 255, 0.85) 100%);
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        border: 2px solid rgba(102, 126, 234, 0.2);
        position: relative;
        overflow: hidden;
    }
    
    .stat-card::before {
        content: "";
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(102, 126, 234, 0.15), transparent);
        transform: rotate(45deg);
        transition: all 0.6s;
    }
    
    .stat-card:hover::before {
        left: 100%;
    }
    
    .stat-card:hover {
        transform: translateY(-15px) scale(1.08);
        box-shadow: 0 25px 50px rgba(102, 126, 234, 0.35);
        border-color: rgba(102, 126, 234, 0.5);
    }
    
    .stat-number {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 0.5rem 0;
    }
    
    .stat-label {
        color: #666;
        font-size: 1rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1.5px;
    }
    
    /* Feature Cards with Slide Animation */
    .feature-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.98) 0%, rgba(255, 255, 255, 0.92) 100%);
        padding: 2.5rem;
        border-radius: 20px;
        margin: 1.5rem 0;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
        border-left: 6px solid #667eea;
        transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
        position: relative;
        overflow: hidden;
    }
    
    .feature-card::after {
        content: "";
        position: absolute;
        top: -50%;
        right: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(102, 126, 234, 0.08) 0%, transparent 70%);
        transition: all 0.5s;
    }
    
    .feature-card:hover::after {
        top: 0;
        right: 0;
    }
    
    .feature-card:hover {
        transform: translateX(15px) scale(1.02);
        box-shadow: 0 20px 40px rgba(102, 126, 234, 0.3);
        border-left-width: 10px;
    }
    
    .feature-card h3 {
        color: #667eea;
        font-size: 1.7rem;
        margin-bottom: 1rem;
        font-weight: 700;
    }
    
    .feature-card p {
        color: #555;
        line-height: 1.8;
        font-size: 1.05rem;
    }
    
    /* Premium Button Styles */
    .stButton button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 1rem 2.5rem;
        border-radius: 50px;
        font-weight: 700;
        font-size: 1.1rem;
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.4);
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1.5px;
    }
    
    .stButton button:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(102, 126, 234, 0.6);
    }
    
    /* Sidebar with Gradient */
    .css-1d391kg, [data-testid="stSidebar"] {
        background: linear-gradient(180deg, rgba(102, 126, 234, 0.95) 0%, rgba(118, 75, 162, 0.95) 100%);
        backdrop-filter: blur(10px);
    }
    
    .css-1d391kg *, [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    /* Enhanced Metrics */
    [data-testid="stMetricValue"] {
        font-size: 2.8rem !important;
        font-weight: 800 !important;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
    }
    
    /* Glowing Expanders */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.15) 0%, rgba(118, 75, 162, 0.15) 100%);
        border-radius: 10px;
        border: 2px solid rgba(102, 126, 234, 0.3);
        font-weight: 600;
        color: #667eea !important;
        transition: all 0.3s;
    }
    
    .streamlit-expanderHeader:hover {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.25) 0%, rgba(118, 75, 162, 0.25) 100%);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.2);
        transform: translateX(5px);
    }
    
    /* Modern Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background: rgba(255, 255, 255, 0.6);
        border-radius: 15px;
        padding: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 10px;
        padding: 12px 24px;
        font-weight: 600;
        transition: all 0.3s;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white !important;
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        transform: scale(1.05);
    }
    
    /* Alert Boxes */
    .stSuccess, .stInfo, .stWarning, .stError {
        border-radius: 15px;
        border-left-width: 5px;
        backdrop-filter: blur(10px);
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
    }
    
    /* Code Blocks */
    code {
        background: rgba(102, 126, 234, 0.12) !important;
        border-radius: 8px;
        padding: 3px 10px;
        font-family: 'Fira Code', monospace !important;
        border: 1px solid rgba(102, 126, 234, 0.25);
        font-size: 0.95em;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>🧬 Bioinformatics Toolkit</h1>
    <p style="font-size: 1.2rem; margin-top: 0.5rem;">Interactive DNA, Protein & Genome Analysis Platform</p>
    <p style="font-size: 0.9rem; opacity: 0.9;">Digital Image Processing Course Project | Made by Hamza Ahmed Siddiqui</p>
</div>
""", unsafe_allow_html=True)

# Get statistics
stats = st.session_state.analytics.get_overall_stats()
most_popular = st.session_state.analytics.get_most_popular_feature()

# Live Statistics Dashboard
st.markdown("## 📊 Live Community Statistics")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-number">{stats['total_visits']:,}</div>
        <div class="stat-label">👥 Total Visits</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-number">{stats['total_analyses']:,}</div>
        <div class="stat-label">🔬 Analyses Run</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    avg_rating = stats['average_rating']
    stars = "⭐" * int(round(avg_rating)) if avg_rating > 0 else "—"
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-number">{avg_rating:.1f}</div>
        <div class="stat-label">{stars}<br>Average Rating</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-number">{stats['total_feedback']:,}</div>
        <div class="stat-label">💬 Feedback Received</div>
    </div>
    """, unsafe_allow_html=True)

if stats['total_analyses'] > 0:
    st.success(f"🏆 **Most Popular Feature:** {most_popular}")

st.markdown("---")

# Features Overview
st.markdown("## 🚀 Available Analysis Tools")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3>🧪 ATP Hydrolysis Analysis</h3>
        <p>Calculate Gibbs free energy (ΔG) for ATP hydrolysis across different tissue types. 
        Analyze cellular energy metabolism with interactive visualizations.</p>
        <ul>
            <li>Thermodynamic calculations</li>
            <li>Tissue comparison (Liver, Muscle, Brain)</li>
            <li>Energy unit conversions</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <h3>🔬 Advanced DNA/Protein Analysis</h3>
        <p>Deep-dive into sequence analysis with open reading frame detection, 
        codon analysis, and protein translation.</p>
        <ul>
            <li>Valid ORF detection with coordinates</li>
            <li>Stop codon distance calculation</li>
            <li>DNA to protein translation</li>
            <li>Hydrophobic fragment extraction</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3>🧬 DNA & Protein Sequence Analysis</h3>
        <p>Fundamental bioinformatics analysis on DNA and protein sequences. 
        Upload your own data or use sample sequences.</p>
        <ul>
            <li>GC content calculation</li>
            <li>Open Reading Frame (ORF) finding</li>
            <li>Amino acid frequency distribution</li>
            <li>Hydrophobic residue analysis</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <h3>📊 N50 Genome Assembly Calculator</h3>
        <p>Assess genome assembly quality with industry-standard metrics. 
        Visualize contig distributions and get comprehensive statistics.</p>
        <ul>
            <li>N50/N90 quality statistics</li>
            <li>Contig length analysis</li>
            <li>Assembly quality visualization</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Instructions
st.markdown("## 📖 How to Use")
st.info("""
👈 **Navigate using the sidebar** to access different analysis tools.

Each tool allows you to:
- 📁 Upload your own data or use sample datasets
- 🔬 Run analyses with interactive parameters
- 📊 View results with beautiful visualizations
- ⭐ Rate features and provide feedback
- 📈 See community statistics on the Analytics Dashboard
""")

# About section
with st.expander("ℹ️ About This Project"):
    st.markdown("""
    ### Bioinformatics Using Python
    
    This interactive web application is part of a **Digital Image Processing Course Project** 
    that implements comprehensive bioinformatics tools using Python.
    
    **Key Technologies:**
    - Python 3.x (core analysis)
    - Streamlit (web interface)
    - Plotly (interactive visualizations)
    - Pure Python implementations (no heavy dependencies)
    
    **Author:** Hamza Ahmed Siddiqui (Roll No: 22FA-043-SE)  
    **Course:** Digital Image Processing using Python  
    **GitHub:** [DIP-PROJECT](https://github.com/Hamza-Ahmed-S/DIP-PROJECT)
    
    ---
    
    ### 🌟 Love this project?
    Give it a star on GitHub and share your feedback! Your input helps improve this tool for everyone.
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 1rem;">
    Made with ❤️ for Bioinformatics Education | 
    <a href="https://github.com/Hamza-Ahmed-S/DIP-PROJECT" target="_blank">View on GitHub</a>
</div>
""", unsafe_allow_html=True)
