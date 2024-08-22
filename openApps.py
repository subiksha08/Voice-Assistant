from Process import *

def openTerminal(var):
    try:
        speak("shall I open Terminal ?", var)
        if osName == 'Windows':
            os.system('start cmd')               
        else:
            terminalPath = "/usr/bin/gnome-terminal"
            os.popen(terminalPath)

        speak("Terminal opened successfully", var)
    except:
        speak('App not found')


def openTelegram():
    try:
        if osName == 'Windows':
            Telegrampath = f"C:\\Users\\{userName}\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
        else:
            Telegrampath = "/snap/bin/telegram-desktop" 
        os.popen(Telegrampath)
    except:
        speak('App not found')


def openPycharm():
    try:
      pythonPath = "/snap/bin/pycharm-community"
      os.popen(pythonPath)
    except:
        speak('App not found')

def openSetting(var):
    try:
        speak("shall I open settings?", var)
        if osName == 'Windows':
            settingPath = "start ms-settings:"
            os.system(settingPath)
        else:
            settingPath = "/usr/bin/gnome-control-center"
            os.popen(settingPath)
        speak("Settings opened successfully", var)
    except:
        speak('App not found')

def searchSetting(var):
    try:
        speak("what should I open in settings", var)
        search = takeCommand(var, "")
        settingPath = "/usr/bin/gnome-control-center"
        os.popen(settingPath + f"  {search}")
        speak(f"opened {search} settings successfully", var)
    except:
        speak('App not found')

