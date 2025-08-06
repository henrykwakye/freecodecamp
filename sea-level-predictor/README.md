# Sea Level Predictor

This project uses linear regression to predict sea level rise through the year 2050 based on historical sea level data from 1880 to 2014.

## Overview

The Sea Level Predictor creates a scatter plot with two lines of best fit:
1. **Full Dataset Trend** (1880-2014): Overall long-term sea level trend
2. **Recent Trend** (2000-2014): Accelerated trend from recent decades

The visualization extrapolates both trends to predict sea levels through 2050, demonstrating the difference between historical and recent rates of change.

## Dataset

**File**: `epa-sea-level.csv`
**Source**: EPA - Global Average Absolute Sea Level Change
**Period**: 1880-2014 (134 years of data)
**Unit**: Sea level in inches relative to baseline
**Frequency**: Annual measurements

## Technical Implementation

### Linear Regression Analysis
- **scipy.stats.linregress**: Calculates slope, intercept, and correlation
- **Full period model**: Uses all data from 1880-2014
- **Recent period model**: Uses data from 2000-2014 only
- **Prediction range**: Extends both models to 2050

### Visualization Features
- **Scatter plot**: Original data points showing historical measurements
- **Trend line 1**: Red line showing full dataset trend (1880-2050)
- **Trend line 2**: Green line showing recent trend (2000-2050)
- **Future projection**: Both lines extended 36 years into the future

## Key Function

```python
def draw_plot():
    """
    Creates scatter plot with two regression lines:
    - Red line: Linear regression using all data (1880-2014)
    - Green line: Linear regression using data from 2000 onwards
    Both lines predict sea level rise through 2050
    """
```

## Scientific Insights

The dual regression approach reveals:
- **Historical trend**: Gradual sea level rise over 134+ years
- **Recent acceleration**: Steeper rate of increase since 2000
- **Climate change impact**: Visual evidence of accelerating sea level rise
- **Future projections**: Two different scenarios based on historical vs. recent trends

## Usage

```python
import sea_level_predictor

# Generate prediction visualization
fig = sea_level_predictor.draw_plot()
```

## Generated Output

- `sea_level_plot.png` - Scatter plot with dual regression lines
- Clear visualization showing:
  - Historical data points (1880-2014)
  - Full dataset trend line (red)
  - Recent trend line (green) 
  - Predictions through 2050

## Statistical Results

The analysis provides:
- **Correlation coefficients** for both time periods
- **Rate of change** (inches per year) for each trend
- **Projected sea levels** for 2050 under both scenarios
- **Visual comparison** of historical vs. accelerated trends

## Files

- `sea_level_predictor.py` - Main prediction script
- `analysis.ipynb` - Jupyter notebook with detailed analysis
- `epa-sea-level.csv` - Historical sea level dataset
- `sea_level_plot.png` - Generated visualization

This project demonstrates proficiency in:
- **Linear regression modeling** with scipy
- **Scientific data visualization** 
- **Predictive modeling** and extrapolation
- **Climate data analysis** and interpretation
- **Trend analysis** and comparative modeling
