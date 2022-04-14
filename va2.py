import pyttsx3 as p
import speech_recognition as sr


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


r=sr.Recognizer()

speak("Hello sir i am your voice assistant How are you?")

with sr.Microphone() as source:
    r.enery_threshould=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening....")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)
if "what" and "about" and "you" in text:
    speak("i am having a good day sir")
speak("what can i do for you??")
