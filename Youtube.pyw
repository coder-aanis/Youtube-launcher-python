from pynput.keyboard import Key, Controller
import webbrowser
import os
import time

a_website = "https://www.youtube.com"
 
# Open url in a new window of the default browser, if possible
webbrowser.open_new(a_website)

keyboard = Controller()

time.sleep(1)
keyboard.press(Key.f11)
keyboard.release(Key.f11)

