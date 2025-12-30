"""
📝 Feedback Survey
Redirect to Google Form for project feedback
"""

import streamlit as st

# Page configuration

# Apply shared styling
from utils.shared_styling import apply_common_styling
apply_common_styling()

st.set_page_config(
    page_title="Feedback Survey",
    page_icon="📝",
    layout="wide"
)

# Google Form URL
GOOGLE_FORM_URL = "https://forms.gle/YUrEef7Gj3GNBKS66"

# Custom styling
st.markdown("""
<style>
    .big-button {
        display: inline-block;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white !important;
        padding: 1.5rem 3rem;
        border-radius: 50px;
        text-decoration: none !important;
        font-size: 1.3rem;
        font-weight: 700;
        box-shadow: 0 10px 25px rgba(102, 126, 234, 0.4);
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        text-align: center;
    }
    
    .big-button:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(102, 126, 234, 0.6);
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.title("📝 Feedback Survey")
st.subheader("Help Us Improve the Bioinformatics Toolkit")

st.markdown("---")

# Main content
col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    st.markdown("### ⭐⭐⭐⭐⭐")
    st.markdown("## Your Opinion Matters!")
    
    st.markdown("""
    We value your feedback! Please take **2 minutes** to complete our survey.  
    Your responses will help us improve this tool for the entire bioinformatics community.
    """)
    
    st.markdown("#### The survey covers:")
    st.markdown("""
    - ✅ Overall experience rating
    - ✅ Most useful features
    - ✅ Ease of use
    - ✅ Suggestions for improvement
    - ✅ General feedback
    """)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Big button
    st.markdown(f"""
    <div style="text-align: center; margin: 2rem 0;">
        <a href="{GOOGLE_FORM_URL}" target="_blank" class="big-button">
            📝 OPEN FEEDBACK SURVEY
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("💡 **Tip:** The survey will open in a new tab so you won't lose your place in the app!")

st.markdown("---")

# Additional info
st.markdown("### 🙏 Thank You!")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **Your feedback helps us:**
    - 🎯 Identify the most useful features
    - 🔧 Improve usability and design
    """)

with col2:
    st.markdown("""
    **We use it to:**
    - ✨ Add new features that users need
    - 📊 Demonstrate community engagement
    """)

st.success("✅ All responses are **anonymous** and will be used solely for improving this educational project.")

st.markdown("---")

# Auto-redirect to Google Form
st.components.v1.html(f"""
<script>
    // Auto-redirect to Google Form when page loads
    window.open("{GOOGLE_FORM_URL}", "_blank");
</script>
""", height=0)

st.success("✅ **Google Form opened in a new tab!** If it didn't open, click the button above.")

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; color: #999; padding: 1rem;">
    <small>Bioinformatics Toolkit | Made with ❤️ for Education</small>
</div>
""", unsafe_allow_html=True)


