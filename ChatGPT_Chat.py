import json
import pyautogui
import time
import keyboard
import subprocess
import pyperclip  # Import pyperclip module for clipboard manipulation

# Execute ChatGPT_init.py script
subprocess.run(["python", "ChatGPT_init.py"])

# Load data from chat.txt
with open('chat.txt', 'r', encoding='utf-8') as text_file:
    chact = text_file.read()

# Clear the clipboard before writing the new content
pyperclip.copy("") 

# Copy the chact text to the clipboard
keyboard.write(chact)

# Wait for a brief moment
time.sleep(1)

# Simulate pressing and releasing the "Ctrl" key
keyboard.press('ctrl')
keyboard.press_and_release('v')
keyboard.release('ctrl')

# Wait for a brief moment
time.sleep(1)

# Simulate pressing and releasing the "Enter" key
keyboard.press('enter')
