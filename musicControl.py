from Process import *
import apptester as ap
from KeyBoardControl import *

def playingMusic():
    try:
        if ap.checkIfProcessRunning('vlc') and osName != 'Windows':
            os.system("vlc-ctrl play")
        else:
            os.system("rhythmbox-client --play")      
    except:
        speak('Internal server error',var)

def pausingMusic():
    try:
        if ap.checkIfProcessRunning('vlc') and osName != 'Windows':
            os.system("vlc-ctrl pause")    
        else:
            os.system("rhythmbox-client --pause")
    except:
        speak('Internal server error',var)

def stopMusic():
    try:
        if ap.checkIfProcessRunning('vlc') and osName != 'Windows':
            os.system("vlc-ctrl stop")    
        else:
            os.system("rhythmbox-client --stop")  
    except:
        speak('Internal server error',var)

def nextMusic():
    try:
        if ap.checkIfProcessRunning('vlc') and osName != 'Windows':
            os.system("vlc-ctrl next")    
        else:
            os.system("rhythmbox-client --next")
    except:
        speak('Internal server error',var)

def previousMusic():
    try:
        if ap.checkIfProcessRunning('vlc') and osName != 'Windows':
            os.system("vlc-ctrl prev")    
        else:
            os.system("rhythmbox-client --previous")
            os.system("rhythmbox-client --previous")
    except:
        speak('Internal server error',var)

def quitMusic():
    try:
        if ap.checkIfProcessRunning('vlc') and osName != 'Windows':
            os.system("vlc-ctrl quit")    
        else:
            os.system("rhythmbox-client --quit")    
    except:
        speak('Internal server error',var)

def increaseVolume(count,var):
    try:
        if ap.checkIfProcessRunning('vlc') and osName != 'Windows':
            os.system(f"vlc-ctrl volume {count}0%")
        else:
            volumeUp(int(count),var)    
    except:
        speak('Internal server error',var)

def decreaseVolume(count,var):
    try:
        if ap.checkIfProcessRunning('vlc') and osName != 'Windows':
            os.system(f"vlc-ctrl volume {count}0%")
        else:
            volumeDown(int(count),var) 
    except:
        speak('Internal server error',var)

def MuteVolume(var):
    try:
        if ap.checkIfProcessRunning('vlc') and osName != 'Windows':
            os.system(f"vlc-ctrl volume 0%")
        else:
            volumeMute(var) 
    except:
        speak('Internal server error',var)

def UnMuteVolume(var):
    try:
        if ap.checkIfProcessRunning('vlc') and osName != 'Windows':
            os.system(f"vlc-ctrl volume 75%")
        else:
            volumeUnMute(var) 
    except:
            speak('Internal server error',var)


def MaxVolume():
    try:
        volumeUp(17)      
    except:
        speak('Internal server error',var)

