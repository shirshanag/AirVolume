# Gesture-Based Volume Controller 🎛️✋

Control your system volume using hand gestures in real time with the power of Computer Vision and AI.

This project uses a webcam to detect hand landmarks and dynamically adjust system volume based on the distance between your thumb and index finger.

---

## 🚀 Features

* Real-time hand tracking
* Gesture-based volume control
* Smooth volume adjustment
* Visual feedback with OpenCV
* FPS counter for performance monitoring
* Beginner-friendly computer vision project

---

## 🛠️ Technologies Used

* Python
* OpenCV
* MediaPipe
* NumPy
* Pycaw

Relevant tools:

* OpenCV
* MediaPipe

---

## 📷 How It Works

1. Webcam captures live video.
2. Hand landmarks are detected using MediaPipe.
3. Distance between thumb tip and index finger tip is calculated.
4. The distance is mapped to system volume.
5. Volume changes dynamically based on gesture movement.

---

## 🎮 Gesture Control

| Gesture                          | Action          |
| -------------------------------- | --------------- |
| Thumb and Index Finger Close     | Lower Volume    |
| Thumb and Index Finger Far Apart | Increase Volume |

---

## 📂 Project Structure

```bash
gesture-volume-controller/
│
├── volumecontrol.py
├── requirements.txt
├── README.md
└── Handtrackingmodule.py
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/shirshanag/AirVolume.git
```

Move into the project directory:

```bash
cd AirVolume
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python volumecontrol.py
```

---

## 📦 Requirements

```txt
opencv-python
mediapipe
numpy
pycaw
comtypes
```

---

## 💡 Future Improvements

* Gesture-based mute/unmute
* Multi-hand support
* Brightness control
* Gesture-controlled media player
* Integration with virtual mouse
* Custom gesture mapping

---

## 🧠 Learning Outcomes

This project helped in understanding:

* Computer Vision fundamentals
* Hand landmark detection
* Real-time video processing
* Human-computer interaction
* Gesture recognition systems

---

## 📜 License

This project is open-source and available under the MIT License.
