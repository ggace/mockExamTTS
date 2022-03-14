import pyttsx3
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # 한국어



engine.save_to_file("", "test.mp3")

engine.runAndWait()



engine.stop()