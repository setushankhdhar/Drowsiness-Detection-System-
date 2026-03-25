import cv2
from .eye_utils import calculate_EAR
from .mouth_utils import calculate_MAR
import mediapipe as mp

face_mesh_detector = mp.solutions.face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

EAR_THRESHOLD = 0.25
MAR_THRESHOLD = 0.7

# Number of consecutive frames eyes must be closed to trigger DROWSY
EAR_CONSEC_FRAMES = 15  # ~0.5 seconds at 30fps, adjust as needed

LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]
MOUTH = [78, 308, 13, 14, 12, 15]

# Frame counter for closed eyes
ear_counter = 0

def process_frame(frame):
    global ear_counter

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh_detector.process(rgb_frame)

    status = "ACTIVE"

    if results.multi_face_landmarks:
        mesh_points = [
            (int(lm.x * frame.shape[1]), int(lm.y * frame.shape[0]))
            for lm in results.multi_face_landmarks[0].landmark
        ]

        left_ear = calculate_EAR(mesh_points, LEFT_EYE)
        right_ear = calculate_EAR(mesh_points, RIGHT_EYE)
        ear = (left_ear + right_ear) / 2.0

        mar = calculate_MAR(mesh_points, MOUTH)

        # Increment counter if eyes are closed, reset if open
        if ear < EAR_THRESHOLD:
            ear_counter += 1
        else:
            ear_counter = 0

        # Only trigger DROWSY if eyes have been closed for enough frames
        if ear_counter >= EAR_CONSEC_FRAMES:
            status = "DROWSY"
        elif mar > MAR_THRESHOLD:
            status = "YAWNING"
        else:
            status = "ACTIVE"

        

        # Show EAR and MAR values for debugging
        cv2.putText(frame, f"EAR: {ear:.2f}", (30, 90),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
        cv2.putText(frame, f"MAR: {mar:.2f}", (30, 120),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)

    # Color-coded status text
    color = (0, 255, 0)  # green = ACTIVE
    if status == "DROWSY":
        color = (0, 0, 255)   # red
    elif status == "YAWNING":
        color = (0, 165, 255)  # orange

    cv2.putText(frame, status, (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)

    return frame, status