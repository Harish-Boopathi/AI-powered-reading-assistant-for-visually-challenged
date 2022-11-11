if 'play' in query:
    mixer.init()
    mixer.music.load("/home/techocular/Documents/sih/result/output.mp3")         
    mixer.music.set_volume(1.5)
    mixer.music.play()

elif 'audio' in query:
    mixer.init()
    mixer.music.load("/home/techocular/Documents/sih/result/output.mp3")         
    mixer.music.set_volume(1.5)
    mixer.music.play()

elif 'pass' in query:
    mixer.music.pause()
    
elif 'pause' in query:
    mixer.music.pause()
    
elif query == "0<=query<=1":
    v = 'query'
    mixer.music.set_volume(v)
    
elif 'continue' in query:
    mixer.music.unpause()
    
elif 'replay' in query:
    mixer.init()
    mixer.music.load("/home/techocular/Documents/sih/result/output.mp3")         
    mixer.music.set_volume(1.5)
    mixer.music.play()
    
elif 'reply' in query:
    mixer.init()
    mixer.music.load("/home/techocular/Documents/sih/result/output.mp3")         
    mixer.music.set_volume(1.5)
    mixer.music.play()
    
elif 'stop' in query:
 # Stop the mixer
     mixer.music.stop()
  
elif 'exit' in query:
     break 
