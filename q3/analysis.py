import marimo

__generated_with = "0.9.14"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    import numpy as np
    import pandas as pd
    import plotly.express as px
    
    # Author: 21f3000426@ds.study.iitm.ac.in
    # This cell imports all required libraries for data analysis
    return mo, np, pd, px


@app.cell
def __(mo):
    # Interactive slider widget to control sample size
    # This creates a dependency that other cells will use
    sample_size_slider = mo.ui.slider(
        start=10,
        stop=1000,
        step=10,
        value=100,
        label="Sample Size"
    )
    sample_size_slider
    return sample_size_slider,


@app.cell
def __(np, pd, sample_size_slider):
    # Generate synthetic dataset based on slider value
    # This cell depends on sample_size_slider from the previous cell
    sample_size = sample_size_slider.value
    
    np.random.seed(42)
    data = pd.DataFrame({
        'x': np.random.randn(sample_size),
        'y': np.random.randn(sample_size) * 2 + 1,
        'category': np.random.choice(['A', 'B', 'C'], sample_size)
    })
    
    # Calculate correlation between x and y
    correlation = data['x'].corr(data['y'])
    return correlation, data, sample_size


@app.cell
def __(mo, sample_size, correlation):
    # Dynamic markdown output that changes based on widget state
    # This cell depends on both sample_size and correlation variables
    mo.md(f"""
    ## Data Analysis Results
    
    **Current Sample Size:** {sample_size}
    
    **Correlation Coefficient:** {correlation:.4f}
    
    The dataset contains {sample_size} observations. 
    {'Strong' if abs(correlation) > 0.5 else 'Weak'} correlation detected between variables x and y.
    
    Adjust the slider above to see how sample size affects the analysis.
    """)
    return


@app.cell
def __(data, px):
    # Visualization of the relationship between variables
    # This cell depends on the data variable from cell 3
    fig = px.scatter(
        data,
        x='x',
        y='y',
        color='category',
        title='Relationship between X and Y variables',
        labels={'x': 'Variable X', 'y': 'Variable Y'}
    )
    fig
    return fig,


@app.cell
def __(data, mo):
    # Summary statistics table
    # This cell also depends on data, showing cell dependencies
    summary_stats = data.describe()
    
    mo.md(f"""
    ### Summary Statistics
    
    {mo.as_html(summary_stats)}
    
    ---
    
    *Analysis by: 21f3000426@ds.study.iitm.ac.in*
    """)
    return summary_stats,


if __name__ == "__main__":
    app.run()
