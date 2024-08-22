from Process import *

def brightnessIncrease(count):
    try:
        if osName == 'Windows':
            sbc.fade_brightness(10*int(count))
        else:
            for _  in range(int(count)):
                os.system("xdotool key XF86MonBrightnessUp")
    except:
        speak('Internal server error')


def brightnessDecrease(count):
    try:
        if osName == 'Windows':
            sbc.fade_brightness(10*int(count))
        else:
            for _  in range(int(count)):        
                os.system("xdotool key XF86MonBrightnessDown")
    except:
        speak('Internal server error')

