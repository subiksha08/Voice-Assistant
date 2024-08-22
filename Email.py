from Process import *

def sendEmail(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
        # Make sure to give app access in your Google account
    print(ProfileFinder('MyDetails','EmailId')[0])
    print(ProfileFinder('MyDetails','Password')[0])
    server.login(ProfileFinder('MyDetails','EmailId')[0],ProfileFinder('MyDetails','Password')[0])
    email = EmailMessage()
    email['From'] = ProfileFinder('MyDetails','EmailId')[0]
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)

count8 = 0  

def EmailBot(var):
    try:
        speak('To Whom you want to send email',var)   
        # name = input("Enter ")
        name = eel.js_inputBox('Enter Name or Mail Address:')()
        print(name)
        
        count1 = 0
        while name == None and count1 < 1:
            time.sleep(3)
            name = eel.js_inputBox("Enter Name or Mail Address:")()
            time.sleep(3)
            print(name)
            count1 += 1
                  
        while name == "" and count8 < 1:
            speak("Say the name again please",var)
            EmailBot(var)
            count8 += 1    
            
        else:  
            test = name.find('@')
            print(test)  
            if test == -1:
                receiver = ProfileFinder('EmailIds',name)[0]
                print(receiver)
                eel.js_textbox(f"Send mail to {receiver}")

            else:
                receiver = name
                print(receiver)
                eel.js_textbox(f"Send mail to {receiver}")
           
            speak('What is the subject of your email?',var)
            subject = takeCommand(var,'')
            count4 = 0
            while subject == '' and count4 < 1:
                subject = takeCommand(var,'')
                count4 += 1
            speak('Tell me the body of your email',var)
            message = takeCommand(var,"")
            count5 = 0
            while message == '' and count5 < 1:
                    message = takeCommand(var,"")
                    count5 += 1
                    
            sendEmail(receiver, subject, message)
            speak("Email has been sent!",var)
                   
    except Exception as e:
        print(e)
        speak("Sorry my friend. I am not able to send this email",var)    


sendEmail('mohamedshameer573@gmail.com',"hello",'world')