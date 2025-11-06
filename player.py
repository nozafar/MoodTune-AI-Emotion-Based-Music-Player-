import pygame, time, os, random

pygame.mixer.init()
pygame.mixer.music.set_volume(1.0)

_playlist = []
_index = 0
_paused = False

def play_folder(path):
    global _playlist, _index
    _playlist = [os.path.join(path,f) for f in os.listdir(path)
                 if f.lower().endswith((".mp3",".wav",".ogg"))]
    random.shuffle(_playlist)
    _index = 0
    _play_current()

def _play_current():
    global _index
    if not _playlist:
        return
    pygame.mixer.music.load(_playlist[_index])
    pygame.mixer.music.play()

def next_song():
    global _index
    if not _playlist:
        return
    _index = (_index + 1) % len(_playlist)
    _play_current()

def pause_music():
    pygame.mixer.music.pause()

def resume_music():
    pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.stop()

def set_volume(v):
    pygame.mixer.music.set_volume(v)
