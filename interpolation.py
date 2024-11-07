from typing import List, Tuple
import numpy as np

def piecewise_linear_interpolation(x: List[float], y: List[float], num_points: int = 100) -> Tuple[List[float], List[float], List[Tuple[float, float]]]:
    """
    Perform piecewise linear interpolation and return the equations.

    Args:
        x: List of x-coordinates (e.g., time steps).
        y: List of y-coordinates (e.g., temperature values).
        num_points: Number of points to interpolate between each pair of original points.

    Returns:
        Two lists: new x-coordinates and new y-coordinates with interpolated values.
        List of tuples representing the equations (slope, intercept) of each segment.
    """
    new_x = []
    new_y = []
    equations = []

    for i in range(len(x) - 1):
        x_interp = np.linspace(x[i], x[i+1], num_points)
        y_interp = np.interp(x_interp, [x[i], x[i+1]], [y[i], y[i+1]])

        slope = (y[i+1] - y[i]) / (x[i+1] - x[i])
        intercept = y[i] - slope * x[i]
        equations.append((slope, intercept))

        new_x.extend(x_interp[:-1])  # Avoid duplication of points
        new_y.extend(y_interp[:-1])

    new_x.append(x[-1])
    new_y.append(y[-1])

    return new_x, new_y, equations
