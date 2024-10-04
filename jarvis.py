import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit

import openai

audio = sr.Recognizer
maquina = pyttsx3.init()

def listen_command():
    try:
        with sr.Microphone() as source:
            print("Escutando... ")
            voz = audio.listen(source)
            comando = audio.recognize.google(voz, language='pt-BR')
            comando = comando.lower()

            if 'jarvis' in comando:
                comando = comando.replace('jarvis','')
                maquina.say(comando)
                maquina.runAndWait()
    except Exception as e:
        print(f'Um erro inesperado aconteceu: {e}')

    return comando

def execute_command():
    comando = listen_command()
    if 'procure por' in comando:
        procurar = comando.replace("procure por", "")
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar,2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()
