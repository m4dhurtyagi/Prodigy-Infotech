# Keylogger Script in Python
This repository contains a Python script that functions as a basic keylogger, capturing keystrokes and saving them to a log file. The script utilizes the pynput library to monitor keyboard events and record key presses and releases.

## Features
* Keystroke Logging: Captures and records all key presses, including special keys like Enter and Space.
* File Logging: Writes logged keystrokes to a file named log.txt, appending new data to the file.
* Special Key Handling: Differentiates between printable characters and special keys, such as Enter, Space, and Escape.
* Graceful Exit: Stops logging when the Escape key is pressed.
