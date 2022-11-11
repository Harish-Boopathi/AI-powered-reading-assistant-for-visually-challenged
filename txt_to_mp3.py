fh = open("/home/techocular/Documents/sih/result/output.txt", "r")
myText = fh.read().replace("\n", " ")
language = 'en'
try:
    output = gTTS(text=myText, lang=language, slow=False)
    output.save("/home/techocular/Documents/sih/result/output.mp3")
    fh.close()
except AssertionError:
    speak("no text to read")
    continue
