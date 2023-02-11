#!/usr/bin/python
from pynput import keyboard
from pygame import mixer
import threading
import random

mixer.init()

song = mixer.Sound("1.wav")
key_cache = {}

def play(s):
    s.play()

class thread(threading.Thread):
    def __init__(self, thread_name, thread_ID, key):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.thread_ID = thread_ID
        self.key = key

    def run(self):
        try:
            if key_cache[str(self.key)]:
                return
        except KeyError:
            pass
        play(song)
        

def on_press(key):
    try:
        # print('Alphanumeric key pressed: {0} '.format(key.char))
        thread1 = thread("abc", int(random.randint(100, 100000)), key)
        thread1.start()
        key_cache[str(key)] = True

    except AttributeError:
        print('special key pressed: {0}'.format(key))

def on_release(key):
    # print('Key released: {0}'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    key_cache[str(key)] = False

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
