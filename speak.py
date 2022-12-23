engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[2].id)
engine.setProperty('rate',168)
engine.setProperty('volume', 2.0)
engine.runAndWait()
    
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
