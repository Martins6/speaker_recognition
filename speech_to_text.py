import speech_recognition as sr
import pyaudio

listen = True
r = sr.Recognizer() 
while listen == True:
    with sr.Microphone() as source:
        #os.system('reset')  # for clearing the terminal.
        print("Say listen to start listening")
        r.adjust_for_ambient_noise(source)  # Eleminating the noise.
        audio = r.listen(source)  # Storing audio.
        print(type(audio))
        with open("Data/microphone-results.wav", "wb") as f:
            f.write(audio.get_wav_data())
        pinger = r.recognize_google(audio)  # Converting speech to text
        print(pinger)
        listen = False
        #if pinger == 'stop':
        #    listen = False