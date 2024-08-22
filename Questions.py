from Function import*
import threading  # Import the threading module

numAry = [str(i) for i in range(0,11)]

class startExecution():
    def __init__(self):
        self.running = True  # Start the program as running
        self.stop_event = threading.Event()  # Create a stop event

    def run(self,var='0'):
        value = self.TaskStarting(var)
        return value

    def stop(self):
        self.stop_event.set()  # Set the stop event to signal the loop to stop

    def voiceChanger(self, output):
        if "male" in output or "mail" in output:
            return "1"

        elif "women" in output:
            return "0"

    def sql_fetch(self,inputs):

        if inputs != "":
            Queries = []
            prepAry = ['the', 'a', 'an','this','is']
            
            con = sqlite3.connect('memory.db')
            cursorObj = con.cursor()
            
            for i in prepAry:
                v = inputs.find(f' {i} ')
                if v != -1:
                    inputs = inputs.replace(f" {i} ", " ")

                else:
                    inputs = inputs
                    
            inputs = inputs.replace(' ','+')
            inputsAry = inputs.split('+and+')
            print(inputs)
            
            for i in inputsAry:
                print(i)
                cursorObj.execute(f"SELECT answer FROM questionsAndAnswers where question = '{i}'")
                rows = cursorObj.fetchall()

                for row in rows:
                    Queries.append(row[0])
                    
            return Queries
        
        else:
            return ""
    

    def TaskExecution(self, var):

         while not self.stop_event.is_set():  
            
            self.query = takeCommand(var).lower()
            Queries = self.sql_fetch(self.query)
            print(Queries)

            # Logic for executing tasks based on self.query

            if self.query == 0:
                continue

            if 'changeTone' in Queries:
                
                if nameIdentifier(var) == "Zein":
                    var = self.voiceChanger("women")
                    name = 'Zara'
                    gender=('Female')                    

                elif nameIdentifier(var) == "Zara":
                    var = self.voiceChanger("male")
                    name = 'Zein'
                    gender=('Male')
                    
                eel.nameJs(name,int(var))

                speak("Hello, I have switched my voice.", var)

                
            if 'wikipedia' in self.query:
                speak('Searching Wikipedia...', var)
                self.query = self.query.replace("wikipedia",'')
                
                if self.voiceChanger("male"):
                    engine.setProperty('rate', 180)
                    engine.setProperty('-s', 100)

                speak("Which related topic you want to know?", var)
                try:
                    # topic = eel.js_inputBox('Enter Topic You Want')()
                    topic = takeCommand()
                    print(topic)
                    
                    count = 0
                    while topic == None and count < 3:
                        time.sleep(3)
                        topic = eel.js_inputBox('Enter Topic You Want')()
                        print(topic)
                        count += 1
                                        
                    results = wikipedia.summary(
                        f"{self.query} ({topic})", sentences=5)
                    speak("According to Wikipedia", var)            # Logic for executing tasks based on self.query

                    speak(results, var)
                except Exception as e:
                    speak("Sorry some error occured try agian later", var)

            if 'send email' in self.query:
                from Email import EmailBot
                EmailBot(var)

            if 'switchTab' in Queries:
                from KeyBoardControl import switchFile
                switchFile(var)

            if 'activity' in self.query:
                from KeyBoardControl import activeFile
                activeFile(var)

            elif 'minimise all' in self.query:
                from KeyBoardControl import minimizeAllFile
                minimizeAllFile(var)
                
            elif 'minimise' in self.query:
                from KeyBoardControl import minimizeFile
                minimizeFile(var)

            elif 'play music' in self.query:                    
                speak("which song should I play", var)    
                if osName == 'Windows':
                    musicPath = f"C:\\Users\\{userName}\\Music\\music"
                else:
                    musicPath = f"/home/{userName}/Music/music"
                            
                playSpecificSong('',musicPath,'',var)
                            
            elif 'play ' in self.query:
                    self.query = self.query.replace("play",'')
                    self.query = self.query.replace("music",'')
                    self.query = self.query.replace("song",'')

                    media = self.query.find('in')
                    if media != -1:
                        ary = self.query.split('in')
                        query = ary[0].strip()
                        player = ary[1].strip()
                        print(player) 

                    else:
                        player = ''
                        query = self.query


                    if osName == 'Windows':
                        musicPath = f"C:\\Users\\{userName}\\Music\\music"
                    else:
                        musicPath = f"/home/{userName}/Music/music"
            
                    playSpecificSong(query,musicPath,player,var)

            
            if osName != 'Windows':
    
                if self.query in ['continue music','continue song']:
                    from musicControl import playingMusic
                    playingMusic()
                    speak("song is playing", var)

                if self.query in ['pass song','pass','pause','pause song','pass music','pause music','hold music']:
                    from musicControl import pausingMusic
                    pausingMusic()
                    speak("song is paused", var)

                if self.query in ['stop music','stop song']:
                    from musicControl import stopMusic
                    stopMusic()
                    speak("song is stopped", var)

                if self.query in ['next song','next music']:
                    from musicControl import nextMusic
                    nextMusic()
                    speak("playing next song", var)

                if self.query in ['previous song','previous music']:
                    from musicControl import previousMusic
                    previousMusic()
                    speak("playing previous song", var)

                if 'close player' in self.query:
                    from musicControl import quitMusic
                    quitMusic()
                    speak("closing media player", var)
            
            if 'open notepad' in self.query:
                if osName == 'Windows':
                    note = "c:\\Windows\\System32\\notepad.exe"        
                else:
                    note = "/usr/bin/gedit"
                os.popen(note)

            if 'openGoogle' in Queries:
                speak("What should I search?", var)
                openGoogle(var)

            if 'openYoutube' in Queries:
                speak("What should I search?", var)
                openYoutube(var)
              
            if 'getWallpaper' in Queries:
                from Wallpapers import changeWallpaper
                changeWallpaper(var)
                speak("Wallpaper Changed", var)

            if 'randomWallpaper' in Queries:
                from Wallpapers import randomWallpaper
                randomWallpaper()
                speak("Wallpaper Changed", var)

            if 'defaultWallpaper' in Queries:
                from Wallpapers import defaultWallpaper
                defaultWallpaper()
                speak("Wallpaper Changed", var)

            if 'remember that' in self.query:
                speak("what should I remember", var)
                rememberMessage = takeCommand(var)
                speak("you said me to remember "+rememberMessage, var)
                remember = open('data.txt', 'w')
                remember.write(f'{rememberMessage},')
                remember.close()

            if 'youRememberThat' in Queries:
                remember = open('data.txt', 'r')
                speak("you said me to remember that " + remember.read(), var)
                print("you said me to remember that " + remember.read())

            if 'openImage' in Queries:
                speak("Opening Picture", var)
                openImage(var)

            if 'openScreenshot' in Queries:
                speak("Opening Picture", var)
                openScreenShot(var)

            if 'openWallpaper' in Queries:
                speak("Opening Picture", var)
                openWall(var)

            if 'open code' in self.query:
                os.system('code ')

            if 'open telegram' in self.query:
                from openApps import openTelegram
                openTelegram()
                
            if 'getTime' in Queries:
                strTime = datetime.datetime.now().strftime("%I:%M %p")
                speak(f"The time is {strTime}", var)

            if 'type' in self.query:
                editmode(var)

            if 'select all' in self.query:
                from KeyBoardControl import selectText
                selectText(var)

            if 'copy' in self.query:
                from KeyBoardControl import copyText
                copyText(var)

            if 'paste' in self.query:
                from KeyBoardControl import pasteText
                pasteText(var)

            if 'save' in self.query:
                from KeyBoardControl import saveFile
                saveFile(var)

            if 'open terminal' in self.query:
                from openApps import openTerminal
                openTerminal(var)

            if 'increaseVolume' in Queries:
                from musicControl import increaseVolume
                speak("how many times you want to increase your volume", var)
                count = takeCommand(var)
                if count not in numAry:
                    count = '1'
                increaseVolume(count, var)

            if 'decreaseVolume' in Queries:
                from musicControl import decreaseVolume
                speak("how many times you want to decrease you volume", var)
                count = takeCommand(var)
                if count not in numAry:
                    count = '1'
                decreaseVolume(count, var)

            if 'increaseBrightness' in Queries:
                from systemControls import brightnessIncrease
                speak("how many times you want to increase your Brightness", var)
                count = takeCommand(var)
                if count not in numAry:
                    count = '1'
                brightnessIncrease(count)

            if 'decreaseBrightness' in Queries:
                from systemControls import brightnessDecrease
                speak("how many times you want to decrease your Brightness", var)
                count = takeCommand(var)
                if count not in numAry:
                    count = '1'
                brightnessDecrease(count)

            elif 'unmute' in self.query:
                from musicControl import UnMuteVolume
                UnMuteVolume(var)

            elif 'mute' in self.query:
                from musicControl import MuteVolume
                MuteVolume(var)
         
            if 'stands for' in self.query:
                speak(
                    'J.A.R.V.I.S stands for JUST A RATHER VERY INTELLIGENT SYSTEM', var)

            if 'getName' in Queries:
                speak(f"my name is {nameIdentifier(var)}", var)

                speak("i am your ai assistant to make your work easier", var)
                speak("now tell me what can I do for you", var)

            if 'getList' in Queries:
                speak("i do multiple tasks", var)
                
            if 'Creater' in Queries:
                speak(ProfileFinder('MyDetails','Name')[0],var)
                
            if 'Version' in Queries:
                speak(f"My Version is {ProfileFinder('MyDetails','version')[0]}",var)

            if 'getLocation' in Queries:
                locateLocation('',var)
                
            if 'map' in self.query:
                self.query = self.query.replace('open','')
                self.query = self.query.replace('map','')
                locateLocation(self.query,var)

            if 'giveLove' in Queries:
                speak("I love you Too", var)

            if 'giveResponce' in Queries:
                speak("Yes, at your service", var)

            elif 'take screenshot' in self.query:
                screenshot(var)

            elif self.query in ['quit', 'bye', 'exit','turn off']:
                speak("Quitting , Thanks for your time Have a good day", var)
                return '1'

            elif self.query in ['you can sleep now','sleep now','take a break']:
                speak("Okay, I am going to sleep you can call me at anytime", var)
                print("Okay, I am going to sleep you can call me at anytime 😴")
                value = self.SleepMode(var)
                return value

    def SleepMode(self,var):
            name = nameIdentifier(var)                
            while not self.stop_event.is_set():  
                
                self.query = takeCommand(var,'').lower()            

                if self.query in ['wake up','wake up wake up', f'wake up {name}', f'ok {name}', 'make up','turn on','turn on turn on']:   
                    speak("I am ready now tell what can I do for you", var)     
                    value = self.TaskExecution(var)
                    if value == '1':
                        break

                elif self.query in ['quit', 'bye', 'exit','turn off']:
                    speak("Quitting , Thanks for your time Have a good day", var)
                    break

            print('1')
            return '1'   
            
    def TaskStarting(self, var):
        
            wishMe(var)                        
                
            while not self.stop_event.is_set():        
                    value = self.TaskExecution(var)

                    if value == '1':
                        break

            print('1')
            return '1'   