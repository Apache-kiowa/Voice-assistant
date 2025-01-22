import os
from actionModules.playAudio import * 

def startVPN():
    play_audio("audio/def.wav")
    os.system(f"sudo /usr/bin/wg-quick up /home/me/Downloads/MUS3_ubuntu_wg0.conf")
    
   
