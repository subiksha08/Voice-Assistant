from Process import *

def wishMe(var):
    hour = int(datetime.datetime.now().hour)
    by = time.strftime("%I:%M %p")
    
    if hour >= 5 and hour <= 10:
        speak(f"Good Morning! , it's {by}", var)

    elif hour >= 10 and hour <= 15:
        speak(f"Good Afternoon! , it's {by}", var)

    elif hour >= 15 and hour <= 19:
        speak(f"Good Evening! , it's {by}", var)

    else:
        speak(f"Good Night! , it's {by}", var)

    speak(
        f"I am {nameIdentifier(var)}. Please tell me how may I help you ", var)
    print("😃")

def YoutubeUrl(search_keyword,var):
    print(search_keyword)
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)

    def ListUrl():
        list_ids = re.findall(r"playlist\?list=(\S{34})", html.read().decode())
        return list_ids[0]

    try:
        if "playlist" in search_keyword:
            listkey= ListUrl()
            listUrl= urllib.request.urlopen(f"https://www.youtube.com/playlist?list={listkey}")
            video_ids = re.findall(r"watch\?v=(\S{11})", listUrl.read().decode())
            return [f"https://www.youtube.com/watch?v={video_ids[0]}&list={listkey}",f'http://img.youtube.com/vi/{video_ids[0]}/mqdefault.jpg']
        
        elif 'channel' in search_keyword:
            listkey= ListUrl()
            try:
                url = [f"https://www.youtube.com/playlist?list={listkey}"]
                
            except:
                listUrl= urllib.request.urlopen(f"https://www.youtube.com/playlist?list={listkey}")
                video_ids = re.findall(r"watch\?v=(\S{11})", listUrl.read().decode())
                url = [f"https://www.youtube.com/watch?v={video_ids[0]}&list={listkey}",f'http://img.youtube.com/vi/{video_ids[0]}/mqdefault.jpg']
                
            return url
        
        elif 'search' in search_keyword:
            return [f"https://youtube.com/results?search_query={search_keyword.replace('search','')}"]
        
        else:
            video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
            return [f"https://www.youtube.com/watch?v={video_ids[0]}",f'http://img.youtube.com/vi/{video_ids[0]}/mqdefault.jpg']

    except:
        speak(f"Sorry, I cannot find that {search_keyword.replace('+',' ')} you said",var)
        return '0'

def openYoutube(var,values = ''):
    time.sleep(2)
    if values == '':
        search = takeCommand(var, "").replace(' ','+')
    else:
        search = values.replace(' ','+')

    try:
        if search == '':
            speak("say again please", var)
            openYoutube(var)
            # count += 1

        else:
            url = YoutubeUrl(search,var)
            if url != '0':      
                try:
                    eel.js_imgbox(url[1],search.replace('+',' '),url[0])
                except:
                    eel.js_imgbox('https://img.youtube.com/vi//mqdefault.jpg',search.replace('+',' '),url[0])
                    print('Img Not Found')
                webbrowser.open_new_tab(url[0])
            else:
                print('Error')
    except:
        speak('Internal server error')

def openGoogle(var):
    time.sleep(2)
    command = takeCommand(var, "")
    
    try:
        if command == "":
            speak("say again please", var)
            openGoogle(var)

        else:
            webbrowser.open_new_tab('https://google.com/search?q=' + command)
            
    except:
        speak('Internal server error')


def locateLocation(Place='',var='0'):
        try:
            if Place == '':
                speak('What is the location ?', var)
                Place = takeCommand(var, "")
            
            url = 'https://google.nl/maps/place/' + str(Place) + '/&amp;'
            webbrowser.open_new_tab(url)
        except:
            speak('Internal server error')

