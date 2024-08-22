from Process import *
def copyText(var):
    try:
        speak("shall I copy ?",var)    
        pyautogui.hotkey('ctrl','c')
        speak("copied successfully",var)    
    except:
        speak('Some error acquired')


def pasteText(var):
    try:
        speak("shall I paste ?",var)    
        pyautogui.hotkey('ctrl','v') 
        speak("pasted successfully",var)   
    except:
        speak('Some error acquired')


def selectText(var):
    try:
        speak("shall I select ?",var)    
        pyautogui.hotkey('ctrl','a')   
        speak("selected successfully",var)
    except:
        speak('Some error acquired')

    
def saveFile(var):
    try:
        speak("shall I save",var)    
        pyautogui.hotkey('ctrl','s')   
        speak("saved successfully",var)
    except:
        speak('Some error acquired')


def switchFile(var):
    try:
        speak("shall I switch",var)    
        pyautogui.hotkey('altleft','Tab')   
        speak("switched successfully",var)
    except:
        speak('Some error acquired')

    
def activeFile(var):
    try:
        speak("shall I check Activities",var)  
        if osName == 'Windows':
            pyautogui.hotkey('winleft','tab')   
        else:
            pyautogui.hotkey('winleft')   
        speak("Activity checked successfully",var)
    except:
        speak('Some error acquired')

    
def minimizeAllFile(var):
    try:
        speak("shall I minimize all ?",var)    
        pyautogui.hotkey('winleft','d')   
        speak("All Tabs are minimized successfully",var)
    except:
        speak('Some error acquired')

    
def minimizeFile(var):
    try:
        speak("shall I minimize ?",var)    
        pyautogui.hotkey('winleft','d')   
        speak("minimize successfully",var)
    except:
        speak('Some error acquired')


def volumeUp(count,var):
    try:
        speak("Ok,shall I increase the volume ?",var)    

        for _ in range(count):
            if osName == 'Windows':
                    pyautogui.hotkey('volumeup')
            else:
                pyautogui.hotkey('winleft','F10')
    except:
        speak('Some error acquired')


def volumeDown(count,var):
    try:
        speak("Ok,shall I decrease the volume ?",var)    
        for _ in range(count):
            if osName == 'Windows':
                pyautogui.hotkey('volumedown')
            else:  
                pyautogui.hotkey('winleft','F12')
    except:
        speak('Some error acquired')


def volumeMute(var):
    try:
        speak("shall I mute the volume ?",var)    
        if osName == 'Windows':
            pyautogui.hotkey('volumemute')
        else:
            pyautogui.hotkey('winleft','F11')
    except:
        speak('Some error acquired')


def volumeUnMute(var):
    try:
        if osName == 'Windows':
            pyautogui.hotkey('volumemute')
        else:
            pyautogui.hotkey('winleft','F10')
            
        speak("I Unmuted the volume.",var)    
    except:
        speak('Some error acquired')
    

