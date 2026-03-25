from django.shortcuts import render
from django.http import StreamingHttpResponse, JsonResponse
import cv2
import threading
from .detection import process_frame

# ── Shared state ──────────────────────────────────────────────────────────────
_lock = threading.Lock()
_current_status = 'ACTIVE'

def _set_status(s):
    global _current_status
    with _lock:
        _current_status = s

def _get_status():
    with _lock:
        return _current_status

# ── Views ─────────────────────────────────────────────────────────────────────
def index(request):
    return render(request, 'drowsiness/index.html')

def about(request):
    return render(request, 'drowsiness/about.html')

def detect(request):
    return render(request, 'drowsiness/detect.html')

def generate_frames():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while True:
        success, frame = cap.read()
        if not success:
            break

        frame, status = process_frame(frame)
        _set_status(status)

        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            continue

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

    cap.release()
    _set_status('ACTIVE')

def video_feed(request):
    return StreamingHttpResponse(
        generate_frames(),
        content_type='multipart/x-mixed-replace; boundary=frame'
    )

def status(request):
    return JsonResponse({'status': _get_status()})
