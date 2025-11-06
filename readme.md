```markdown
# 🎵 MoodTune AI (Emotion-Based Music Player)

MoodTune AI is a desktop application that detects a user's **facial emotion** using a real-time webcam feed and automatically plays music from mood-based playlists.

It combines computer vision, deep learning (ONNX), audio control, and a modern GUI to create an adaptive, personalized music experience.

---

## ✨ Features

✅ Live emotion detection  
✅ Real-time computer vision  
✅ Mood-based music playlists  
✅ Play / Pause / Resume / Next / Stop  
✅ Volume slider  
✅ Dark/Light theme toggle  
✅ Replay last detected mood  
✅ Clean UI  
✅ Debug logs for troubleshooting  

Supported emotions:
- Happy
- Sad
- Angry
- Neutral
- Fear
- Surprise

---

## 🧠 AI Model (ONNX)

The real-time emotion classifier was trained using:
- PyTorch
- FER-2013 dataset
- Exported to ONNX format

Inference runs on CPU using **onnxruntime**.

---

## 🖥 Tech Stack

| Component | Technology |
|----------|------------|
| GUI | CustomTkinter |
| AI Inference | ONNX Runtime |
| Computer Vision | MediaPipe FaceMesh |
| Audio Playback | Pygame Mixer |
| Dataset | FER-2013 |

---

## 📁 Folder Structure

```

moodtune/
│
├─ app.py                  # Main UI application
├─ mood.py                 # ONNX inference / vision logic
├─ player.py               # Music playback manager
│
├─ models/
│    └─ emotion.onnx       # AI model
│
├─ data/
│    └─ songs/
│         ├─ angry/
│         ├─ happy/
│         ├─ sad/
│         ├─ neutral/
│         ├─ fearful/
│         └─ surprised/
│
└─ assets/                 # (optional) images/icons

````

---

## 🚀 Installation

### 1. Clone repository
```bash
git clone https://github.com/your-username/moodtune.git
cd moodtune
````

### 2. Create virtual environment (recommended)

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

### 3. Install required packages

```bash
pip install -r requirements.txt
```

**Example requirements.txt**

```
customtkinter
opencv-python
mediapipe
pygame
onnxruntime
numpy
```

---

## ▶️ Run the program

```bash
python app.py
```

---

## 🎶 Add your music

Place `.mp3`, `.wav`, or `.ogg` files into:

```
data/songs/happy
data/songs/angry
data/songs/sad
...
```

Playlists are mood-based.

---

## 🧩 How It Works

1. Webcam detects a face
2. MediaPipe extracts facial landmarks
3. ONNX model predicts emotion
4. App selects corresponding folder
5. Random playlist begins
6. You can control playback freely

---

## 🎛 Controls

* 🎥 Detect & Play
* 🔁 Play Again
* ⏸ Pause
* ▶ Resume
* ⏭ Next Song
* ⛔ Stop
* 🔊 Volume Slider
* 🌓 Theme Toggle
* 🚪 Exit

---

## 🌓 Theme Support

* Default: Dark
* Toggle to Light anytime

---

## 📌 Logs (console)

Terminal logs help with troubleshooting:

```
[DEBUG] Model predicted mood: happy
[DEBUG] Folder resolved: data/songs/happy
[DEBUG] Files: [...]
```

---

## 🧭 Roadmap

Future planned upgrades:

* Face login
* Mood history database
* Analytics charts
* Personalized recommendations
* Song rating preferences
* Animated UI transitions
* Packaged EXE build

---

## 🏁 Build Windows Executable (optional)

```bash
pip install pyinstaller
pyinstaller --noconsole --onefile app.py
```

Executable will appear in `dist/`.

---

## 🤝 Contributing

Pull requests are welcome!
Feel free to improve UI, playlist logic, or AI accuracy.

---

## 📜 License

MIT License
Free for personal and commercial use.

---

## ⭐ Support

If you like this project, please ⭐ it on GitHub!

```

---

✅ That’s it — professional, clean, GitHub-ready.  
Just paste into `README.md` and push.

Want badges + GIF preview?  
Reply:

> add badges and preview GIF

Happy shipping! 🚀
```
