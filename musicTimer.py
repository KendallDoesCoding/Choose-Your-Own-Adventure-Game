import threading

# initialize musicTimerObj here to be able to access it from both music.py and chapters.py
musicTimerObj = threading.Timer(0, lambda: None)
