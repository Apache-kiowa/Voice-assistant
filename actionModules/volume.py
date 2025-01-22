import os
from actionModules.playAudio import play_audio 

def volume(num):
    num = max(0, min(num, 100))
    volume_level = round(num / 100, 2)
    os.system(f"wpctl set-volume @DEFAULT_AUDIO_SINK@ {volume_level}")
    play_audio("audio/sus.wav")

    