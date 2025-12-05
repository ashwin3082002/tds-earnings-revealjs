"""
Manufacturing Performance Analysis - Equipment Efficiency Rate
Analyst: 21f3000426@ds.study.iitm.ac.in

Business Case: Manufacturing company needs to understand declining equipment 
efficiency and develop strategies to reach industry benchmark of 90.

This analysis examines Q1-Q4 2024 quarterly performance data.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set visualization style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

print("=" * 70)
print("MANUFACTURING PERFORMANCE ANALYSIS")
print("Equipment Efficiency Rate - 2024 Quarterly Report")
print("=" * 70)
print(f"Analyst: 21f3000426@ds.study.iitm.ac.in\n")

# Define the quarterly data
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
efficiency_rates = [76.99, 77.64, 76.55, 76.11]
industry_target = 90

# Create DataFrame
data = pd.DataFrame({
    'Quarter': quarters,
    'Efficiency_Rate': efficiency_rates
})

# Calculate key metrics
average_efficiency = np.mean(efficiency_rates)
max_efficiency = np.max(efficiency_rates)
min_efficiency = np.min(efficiency_rates)
trend_change = efficiency_rates[-1] - efficiency_rates[0]
gap_to_target = industry_target - average_efficiency

print("KEY METRICS:")
print("-" * 70)
print(f"Average Efficiency Rate (2024):     {average_efficiency:.2f}")
print(f"Industry Target:                     {industry_target}")
print(f"Gap to Target:                       {gap_to_target:.2f} points")
print(f"Maximum Quarter (Q2):                {max_efficiency:.2f}")
print(f"Minimum Quarter (Q4):                {min_efficiency:.2f}")
print(f"Year-over-Year Trend:                {trend_change:.2f} (Declining)")
print(f"Performance vs Target:               {(average_efficiency/industry_target*100):.1f}%")

# Statistical analysis
std_dev = np.std(efficiency_rates)
variance = np.var(efficiency_rates)

print("\nSTATISTICAL ANALYSIS:")
print("-" * 70)
print(f"Standard Deviation:                  {std_dev:.2f}")
print(f"Variance:                            {variance:.2f}")
print(f"Coefficient of Variation:            {(std_dev/average_efficiency*100):.2f}%")

# Trend analysis
if trend_change < 0:
    trend_direction = "DECLINING"
    concern_level = "HIGH CONCERN"
else:
    trend_direction = "IMPROVING"
    concern_level = "MODERATE"

print(f"\nTrend Direction:                     {trend_direction}")
print(f"Concern Level:                       {concern_level}")

# Create comprehensive visualization
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Manufacturing Equipment Efficiency Analysis - 2024\nAnalyst: 21f3000426@ds.study.iitm.ac.in', 
             fontsize=16, fontweight='bold', y=0.995)

# 1. Quarterly Trend Line
ax1 = axes[0, 0]
ax1.plot(quarters, efficiency_rates, marker='o', linewidth=3, markersize=10, 
         color='#e74c3c', label='Actual Performance')
ax1.axhline(y=industry_target, color='#27ae60', linestyle='--', linewidth=2, 
            label=f'Industry Target ({industry_target})')
ax1.axhline(y=average_efficiency, color='#f39c12', linestyle=':', linewidth=2, 
            label=f'2024 Average ({average_efficiency:.2f})')
ax1.fill_between(range(len(quarters)), efficiency_rates, industry_target, 
                  alpha=0.2, color='red', label='Performance Gap')
ax1.set_xlabel('Quarter', fontweight='bold', fontsize=11)
ax1.set_ylabel('Efficiency Rate', fontweight='bold', fontsize=11)
ax1.set_title('Quarterly Efficiency Trend vs Target', fontweight='bold', fontsize=12)
ax1.legend(loc='best')
ax1.grid(True, alpha=0.3)
for i, v in enumerate(efficiency_rates):
    ax1.text(i, v-1.5, f'{v:.2f}', ha='center', fontweight='bold', fontsize=9)

# 2. Bar Chart Comparison
ax2 = axes[0, 1]
bars = ax2.bar(quarters, efficiency_rates, color=['#e74c3c' if x < industry_target else '#27ae60' 
                                                    for x in efficiency_rates], 
               edgecolor='black', linewidth=1.5, alpha=0.8)
ax2.axhline(y=industry_target, color='#27ae60', linestyle='--', linewidth=2, 
            label=f'Target: {industry_target}')
ax2.set_xlabel('Quarter', fontweight='bold', fontsize=11)
ax2.set_ylabel('Efficiency Rate', fontweight='bold', fontsize=11)
ax2.set_title('Quarterly Performance vs Industry Benchmark', fontweight='bold', fontsize=12)
ax2.legend()
ax2.grid(True, alpha=0.3, axis='y')
for bar, val in zip(bars, efficiency_rates):
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height + 0.5,
             f'{val:.2f}', ha='center', va='bottom', fontweight='bold', fontsize=10)

# 3. Gap Analysis
ax3 = axes[1, 0]
gaps = [industry_target - x for x in efficiency_rates]
colors_gap = ['#c0392b' if g > 13 else '#e67e22' if g > 12 else '#f39c12' for g in gaps]
ax3.barh(quarters, gaps, color=colors_gap, edgecolor='black', linewidth=1.5, alpha=0.8)
ax3.set_xlabel('Gap to Target (points)', fontweight='bold', fontsize=11)
ax3.set_ylabel('Quarter', fontweight='bold', fontsize=11)
ax3.set_title('Efficiency Gap to Industry Target', fontweight='bold', fontsize=12)
ax3.grid(True, alpha=0.3, axis='x')
for i, (q, g) in enumerate(zip(quarters, gaps)):
    ax3.text(g + 0.2, i, f'{g:.2f}', va='center', fontweight='bold', fontsize=10)

# 4. Performance Distribution
ax4 = axes[1, 1]
categories = ['Current\nAverage\n(76.82)', 'Industry\nTarget\n(90)', 'Gap\n(13.18)']
values = [average_efficiency, industry_target, gap_to_target]
colors_dist = ['#e74c3c', '#27ae60', '#95a5a6']
bars4 = ax4.bar(categories, values, color=colors_dist, edgecolor='black', 
                linewidth=1.5, alpha=0.8)
ax4.set_ylabel('Efficiency Rate / Gap', fontweight='bold', fontsize=11)
ax4.set_title('Performance Summary: Current vs Target', fontweight='bold', fontsize=12)
ax4.grid(True, alpha=0.3, axis='y')
for bar, val in zip(bars4, values):
    height = bar.get_height()
    ax4.text(bar.get_x() + bar.get_width()/2., height + 1,
             f'{val:.2f}', ha='center', va='bottom', fontweight='bold', fontsize=11)

plt.tight_layout()
plt.savefig('equipment_efficiency_analysis.png', dpi=150, bbox_inches='tight')
print("\n" + "=" * 70)
print("✓ Visualization saved: equipment_efficiency_analysis.png")
print("=" * 70)

# Generate recommendations
print("\nKEY FINDINGS:")
print("-" * 70)
print("1. Performance is consistently 13-14 points below industry target")
print("2. Declining trend from Q2 (77.64) to Q4 (76.11)")
print("3. No quarter achieved even 80% efficiency")
print("4. Current performance is only 85.4% of industry benchmark")

print("\nBUSINESS IMPLICATIONS:")
print("-" * 70)
print("• Increased downtime leading to production delays")
print("• Higher maintenance costs due to reactive repairs")
print("• Potential revenue loss from inefficient operations")
print("• Competitive disadvantage vs industry peers")
print("• Risk of equipment failures and safety concerns")

print("\nRECOMMENDED SOLUTION:")
print("-" * 70)
print("★ IMPLEMENT PREDICTIVE MAINTENANCE PROGRAM ★")
print("\nExpected Benefits:")
print("  • Reduce unplanned downtime by 30-50%")
print("  • Increase equipment efficiency by 10-15 points")
print("  • Lower maintenance costs by 25-30%")
print("  • Extend equipment lifespan")
print("  • Achieve industry target of 90 within 12-18 months")

print("\nImplementation Roadmap:")
print("  1. Install IoT sensors for real-time monitoring")
print("  2. Deploy ML models for failure prediction")
print("  3. Establish preventive maintenance schedules")
print("  4. Train staff on predictive analytics tools")
print("  5. Set up performance dashboards and alerts")

print("\n" + "=" * 70)
print("Report Generated By: 21f3000426@ds.study.iitm.ac.in")
print("=" * 70)

# Save data to CSV
data.to_csv('quarterly_efficiency_data.csv', index=False)
print("\n✓ Data saved: quarterly_efficiency_data.csv")
print("✓ Analysis complete!")
