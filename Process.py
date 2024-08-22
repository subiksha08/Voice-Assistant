from Packages import *  # Import everything from the Packages module
import comtypes.client  # Import comtypes.client

# Ensure comtypes is correctly set up
comtypes.client.GetModule('C:\\Windows\\System32\\Speech\\Common\\sapi.dll')

# Initialize Eel
eel.init(".")

# Global variables
var = "index.html"
arr = []

# Get system details
osName, Version = platform.system(), platform.release()
userName = os.getlogin()

# Function to identify name based on input
def nameIdentifier(var):
    return "Zein" if var == "1" else "Zara"

# Initialize pyttsx3 engine for text-to-speech
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Function to handle speech output
def speak(audio, output='0'):
    try:
        if "0" in output:
            print(audio)
            response = gtts.gTTS(text=audio, lang='en')
            file = "speech.mp3"
            eel.js_textbox(audio)
            response.save(file)
            playsound.playsound(file)
            os.remove(file)

        elif "1" in output:
            if osName == 'Windows' and int(Version) >= 7:
                engine.setProperty('rate', 180)
                engine.setProperty('voice', voices[1].id)
            elif osName == 'Linux':
                engine.setProperty('voice', voices[11].id)

            engine.say(audio)
            print(audio)
            eel.js_textbox(audio)
            engine.runAndWait()
    except Exception as e:
        print(f"Error in speak function: {e}")
    return audio

# Function to take voice command input
def takeCommand(var='0', exception=''):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        eel.js_listenebox("Listening...")
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        eel.js_listenebox("Recognizing...")
        print("Recognizing...")
        time.sleep(1)
        query = r.recognize_google(audio, language='en-in').lower()
        query = query.replace('pass', 'pause')
        time.sleep(2)
        eel.js_listenebox(query)
        print(f"User said: {query}\n")
        eel.js_rightbox(query)
    except Exception as e:
        print(f"Error recognizing audio: {e}")
        if exception:
            speak(exception, var)
        return ""
    
    eel.js_listenebox("")
    return query

# Function to find profiles in the database
def ProfileFinder(table, inputs):
    try:
        con = sqlite3.connect('memory.db')
        cursorObj = con.cursor()

        if table == 'AssistantDetails':
            cursorObj.execute(f"SELECT Name FROM AssistantDetails WHERE Assistants LIKE '%{inputs}%'")
        elif table == 'MyDetails':
            cursorObj.execute(f"SELECT answers FROM MyDetails WHERE questions LIKE '%{inputs}%'")
        elif table == 'EmailIds':
            cursorObj.execute(f"SELECT emailId FROM EmailIds WHERE Name LIKE '%{inputs}%'")

        rows = cursorObj.fetchall()
        queries = [row[0] for row in rows]

        filterVal = []
        for query in queries:
            try:
                filterVal.append(b64decode(query.encode()).decode())
            except Exception as e:
                print(f"Error decoding base64: {e}")
                filterVal.append(query)

        return filterVal

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []

    finally:
        if con:
            con.close()
