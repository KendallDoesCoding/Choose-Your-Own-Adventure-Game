def music():
    import sys
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install',  'playsound'])
    from playsound import playsound
    playsound('sotb.mp3', False)
    print("Music has started.")
