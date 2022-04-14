
import pyttsx3 as p
import speech_recognition as sr
from selenium import webdriver
import randfacts
#from YT_auto import *
import requests
import pyjokes
import datetime
import time


engine =p.init()
rate=engine.getProperty('rate')
engine.setProperty('rate',130)
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)


#print(voices)
#print(rate)
#engine.say("hell Rehan  my name is Ali")
#engine.say("Hello there i am your Siri")
#engine.runAndWait()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Sir !")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon Sir !")  
  
    else:
        speak("Good Evening Sir !")


#url="https://official-joke-api.appspot.com/random_joke"
#json_data=requests.get(url).json()

#arr=["",""]
#arr[0]=json_data["setup"]
#arr[1]=json_data["punchline"]

#def joke():
#    return arr

# class camera():
#     def detect_face():
#         cascPath=os.path.dirname(cv2.__file__)+"/data/haarcascade_frontalface_default.xml"
#     faceCascade = cv2.CascadeClassifier(cascPath)
#     video_capture = cv2.VideoCapture(0)

#     while True:
#         # Capture frame-by-frame
#         ret, frames = video_capture.read()

#         gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

#         faces = faceCascade.detectMultiScale(
#                 gray,
#                 scaleFactor=1.1,
#                 minNeighbors=5,
#                 minSize=(30, 30),
#                 flags=cv2.CASCADE_SCALE_IMAGE
#                 )

#         # Draw a rectangle around the faces
#         for (x, y, w, h) in faces:
#             cv2.rectangle(frames, (x, y), (x+w, y+h), (0, 255, 0), 2)

#         # Display the resulting frame
#         cv2.imshow('Video', frames)
#         speak("detecting face")
#         print("Detecting face.....")
#         time.sleep(10)      
#         pyautogui.press('q')
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     video_capture.release()
#     cv2.destroyAllWindows()
 
