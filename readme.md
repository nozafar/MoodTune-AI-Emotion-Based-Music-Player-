```markdown
# 🎵 MoodTune AI — Emotion Based Music Player(DATA INCLUDED FOR TRAINING)

MoodTune AI is a desktop application that detects a user's **facial emotion** in real-time using a webcam and automatically plays music from mood-based playlists.

This project combines:
- Computer Vision (MediaPipe)
- ONNX AI inference
- Pygame audio playback
- CustomTkinter GUI


---

## ⭐ Repository

GitHub: https://github.com/nozafar/MoodTune-AI-Emotion-Based-Music-Player-

---

## 🚀 Features

✅ Real-time webcam emotion detection  
✅ Mood-based playlist selection  
✅ Modern UI (CustomTkinter)  
✅ Dark / Light theme toggle  
✅ Volume slider  
✅ Play / Pause / Resume / Next / Stop  
✅ Replay last detected mood playlist  
✅ Debug terminal logging  
✅ Lightweight ONNX inference (no heavy TensorFlow)

Supported emotions:
- Happy
- Sad
- Angry
- Neutral
- Fear
- Surprise

---

## 🧠 AI Model Details

- Trained on **FER-2013** dataset
- Built using **PyTorch**
- Exported to **ONNX**
- Runs efficiently on CPU
- Uses landmark features from MediaPipe

---

## 🛠 Tech Stack

| Component | Technology |
|----------|------------|
| UI | CustomTkinter |
| AI Runtime | ONNX Runtime |
| Computer Vision | MediaPipe |
| Audio | Pygame Mixer |
| Dataset | FER-2013 |
| Language | Python 3.x |

---

## 📁 Project Structure

MoodTune-AI-Emotion-Based-Music-Player-/
│
├── app.py                     # Main UI application
├── mood.py                    # ONNX inference logic
├── player.py                  # Music playback system
├── db.py                      # (optional) storage
├── train.py                   # Model training script
├── dataset_fer.py             # Dataset loader
│
├── models/
│   ├── emotion.onnx
│   ├── emotion.onnx.data
│   └── emotion.pt
│
├── data/
│   ├── songs/
│   │   ├── angry/
│   │   ├── happy/
│   │   ├── sad/
│   │   ├── neutral/
│   │   ├── fearful/
│   │   └── surprised/
│   │
│   ├── fer2013/ (dataset)
│   │   ├── train/
│   │   ├── test/
│   │   └── val/
│
├── moodtune.db                # (optional) database
├── readme.md                  # You are here
└── requirements.txt           # Dependencies

```



````

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/nozafar/MoodTune-AI-Emotion-Based-Music-Player-.git
cd MoodTune-AI-Emotion-Based-Music-Player-
````

### 2️⃣ Create virtual environment (recommended)

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:

```
customtkinter
opencv-python
mediapipe
pygame
onnxruntime
numpy
Pillow
```

---

## ▶️ Run the Application

```bash
#before running tarin the model scroll below for train model code
# data inlcluded just train and run
python app.py
```

---

## 🎶 Add Songs

Place `.mp3`, `.wav`, or `.ogg` files into:

```
data/songs/happy
data/songs/angry
data/songs/sad
data/songs/neutral
data/songs/fearful
data/songs/surprised
```

The app will automatically pick songs from the detected mood folder.

---

## 🎛️ UI Controls

| Button        | Action                       |
| ------------- | ---------------------------- |
| Detect & Play | Detect mood + start playlist |
| Play Again    | Replay last mood playlist    |
| Pause         | Pause audio                  |
| Resume        | Resume audio                 |
| Next          | Skip to next track           |
| Stop          | Stop music                   |
| Volume Slider | Adjust volume                |
| Toggle Theme  | Switch Dark / Light          |
| Exit          | Close application            |

---

## 🌓 Theme Support

* Default: **Dark mode**
* Click **Toggle Theme** to switch to light UI

---

## 🔧 Debug Logging

Console displays useful events:

```
[DEBUG] Model predicted mood: happy
[DEBUG] Songs found in folder
```

---

## 🏗 Training (optional)

If you want to train your own model:

```bash
python train.py
```

Export the ONNX:

```bash
python export_onnx.py
```

---

## 🧾 Build Windows EXE (optional)

```bash
pip install pyinstaller
pyinstaller --noconsole --onefile app.py
```

Executable appears in:

```
/dist/app.exe
```

---

## 📷 Screenshots (optional)

Place images in:

```
assets/
```

Add them like:

```
![Screenshot](assets/screenshot01.png)
```

---

## 📌 Roadmap

* ✅ Better UI controls
* ✅ Dark/Light theme
* ✅ Volume slider
* 📊 Mood history statistics
* 📈 Analytics charts
* 🔐 Face login recognition
* ❤️ Personalized recommendations
* 🎚 EQ / audio effects
* 📦 Auto update system

---

## 🙌 Contributing

Pull Requests welcome!

How to contribute:

1. Fork the repo
2. Create a new branch
3. Commit your changes
4. Submit a PR

---

## 📜 License

MIT License — free for personal & commercial use.

---

## ⭐ Support the project!

If you like this project, please star ⭐ the repo — it helps a lot!

```
⭐ GitHub: https://github.com/nozafar/MoodTune-AI-Emotion-Based-Music-Player-
```

Made with ❤️ by **nozafar**

```

---

✅ You’re all set — just paste this into your repository’s `README.md`.

If you want:

📌 badges  
📌 animated preview GIF  
📌 demo video section  
📌 installation screenshots  

Just say:

> add badges & preview GIF section
```
