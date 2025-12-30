"""
📈 Analytics Dashboard
Public statistics and community feedback
"""

import streamlit as st
from analytics import Analytics
from utils.visualizations import create_bar_chart, create_rating_distribution_chart
from datetime import datetime

# Initialize analytics
if 'analytics' not in st.session_state:
    st.session_state.analytics = Analytics()


# Apply shared styling
from utils.shared_styling import apply_common_styling
apply_common_styling()

st.set_page_config(page_title="Analytics Dashboard", page_icon="📈", layout="wide")

# Header
st.title("📈 Community Analytics Dashboard")
st.markdown("Real-time statistics and feedback from the community")

st.markdown("---")

# Get overall stats
overall_stats = st.session_state.analytics.get_overall_stats()

# Key Metrics
st.markdown("## 🎯 Key Metrics")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("👥 Total Visits", f"{overall_stats['total_visits']:,}")

with col2:
    st.metric("🔬 Total Analyses", f"{overall_stats['total_analyses']:,}")

with col3:
    avg_rating = overall_stats['average_rating']
    stars = "⭐" * int(round(avg_rating)) if avg_rating > 0 else "—"
    st.metric("Average Rating", f"{avg_rating:.2f} {stars}")

with col4:
    st.metric("💬 Feedback Items", f"{overall_stats['total_feedback']:,}")

# Last updated
if st.session_state.analytics.data.get("last_updated"):
    last_updated = datetime.fromisoformat(st.session_state.analytics.data["last_updated"])
    st.caption(f"Last updated: {last_updated.strftime('%Y-%m-%d %H:%M:%S')}")

st.markdown("---")

# Feature Usage Distribution
st.markdown("## 📊 Feature Usage")

usage_data = st.session_state.analytics.get_feature_usage_distribution()

if any(usage_data.values()):
    col1, col2 = st.columns([2, 1])
    
    with col1:
        fig = create_bar_chart(
            usage_data,
            "Analyses by Feature",
            "Feature",
            "Number of Analyses"
        )
        st.plotly_chart(fig, width='stretch')
    
    with col2:
        st.markdown("### Most Popular")
        most_popular = st.session_state.analytics.get_most_popular_feature()
        st.success(f"🏆 **{most_popular}**")
        
        st.markdown("### Feature Rankings")
        sorted_usage = sorted(usage_data.items(), key=lambda x: x[1], reverse=True)
        for idx, (feature, count) in enumerate(sorted_usage, 1):
            if count > 0:
                st.write(f"{idx}. **{feature}**: {count} uses")
else:
    st.info("📊 No usage data yet. Be the first to try our analysis tools!")

st.markdown("---")

# Ratings Analysis
st.markdown("## ⭐ Ratings Analysis")

# Collect all ratings
all_ratings = []
for feature_data in st.session_state.analytics.data["features"].values():
    all_ratings.extend([r["rating"] for r in feature_data["ratings"]])

if all_ratings:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        fig = create_rating_distribution_chart(all_ratings)
        if fig:
            st.plotly_chart(fig, width='stretch')
    
    with col2:
        st.markdown("### Rating Statistics")
        avg_rating = sum(all_ratings) / len(all_ratings)
        st.metric("Average", f"{avg_rating:.2f} ⭐")
        st.metric("Total Ratings", len(all_ratings))
        
        # Count by stars
        st.markdown("**Distribution:**")
        for stars in range(5, 0, -1):
            count = all_ratings.count(stars)
            percentage = (count / len(all_ratings) * 100) if all_ratings else 0
            st.write(f"{'⭐' * stars} {count} ({percentage:.0f}%)")
else:
    st.info("⭐ No ratings yet. Help us improve by rating our features!")

st.markdown("---")

# Feature-Specific Stats
st.markdown("## 🔬 Feature-Specific Statistics")

feature_names = {
    "atp_hydrolysis": "🧪 ATP Hydrolysis",
    "dna_analysis": "🧬 DNA Analysis",
    "advanced_analysis": "🔬 Advanced Analysis",
    "n50_calculator": "📊 N50 Calculator"
}

cols = st.columns(2)

for idx, (feature_key, feature_name) in enumerate(feature_names.items()):
    with cols[idx % 2]:
        stats = st.session_state.analytics.get_feature_stats(feature_key)
        
        with st.container():
            st.markdown(f"### {feature_name}")
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Uses", f"{stats.get('count', 0)}")
            with col2:
                avg = stats.get('average_rating', 0)
                st.metric("Avg Rating", f"{avg:.1f} ⭐" if avg > 0 else "—")
            
            if stats.get('total_ratings', 0) > 0:
                st.caption(f"📝 {stats.get('feedback_count', 0)} feedback items")
            
            st.markdown("---")

# Recent Feedback
st.markdown("## 💬 Recent Feedback")

recent_feedback = st.session_state.analytics.get_recent_feedback(limit=10)

if recent_feedback:
    for fb in recent_feedback:
        # Format feature name
        feature_display = feature_names.get(fb['feature'], fb['feature'].replace("_", " ").title())
        
        # Parse timestamp
        try:
            timestamp = datetime.fromisoformat(fb['timestamp'])
            time_str = timestamp.strftime("%Y-%m-%d %H:%M")
        except:
            time_str = "Unknown"
        
        # Create feedback card
        rating_stars = "⭐" * fb.get('rating', 0) if fb.get('rating') else ""
        
        with st.container():
            st.markdown(f"""
            <div style="background: #f0f2f6; padding: 1rem; border-radius: 8px; margin-bottom: 1rem; border-left: 4px solid #667eea;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                    <strong>{feature_display}</strong>
                    <span style="color: #666;">{time_str}</span>
                </div>
                <div style="margin-bottom: 0.5rem;">{rating_stars}</div>
                <div>{fb['text']}</div>
            </div>
            """, unsafe_allow_html=True)
else:
    st.info("💬 No feedback yet. Share your thoughts to help us improve!")

st.markdown("---")

# Community Highlights
st.markdown("## 🌟 Community Highlights")

if overall_stats['total_analyses'] > 0:
    highlights = [
        f"🎉 **{overall_stats['total_analyses']:,} sequences analyzed** by our community!",
        f"📊 **{overall_stats['total_visits']:,} visitors** have explored our tools",
    ]
    
    if overall_stats['average_rating'] >= 4.5:
        highlights.append(f"⭐ **{overall_stats['average_rating']:.1f}/5.0 average rating** - Excellent feedback!")
    elif overall_stats['average_rating'] >= 4.0:
        highlights.append(f"⭐ **{overall_stats['average_rating']:.1f}/5.0 average rating** - Great feedback!")
    
    for highlight in highlights:
        st.success(highlight)

# Milestones
milestones = []
if overall_stats['total_analyses'] >= 100:
    milestones.append("🏆 **100+ Analyses Milestone Reached!**")
if overall_stats['total_visits'] >= 50:
    milestones.append("🎯 **50+ Visitors Milestone Reached!**")
if overall_stats['total_ratings'] >= 20:
    milestones.append("⭐ **20+ Ratings Milestone Reached!**")

if milestones:
    st.markdown("### 🏅 Milestones Achieved")
    for milestone in milestones:
        st.info(milestone)

st.markdown("---")

# Footer
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem;">
    <p>Thank you for being part of our community! 🙏</p>
    <p>Your feedback helps us improve this tool for everyone.</p>
</div>
""", unsafe_allow_html=True)
