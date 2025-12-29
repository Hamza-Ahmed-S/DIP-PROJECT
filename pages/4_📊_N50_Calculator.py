"""
📊 N50 Genome Assembly Calculator
Quality metrics for genome assemblies
"""

import streamlit as st
from analytics import Analytics
from utils.visualizations import create_line_chart, create_bar_chart
from utils.data_loader import get_sample_contigs, parse_contig_lengths

# Initialize analytics
if 'analytics' not in st.session_state:
    st.session_state.analytics = Analytics()

st.set_page_config(page_title="N50 Calculator", page_icon="📊", layout="wide")

# Header
st.title("📊 N50 Genome Assembly Calculator")
st.markdown("Calculate assembly quality metrics: N50, N90, and contig statistics")

# Track feature usage
if 'n50_analysis_tracked' not in st.session_state:
    st.session_state.analytics.track_feature_usage("n50_calculator")
    st.session_state.n50_analysis_tracked = True

# Educational information
with st.expander("ℹ️ What is N50?"):
    st.markdown("""
    ### N50 - Assembly Quality Metric
    
    **N50** is a statistical measure used to evaluate the quality of genome assemblies.
    
    **Definition:**
    - Sort all contigs by length (longest first)
    - Calculate cumulative length
    - **N50 = Length of the contig at 50% of total assembly**
    
    **Interpretation:**
    - **Higher N50** = Better assembly quality
    - Indicates longer, more contiguous sequences
    - Shows fewer fragmentation in the assembly
    
    **Example:**
    - If total assembly = 10,000 bp and N50 = 2,000 bp
    - This means half the assembly is in contigs ≥ 2,000 bp
    
    **N90** follows the same principle but at 90% of total length.
    """)

st.markdown("---")

# Input section
st.markdown("## 📥 Input Contig Lengths")

input_method = st.radio("Choose input method:", ["Use Sample Data", "Enter Manually", "Upload File"], key="n50_input")

contig_lengths = []

if input_method == "Use Sample Data":
    contig_lengths = get_sample_contigs()
    st.info(f"✅ Loaded {len(contig_lengths)} sample contigs")
    st.code(", ".join(map(str, contig_lengths)), language="text")

elif input_method == "Enter Manually":
    manual_input = st.text_area(
        "Enter contig lengths (one per line or comma-separated):",
        height=150,
        placeholder="2000\n1800\n1500\n...\n\nor\n\n2000, 1800, 1500, ...",
        key="manual_contigs"
    )
    
    if manual_input.strip():
        # Try to parse
        try:
            # Replace commas with newlines
            cleaned = manual_input.replace(",", "\n")
            contig_lengths = [int(x.strip()) for x in cleaned.split() if x.strip().isdigit()]
        except:
            st.error("⚠️ Invalid input format")

else:  # Upload File
    uploaded_file = st.file_uploader("Upload file with contig lengths:", type=["txt", "csv"], key="upload_contigs")
    if uploaded_file:
        content = uploaded_file.read().decode("utf-8")
        contig_lengths = parse_contig_lengths(content)
        st.info(f"✅ Loaded {len(contig_lengths)} contigs from file")

