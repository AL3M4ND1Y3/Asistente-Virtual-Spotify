import pyttsx3
import speech_recognition as sr
import pywhatkit
import webbrowser
import datetime
import wikipedia
import os
import spotify

client_id = '04a53104dcd24b90b51bd32d9335507a'
client_secret = 'a91f56677b6a4c96ba4c816d3171369d'
username = "21luhlbi3qc2a5ln6u4yzlgry"

#Escuchar el microfono y convertilo en texto
def  escuchar_convertir():
    
    #Almacenar la voz

    r = sr.Recognizer()

    #Configurar
    with sr.Microphone() as origen:

        #Tiempo de espera
        r.pause_threshold = 0.5

        #Informar que escucha 
        print("Te escucho")

        #Guardar en una variale el audio

        audio = r.listen(origen)

        try:
            #Buscar en google lo que escucha
            pedido = r.recognize_google(audio,language="es-arg")

            #prueba de que ingresa
            print("Dijiste: " + pedido  )

            #devolver a pedido
            return pedido
        except sr.UnknownValueError:
            print("No puede entender lo que me dijiste")

            return "sigo esperando"
        except sr.RequestError:
            print("Me pediste algo que no puedo lograr")

            return "sigo esperando"
        
        except:
            print("En este momento no puedo ayudarte")

            return "sigo esperando"

def hablar(mensaje):
    #Encender la voz
    engine = pyttsx3.init()

    #Hablar
    engine.say(mensaje)
    engine.runAndWait()


def pedir_dia():

    # crear variable con datos de hoy
    dia = datetime.date.today()
    print(dia)

    # crear variable para el dia de semana
    dia_semana = dia.weekday()
    print(dia_semana)

    # diccionario con nombres de dias
    calendario = {0: 'Lunes',
                  1: 'Martes',
                  2: 'Miércoles',
                  3: 'Jueves',
                  4: 'Viernes',
                  5: 'Sábado',
                  6: 'Domingo'}

    # decir el dia de la semana
    hablar(f'Hoy es {calendario[dia_semana]}')


# informar que hora es
def pedir_hora():

    # crear una variab;e con datos de la hora
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
    print(hora)

    # decir la hora
    hablar(hora)

def saludo():
    #Decir el saludo
    hablar("Hola, Soy tu asistente virtual, dime en que te puedo ayudar?")


def centro_comandos():
    saludo()    
    recibido = True                                                             

    while recibido == True:     
        #activar el microfono
        pedido = escuchar_convertir()

        if 'abrir youtube' in pedido:
            hablar("Abriendo Youtube")
            webbrowser.open("https://www.youtube.com")
            continue
        elif "abrir navegador" in pedido:
            os.system("start brave.exe") #Windows
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif "busca en wikipedia" in pedido:
            hablar("Buscando en wikipedia")
            pedido = pedido.replace("wikipedia", "")
            wikipedia.set_lang("es")
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar("Lo que encontre fue")
            hablar(resultado)
        elif "búscame" in pedido:
            hablar("Buscando en Google")
            pedido = pedido.replace("búscame", "")
            pywhatkit.search(pedido)
            hablar("esto es lo que encontre")
            continue    
        elif "canción" in pedido:
                pedido.lower()
                print(pedido)
                spotify.spotify(pedido)
        elif "ya no quiero nada" in pedido :
            hablar("Apagandome...")
            recibido = False
            continue
centro_comandos()