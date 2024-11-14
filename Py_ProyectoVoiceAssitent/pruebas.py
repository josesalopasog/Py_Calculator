import speech_recognition as sr

# Listar los micrófonos disponibles
mic_list = sr.Microphone.list_microphone_names()

print("Micrófonos disponibles:")
for i, mic_name in enumerate(mic_list):
    print(f"{i}: {mic_name}")

# Selecciona el micrófono por su índice
mic_index = int(input("Elige el número del micrófono que quieres usar: "))

# Crear una instancia del micrófono seleccionado
with sr.Microphone(device_index=mic_index) as origen:
    recognizer = sr.Recognizer()
    print("Ajustando el nivel de ruido ambiental...")
    recognizer.adjust_for_ambient_noise(origen)
    print("Escuchando...")
    audio = recognizer.listen(origen)

# Procesar el audio capturado
try:
    texto = recognizer.recognize_google(audio, language='es-ES')
    print("Dijiste: " + texto)
except sr.UnknownValueError:
    print("No se pudo entender el audio")
except sr.RequestError as e:
    print(f"Error al solicitar resultados del servicio Google Speech Recognition; {e}")