# Calculate button
if st.button("📊 Calculate N50/N90 Statistics", type="primary", key="calc_n50"):
    if not contig_lengths:
        st.error("⚠️ Please provide contig lengths")
    else:
        st.markdown("---")
        st.markdown("## 📈 Results")
        
        # Sort contigs by length (descending)
        sorted_contigs = sorted(contig_lengths, reverse=True)
        
        # Calculate total length
        total_length = sum(sorted_contigs)
        
        # Calculate N50
        cumulative_length = 0
        n50 = 0
        n50_index = -1
        
        for i, length in enumerate(sorted_contigs):
            cumulative_length += length
            if cumulative_length >= total_length * 0.5:
                n50 = length
                n50_index = i
                break
        
        # Calculate N90
        cumulative_length = 0
        n90 = 0
        n90_index = -1
        
        for i, length in enumerate(sorted_contigs):
            cumulative_length += length
            if cumulative_length >= total_length * 0.9:
                n90 = length
                n90_index = i
                break
        
        # Display key metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("N50", f"{n50:,} bp")
            st.caption(f"Contig #{n50_index + 1}")
        
        with col2:
            st.metric("N90", f"{n90:,} bp")
            st.caption(f"Contig #{n90_index + 1}")
        
        with col3:
            st.metric("Total Length", f"{total_length:,} bp")
            st.caption(f"{len(sorted_contigs)} contigs")
        
        with col4:
            st.metric("Longest Contig", f"{sorted_contigs[0]:,} bp")
            st.caption(f"Shortest: {sorted_contigs[-1]:,} bp")
        
        # Additional statistics
        st.markdown("---")
        st.markdown("### 📊 Detailed Statistics")
        
        col1, col2 = st.columns(2)
        
        with col1:
            mean_length = total_length / len(sorted_contigs)
            median_length = sorted_contigs[len(sorted_contigs) // 2]
            
            st.write(f"**Mean Contig Length:** {mean_length:,.0f} bp")
            st.write(f"**Median Contig Length:** {median_length:,} bp")
            st.write(f"**Number of Contigs:** {len(sorted_contigs)}")
            st.write(f"**Shortest Contig:** {sorted_contigs[-1]:,} bp")
            st.write(f"**Longest Contig:** {sorted_contigs[0]:,} bp")
        
        with col2:
            # Quality assessment
            st.markdown("**Assembly Quality:**")
            if n50 > mean_length * 1.5:
                st.success("🟢 Excellent - N50 significantly above mean")
            elif n50 > mean_length:
                st.info("🔵 Good - N50 above mean")
            else:
                st.warning("🟡 Fair - N50 below mean, consider improving assembly")
        
        # Visualization: Cumulative Length
        st.markdown("---")
        st.markdown("### 📈 Cumulative Length Distribution")
        
        cumulative_lengths = []
        cumulative = 0
        for length in sorted_contigs:
            cumulative += length
            cumulative_lengths.append(cumulative)
        
        fig = create_line_chart(
            list(range(1, len(sorted_contigs) + 1)),
            cumulative_lengths,
            "Cumulative Assembly Length",
            "Contig Number (sorted by length)",
            "Cumulative Length (bp)"
        )
        
        # Add N50 and N90 markers
        import plotly.graph_objects as go
        fig.add_trace(go.Scatter(
            x=[n50_index + 1],
            y=[cumulative_lengths[n50_index]],
            mode='markers',
            name='N50',
            marker=dict(size=15, color='red', symbol='diamond')
        ))
        fig.add_trace(go.Scatter(
            x=[n90_index + 1],
            y=[cumulative_lengths[n90_index]],
            mode='markers',
            name='N90',
            marker=dict(size=15, color='orange', symbol='diamond')
        ))
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Contig length distribution
        st.markdown("### 📊 Contig Length Distribution")
        
        # Group contigs by size ranges
        ranges = {
            "< 500 bp": len([x for x in sorted_contigs if x < 500]),
            "500-1000 bp": len([x for x in sorted_contigs if 500 <= x < 1000]),
            "1000-2000 bp": len([x for x in sorted_contigs if 1000 <= x < 2000]),
            "> 2000 bp": len([x for x in sorted_contigs if x >= 2000])
        }
        
        fig2 = create_bar_chart(ranges, "Contig Size Distribution", "Size Range", "Number of Contigs")
        st.plotly_chart(fig2, use_container_width=True)
        
        # Contig table
        with st.expander("📋 View All Contigs"):
            st.markdown("**Top 20 Longest Contigs:**")
            for i, length in enumerate(sorted_contigs[:20], 1):
                marker = ""
                if i == n50_index + 1:
                    marker = " ⭐ N50"
                elif i == n90_index + 1:
                    marker = " 🔶 N90"
                
                col1, col2, col3 = st.columns([1, 2, 2])
                with col1:
                    st.write(f"**#{i}**")
                with col2:
                    st.write(f"{length:,} bp")
                with col3:
                    st.write(marker)
        
        # Interpretation guide
        with st.expander("📖 How to Interpret Results"):
            st.markdown("""
            ### Quality Guidelines
            
            **N50 Value:**
            - **> 10 kb**: Excellent for most bacterial genomes
            - **5-10 kb**: Good quality assembly
            - **< 5 kb**: May need improvement
            
            **Number of Contigs:**
            - **Fewer contigs** = Better assembly continuity
            - **Many small contigs** = Fragmented assembly
            
            **Recommendations:**
            - Compare N50 to expected genome size
            - Higher N50 relative to genome size is better
            - Consider long-read sequencing to improve N50
            """)

st.markdown("---")

# Rating section
st.markdown("## ⭐ Rate This Feature")
rating = st.slider("How useful was this analysis?", 1, 5, 5, key="n50_rating")
feedback = st.text_area("Share your feedback (optional):", key="n50_feedback")

if st.button("Submit Rating"):
    st.session_state.analytics.add_rating("n50_calculator", rating, feedback)
    st.success("✅ Thank you for your feedback!")
    st.balloons()
