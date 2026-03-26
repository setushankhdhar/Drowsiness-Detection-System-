# 🚗 Driver Drowsiness Detection System

A real-time **Driver Drowsiness Detection System** built using **Python, OpenCV, MediaPipe, and Django**.
The system monitors the driver's eyes through a webcam and detects drowsiness based on eye movement and closure.

---

## 📌 Features

* 🎥 Real-time webcam-based detection
* 👁️ Face and eye landmark detection using MediaPipe
* 😴 Detects eye closure (drowsiness)
* 🚨 Alarm system to alert the driver
* 🌐 Integrated with Django web interface
* ⚡ Fast and lightweight (no heavy ML model required)

---

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS
* **Backend:** Django (Python)
* **Computer Vision:** OpenCV
* **Face Mesh Detection:** MediaPipe
* **Other Tools:** NumPy

---

## ⚙️ How It Works

1. The webcam captures live video feed.
2. MediaPipe Face Mesh detects facial landmarks in real-time.
3. Eye landmarks are extracted from the face mesh.
4. Eye Aspect Ratio (EAR) or similar logic is used to determine if eyes are closed.
5. If eyes remain closed for a defined duration, the system triggers an **alarm**.

---

## 📸 Screenshots

### 🏠 Home Page

![WhatsApp Image 2026-03-26 at 12 56 22 PM](https://github.com/user-attachments/assets/19f782e3-7198-4862-826d-9b066636c081)


### 🎥 Working

![WhatsApp Image 2026-03-26 at 12 56 58 PM](https://github.com/user-attachments/assets/969d9f0d-1ec1-4c71-9bd8-5db0af973451)


### 👁️ Eye Aspect Ratio

![WhatsApp Image 2026-03-26 at 12 57 23 PM](https://github.com/user-attachments/assets/45c17dba-379c-4d0d-818d-fe7fea10997a)


### 😴 Drowsiness Detection

![WhatsApp Image 2026-03-26 at 1 15 13 PM](https://github.com/user-attachments/assets/26fb24ab-b637-4a32-8383-0771e2f38a41)


---

## 🎥 Demo Video

[▶️ Watch Demo]

https://github.com/user-attachments/assets/182a2250-af85-456b-b48e-43628b048959



---

## 📂 Project Structure

```id="g6y3pb"
driver-drowsiness/
│── drowsiness/        # Django app
│── static/            # CSS, JS, images
│── templates/         # HTML templates
│── utils/             # Detection logic
│── manage.py
│── requirements.txt
```

---

## 🚀 Installation & Setup

1. Clone the repository:

```id="1q6s5y"
git clone https://github.com/your-username/driver-drowsiness.git
cd driver-drowsiness
```

2. Create virtual environment:

```id="s0azc0"
python -m venv venv
venv\Scripts\activate   # Windows
```

3. Install dependencies:

```id="6ow6zx"
pip install -r requirements.txt
```

4. Run the server:

```id="b2o3qk"
python manage.py runserver
```

5. Open in browser:

```id="9r6kkd"
http://127.0.0.1:8000/
```

---

## 🧠 Future Improvements

* 📱 Mobile app integration
* 📊 Drowsiness analytics dashboard
* 🌙 Improved night-time detection
* 🚗 Integration with vehicle systems

---

## ⚠️ Note

The system is designed for **real-time webcam input**.
For demonstration purposes, recorded video may be used to simulate real-time conditions.

---

## 🙌 Author

**Setu Shankhdhar**
Python Developer | Machine Learning Enthusiast

---

## ⭐ Contribute

Feel free to fork this repository and improve the project!

---
