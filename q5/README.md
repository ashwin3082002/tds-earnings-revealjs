# Customer Analytics: Purchase Amount Distribution by Customer Segment

**Author:** 21f3000426@ds.study.iitm.ac.in

## Project Overview

This project visualizes the distribution of purchase amounts across different customer segments for Champlin Inc, providing actionable insights for executive decision-making and strategic planning.

## Business Context

A major retail client required a professional, publication-ready visualization to analyze customer spending behavior across segments. This analysis supports quarterly business reviews, executive presentations, board reports, and strategic planning documents.

## Customer Segments Analyzed

- **Budget**: Low-spending customers (avg ~$178)
- **Standard**: Medium-spending customers (avg ~$457)
- **Premium**: High-spending customers (avg ~$833)
- **VIP**: Highest-spending customers (avg ~$1,218)

## Files

- `chart.py` - Python script using Seaborn to generate the boxplot visualization
- `chart.png` - Generated chart image (512x512 pixels)
- `README.md` - This documentation file

## Key Insights

1. **Clear Segmentation**: Distinct purchase amount distributions across all four customer segments
2. **VIP Segment**: Highest average spend with widest variation, indicating diverse purchase patterns
3. **Budget Segment**: Most consistent spending behavior with lowest variation
4. **Premium vs Standard**: Clear differentiation with Premium customers spending ~80% more on average

## Technical Implementation

- **Library**: Seaborn with matplotlib backend
- **Chart Type**: Boxplot (sns.boxplot)
- **Styling**: Professional whitegrid theme with presentation-ready context
- **Color Palette**: Set2 for clear segment differentiation
- **Dimensions**: 512x512 pixels (8x8 inches at 64 DPI)

## Data Statistics

- **Total Observations**: 630 customer transactions
- **Budget Segment**: 180 observations
- **Standard Segment**: 200 observations
- **Premium Segment**: 150 observations
- **VIP Segment**: 100 observations

## Usage

```bash
python3 chart.py
```

This will generate `chart.png` with the purchase amount distribution visualization.

## Contact

21f3000426@ds.study.iitm.ac.in
