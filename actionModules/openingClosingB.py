import webbrowser   
from actionModules.playAudio import * 
import os




def openingClosingB():
    os.system(f"google-chrome-stable --ozone-platform=wayland")
    

def search(request):

    url_search = f"https://www.google.com/search?q={request.replace(' ', '+')}"

    webbrowser.open(url_search)
    play_audio("audio/sus.wav")
    

    
