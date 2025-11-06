import customtkinter as ctk
from tkinter import messagebox
from mood import detect_mood
import player, os

# Map moods to folders (adjust to match your directories)
MOOD_MAP = {
    "angry": "data/songs/angry",
    "happy": "data/songs/happy",
    "neutral": "data/songs/neutral",
    "sad": "data/songs/sad",
    "fear": "data/songs/fearful",
    "surprise": "data/songs/surprised"
}

last_mood = None
dark_mode = True

# -----------------------------
# Helper Functions
# -----------------------------

def detect_and_play():
    global last_mood
    mood = detect_mood()
    print("[DEBUG] Model predicted mood:", mood)
    last_mood = mood
    mood_label.configure(text=f"Mood: {mood}")
    play_by_mood(mood)

def play_by_mood(mood):
    print("[DEBUG] Requested mood:", mood)

    if mood not in MOOD_MAP:
        print("[ERROR] Mood not in map:", mood)
        messagebox.showerror("Error", f"No mapping for: {mood}")
        return

    folder = MOOD_MAP[mood]
    print("[DEBUG] Folder resolved to:", folder)

    if not os.path.exists(folder):
        print("[ERROR] Folder does not exist:", folder)
        messagebox.showerror("Error", f"Folder not found:\n{folder}")
        return

    files = [f for f in os.listdir(folder) if f.lower().endswith((".mp3",".wav",".ogg"))]
    if not files:
        print("[ERROR] No audio files found.")
        messagebox.showwarning("No Songs", f"No audio files in {folder}")
        return

    player.play_folder(folder)

def play_song_button():
    if last_mood is None:
        messagebox.showwarning("Warning", "Detect mood first!")
        return
    play_by_mood(last_mood)

def pause_song():
    player.pause_music()

def resume_song():
    player.resume_music()

def next_song():
    player.next_song()

def stop_song():
    player.stop_music()

def volume_changed(v):
    player.set_volume(float(v))

def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    ctk.set_appearance_mode("dark" if dark_mode else "light")

def exit_app():
    try:
        player.stop_music()
    except Exception as e:
        print("[DEBUG] Error stopping player:", e)
    app.destroy()

# -----------------------------
# UI Setup
# -----------------------------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("🎵 MoodTune AI Player")
app.geometry("520x500")
app.resizable(False, False)

# Title
title_label = ctk.CTkLabel(app, text="MoodTune AI Music Player", font=("Segoe UI", 22, "bold"))
title_label.pack(pady=15)

# Mood label
mood_label = ctk.CTkLabel(app, text="Mood: None", font=("Segoe UI", 16))
mood_label.pack(pady=10)

# Buttons Frame
frame = ctk.CTkFrame(app)
frame.pack(pady=15)

# Row 1
ctk.CTkButton(frame, text="🎥 Detect & Play", width=180, command=detect_and_play).grid(row=0, column=0, padx=10, pady=8)
ctk.CTkButton(frame, text="🎵 Play Again", width=180, command=play_song_button).grid(row=0, column=1, padx=10, pady=8)

# Row 2
ctk.CTkButton(frame, text="⏸ Pause", width=180, command=pause_song).grid(row=1, column=0, padx=10, pady=8)
ctk.CTkButton(frame, text="▶ Resume", width=180, command=resume_song).grid(row=1, column=1, padx=10, pady=8)

# Row 3
ctk.CTkButton(frame, text="⏭ Next Song", width=180, command=next_song).grid(row=2, column=0, padx=10, pady=8)
ctk.CTkButton(frame, text="⛔ Stop", width=180, command=stop_song).grid(row=2, column=1, padx=10, pady=8)

# Volume
ctk.CTkLabel(app, text="Volume").pack(pady=(10, 2))
volume_slider = ctk.CTkSlider(app, from_=0, to=1, number_of_steps=10, command=volume_changed, width=350)
volume_slider.set(1)
volume_slider.pack(pady=5)

# Theme toggle + Exit
ctk.CTkButton(app, text="🌓 Toggle Theme", command=toggle_theme, width=200).pack(pady=10)
ctk.CTkButton(app, text="🚪 Exit", command=exit_app, width=200).pack(pady=10)

# Footer
ctk.CTkLabel(app, text="AI-powered Emotion Recognition Music Player", text_color="#888", font=("Segoe UI", 10)).pack(side="bottom", pady=5)

app.mainloop()
