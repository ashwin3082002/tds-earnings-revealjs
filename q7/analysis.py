"""
Employee Performance Analysis
Data Analyst: 21f3000426@ds.study.iitm.ac.in

Business Case: Finance Company Employee Performance Analysis
This script analyzes employee performance data across multiple departments and regions
to support strategic workforce planning decisions.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from io import BytesIO

# Load the employee data
print("Loading employee performance data...")
print("Analyst: 21f3000426@ds.study.iitm.ac.in\n")

df = pd.read_csv('employee_data.csv')

print("=" * 60)
print("EMPLOYEE PERFORMANCE ANALYSIS")
print("=" * 60)
print(f"\nTotal Employees: {len(df)}")
print(f"\nFirst 5 rows of data:")
print(df.head())

# Calculate frequency count for IT department
print("\n" + "=" * 60)
print("IT DEPARTMENT ANALYSIS")
print("=" * 60)

it_count = df[df['department'] == 'IT'].shape[0]
print(f"\nFrequency count for IT department: {it_count}")

# Additional IT department statistics
it_dept = df[df['department'] == 'IT']
print(f"\nIT Department Statistics:")
print(f"  - Average Performance Score: {it_dept['performance_score'].mean():.2f}")
print(f"  - Average Years Experience: {it_dept['years_experience'].mean():.2f}")
print(f"  - Average Satisfaction Rating: {it_dept['satisfaction_rating'].mean():.2f}")

# Department distribution analysis
print("\n" + "=" * 60)
print("DEPARTMENT DISTRIBUTION")
print("=" * 60)
dept_counts = df['department'].value_counts()
print("\nFrequency count by department:")
print(dept_counts)

# Create histogram showing distribution of departments
print("\n" + "=" * 60)
print("GENERATING VISUALIZATION")
print("=" * 60)

# Set style
sns.set_style("whitegrid")
plt.figure(figsize=(12, 6))

# Create histogram
dept_counts.plot(kind='bar', color='#3498db', edgecolor='black', alpha=0.7)
plt.title('Employee Distribution Across Departments\nFinance Company - Workforce Analysis', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Department', fontsize=12, fontweight='bold')
plt.ylabel('Number of Employees', fontsize=12, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', alpha=0.3)

# Add value labels on bars
for i, v in enumerate(dept_counts):
    plt.text(i, v + 0.5, str(v), ha='center', va='bottom', fontweight='bold')

# Add footer
plt.text(0.99, 0.01, '21f3000426@ds.study.iitm.ac.in', 
         transform=plt.gca().transAxes, fontsize=8, alpha=0.6,
         ha='right', va='bottom')

plt.tight_layout()

# Save the plot
plt.savefig('department_distribution.png', dpi=100, bbox_inches='tight')
print("\n✓ Visualization saved as 'department_distribution.png'")

# Show the plot
plt.show()

print("\n" + "=" * 60)
print("ANALYSIS COMPLETE")
print("=" * 60)
print(f"\nKey Findings:")
print(f"1. IT department has {it_count} employees (largest department)")
print(f"2. Total departments analyzed: {df['department'].nunique()}")
print(f"3. Regions covered: {df['region'].nunique()}")
print(f"\nReport prepared by: 21f3000426@ds.study.iitm.ac.in")
