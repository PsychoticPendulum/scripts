# Python program to translate
# speech to text and text to speech
 
 
import speech_recognition as sr
import os
 
r = sr.Recognizer()
     
def HandleText(text):
    text = text.split(" ")
    if len(text) == 1:
        print(text)
        return

    if text[0] == "light":
        text[0] = "light/hall"
    
    os.system(f"mosquitto_pub -h 192.168.4.37 -t {text[0]} -m {text[1]}")

while(1):   
    try:
        with sr.Microphone() as source:
            # r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)
             
            text = r.recognize_google(audio).lower()
            HandleText(text)
             
    except KeyboardInterrupt:
        print("Exiting ...")
        exit(0)
    except:
        pass 