def calculator():
        global query
        
        if 'add' in query or 'edi' in query:
            speak('Enter a number')
            a = float(input("Enter a number:"))
            speak('Enter another number to add')
            b = float(input("Enter another number to add:"))
            c = a+b
            print(f"{a} + {b} = {c}")
            speak(f'The addition of {a} and {b} is {c}. Your answer is {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'y' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
                
        elif 'sub' in query:
            speak('Enter a number')
            a = float(input("Enter a number:"))
            speak('Enter another number to subtract')
            b = float(input("Enter another number to subtract:"))
            c = a-b
            print(f"{a} - {b} = {c}")
            speak(f'The subtraction of {a} and {b} is {c}. Your answer is {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'y' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
                    
        elif 'mod' in query:
            speak('Enter a number')
            a = float(input("Enter a number:"))
            speak('Enter another number')
            b = float(input("Enter another number:"))
            c = a%b
            print(f"{a} % {b} = {c}")
            speak(f'The modular division of {a} and {b} is equal to {c}. Your answer is {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'y' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
                    
        elif 'div' in query:
            speak('Enter a number as dividend')
            a = float(input("Enter a number:"))
            speak('Enter another number as divisor')
            b = float(input("Enter another number as divisor:"))
            c = a/b
            print(f"{a} / {b} = {c}")
            speak(f'{a} divided by {b} is equal to {c}. Your answer is {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'y' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
        elif 'multi' in query:
            speak('Enter a number')
            a = float(input("Enter a number:"))
            speak('Enter another number to multiply')
            b = float(input("Enter another number to multiply:"))
            c = a*b
            print(f"{a} x {b} = {c}")
            speak(f'The multiplication of {a} and {b} is {c}. Your answer is {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'y' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
        elif 'square root' in query:
            speak('Enter a number to find its sqare root')
            a = float(input("Enter a number:"))
            c = a**(1/2)
            print(f"Square root of {a} = {c}")
            speak(f'Square root of {a} is {c}. Your answer is {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'y' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
        elif 'square' in query:
            speak('Enter a number to find its sqare')
            a = float(input("Enter a number:"))
            c = a**2
            print(f"{a} x {a} = {c}")
            speak(f'Square of {a} is {c}. Your answer is {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'y' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
        elif 'cube root' in query:
            speak('Enter a number to find its cube root')
            a = float(input("Enter a number:"))
            c = a**(1/3)
            print(f"Cube root of {a} = {c}")
            speak(f'Cube root of {a} is {c}. Your answer is {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'y' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
        elif 'cube' in query:
            speak('Enter a number to find its sqare')
            a = float(input("Enter a number:"))
            c = a**3
            print(f"{a} x {a} x {a} = {c}")
            speak(f'Cube of {a} is {c}. Your answer is {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'y' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
                
        elif 'fact' in query:
            try:
                n = int(input('Enter the number whose factorial you want to find:'))
                fact = 1
                for i in range(1,n+1):
                    fact = fact*i
                print(f"{n}! = {fact}")
                speak(f'{n} factorial is equal to {fact}. Your answer is {fact}.')
                speak('Do you want to do another calculation?')
                query = takeCommand().lower()
                if 'y' in query:
                    speak('ok which calculation you want to do?')
                    query = takeCommand().lower()
                    calculator()
                else:
                    speak('ok')
            except Exception as e:
                #print(e)
                speak('I unable to calculate its factorial.')
                speak('Do you want to do another calculation?')
                query = takeCommand().lower()
                if 'y' in query:
                    speak('ok which calculation you want to do?')
                    query = takeCommand().lower()
                    calculator()
                else:
                    speak('ok')
                    
        elif 'power' in query or 'raise' in query:
            speak('Enter a number whose power you want to raised')
            a = float(input("Enter a number whose power to be raised :"))
            speak(f'Enter a raised power to {a}')
            b = float(input(f"Enter a raised power to {a}:"))
            c = a**b
            print(f"{a} ^ {b} = {c}")
            speak(f'{a} raise to the power {b} = {c}. Your answer is {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'y' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
        
                
        elif 'percent' in query:
            speak('Enter a number whose percentage you want to calculate')
            a = float(input("Enter a number whose percentage you want to calculate :"))
            speak(f'How many percent of {a} you want to calculate?')
            b = float(input(f"Enter how many percentage of {a} you want to calculate:"))
            c = (a*b)/100
            print(f"{b} % of {a} is {c}")
            speak(f'{b} percent of {a} is {c}. Your answer is {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'y' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
            
        elif 'interest' in query:
            speak('Enter the principal value or amount')
            p = float(input("Enter the principal value (P):"))
            speak('Enter the rate of interest per year')
            r = float(input("Enter the rate of interest per year (%):"))
            speak('Enter the time in months')
            t = int(input("Enter the time (in months):"))            
            interest = (p*r*t)/1200
            sint = round(interest)
            fv = round(p + interest) 
            print(f"Interest = {interest}")
            print(f"The total amount accured, principal plus interest, from simple interest on a principal of {p} at a rate of {r}% per year for {t} months is {p + interest}.")
            speak(f'interest is {sint}. The total amount accured, principal plus interest, from simple interest on a principal of {p} at a rate of {r}% per year for {t} months is {fv}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'y' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
    
        



class music():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='F:/py/chromedriver.exe')
    def play(self,query):
        self.query=query
        self.driver.get(url="https://www.youtube.com/results?search_query="+query)
        video = self.driver.find_element_by_xpath('//*[@id="dismissible"]')
        video.click()

class infow():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='F:/py/chromedriver.exe')
    
    def get_info(self,query):
        self.query=query
        self.driver.get(url="https://www.wikipedia.org")
        search = self.driver.find_element_by_xpath('//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button/i')
        enter.click()


r=sr.Recognizer()
wishMe()
h="Hello sir i am your voice assistant How are you?"
print(h)
speak(h)


with sr.Microphone() as source:
    r.enery_threshould=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening....")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)
    
if "what" and "about" and "you" in text:
    speak("i am also having a good day sir")
h2="what can i do for you?"
print(h2)
speak(h2)


with sr.Microphone() as source:
    r.enery_threshould=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening...")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)
    print(text2)

if "information" in text2:

    h3="you need information related to with topic"
    print(h3)
    speak(h3)

    with sr.Microphone() as source:
        r.enery_threshould=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("listening...")
        audio = r.listen(source)
        infor = r.recognize_google(audio)
        print(infor)
    speak("searching {} in wikipedia".format(infor))
    assist=infow()
    assist.get_info(infor)

elif 'video' and 'play' in text2:
    h4="you want me to play which video?"
    print(h4)
    speak(h4)

    with sr.Microphone() as source:
        r.enery_threshould=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("listening...")
        audio = r.listen(source)
        vid = r.recognize_google(audio)
        print(vid)
    speak("playing {} in youtube".format(vid))
    assist=music()
    assist.play(vid)



elif "fact" or "facts" in text2:
    speak("Sure sir,")
    x=randfacts.getFact()
    print(x)
    speak("Did you know that, "+x)
    

elif "joke" or "jokes" in text2:
    speak("sure sir, get ready for some chukles")
    #arr=joke()
    #print(arr[0])
    #speak(arr[0])
    #print(arr[1])
    #speak(arr[1])
    My_joke = pyjokes.get_joke(language="en", category="neutral")
    print(My_joke)

elif "send message " in text2:
                # You need to create an account on Twilio to use this service
                account_sid = 'Account Sid key'
                auth_token = 'Auth token'
                client = Client(account_sid, auth_token)
 
                message = client.messages \
                                .create(
                                    body = takeCommand(),
                                    from_='Sender No',
                                    to ='Receiver No'
                                )
 
                print(message.sid)


elif "calculator" in text2:
    with sr.Microphone() as source:
        r.enery_threshould=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("listening...")
        assist=cal()
        assist.calculator(vid)

elif 'amazon' in text2:
            webbrowser.open('https://www.amazon.com')
            time.sleep(10)
elif 'flipkart' in text2:
            webbrowser.open('https://www.flipkart.com')
            time.sleep(10)







