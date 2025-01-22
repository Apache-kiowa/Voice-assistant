import os
from actionModules.playAudio import * 

def shutdown():

    play_audio("audio/yes.wav")
    os.system(f"shutdown now ")
    