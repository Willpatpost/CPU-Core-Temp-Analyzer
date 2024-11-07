from typing import List, Tuple

def transpose(matrix: List[List[float]]) -> List[List[float]]:
    """
    Transpose a matrix.

    Args:
        matrix: A 2D list representing the matrix.

    Returns:
        Transposed matrix as a 2D list.
    """
    return list(map(list, zip(*matrix)))

def mat_mult(A: List[List[float]], B: List[List[float]]) -> List[List[float]]:
    """
    Multiply two matrices A and B.

    Args:
        A: A 2D list representing matrix A.
        B: A 2D list representing matrix B.

    Returns:
        The product of matrices A and B.
    """
    result = [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]
    return result

def invert_2x2(matrix: List[List[float]]) -> List[List[float]]:
    """
    Invert a 2x2 matrix.

    Args:
        matrix: A 2D list representing a 2x2 matrix.

    Returns:
        The inverse of the 2x2 matrix.
    """
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if det == 0:
        raise ValueError("Matrix is singular and cannot be inverted.")
    return [[matrix[1][1] / det, -matrix[0][1] / det],
            [-matrix[1][0] / det, matrix[0][0] / det]]

def mat_vec_mult(matrix: List[List[float]], vec: List[float]) -> List[float]:
    """
    Multiply a matrix by a vector.

    Args:
        matrix: A 2D list representing the matrix.
        vec: A list representing the vector.

    Returns:
        The product of the matrix and vector.
    """
    return [sum(m * v for m, v in zip(matrix_row, vec)) for matrix_row in matrix]

def least_squares_approximation(x: List[float], y: List[float]) -> Tuple[float, float]:
    """
    Perform a least squares approximation to fit a line y = mx + b to the data using the X^T X | X^T Y method.

    Args:
        x: List of x-coordinates (e.g., time steps).
        y: List of y-coordinates (e.g., temperature values).

    Returns:
        Tuple containing the slope (m) and intercept (b) of the best fit line.
    """
    # Form the design matrix X
    X = [[xi, 1] for xi in x]

    # Compute X^T X
    Xt = transpose(X)
    XtX = mat_mult(Xt, X)

    # Compute X^T Y
    XtY = mat_vec_mult(Xt, y)

    # Invert XtX manually (2x2 matrix inversion)
    XtX_inv = invert_2x2(XtX)

    # Compute beta = XtX_inv * XtY
    beta = mat_vec_mult(XtX_inv, XtY)

    # Return the slope (m) and intercept (b)
    return beta[0], beta[1]
