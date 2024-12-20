# CPU Core Temperature Analyzer

A Python-based tool for analyzing and visualizing CPU core temperature data. This repository allows users to process temperature data files, perform piecewise linear interpolation, compute least-squares approximations, and generate insightful visualizations for better understanding of core temperature trends.

## Features

- **Data Parsing**: Reads CPU core temperature data from a file and organizes it by time step and core.
- **Piecewise Linear Interpolation**: Provides smooth temperature trends using piecewise linear equations.
- **Least-Squares Approximation**: Fits a best-fit line (`y = mx + b`) for the entire dataset using least-squares regression.
- **Visualization**: Generates plots comparing original data, interpolated data, and least-squares fit for each CPU core.
- **Output Files**: Saves interpolation equations and least-squares equations to core-specific text files.

## Requirements

- Python 3.6+
- Required libraries:
  - `matplotlib`
  - `numpy`

Install the dependencies using:

```bash
pip install -r requirements.txt
