import tkinter as tk
from pygame import mixer
from pynput import keyboard

mixer.init()

root = tk.Tk()
root.title("Keyboard Music Player")

def play():
    mixer.music.load("sample.mp3")
    mixer.music.play()

def stop():
    mixer.music.stop()

def next_song():
    pass

def prev_song():
    pass

def on_press(key):
    try:
        if key.char == 'p':
            play()
        elif key.char == 's':
            stop()
        elif key.char == 'n':
            next_song()
        elif key.char == 'b':
            prev_song()
    except AttributeError:
        pass

listener = keyboard.Listener(on_press=on_press)
listener.start()

root.mainloop()