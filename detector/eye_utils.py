import numpy as np

def calculate_EAR(mesh_points, eye_indices):
    eye = np.array([mesh_points[p] for p in eye_indices])

    # Vertical distances
    A = np.linalg.norm(eye[1] - eye[5])
    B = np.linalg.norm(eye[2] - eye[4])

    # Horizontal distance
    C = np.linalg.norm(eye[0] - eye[3])

    if C == 0:
        return 0.0

    return (A + B) / (2.0 * C)