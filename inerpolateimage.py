import numpy as np
from scipy import interpolate 
def quadratic_b_spline(t):
    """
    Compute the quadratic B-spline basis functions.
    """
    b0 = (1 - t) ** 2 / 2
    b1 = (2 - 2 * t ** 2) / 2
    b2 = t ** 2 / 2
    return np.array([b0, b1, b2])

def interpolate_matrix(input_matrix, out_shape):
    """
    Interpolate a 2D matrix using quadratic B-spline.
    """
    in_m, in_n = input_matrix.shape
    out_m, out_n = out_shape

    # Compute interpolation indices
    x_indices = np.linspace(0, in_n - 1, out_n)
    y_indices = np.linspace(0, in_m - 1, out_m)

    # Initialize output matrix
    output_matrix = np.zeros((out_m, out_n))

    # Interpolate row by row
    for i, y in enumerate(y_indices):
        y_int = int(y)
        t = y - y_int

        # Get basis functions for row interpolation
        basis_y = quadratic_b_spline(t)

        # Interpolate column by column
        for j, x in enumerate(x_indices):
            x_int = int(x)
            t = x - x_int

            # Get basis functions for column interpolation
            basis_x = quadratic_b_spline(t)

            # Compute interpolated value
            for m in range(3):
                for n in range(3):
                    y_idx = y_int + m - 1
                    x_idx = x_int + n - 1
                    if 0 <= y_idx < in_m and 0 <= x_idx < in_n:
                        output_matrix[i, j] += (
                            basis_y[m] * basis_x[n] * input_matrix[y_idx, x_idx]
                        )

    return output_matrix