import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

#Voces disponibles 
id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
id2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
id3 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0'
id4 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'

#Escuchar nuestro microfono y devolver el audio como texto  
def voice_to_text():
    #Almacenar recognize en una variable 
    recognizer = sr.Recognizer()
    #Configurar el microfono 
    with sr.Microphone(device_index=1) as origen:
        print("Ajustando el nivel de ruido ambiental...")
        recognizer.adjust_for_ambient_noise(origen)
        print("Escuchando...")
        audio = recognizer.listen(origen)
        try:
            #Buscar en google lo que haya escuchado
            texto = recognizer.recognize_google(audio, language="es-ar")
            #Prueba de que pudo ingresar
            print("Dijiste: "+ texto) 
            #Devolver pedido
            return texto
        except sr.UnknownValueError:
            #Prueba de que no comprendio el audio 
            print("No te entendi")
            return "Repite"
        except sr.RequestError:
            print("No te esuche")
            return "Repite"
        except:
            print("Algos salio mal")
            return "Repite"

#Funcion para que el asistente pueda ser escuchado 
def speak(mensaje):
    #Enecender el motor pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice',id4)
    #Pronunciar mensaje 
    engine.say(mensaje)
    engine.runAndWait()

#Mirar voces disponibles para el speech 
def voices_available():
    id_voice = []
    engine = pyttsx3.init()
    for voice in engine.getProperty('voices'):
        id_voice.append(voice)
    return id_voice
    
#Informar el día de la semana
def pedir_dia():
    #Crear variable con datos de hoy
    dia=datetime.date.today()
    print(dia)
    #Crear variable con datos de la semana
    dia_semana=dia.weekday()
    print(dia_semana)
    
    #Diccionario 
    calendario = {0: 'Lunes',
                  1: 'Martes',
                  2: 'Miércoles',
                  3: 'Jueves',
                  4: 'Viernes',
                  5: 'Sábado',
                  6: 'Domingo'}
    #Decir día de la semana
    speak(f"El día de hoy es {calendario[dia_semana]}")

#Informar que hora es 
def pedir_hora():
    #Crear variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f"Son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos"
    speak(hora)
    
def saludo_incial():
    #Crear variable con datos de hora 
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour> 20:
        momento = 'Buenas noches'
    elif 6<=hora.hour<=13:
        momento = 'Buenos días'
    else: 
        momento = 'Buenas tardes'
    speak(f'{momento}, soy Elevi tu asistente personal. ¿En que te puedo ayudar?')   

def pedir():
    #Activar saludo inicial
    saludo_incial()
    #Variable de corta
    start = True
    #Main loop
    while start:
        #Activar el microfono y guardar el audio en texto
        request = voice_to_text().lower()
        if 'abrir youtube' in request:
            speak("Abriendo youtube...")
            webbrowser.open('https://www.youtube.com/')
            continue
        elif 'abrir navegador' in request:
            speak("Abriendo Google...")
            webbrowser.open('https://www.google.com/')
            continue
        elif 'qué día es hoy' in request:
            pedir_dia()
        elif 'qué hora es' in request:
            pedir_hora()
        elif 'busca en wikipedia' in request:
            request = request.replace('wikipedia','')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(request, sentences=1)
            speak("Wikipedia dice lo siguiente: ")
            speak(resultado)
            continue
        elif 'buscar en internet' in request:
            speak('Claro que si.')
            request = request.replace('busca en internet','')
            pywhatkit.search(request)
            speak('Esto es lo que he encontrado; ')
            continue
        elif 'adiós' in request:
            speak("Hasta luego, que estes bien!")
            break


pedir()        
