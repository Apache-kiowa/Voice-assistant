import subprocess
import os

def playSong():

    file_path = "audio/AC_DC-Highway to Hell.mp3"
    subprocess.run(['vlc', file_path])