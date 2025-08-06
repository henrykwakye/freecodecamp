# Medical Data Visualizer

This project analyzes medical examination data and creates visualizations to explore relationships between cardiovascular disease and various health factors.

## Overview

The Medical Data Visualizer analyzes a dataset of medical examinations and creates two main types of visualizations:

1. **Categorical Plot**: Shows the relationship between cardiovascular disease and various health factors (cholesterol, glucose, smoking, alcohol consumption, physical activity, and overweight status)
2. **Correlation Heatmap**: Displays correlations between different medical examination variables

## Files

- `analysis.ipynb` - Jupyter notebook with complete data analysis and visualizations
- `medical_data_visualizer.py` - Main Python script with visualization functions
- `medical_examination.csv` - Medical examination dataset
- `catplot.png` - Generated categorical plot
- `heatmap.png` - Generated correlation heatmap

## Features

### Data Processing
- Adds an overweight column based on BMI calculation
- Normalizes cholesterol and glucose data (0 for normal, 1 for above normal)
- Filters out incorrect data (diastolic pressure higher than systolic, extreme height/weight values)

### Visualizations
1. **Categorical Plot (`draw_cat_plot()`)**: 
   - Uses `sns.catplot()` to create bar charts
   - Shows counts of categorical features split by cardiovascular disease presence
   - Separates data by cardio status (0 = no disease, 1 = disease)

2. **Correlation Heatmap (`draw_heat_map()`)**:
   - Creates a correlation matrix of all numeric variables
   - Uses a triangular mask to show only upper triangle
   - Applies data cleaning to remove outliers

## Requirements

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
```

## Usage

### Running the Jupyter Notebook
Open `analysis.ipynb` in Jupyter Notebook or VS Code and run all cells to:
- Load and explore the data
- Generate visualizations
- Save plots as PNG files

### Running the Python Script
```python
python medical_data_visualizer.py
```

## Data Description

The dataset includes the following features:
- **Age**: Age in days
- **Height**: Height in cm
- **Weight**: Weight in kg
- **Gender**: Gender (1 = women, 2 = men)
- **Systolic BP**: Systolic blood pressure
- **Diastolic BP**: Diastolic blood pressure
- **Cholesterol**: Cholesterol level (1 = normal, 2 = above normal, 3 = well above normal)
- **Glucose**: Glucose level (1 = normal, 2 = above normal, 3 = well above normal)
- **Smoking**: Smoking status (0 = no, 1 = yes)
- **Alcohol**: Alcohol consumption (0 = no, 1 = yes)
- **Physical Activity**: Physical activity (0 = no, 1 = yes)
- **Cardiovascular Disease**: Target variable (0 = no, 1 = yes)

## Key Insights

The analysis reveals correlations between cardiovascular disease and:
- Overweight status (higher BMI)
- Cholesterol levels
- Blood pressure readings
- Age factors

## License

This project is open source and available under the MIT License.
