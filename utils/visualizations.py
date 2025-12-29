"""
Visualization utilities for the Bioinformatics Web App
"""

import plotly.graph_objects as go
import plotly.express as px
from typing import Dict, List


def create_bar_chart(data: Dict[str, float], title: str, x_label: str, y_label: str):
    """Create a bar chart using Plotly"""
    fig = go.Figure(data=[
        go.Bar(
            x=list(data.keys()),
            y=list(data.values()),
            marker_color='rgb(55, 83, 109)',
            text=list(data.values()),
            textposition='auto',
        )
    ])
    
    fig.update_layout(
        title=title,
        xaxis_title=x_label,
        yaxis_title=y_label,
        template='plotly_white',
        height=400
    )
    
    return fig


def create_pie_chart(data: Dict[str, float], title: str):
    """Create a pie chart using Plotly"""
    fig = go.Figure(data=[
        go.Pie(
            labels=list(data.keys()),
            values=list(data.values()),
            hole=0.3,
            textinfo='label+percent',
        )
    ])
    
    fig.update_layout(
        title=title,
        template='plotly_white',
        height=400
    )
    
    return fig


def create_line_chart(x_data: List, y_data: List, title: str, x_label: str, y_label: str):
    """Create a line chart using Plotly"""
    fig = go.Figure(data=[
        go.Scatter(
            x=x_data,
            y=y_data,
            mode='lines+markers',
            marker=dict(size=8, color='rgb(55, 83, 109)'),
            line=dict(width=2)
        )
    ])
    
    fig.update_layout(
        title=title,
        xaxis_title=x_label,
        yaxis_title=y_label,
        template='plotly_white',
        height=400
    )
    
    return fig


def create_horizontal_bar_chart(data: Dict[str, float], title: str):
    """Create a horizontal bar chart for amino acid frequencies"""
    # Sort by value
    sorted_data = dict(sorted(data.items(), key=lambda x: x[1], reverse=True))
    
    fig = go.Figure(data=[
        go.Bar(
            x=list(sorted_data.values()),
            y=list(sorted_data.keys()),
            orientation='h',
            marker_color='rgb(55, 83, 109)',
            text=[f"{v:.1f}%" for v in sorted_data.values()],
            textposition='auto',
        )
    ])
    
    fig.update_layout(
        title=title,
        xaxis_title="Percentage (%)",
        yaxis_title="Amino Acid",
        template='plotly_white',
        height=600
    )
    
    return fig


def visualize_dna_sequence(sequence: str, max_length: int = 100):
    """Create a colored HTML representation of DNA sequence"""
    colors = {
        'A': '#FF6B6B',  # Red
        'T': '#4ECDC4',  # Cyan
        'G': '#95E1D3',  # Light green
        'C': '#FFE66D',  # Yellow
        'N': '#CCCCCC'   # Gray for unknown
    }
    
    # Truncate if too long
    display_seq = sequence[:max_length]
    truncated = len(sequence) > max_length
    
    html = '<div style="font-family: monospace; font-size: 14px; line-height: 1.6;">'
    
    for i, base in enumerate(display_seq):
        color = colors.get(base.upper(), '#CCCCCC')
        html += f'<span style="background-color: {color}; padding: 2px 4px; margin: 1px; border-radius: 3px;">{base}</span>'
        
        # Add line break every 50 bases
        if (i + 1) % 50 == 0:
            html += '<br>'
    
    if truncated:
        html += '<br><em>... (sequence truncated for display)</em>'
    
    html += '</div>'
    
    return html


def visualize_protein_sequence(sequence: str, hydrophobic_residues: str = "AILMFWYV", max_length: int = 100):
    """Create a colored HTML representation of protein sequence highlighting hydrophobic residues"""
    # Truncate if too long
    display_seq = sequence[:max_length]
    truncated = len(sequence) > max_length
    
    html = '<div style="font-family: monospace; font-size: 14px; line-height: 1.6;">'
    
    for i, aa in enumerate(display_seq):
        if aa.upper() in hydrophobic_residues:
            # Hydrophobic - orange
            html += f'<span style="background-color: #FF9F43; padding: 2px 4px; margin: 1px; border-radius: 3px; color: white; font-weight: bold;">{aa}</span>'
        else:
            # Hydrophilic - blue
            html += f'<span style="background-color: #5F9FE8; padding: 2px 4px; margin: 1px; border-radius: 3px; color: white;">{aa}</span>'
        
        # Add line break every 50 amino acids
        if (i + 1) % 50 == 0:
            html += '<br>'
    
    if truncated:
        html += '<br><em>... (sequence truncated for display)</em>'
    
    html += '</div>'
    html += '<p style="font-size: 12px; margin-top: 10px;"><strong>Legend:</strong> '
    html += '<span style="background-color: #FF9F43; padding: 2px 8px; border-radius: 3px; color: white;">Hydrophobic</span> '
    html += '<span style="background-color: #5F9FE8; padding: 2px 8px; border-radius: 3px; color: white;">Hydrophilic</span></p>'
    
    return html


def create_rating_distribution_chart(ratings: List[int]):
    """Create a histogram of rating distribution"""
    if not ratings:
        return None
    
    # Count ratings
    rating_counts = {i: ratings.count(i) for i in range(1, 6)}
    
    fig = go.Figure(data=[
        go.Bar(
            x=list(rating_counts.keys()),
            y=list(rating_counts.values()),
            marker_color=['#E74C3C', '#E67E22', '#F39C12', '#2ECC71', '#27AE60'],
            text=list(rating_counts.values()),
            textposition='auto',
        )
    ])
    
    fig.update_layout(
        title="Rating Distribution",
        xaxis_title="Stars",
        yaxis_title="Number of Ratings",
        template='plotly_white',
        height=350,
        xaxis=dict(tickmode='linear', tick0=1, dtick=1)
    )
    
    return fig
