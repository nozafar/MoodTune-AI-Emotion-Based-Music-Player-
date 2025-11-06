import customtkinter as ctk
from mood import detect_mood
import player
import db

MOOD_MAP={
    "happy":"data/songs/happy",
    "sad":"data/songs/sad",
    "angry":"data/songs/angry",
    "neutral":"data/songs/neutral",
    "fear":"data/songs/fear",
    "surprise":"data/songs/surprise"
}

last_mood = None
dark = True

class Dashboard(ctk.CTk):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.title("MoodTune Dashboard")
        self.geometry("700x500")
        ctk.set_appearance_mode("dark")

        ctk.CTkLabel(self,text=f"Welcome, {user[1]}",font=("Segoe UI",22)).pack(pady=10)

        self.mood_label = ctk.CTkLabel(self,text="Mood: None",font=("Segoe UI",18))
        self.mood_label.pack(pady=5)

        # Buttons frame
        frame = ctk.CTkFrame(self)
        frame.pack(pady=10)

        ctk.CTkButton(frame,text="Detect Mood",command=self.detect_mood_action,width=150).grid(row=0,column=0,padx=10,pady=8)
        ctk.CTkButton(frame,text="Play Again",command=self.play_again,width=150).grid(row=0,column=1,padx=10,pady=8)

        ctk.CTkButton(frame,text="⏸ Pause",command=player.pause_music,width=150).grid(row=1,column=0,padx=10,pady=8)
        ctk.CTkButton(frame,text="▶ Resume",command=player.resume_music,width=150).grid(row=1,column=1,padx=10,pady=8)

        ctk.CTkButton(frame,text="⏭ Next",command=player.next_song,width=150).grid(row=2,column=0,padx=10,pady=8)
        ctk.CTkButton(frame,text="⛔ Stop",command=player.stop_music,width=150).grid(row=2,column=1,padx=10,pady=8)

        # Volume slider
        ctk.CTkLabel(self,text="Volume").pack(pady=5)
        self.volume_slider = ctk.CTkSlider(self,from_=0,to=1,command=self.volume_changed,width=350)
        self.volume_slider.pack()
        self.volume_slider.set(1)

        ctk.CTkButton(self,text="Toggle Theme",command=self.toggle_theme,width=200).pack(pady=10)
        ctk.CTkButton(self,text="Logout",command=self.logout,width=200).pack(pady=5)
        ctk.CTkButton(self,text="Exit",command=self.destroy,width=200).pack(pady=5)

    def detect_mood_action(self):
        global last_mood
        mood = detect_mood()
        last_mood = mood
        self.mood_label.configure(text=f"Mood: {mood}")
        player.play_folder(MOOD_MAP[mood])

    def play_again(self):
        if last_mood:
            player.play_folder(MOOD_MAP[last_mood])

    def volume_changed(self, val):
        player.set_volume(float(val))

    def toggle_theme(self):
        global dark
        dark = not dark
        ctk.set_appearance_mode("dark" if dark else "light")

    def logout(self):
        self.destroy()
        from ui_login import LoginUI
        LoginUI().mainloop()
