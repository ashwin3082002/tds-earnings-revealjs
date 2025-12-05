import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import pandas as pd
import numpy as np
from PIL import Image

# Author: 21f3000426@ds.study.iitm.ac.in
# This script generates an Alluvial Diagram for customer journey flow analysis

# Load the customer journey data
data = pd.read_csv('customer_journey_data.csv')

# Create figure with white background
fig, ax = plt.subplots(figsize=(8, 8), dpi=64, facecolor='white')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')
ax.set_facecolor('white')

# Title
ax.text(5, 9.5, 'Customer Journey Flow: Alluvial Diagram', 
        ha='center', va='top', fontsize=18, fontweight='bold', color='#2C3E50')
ax.text(5, 9.1, 'Channel → Journey Stage Flow Analysis', 
        ha='center', va='top', fontsize=12, color='#5D6D7E')

# Define positions for source (left) and target (right) nodes
sources = data['source'].unique()
targets = data['target'].unique()

# Calculate totals for sizing
source_totals = data.groupby('source')['value'].sum().to_dict()
target_totals = data.groupby('target')['value'].sum().to_dict()

# Color scheme
colors = {
    'Social Media': '#FF6B6B',
    'Search Engine': '#4ECDC4',
    'Email Marketing': '#45B7D1',
    'Display Ads': '#FFA07A',
    'Direct Traffic': '#98D8C8',
    'Referral': '#F7DC6F',
    'Content Marketing': '#BB8FCE',
    'Organic Search': '#85C1E2'
}

target_colors = {
    'Awareness': '#E8F5E9',
    'Consideration': '#FFF3E0',
    'Interest': '#E3F2FD',
    'Purchase': '#C8E6C9'
}

# Position sources on left (x=1-2)
y_pos = 7.5
source_positions = {}
for source in sources:
    size = source_totals[source] / 100  # Scale down
    source_positions[source] = (1.5, y_pos)
    
    # Draw source node
    rect = FancyBboxPatch((0.8, y_pos - size/2), 1.4, size,
                           boxstyle="round,pad=0.05",
                           facecolor=colors.get(source, '#95A5A6'),
                           edgecolor='white', linewidth=2, alpha=0.8)
    ax.add_patch(rect)
    
    # Add label
    ax.text(0.6, y_pos, source, ha='right', va='center', fontsize=9, fontweight='bold')
    ax.text(2.3, y_pos, f'{int(source_totals[source])}', ha='left', va='center', 
            fontsize=8, alpha=0.7)
    
    y_pos -= (size + 0.3)

# Position targets on right (x=8-9)
y_pos = 7.5
target_positions = {}
for target in targets:
    size = target_totals[target] / 100  # Scale down
    target_positions[target] = (8.5, y_pos)
    
    # Draw target node
    rect = FancyBboxPatch((7.8, y_pos - size/2), 1.4, size,
                           boxstyle="round,pad=0.05",
                           facecolor=target_colors.get(target, '#BDC3C7'),
                           edgecolor='white', linewidth=2, alpha=0.8)
    ax.add_patch(rect)
    
    # Add label
    ax.text(9.4, y_pos, target, ha='left', va='center', fontsize=9, fontweight='bold')
    ax.text(7.6, y_pos, f'{int(target_totals[target])}', ha='right', va='center', 
            fontsize=8, alpha=0.7)
    
    y_pos -= (size + 0.3)

# Draw flows (alluvial connections)
for _, row in data.iterrows():
    source = row['source']
    target = row['target']
    value = row['value']
    
    if source in source_positions and target in target_positions:
        x1, y1 = source_positions[source]
        x2, y2 = target_positions[target]
        
        # Create curved connection (Bezier-like)
        width = value / 150  # Scale width based on value
        
        # Draw flow ribbon
        from matplotlib.path import Path
        verts = [
            (x1 + 0.7, y1),  # Start
            (x1 + 3, y1),     # Control 1
            (x2 - 3, y2),     # Control 2
            (x2 - 0.7, y2),   # End
        ]
        
        codes = [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4]
        path = Path(verts, codes)
        patch = mpatches.PathPatch(path, facecolor='none',
                                   edgecolor=colors.get(source, '#95A5A6'),
                                   linewidth=width, alpha=0.3)
        ax.add_patch(patch)

# Add footer
ax.text(5, 0.3, '21f3000426@ds.study.iitm.ac.in', 
        ha='center', va='bottom', fontsize=8, alpha=0.6)

# Legend
ax.text(0.8, 8.8, 'Channels', ha='left', fontsize=10, fontweight='bold', color='#2C3E50')
ax.text(7.8, 8.8, 'Journey Stages', ha='left', fontsize=10, fontweight='bold', color='#2C3E50')

plt.tight_layout()

# Save as temporary file first
plt.savefig('temp_chart.png', dpi=64, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
plt.close()

# Ensure exact dimensions using PIL (within 300-512px range)
img = Image.open('temp_chart.png')
target_size = (512, 512)
img_resized = img.resize(target_size, Image.Resampling.LANCZOS)
img_resized.save('chart.png', 'PNG')

# Clean up temp file
import os
if os.path.exists('temp_chart.png'):
    os.remove('temp_chart.png')

# Verify dimensions
final_img = Image.open('chart.png')
print(f"Chart generated successfully!")
print(f"Image dimensions: {final_img.size}")
print(f"Format: {final_img.format}")
print(f"\nCustomer Journey Flow Statistics:")
print(data.groupby('target')['value'].sum().sort_values(ascending=False))

assert final_img.size[0] >= 300 and final_img.size[0] <= 512, "Width must be 300-512px"
assert final_img.size[1] >= 300 and final_img.size[1] <= 512, "Height must be 300-512px"
print("\n✓ Dimensions validated: 300-512px range")
print("✓ Alluvial diagram generated successfully!")
