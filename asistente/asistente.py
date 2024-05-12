import speech_recognition as sr
import pyttsx3
import pywhatkit



escuchar = sr. Recognizer()

inicializar = pyttsx3.init()

velocidad_de_voz = 140
inicializar.setProperty('rate', velocidad_de_voz)
nombre = "maria"

def habla(texto):
    inicializar.say(texto)
    inicializar.runAndWait()


def tomar():
 try:
    with sr.Microphone() as voz:
        print("ESCUCHANDO...............")
        voice = escuchar.listen(voz)
        command = escuchar.recognize_google(voice)
        command = command.lower()
        if nombre in command:
            command = command.replace(nombre,"")
            print(command)
 except:
    pass
 return command


def maria():
   command = tomar()
   if "reproduce" in command:
      cancion = command.replace("reproduce",'')
      habla("reproduciondo a " + cancion)
      pywhatkit.playonyt(cancion)
   
maria()



