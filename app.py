# pip install SpeechRecognition

# pip install PyAudio

import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
	print("Some thing")
	audio = r.listen(source)
	print("Some thing")

try: 
	print("Text: "+r.Recognize_google(audio, language = 'vi-VN'))
except:
	pass	