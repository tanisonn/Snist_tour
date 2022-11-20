import speech_recognition as a
l =a.Recognizer()
try:
    print("hi")
    with a.Microphone() as b:
        print("I am listening.....")
        v=l.listen(b)
        print("1")
        c = l.recognize_google(v)
        print("2")
        print(c)
        
except:
    pass
