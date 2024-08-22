from Process import *

def changeWallpaper(var):
    try:
        speak("what should I put ?", var)
        wallpaper = takeCommand(var, "")
        print(wallpaper)
        
        if osName == 'Windows':
            WallpaperPath = f'C:\\Users\\{userName}\\Pictures\\Wallpapers\\' + wallpaper + '.jpg'
            ctypes.windll.user32.SystemParametersInfoW(20, 0, WallpaperPath, 3)

        else:

            wallpaperPath = f"/home/{userName}/Pictures/Wallpapers"
            command = 'gsettings set org.gnome.desktop.background picture-uri file:///' + wallpaperPath + '/' + wallpaper + '.jpg'
            os.system(command)
    except:
        speak('Internal server error')

def randomWallpaper():
    try:
        if osName == 'Windows':
            wallpaperPath = f"C:\\Users\\{userName}\\Pictures\\Wallpapers\\"
        else:
            wallpaperPath = f"/home/{userName}/Pictures/Wallpapers"
            
        wallpapers = os.listdir(wallpaperPath)        
        wallpaper = random.choice(wallpapers)
        print(wallpaper)
        
        if osName == 'Windows':
            command = wallpaperPath + wallpaper
            ctypes.windll.user32.SystemParametersInfoW(20, 0, command, 3)

        else:
            command = 'gsettings set org.gnome.desktop.background picture-uri file:///' + wallpaperPath + "/" + wallpaper
            os.system(command)
    except:
        speak('Internal server error')


def defaultWallpaper():
    try:
        if osName == 'Windows':
            wallpaperPath = f"C:\\Users\\{userName}\\Pictures\\Wallpapers\\"
        else:
            wallpaperPath = f"/home/{userName}/Pictures/Wallpapers"
                
        if osName == 'Windows':
            command = wallpaperPath + '5.jpg'
            ctypes.windll.user32.SystemParametersInfoW(20, 0, command, 3)

        else:
            command = 'gsettings set org.gnome.desktop.background picture-uri file:///' + \
                wallpaperPath + "/" + 'red.jpg'
            os.system(command)
    except:
        speak('Internal server error')

