# Advanced Data Visualization: Alluvial Diagram

**Author:** 21f3000426@ds.study.iitm.ac.in

## Project Overview

This project creates a professional Alluvial Diagram to visualize customer journey flow from awareness to purchase across different marketing channels for Okuneva Feeney and Mills, a strategic consulting firm specializing in advanced data visualization.

## Business Context

A major client required a sophisticated visualization to analyze customer journey flow patterns and conversion funnels across multiple touchpoints. The Alluvial Diagram effectively communicates complex data relationships showing how customers move through different stages of their journey depending on their initial channel.

## Visualization Type

**Alluvial Diagram** - Ideal for visualizing flow and movement between categorical states, making it perfect for customer journey mapping and conversion funnel analysis.

## Data Structure

The analysis includes 20 data points representing customer flows:

### Source Channels:
- Social Media
- Search Engine
- Email Marketing
- Display Ads
- Direct Traffic
- Referral
- Content Marketing
- Organic Search

### Target Journey Stages:
- **Awareness**: 2,250 customers
- **Purchase**: 2,152 customers
- **Interest**: 1,358 customers
- **Consideration**: 964 customers

## Files

- `customer_journey_data.csv` - Source data with 20 flow records
- `generate_chart.py` - Python script to create the alluvial diagram
- `chart.png` - Generated visualization (512x512 pixels)
- `README.md` - This documentation file

## Key Insights

1. **Awareness Dominance**: Most customer touchpoints start at the Awareness stage (2,250)
2. **High Purchase Intent**: Strong flow directly to Purchase stage (2,152) indicates effective channels
3. **Social Media Strength**: Social Media shows strong flows across multiple journey stages
4. **Multi-Stage Engagement**: Email Marketing effectively drives Consideration and Interest stages

## Visualization Features

- **Flow Visualization**: Curved ribbons show customer movement between channels and stages
- **Proportional Sizing**: Node and flow sizes represent relative volume
- **Color Coding**: Distinct colors for each channel for easy identification
- **Professional Styling**: Clean layout suitable for executive presentations
- **Quantitative Labels**: Exact values displayed for each node

## Technical Implementation

- **Visualization Method**: Custom alluvial/flow diagram using matplotlib
- **Dimensions**: 512x512 pixels (within required 300-512px range)
- **Format**: PNG with white background
- **Data Processing**: Pandas for data aggregation and analysis
- **Image Processing**: PIL for exact dimension control

## Usage

Generate the visualization:

```bash
python3 generate_chart.py
```

This will create `chart.png` with the customer journey flow visualization.

## Data Sample

```csv
source,target,value
Social Media,Awareness,450
Social Media,Consideration,357
Social Media,Purchase,469
Search Engine,Awareness,380
Email Marketing,Purchase,425
...
```

## Strategic Value

This visualization enables executives to:
- Understand customer journey patterns
- Identify high-performing channels
- Optimize marketing budget allocation
- Improve conversion funnel efficiency
- Make data-driven strategic decisions

## Contact

21f3000426@ds.study.iitm.ac.in
