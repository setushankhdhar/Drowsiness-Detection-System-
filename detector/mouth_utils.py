import numpy as np

def calculate_MAR(mesh_points, mouth_indices):
    mouth = np.array([mesh_points[p] for p in mouth_indices])

    # mouth[0] = 78  (left corner)
    # mouth[1] = 308 (right corner)
    # mouth[2] = 13  (top inner lip)
    # mouth[3] = 14  (bottom inner lip)
    # mouth[4] = 12  (top outer lip)
    # mouth[5] = 15  (bottom outer lip)

    # Vertical distances
    A = np.linalg.norm(mouth[2] - mouth[3])  # inner lip vertical
    B = np.linalg.norm(mouth[4] - mouth[5])  # outer lip vertical

    # Horizontal distance
    C = np.linalg.norm(mouth[0] - mouth[1])  # corner to corner

    if C == 0:
        return 0.0

    return (A + B) / (2.0 * C)