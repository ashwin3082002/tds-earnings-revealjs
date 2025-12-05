import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image

# Author: 21f3000426@ds.study.iitm.ac.in

# Set Seaborn style for professional appearance
sns.set_style("whitegrid")
sns.set_context("talk")  # Presentation-ready text sizes

# Generate realistic synthetic data for customer purchase amounts by segment
np.random.seed(42)

# Define customer segments with realistic purchase patterns
segments = {
    'Premium': np.random.normal(850, 200, 150),      # High spenders
    'Standard': np.random.normal(450, 120, 200),     # Medium spenders
    'Budget': np.random.normal(180, 60, 180),        # Low spenders
    'VIP': np.random.normal(1200, 300, 100)          # Highest spenders
}

# Create DataFrame in proper format for Seaborn
data_list = []
for segment, amounts in segments.items():
    for amount in amounts:
        data_list.append({
            'Customer Segment': segment,
            'Purchase Amount ($)': max(0, amount)  # Ensure no negative values
        })

df = pd.DataFrame(data_list)

# Create figure with exact dimensions for 512x512 output
plt.figure(figsize=(8, 8))

# Create professional boxplot
ax = sns.boxplot(
    data=df,
    x='Customer Segment',
    y='Purchase Amount ($)',
    palette='Set2',
    order=['Budget', 'Standard', 'Premium', 'VIP']  # Logical ordering
)

# Customize the chart
plt.title('Purchase Amount Distribution by Customer Segment', 
          fontsize=16, 
          fontweight='bold',
          pad=20)
plt.xlabel('Customer Segment', fontsize=14, fontweight='bold')
plt.ylabel('Purchase Amount ($)', fontsize=14, fontweight='bold')

# Add grid for better readability
ax.grid(True, alpha=0.3, axis='y')

# Rotate x-axis labels if needed
plt.xticks(rotation=0)

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Save chart as temporary file first
plt.savefig('temp_chart.png', dpi=64)
plt.close()

# Ensure exact 512x512 dimensions using PIL
img = Image.open('temp_chart.png')
if img.size != (512, 512):
    img = img.resize((512, 512), Image.Resampling.LANCZOS)
img.save('chart.png', 'PNG', optimize=False)

# Clean up temp file
import os
if os.path.exists('temp_chart.png'):
    os.remove('temp_chart.png')

# Verify dimensions
final_img = Image.open('chart.png')
print(f"Final image dimensions: {final_img.size}")
assert final_img.size == (512, 512), "Image is not 512x512!"

print("Chart generated successfully!")
print(f"\nDataset Summary:")
print(f"Total observations: {len(df)}")
print(f"\nPurchase Amount Statistics by Segment:")
print(df.groupby('Customer Segment')['Purchase Amount ($)'].describe())
