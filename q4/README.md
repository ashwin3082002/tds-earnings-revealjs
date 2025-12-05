# Supply Chain Analytics: Correlation Matrix Visualization

**Author:** 21f3000426@ds.study.iitm.ac.in

## Project Overview

This project analyzes supply chain metrics for OptimalFlow Logistics to understand relationships between key performance indicators in supplier management and procurement processes.

## Dataset

The analysis includes 50 procurement transactions with the following metrics:

- **Supplier_Lead_Time**: Days from order placement to delivery
- **Inventory_Levels**: Current stock quantities (units)
- **Order_Frequency**: Number of orders placed per month
- **Delivery_Performance**: On-time delivery rate (%)
- **Cost_Per_Unit**: Unit cost in dollars ($)

## Files

- `correlation.csv` - Correlation matrix values generated from the supply chain dataset
- `heatmap.png` - Visualization of correlation matrix with Red-White-Green color scheme
- `README.md` - This documentation file

## Key Findings

The correlation analysis reveals:

1. **Strong Negative Correlation** between Supplier Lead Time and Delivery Performance (-0.877)
2. **Strong Positive Correlation** between Cost Per Unit and Supplier Lead Time (0.955)
3. **Strong Negative Correlation** between Delivery Performance and Cost Per Unit (-0.901)
4. **Strong Correlation** between Order Frequency and both Delivery Performance (0.739) and Supplier Lead Time (-0.824)

## Analysis Method

1. Loaded supply chain dataset using pandas
2. Generated correlation matrix using `.corr()` method
3. Created heatmap visualization with seaborn using Red-Yellow-Green color palette
4. Exported correlation values to CSV format
5. Saved heatmap as PNG (512x512 pixels)

## Contact

21f3000426@ds.study.iitm.ac.in
