# Time Series Visualizer

This project visualizes time series data using line plots, bar charts, and box plots to explore patterns in FreeCodeCamp forum page views from May 2016 to December 2019.

## Overview

The Time Series Visualizer creates three different types of visualizations:
1. **Line Plot** - Daily page views over the entire time period
2. **Bar Chart** - Average monthly page views grouped by year  
3. **Box Plots** - Monthly and yearly distributions showing seasonality and trends

## Dataset

**File**: `fcc-forum-pageviews.csv`
**Period**: May 2016 - December 2019
**Frequency**: Daily page view counts
**Data Cleaning**: Filters out top and bottom 2.5% of values to remove outliers

## Visualization Functions

### 1. `draw_line_plot()`
- Creates a line plot showing daily page views over time
- Highlights overall growth trend and seasonal patterns
- Uses red line with appropriate styling

### 2. `draw_bar_plot()`  
- Groups data by year and month to show average monthly views
- Creates a bar chart with months as categories and years as legend
- Demonstrates clear seasonal patterns and year-over-year growth

### 3. `draw_box_plot()`
- Creates side-by-side box plots for:
  - **Year-wise Box Plot**: Distribution of views by year (2016-2019)
  - **Month-wise Box Plot**: Seasonal patterns across all months
- Shows quartiles, medians, and outliers for detailed distribution analysis

## Technical Features

- **Data preprocessing**: Date parsing and outlier removal (2.5% trim)
- **Advanced plotting**: Custom styling with matplotlib and seaborn
- **Statistical visualization**: Box plots showing quartiles and distributions
- **Time series handling**: Proper date indexing and temporal grouping

## Usage

```python
import time_series_visualizer

# Generate all three visualizations
line_fig = time_series_visualizer.draw_line_plot()
bar_fig = time_series_visualizer.draw_bar_plot()
box_fig = time_series_visualizer.draw_box_plot()
```

## Generated Visualizations

- `line_plot.png` - Daily time series line plot
- `bar_plot.png` - Monthly averages by year  
- `box_plot.png` - Year-wise and month-wise distribution box plots

## Key Insights

The visualizations reveal:
- **Growth trend**: Steady increase in forum activity over time
- **Seasonal patterns**: Consistent monthly variations in page views
- **Yearly progression**: Clear year-over-year growth from 2016-2019
- **Distribution changes**: Evolving patterns in view count distributions

## Files

- `time_series_visualizer.py` - Main visualization script
- `analysis.ipynb` - Jupyter notebook with detailed analysis
- `fcc-forum-pageviews.csv` - Time series dataset
- Generated plot files (PNG format)

This project demonstrates advanced time series visualization techniques, statistical distribution analysis, and professional data presentation skills.