def screenshot(var):
    try:
        speak("taking screenshot",var)
        img = pyautogui.screenshot()
        
        speak('what should I write ?',var)
        name = takeCommand(var,"")
        
        try:
            count = 0
            while name == '' and count < 1:
                    name = takeCommand(var,"")
                    count += 1
                            
            if osName == 'Windows':
                img.save(f'C:\\Users\\{userName}\\Pictures\\screenshot\\'+name.replace(' ','-')+'.jpg')
            else:
                img.save(f'/home/{userName}/Pictures/screenshot/'+name.replace(' ','-')+'.jpg')
                        
        except:
            speak('Sorry some Error acquired I uploaded a file by random name',var)
                
            name = str(datetime.datetime.now()).replace(' ','-')
            name = name.replace('.','-')
            if osName == 'Windows':
                img.save(f'C:\\Users\\{userName}\\Pictures\\screenshot\\'+name+'.jpg')
            else:
                img.save(f'/home/{userName}/Pictures/screenshot/'+name+'.jpg')
                        
        speak("succesfully uploaded",var)
    except:
        speak('Internal server error')

def editmode(var):
    try:
        speak("what should I write ?",var) 
        search = takeCommand(var,"")
        pyautogui.write(search, interval="0.25")
    except:
        speak('Internal server error')

def openImage(var):
    try:
        
        if osName == 'Windows':
            os.system(f'start C:\\Users\\{userName}\\Pictures\\')
        else:
            im = f"/home/{userName}/Pictures/"  
            os.system(f'eog {im}')
                    
    except:
        speak("picture is unavialable kindly search other image",var)
    
def openScreenShot(var):
    try:
        
        if osName == 'Windows':
            os.system(f'start C:\\Users\\{userName}\\Pictures\\screenshot\\')
        else:
            im = f"/home/{userName}/Pictures/screenshot/"
            os.system(f'eog {im}')
                    
    except:
        speak("picture is unavialable kindly search other image",var)

def openWall(var):
    try:
        
        if osName == 'Windows':
            os.system(f'start C:\\Users\\{userName}\\Pictures\\Wallpapers\\')
        else:
            im = f"/home/{userName}/Pictures/Wallpapers/"  
            os.system(f'eog {im}')
                    
    except:
        speak("picture is unavialable kindly search other image",var)
         

def playSpecificSong(songName='',musicPath='',mediaName='vlc',var='0'):
        print(songName)
       
        if songName == '':
            song = eel.js_inputBox('Enter a music you want to search')()
            print(song)
            
            count = 0
            while (song == None or song == '') and count < 1:
                time.sleep(3)
                song = eel.js_inputBox('Enter a music you want to search')()
                print(song)
                count += 1
            
            search = song
            
        else:
            search = songName
                  
        try:
            if search == '':
                return None
            file_search.set_root(musicPath)
            songsList = file_search.searchFile(search.lower())
            songsList.reverse()
            
            try:
                song_uri = songsList[0]
                print(song_uri)

                if mediaName == '' and osName != 'Windows':
                        
                        speak("Which Player you want to hear song ?", var)
                        
                        time.sleep(3)
                        # media = input('Search ').lower()
                        media = eel.js_inputBox('Enter a player you want')()
                        print(media)
                        
                        count1 = 0
                        while media == None and count1 < 1:
                            time.sleep(3)
                            media = eel.js_inputBox('Enter a player you want')()
                            print(media)
                            count1 += 1
                            
                        player = media.lower()
                    
                else:
                        player = mediaName.lower()
                    
                try:
                    if osName == 'Windows':
                        os.popen(f'vlc "{song_uri}"')
                        eel.js_textbox(f"playing"+song_uri.split('{musicPath}\\')[-1])
                    
                    else: 
                        if player in ['vlc','default']:
                            command = 'vlc-ctrl play -p"'+"'"+song_uri+"'"+'"'
                            os.system(command)

                        elif player in ['rhythmbox', 'rhythm box'] :
                            command = 'rhythmbox-client --play-uri="' + song_uri + '"'
                            os.system(command)
                            
                        else:
                            command = 'vlc-ctrl play -p"'+"'"+song_uri+"'"+'"'
                            os.system(command)

                        eel.js_textbox(f"playing {song_uri.split(f'{musicPath}/')[-1]}")
                except:
                    speak('Sorry, some Error  acquired so I playing Song in the Vlc Player',var)
                    command = 'vlc-ctrl play -p"'+"'"+song_uri+"'"+'"'
                    os.system(command)
                    eel.js_textbox(f"playing {song_uri.split(f'{musicPath}/')[-1]}")

            except:
                speak("song is not available so I play this song in youtube", var)
                openYoutube(var,songName)
        except:
            speak('Sorry, some Error  acquired',var)
            return  None
 