# Mean-Variance-Standard Deviation Calculator

This project implements a statistical calculator that computes mean, variance, standard deviation, maximum, minimum, and sum for 3x3 matrices using NumPy.

## Overview

The calculator takes a list of 9 numbers, converts them into a 3x3 NumPy array, and calculates statistics along different axes:
- **Axis 0**: Column-wise calculations (down the columns)
- **Axis 1**: Row-wise calculations (across the rows)  
- **Flattened**: Calculations for the entire matrix

## Function Specification

```python
def calculate(list):
    """
    Input: List of 9 numbers
    Output: Dictionary with statistical calculations
    Raises: ValueError if list doesn't contain exactly 9 numbers
    """
```

## Statistical Calculations

For each statistic, the function returns three values:
1. **Column-wise** (axis=0): Statistics for each of the 3 columns
2. **Row-wise** (axis=1): Statistics for each of the 3 rows
3. **Overall**: Single value for the entire 3x3 matrix

### Calculated Statistics:
- **Mean**: Average values
- **Variance**: Measure of spread from the mean
- **Standard Deviation**: Square root of variance
- **Maximum**: Largest values
- **Minimum**: Smallest values  
- **Sum**: Total of all values

## Example Usage

```python
from mean_var_std import calculate

# Input: 9 numbers
result = calculate([0,1,2,3,4,5,6,7,8])

# Output: Dictionary with all statistics
{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.6666667, 0.6666667, 0.6666667], 6.666667],
  'standard deviation': [[2.449489, 2.449489, 2.449489], [0.816497, 0.816497, 0.816497], 2.581989],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}
```

## Matrix Representation

Input list `[0,1,2,3,4,5,6,7,8]` becomes:
```
[[0, 1, 2],
 [3, 4, 5], 
 [6, 7, 8]]
```

## Technical Implementation

- **NumPy array reshaping**: `np.array(list).reshape(3, 3)`
- **Axis operations**: Uses `axis=0` and `axis=1` parameters
- **Error handling**: Validates input length before processing
- **List conversion**: Converts NumPy arrays back to Python lists
- **Statistical functions**: Leverages NumPy's optimized mathematical operations

## Key Learning Objectives

This project demonstrates:
- **NumPy fundamentals**: Array creation, reshaping, and manipulation
- **Statistical computing**: Multiple statistical measures in one function
- **Axis operations**: Understanding multi-dimensional array operations
- **Error handling**: Input validation and appropriate exception raising
- **Data structures**: Working with nested lists and dictionaries
- **Mathematical operations**: Mean, variance, standard deviation calculations

## Error Handling

```python
if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
```

The function validates input and raises a descriptive error message for invalid inputs.

## Files

- `mean_var_std.py` - Main calculator function
- `analysis.ipynb` - Jupyter notebook with examples and testing

This project serves as an introduction to NumPy and demonstrates fundamental concepts in:
- Statistical computing
- Array manipulation  
- Multi-dimensional data operations
- Mathematical function implementation
