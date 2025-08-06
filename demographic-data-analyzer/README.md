# Demographic Data Analyzer

This project analyzes demographic data from the 1994 Census database extracted from the UCI Machine Learning Repository.

## Overview

The Demographic Data Analyzer uses pandas to answer specific questions about the census data including:
- Race representation in the dataset
- Average age demographics
- Education statistics and income correlation
- Work hours analysis
- Country demographics and earnings

## Dataset

**File**: `adult.data.csv`
**Source**: 1994 Census database (UCI ML Repository)
**Records**: ~32,000 individuals
**Features**: Age, workclass, education, occupation, race, sex, hours-per-week, native-country, income

## Key Functions

The main function `calculate_demographic_data()` returns a dictionary with answers to:

1. **Race count** - How many people of each race are represented
2. **Average age of men** - Mean age for male individuals  
3. **Percentage with Bachelor's degrees** - Education statistics
4. **Higher education income correlation** - % earning >50K with/without advanced degrees
5. **Work hours analysis** - Min hours worked and % earning >50K
6. **Country statistics** - Rich countries and top earning country demographics

## Usage

```python
from demographic_data_analyzer import calculate_demographic_data

# Get all demographic statistics
stats = calculate_demographic_data(print_data=True)
```

## Sample Output

```
Race count: 
White                 27816
Black                  3124
Asian-Pac-Islander     1039
Amer-Indian-Eskimo      311
Other                   271

Average age of men: 39.4
Percentage with Bachelors degrees: 16.4%
Percentage with higher education that earn >50K: 46.5%
Percentage without higher education that earn >50K: 17.4%
Min work time: 1 hours/week
Percentage of rich among those who work fewest hours: 10.0%
Country with highest percentage of rich: Iran
Highest percentage of rich people in country: 41.9%
Top occupations in India: Prof-specialty
```

## Technical Implementation

- **Data cleaning**: Handles missing values and data type conversions
- **Statistical analysis**: Uses pandas for grouping, filtering, and aggregation
- **Percentage calculations**: Precise calculations with proper rounding
- **Data filtering**: Complex boolean indexing for demographic subsets

## Files

- `demographic_data_analyzer.py` - Main analysis script
- `analysis.ipynb` - Jupyter notebook with detailed exploration
- `adult.data.csv` - Census dataset

This project demonstrates proficiency in pandas data manipulation, statistical analysis, and working with real-world demographic datasets.
