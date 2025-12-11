# ESTO ES UN ASISTENTE VIRTUAL HECHO POR ALVAROOOO

import time
import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
import random
import subprocess
import requests
from num2words import num2words
import os
import psutil
import json
import threading
import socket


# Opciones de voz/idioma
id1 = "com.apple.speech.synthesis.voice.juan"
id2 = "com.apple.speech.synthesis.voice.diego"
id3 = "com.apple.speech.synthesis.voice.jorge"

frases = (
    "El éxito es la suma de pequeños esfuerzos repetidos día tras día.",
    "La única manera de hacer un gran trabajo es amar lo que haces.",
    "No te rindas, cada fracaso es un paso más hacia el éxito.",
    "El optimismo es la fe que lleva al logro.",
    "Cree en ti mismo y todo será posible.",
    "Cada día es una nueva oportunidad para brillar.",
    "Lo que haces hoy puede mejorar todos tus mañanas.",
    "Si puedes soñarlo, puedes lograrlo.",
    "La vida es un viaje, no un destino.",
    "El miedo es solo una ilusión, la valentía es real.",
    "No importa lo lento que avances, siempre y cuando no te detengas.",
    "Sé fuerte ahora porque las cosas mejorarán.",
    "Nunca es tarde para ser quien podrías haber sido.",
    "Cambia tus pensamientos y cambiarás tu mundo.",
    "El único lugar donde el éxito viene antes del trabajo es en el diccionario.",
    "Los sueños no funcionan a menos que tú trabajes por ellos.",
    "El fracaso es solo la oportunidad de comenzar de nuevo con más experiencia.",
    "Haz hoy lo que otros no quieren, haz mañana lo que otros no pueden.",
    "Si vas a dudar de algo, duda de tus límites.",
    "El dolor es temporal, el orgullo es para siempre.",
    "No cuentes los días, haz que los días cuenten.",
    "No esperes a que las condiciones sean perfectas para empezar.",
    "Hazlo con miedo, pero hazlo.",
    "Tú eres más fuerte de lo que piensas.",
    "Cada pequeño paso cuenta.",
    "La disciplina vence al talento cuando el talento no se disciplina.",
    "Todo es difícil antes de ser fácil.",
    "No tienes que ser el mejor, solo mejor que ayer.",
    "Enfócate en el progreso, no en la perfección.",
    "Actitud es una pequeña cosa que hace una gran diferencia."
)

datos_curiosos = [
    "Los pulpos tienen tres corazones, y cuando nadan, uno se detiene.",
    "La miel nunca se echa a perder. ¡Frascos en tumbas egipcias todavía eran comestibles!",
    "Los plátanos son radiactivos. Contienen potasio-40.",
    "El tiburón de Groenlandia puede vivir más de 400 años.",
    "Las vacas tienen mejores amigas y se estresan cuando están separadas.",
    "El corazón de una ballena azul pesa lo mismo que un coche pequeño.",
    "Los flamencos nacen grises, no rosados.",
    "Las cebras no pueden dormir solas, necesitan compañía.",
    "Tu estómago se renueva cada 3 o 4 días para no digerirse a sí mismo.",
    "Las mariposas saborean con sus patas.",
    "La Tierra pesa 5,972 trillones de toneladas.",
    "El Sol representa el 99.86% de la masa del sistema solar.",
    "Hay más estrellas en el universo que granos de arena en todas las playas.",
    "Las ratas y los caballos no pueden vomitar.",
    "El récord de estornudos consecutivos es de 978 días.",
    "Los elefantes no pueden saltar.",
    "Los gatos tienen 32 músculos en cada oreja.",
    "Una cucharadita de estrella de neutrones pesaría 6 mil millones de toneladas.",
    "Las hormigas no duermen.",
    "Hay más árboles en la Tierra que estrellas en la Vía Láctea."
]

palabras_del_dia = [
    {"palabra": "Efímero", "significado": "Que dura poco tiempo."},
    {"palabra": "Resiliencia", "significado": "Capacidad de adaptarse y superar la adversidad."},
    {"palabra": "Inmarcesible", "significado": "Que no puede marchitarse o corromperse."},
    {"palabra": "Serendipia", "significado": "Descubrimiento afortunado e inesperado."},
    {"palabra": "Perenne", "significado": "Que dura indefinidamente o que se mantiene constante."},
    {"palabra": "Lúgubre", "significado": "Triste, sombrío o melancólico."},
    {"palabra": "Inefable", "significado": "Tan increíble que no se puede expresar con palabras."},
    {"palabra": "Vorágine", "significado": "Agitación intensa de gente o cosas en movimiento."},
    {"palabra": "Acendrado", "significado": "Puro, sin mancha ni defecto."},
    {"palabra": "Epifanía", "significado": "Revelación o manifestación repentina de algo importante."},
    {"palabra": "Onírico", "significado": "Relacionado con los sueños."},
    {"palabra": "Melifluo", "significado": "Que tiene una dulzura excesiva o empalagosa."},
    {"palabra": "Ecléctico", "significado": "Que combina elementos de diferentes estilos o ideas."},
    {"palabra": "Estoico", "significado": "Que muestra fortaleza ante la adversidad sin quejarse."},
    {"palabra": "Irrisorio", "significado": "Tan pequeño o ridículo que provoca risa o burla."},
    {"palabra": "Candor", "significado": "Inocencia o sinceridad extrema."},
    {"palabra": "Diletante", "significado": "Persona que se interesa superficialmente por el arte o la ciencia."},
    {"palabra": "Ataraxia", "significado": "Estado de serenidad y ausencia de perturbación."},
    {"palabra": "Aciago", "significado": "Desgraciado, que presagia algo malo."},
    {"palabra": "Ubiquidad", "significado": "Capacidad de estar en varios lugares al mismo tiempo."}
]

# Diccionario con criptomonedas y metales preciosos
activos = {
    # Criptomonedas
    "bitcoin": "BTC-USD",
    "ethereum": "ETH-USD",
    "tether": "USDT-USD",
    "binance coin": "BNB-USD",
    "solana": "SOL-USD",
    "cardano": "ADA-USD",
    "ripple": "XRP-USD",
    "xrp": "XRP-USD",
    "dogecoin": "DOGE-USD",
    "polkadot": "DOT-USD",
    "avalanche": "AVAX-USD",
    "chainlink": "LINK-USD",
    "litecoin": "LTC-USD",
    "shiba inu": "SHIB-USD",
    "toncoin": "TON-USD",

    # Metales preciosos
    "oro": "GC=F",
    "plata": "SI=F",
    "platino": "PL=F",
    "paladio": "PA=F"
}

# Lista completa de cartas españolas
carta = [
    "As de Corazones", "2 de Corazones", "3 de Corazones", "4 de Corazones", 
    "5 de Corazones", "6 de Corazones", "7 de Corazones", "8 de Corazones", 
    "9 de Corazones", "10 de Corazones", "Jota de Corazones", "Reina de Corazones", "Rey de Corazones",
    "As de Diamantes", "2 de Diamantes", "3 de Diamantes", "4 de Diamantes",
    "5 de Diamantes", "6 de Diamantes", "7 de Diamantes", "8 de Diamantes",
    "9 de Diamantes", "10 de Diamantes", "Jota de Diamantes", "Reina de Diamantes", "Rey de Diamantes",
    "As de Tréboles", "2 de Tréboles", "3 de Tréboles", "4 de Tréboles",
    "5 de Tréboles", "6 de Tréboles", "7 de Tréboles", "8 de Tréboles",
    "9 de Tréboles", "10 de Tréboles", "Jota de Tréboles", "Reina de Tréboles", "Rey de Tréboles",
    "As de Picas", "2 de Picas", "3 de Picas", "4 de Picas",
    "5 de Picas", "6 de Picas", "7 de Picas", "8 de Picas",
    "9 de Picas", "10 de Picas", "Jota de Picas", "Reina de Picas", "Rey de Picas"
]

# Citas de filósofos famosos
citas_filosoficas = [
    "El único conocimiento verdadero es saber que no sabes nada - Sócrates",
    "La vida no examinada no vale la pena vivirla - Sócrates",
    "Pienso, luego existo - René Descartes",
    "El hombre es condenado a ser libre - Jean-Paul Sartre",
    "Conócete a ti mismo - Oráculo de Delfos",
    "La felicidad depende de nosotros mismos - Aristóteles",
    "El futuro pertenece a quienes creen en la belleza de sus sueños - Eleanor Roosevelt",
    "No es lo que nos pasa, sino cómo reaccionamos lo que importa - Epicteto",
    "El tiempo es la cosa más valiosa que podemos gastar - Theophrastus"
]

# Trabalenguas divertidos
trabalenguas = [
    "Tres tristes tigres tragaban trigo en un trigal",
    "Perejil comí, perejil cené, y de tanto perejil me emperejilé",
    "El cielo está enladrillado, quién lo desenladrillará, el desenladrillador que lo desenladrille buen desenladrillador será",
    "Pablito clavó un clavito en la calva de un calvito",
    "Como poco coco como, poco coco compro"
]

# Adivinanzas
adivinanzas = [
    {"pregunta": "Oro parece, plata no es. ¿Qué es?", "respuesta": "plátano"},
    {"pregunta": "Blanca por dentro, verde por fuera. Si quieres que te lo diga, espera", "respuesta": "pera"},
    {"pregunta": "Una señorita muy señoreada, siempre va en coche y siempre va mojada", "respuesta": "lengua"},
    {"pregunta": "Tengo agujas pero no sé coser, tengo números pero no sé leer", "respuesta": "reloj"},
    {"pregunta": "Verde fue mi nacimiento, negro fue mi desarrollo, y ahora de rojo me visto en el árbol", "respuesta": "café"}
]

# Chistes adicionales en español
chistes_propios = [
    "¿Por qué los pájaros vuelan hacia el sur en invierno? Porque caminando tardarían mucho.",
    "¿Cómo se llama un perro mago? Labracadabrador.",
    "¿Qué le dice una iguana a su hermana gemela? Somos iguanitas.",
    "¿Por qué no se puede confiar en las escaleras? Porque siempre están tramando algo.",
    "¿Cómo se despiden los químicos? Ácido un placer."
]

# Consejos de salud y bienestar
consejos_salud = [
    "Bebe al menos 8 vasos de agua al día para mantener tu cuerpo hidratado",
    "Camina al menos 30 minutos diarios para mejorar tu salud cardiovascular",
    "Duerme entre 7-8 horas para que tu cerebro se recupere completamente",
    "Come frutas y verduras de diferentes colores para obtener todos los nutrientes",
    "Practica la respiración profunda para reducir el estrés",
    "Estira tu cuerpo cada mañana para mejorar tu flexibilidad",
    "Mantén una postura correcta mientras trabajas en la computadora"
]

# ========== NUEVAS FUNCIONES AVANZADAS ==========

def abrir_spotify():
    """Abre la aplicación Spotify"""
    try:
        subprocess.run(["open", "-a", "Spotify"])
        hablar("Abriendo Spotify para que disfrutes tu música favorita")
    except:
        hablar("No pude abrir Spotify, ¿lo tienes instalado?")

def estado_sistema():
    """Muestra el estado del sistema"""
    try:
        cpu_percent = psutil.cpu_percent(interval=1)
        memoria = psutil.virtual_memory()
        disco = psutil.disk_usage('/')
        
        mensaje = f"Estado del sistema: CPU al {cpu_percent}%, memoria usada {memoria.percent}%, disco usado {round(disco.percent, 1)}%"
        print(mensaje)
        hablar(mensaje)
    except Exception as e:
        hablar("No pude obtener información del sistema")

def crear_recordatorio():
    """Crea un recordatorio simple"""
    hablar("¿Para cuándo es el recordatorio? Di los minutos")
    try:
        minutos = int(input("Minutos: "))
        hablar("¿Qué quieres que te recuerde?")
        mensaje = input("Mensaje: ")
        
        def recordar():
            time.sleep(minutos * 60)
            hablar(f"Recordatorio: {mensaje}")
            print(f"🔔 RECORDATORIO: {mensaje}")
        
        threading.Thread(target=recordar, daemon=True).start()
        hablar(f"Perfecto, te recordaré '{mensaje}' en {minutos} minutos")
    except:
        hablar("No pude crear el recordatorio")

def juego_adivinanza():
    """Juego de adivinanzas"""
    adivinanza = random.choice(adivinanzas)
    hablar("Te voy a hacer una adivinanza")
    hablar(adivinanza["pregunta"])
    
    print(f"Adivinanza: {adivinanza['pregunta']}")
    respuesta = input("Tu respuesta: ").lower().strip()
    
    if respuesta == adivinanza["respuesta"]:
        hablar("¡Correcto! Eres muy inteligente")
        print("🎉 ¡CORRECTO!")
    else:
        hablar(f"No es correcto, la respuesta era {adivinanza['respuesta']}")
        print(f"❌ Respuesta: {adivinanza['respuesta']}")

def decir_trabalenguas():
    """Dice un trabalenguas"""
    trabalenguas_elegido = random.choice(trabalenguas)
    hablar("Te voy a decir un trabalenguas, a ver si lo puedes repetir")
    hablar(trabalenguas_elegido)
    print(f"Trabalenguas: {trabalenguas_elegido}")

def cita_filosofica():
    """Comparte una cita filosófica"""
    cita = random.choice(citas_filosoficas)
    hablar("Aquí tienes una reflexión filosófica")
    hablar(cita)
    print(f"💭 {cita}")

def consejo_salud():
    """Da un consejo de salud"""
    consejo = random.choice(consejos_salud)
    hablar("Te doy un consejo para cuidar tu salud")
    hablar(consejo)
    print(f"🏥 {consejo}")

def chiste_propio():
    """Cuenta un chiste propio"""
    chiste = random.choice(chistes_propios)
    hablar(chiste)
    print(f"😂 {chiste}")

def obtener_clima():
    """Obtiene información básica del clima (requiere API key)"""
    hablar("Para obtener el clima necesitarías configurar una API key de OpenWeatherMap, pero puedo ayudarte a abrir el clima en línea")
    webbrowser.open("https://weather.com")

def contar_hasta_numero():
    """Cuenta hasta un número especificado"""
    try:
        hablar("¿Hasta qué número quieres que cuente?")
        numero = int(input("Número: "))
        if numero <= 20:
            hablar(f"Voy a contar hasta {numero}")
            for i in range(1, numero + 1):
                print(i)
                hablar(str(i))
                time.sleep(0.5)
            hablar("¡Listo!")
        else:
            hablar("Ese número es muy grande, elige uno menor a 20")
    except:
        hablar("No entendí el número")

def juego_piedra_papel_tijeras():
    """Juego de piedra, papel o tijeras"""
    opciones = ["piedra", "papel", "tijeras"]
    eleccion_pc = random.choice(opciones)
    
    hablar("Juguemos piedra, papel o tijeras. ¿Cuál eliges?")
    eleccion_usuario = input("Tu elección (piedra/papel/tijeras): ").lower()
    
    if eleccion_usuario not in opciones:
        hablar("Opción no válida")
        return
    
    hablar(f"Yo elegí {eleccion_pc}")
    print(f"🤖 Yo: {eleccion_pc}")
    print(f"👤 Tú: {eleccion_usuario}")
    
    if eleccion_usuario == eleccion_pc:
        resultado = "¡Empate!"
    elif ((eleccion_usuario == "piedra" and eleccion_pc == "tijeras") or
          (eleccion_usuario == "papel" and eleccion_pc == "piedra") or
          (eleccion_usuario == "tijeras" and eleccion_pc == "papel")):
        resultado = "¡Ganaste!"
    else:
        resultado = "¡Gané yo!"
    
    hablar(resultado)
    print(f"🏆 {resultado}")

def generar_contrasena():
    """Genera una contraseña segura"""
    import string
    caracteres = string.ascii_letters + string.digits + "!@#$%&*"
    longitud = random.randint(12, 16)
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    
    hablar("Te he generado una contraseña segura")
    print(f"🔐 Contraseña generada: {contrasena}")
    hablar("La puedes ver en la pantalla")

def tareas_pendientes():
    """Sistema simple de tareas"""
    archivo_tareas = "tareas.txt"
    
    hablar("¿Qué quieres hacer? Agregar tarea, ver tareas, o marcar como completada?")
    accion = input("Acción (agregar/ver/completar): ").lower()
    
    if accion == "agregar":
        tarea = input("Nueva tarea: ")
        with open(archivo_tareas, "a", encoding="utf-8") as f:
            f.write(f"[ ] {tarea}\n")
        hablar("Tarea agregada correctamente")
    
    elif accion == "ver":
        try:
            with open(archivo_tareas, "r", encoding="utf-8") as f:
                tareas = f.read()
            if tareas:
                hablar("Aquí tienes tus tareas")
                print("📝 TAREAS:")
                print(tareas)
            else:
                hablar("No tienes tareas pendientes")
        except FileNotFoundError:
            hablar("No tienes tareas guardadas")

def dato_matematico():
    """Comparte datos matemáticos interesantes"""
    datos_matematicos = [
        "El número Pi tiene infinitos decimales y nunca se repite",
        "El número 0 fue inventado en la India alrededor del siglo V",
        "Un googol es 1 seguido de 100 ceros",
        "El número áureo (1.618) aparece frecuentemente en la naturaleza",
        "La probabilidad de que dos personas compartan cumpleaños en un grupo de 23 es del 50%"
    ]
    
    dato = random.choice(datos_matematicos)
    hablar("Aquí tienes un dato matemático fascinante")
    hablar(dato)
    print(f"🔢 {dato}")


def verificar_dependencias():
    """Verifica que las dependencias estén instaladas"""
    dependencias = [
        'pyttsx3', 'speech_recognition', 'pywhatkit', 
        'yfinance', 'pyjokes', 'wikipedia', 'num2words', 'psutil'
    ]
    
    faltantes = []
    for dep in dependencias:
        try:
            __import__(dep.replace('-', '_'))
        except ImportError:
            faltantes.append(dep)
    
    if faltantes:
        print("⚠️  Faltan las siguientes dependencias:")
        for dep in faltantes:
            print(f"   - {dep}")
        print("\nPara instalarlas ejecuta:")
        print(f"pip install {' '.join(faltantes)}")
        return False
    else:
        print("✅ Todas las dependencias están instaladas")
        return True

def mostrar_menu_inicial():
    """Muestra el menú de opciones del asistente"""
    print("\n" + "="*50)
    print("🤖 ASISTENTE VIRTUAL JORGE")
    print("="*50)
    print("Funcionalidades disponibles:")
    print("📱 Aplicaciones: Spotify, calculadora, terminal, notas")
    print("🎮 Juegos: Piedra/papel/tijeras, adivinanzas, volados")
    print("💰 Finanzas: Precios de criptomonedas, acciones, divisas")
    print("🧠 Educativo: Datos curiosos, citas filosóficas, matemáticas")
    print("🎯 Utilidades: Recordatorios, tareas, contraseñas, clima")
    print("🃏 Entretenimiento: Chistes, trabalenguas, cartas, música")
    print("💡 Salud: Consejos de bienestar y salud")
    print("="*50)
    print("Di 'ayuda' para ver todas las opciones")
    print("Di 'adiós' para salir")
    print("="*50 + "\n")

def elegir_modo_entrada():
    """Permite elegir entre voz o texto"""
    print("🎚️  CONFIGURACIÓN DE ENTRADA:")
    print("1. 🎤 Modo voz (requiere micrófono)")
    print("2. ⌨️  Modo texto (escribir comandos)")
    
    while True:
        try:
            opcion = input("Elige opción (1 o 2): ").strip()
            if opcion == "1":
                return "voz"
            elif opcion == "2":
                return "texto"
            else:
                print("❌ Opción inválida, elige 1 o 2")
        except KeyboardInterrupt:
            print("\n👋 ¡Hasta luego!")
            exit()

def obtener_comando(modo):
    """Obtiene el comando según el modo seleccionado"""
    if modo == "voz":
        return transformar_audio_en_texto().lower()
    else:
        print("\n💬 Escribe tu comando:")
        try:
            return input(">> ").lower()
        except KeyboardInterrupt:
            return "adiós"

# Escuchar mi micrófono y devolver audio a texto
def transformar_audio_en_texto():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as origen:
            r.pause_threshold = 0.8
            print("🎤 Ya puedes hablar...")
            audio = r.listen(origen)
            try:
                pedido = r.recognize_google(audio, language="es-MX")
                print(f"📝 Dijiste: {pedido}")
                return pedido
            except sr.UnknownValueError:
                print("❌ No entendí lo que dijiste")
                return "sigo esperando"
            except sr.RequestError:
                print("❌ Sin conexión a internet para reconocimiento de voz")
                return "sigo esperando"
            except Exception as e:
                print(f"❌ Error: {e}")
                return "sigo esperando"
    except Exception as e:
        print(f"❌ Error con el micrófono: {e}")
        print("💡 Usaremos modo texto. Escribe tu comando:")
        return input(">> ").lower()

# Función para que asistente pueda ser escuchado
def hablar(mensaje):
    try:
        engine = pyttsx3.init()
        engine.setProperty("voice", id3)
        engine.say(mensaje)
        engine.runAndWait()
    except Exception as e:
        print(f"🔊 Jorge dice: {mensaje}")
        print(f"⚠️ Error de voz: {e}")
        # Usar comando de sistema de macOS como respaldo
        try:
            subprocess.run(["say", mensaje], check=True)
        except:
            print("💬 (Modo texto solamente)")

# Función alternativa para texto cuando la voz falla
def hablar_texto_only(mensaje):
    print(f"🤖 Jorge: {mensaje}")

# Informar el día de la semana
def pedir_dia():
    dia = datetime.date.today()

    dia_semana = dia.weekday()

    calendario = {
        0: "Lunes",
        1: "Martes",
        2: "Miércoles",
        3: "Jueves",
        4: "Viernes",
        5: "Sábado",
        6: "Domingo"
    }
    hablar(f"Hoy es {calendario[dia_semana]}")

#informar que hora es
def pedir_hora():

    #crear una variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f"En este preciso momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos"
    print(hora)

    #decir la hora
    hablar(hora)

#funcion inicial
def saludo_inicial():

    #crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour >20:
        momento = "Buenas noches"
    elif 6 <= hora.hour < 12:
        momento = "Buen dia"
    else:
        momento = "Buenas Tardes"

    #decir el saludo
    hablar(f"{momento}, soy Jorge, tu asistente virtual, porfavor, dime en que te puedo ayudar")

#funcion volado
def lanzar_moneda():
    resultado = random.choice(["aguila", "sol"])
    hablar(f"He lanzado la moneda y ha salido {resultado}")

# Número al azar del 1 al 100
def numero_al_azar():
    al_azar = random.randint(1, 100)
    hablar(f"He escogido el número {al_azar}")
    print(f"Número al azar: {al_azar}")

#funcion calculadora
def abrir_calculadora():
    hablar("Vamos a hacer unos calculos bien matematicos")
    print("Abriendo la calculadora")
    subprocess.run(["open", "-a", "Calculator"])

#funcion divisas
def obtener_tipo_cambio(base="USD", destino="MXN"):
    try:
        url = f"https://api.frankfurter.app/latest?from={base}&to={destino}"
        response = requests.get(url)
        data = response.json()
        tasa = data["rates"][destino]

        tasa_redondeada = round(tasa, 2)
        tasa_en_palabras = num2words(tasa_redondeada, lang='es')

        mensaje = f"El tipo de cambio actual de {base} a {destino} es de {tasa_en_palabras} pesos."
        print(mensaje)
        hablar(mensaje)

    except Exception as e:
        print(f"Error al obtener tipo de cambio: {e}")
        hablar("Lo siento, ocurrió un error al consultar el tipo de cambio.")

#funcion datos curiosos
def dato_curioso():
    dato = random.choice(datos_curiosos)
    print(f"Dato curioso: {dato}")
    hablar(f"¿Sabías que...? {dato}")

#funcion palabra del dia
def palabra_del_dia():
    palabra = random.choice(palabras_del_dia)
    hablar(f"La palabra del día es {palabra['palabra']}. Significa: {palabra['significado']}")

#funcion central del asistente
def pedir_cosas():
    # Verificar dependencias al inicio
    if not verificar_dependencias():
        print("\n❌ No se puede ejecutar el asistente sin las dependencias.")
        return
    
    # Mostrar menú inicial
    mostrar_menu_inicial()
    
    # Elegir modo de entrada
    modo_entrada = elegir_modo_entrada()
    print(f"\n✅ Modo seleccionado: {modo_entrada}")

    #activar saludo inicial
    saludo_inicial()

    #variable de corte
    comenzar = True

    #loop central
    while comenzar:

        #activar micrófono o teclado según el modo
        pedido = obtener_comando(modo_entrada)
        
        if pedido == "sigo esperando":
            continue

        if "abrir youtube" in pedido:

            hablar("Con gusto, estoy abriendo youtube")

            webbrowser.open("https://www.youtube.com")
            continue

        elif "abrir navegador" in pedido:

            hablar("Claro, estoy en eso")

            webbrowser.open("https://google.com")
            continue

        elif "qué día es hoy" in pedido:

            pedir_dia()
            continue
        elif "qué hora es" in pedido:

            pedir_hora()
            continue
        elif "busca en wikipedia" in pedido:

            hablar("Estoy buscando eso")
            pedido = pedido.replace("busca en wikipedia","")

            wikipedia.set_lang("es")
            resultado = wikipedia.summary(pedido,sentences=1.5)

            hablar("Segun Wikipedia...:")
            hablar(resultado)

        elif "busca en internet" in pedido:
            hablar("Claro que si, ya estoy en eso")

            pedido = pedido.replace("busca en internet","")
            pywhatkit.search(pedido)

            hablar("Esto es lo que he encontrado ")
            continue
        elif "reproducir" in pedido:
            hablar("Ok, ya lo voy a empezar a reproducir en YouTube")
            # Extraer el nombre de la canción/video
            busqueda = pedido.replace("reproducir", "").strip()
            # Abrir YouTube con la búsqueda directamente en el navegador
            url_youtube = f"https://www.youtube.com/results?search_query={busqueda.replace(' ', '+')}"
            webbrowser.open(url_youtube)
            print(f"🎵 Buscando en YouTube: {busqueda}")
            continue

        elif "chiste" in pedido:

            hablar(pyjokes.get_joke("es"))
            continue

        elif "lanza una moneda" in pedido or "haz un volado" in pedido or "cara o cruz" in pedido:
            lanzar_moneda()
            continue

        elif "pagina secreta" in pedido or "página secreta" in pedido or "la página secreta" in pedido:

            hablar("Con que quieres abrir la pagina secreta?... esta bien ya la abro para ti")
            webbrowser.open("https://www.anothersadtrombone.com/")
            continue

        elif "modo pro" in pedido:
            hablar("Activando modo pro.   Lamentablemente necesitas tener el internet de la nasa para abrir este modo.    hay otra opcion.   Recuerda un truco de los juegos antiguos.   Te doy una pista.    Arriba Arriba Abajo Abajo")
            continue

        elif "arriba arriba abajo abajo izquierda derecha izquierda derecha b a start" in pedido:
            hablar("SORPRENDENTE!.  HAS ENCONTRADO EL CODIGO SECRETO.  AQUI ESTA TU RECOMPENSA")
            hablar("comprate algo bonito")
            webbrowser.open("https://www.google.com/imgres?q=peso%20mexicano&imgurl=https%3A%2F%2Fwww.debate.com.mx%2F__export%2F1726167950870%2Fsites%2Fdebate%2Fimg%2F2024%2F09%2F12%2Fcual_es_el_origen_del_peso_mexicano_orlando_samaniego_debate.jpg_1902800913.jpg&imgrefurl=https%3A%2F%2Fwww.debate.com.mx%2Feconomia%2FCual-es-el-origen-del-peso-mexicano-20240912-0140.html&docid=xzE9Tt4PgyGmUM&tbnid=G9DjI_xKI78mBM&vet=12ahUKEwjxycqckuqOAxWbIkQIHSnUIRYQM3oECEoQAA..i&w=1200&h=900&hcb=2&ved=2ahUKEwjxycqckuqOAxWbIkQIHSnUIRYQM3oECEoQAA")
            continue


        elif "precio del" in pedido:
            try:
                # Busca si alguno de los activos está mencionado en el pedido
                activo = None
                for nombre in activos:
                    if nombre in pedido:
                        activo = nombre
                        break

                if activo:
                    ticker = activos[activo]
                    print(f"Buscando ticker: {ticker}")  # Para debugging
                    stock = yf.Ticker(ticker)
                    precio_usd = stock.info["regularMarketPrice"]
                    # Conversión estimada a pesos mexicanos
                    tasa_cambio = 19.0
                    precio_mxn = round(precio_usd * tasa_cambio, 2)
                    mensaje = f"Para hoy, el precio de {activo} es de {precio_usd} dólares, aproximadamente {precio_mxn} pesos mexicanos. ¿Te apetece comprar una?"
                    hablar(f"La encontré. {mensaje}")
                    print(mensaje)
                else:
                    hablar("Lo siento, ese activo no está en mi lista.")
            except Exception as e:
                print(f"Error al buscar el activo: {e}")
                hablar("Perdón, ocurrió un error al consultar ese activo.")


        elif "precio de las acciones" in pedido:

            accion = pedido.split("de")[-1].strip().lower()

            # Diccionario ampliado con más empresas populares

            cartera = {

                "apple": "AAPL",

                "amazon": "AMZN",

                "google": "GOOGL",

                "microsoft": "MSFT",

                "tesla": "TSLA",

                "netflix": "NFLX",

                "zoom": "ZM",

                "alibaba": "BABA",

                "uber": "UBER",

                "3m": "MMM",

                "nvidia": "NVDA",

                "meta": "META",

                "coca cola": "KO",

                "pepsi": "PEP",

                "intel": "INTC",

                "amd": "AMD",

                "starbucks": "SBUX",

                "paypal": "PYPL",

                "disney": "DIS",

                "visa": "V",

                "boeing": "BA",

                "nike": "NKE",

                "ford": "F",

                "walmart": "WMT"

            }

            try:

                if accion in cartera:

                    ticker = cartera[accion]

                    print(f"Buscando ticker: {ticker}")  # Para debugging

                    stock = yf.Ticker(ticker)

                    precio_usd = stock.info["regularMarketPrice"]

                    # Conversión estimada a pesos mexicanos (actualiza si deseas una tasa más precisa)

                    tasa_cambio = 17.0

                    precio_mxn = round(precio_usd * tasa_cambio, 2)

                    mensaje = f"El precio de {accion} es {precio_usd} dólares, aproximadamente {precio_mxn} pesos mexicanos. BASTANTE BARATO JAJA"

                    hablar(f"La encontré. {mensaje}")

                    print(mensaje)

                else:

                    hablar("Lo siento, esa acción no está en mi lista.")

            except Exception as e:

                print(f"Error al buscar acción: {e}")

                hablar("Perdón, ocurrió un error al consultar esa acción.")


        elif "comprar pizza" in pedido:
            hablar("UY. que sabroso. espero que me regales una rebanada. ya te dirijo a las pipsshas")
            webbrowser.open("https://www.dominos.com.mx/")
            continue


        elif "frase motivadora" in pedido or "frase" in pedido or "motivacion" in pedido:
            frase = random.choice(frases)
            print(f"Frase motivadora: {frase}")
            hablar(frase)
            hablar("WOW. QUE POETICO CASI LLORO")

        elif "cine" in pedido:
            hablar("Ojala pudiera ir pero ahi me compartes unas palomitas. ya te dirijo para alla. ")
            webbrowser.open("https://cinepolis.com/")
            continue

        elif "mundo" in pedido:
            hablar("Con que quieres ir a ver  galaxias ya te mando alla")
            webbrowser.open("https://scaleofuniverse.com/en")
            continue

        elif "capilla" in pedido or "sixtina" in pedido:
            hablar("Ya veras lo bonita que es la capilla sixtina")
            webbrowser.open("https://www.museivaticani.va/content/museivaticani/es/collezioni/musei/cappella-sistina/tour-virtuale.html")
            continue

        elif "quién te creó" in pedido or "quién te hizo" in pedido or "quién te desarrolló" in pedido:
            hablar("JAJAJA, interesante pregunta, mi desarrollador se llama Alvaro")
            continue

        elif "abrir calculadora" in pedido or "calculadora" in pedido:
            abrir_calculadora()
            continue

        elif "cuánto está el dólar" in pedido or "valor del dólar" in pedido:
            obtener_tipo_cambio("USD", "MXN")
            continue

        elif "cuánto está el euro" in pedido or "valor del euro" in pedido:
            obtener_tipo_cambio("EUR", "MXN")
            continue

        elif "cuánto está el yen" in pedido:
            obtener_tipo_cambio("JPY", "MXN")
            continue

        elif "cómo estás" in pedido:
            hablar("Muchas gracias por preguntarme eso. Yo estoy bastante bien. y tu?")
            continue

        elif "siri" in pedido or "alexa" in pedido:
            hablar("No me confundaaasss, Ambas son excelentes asistentes virtuales. yo me quedo corto a comparacion de ellas. pero mi programador esta implementandome muchas cosas nuevas que estoy aprendiendo para poder estar a su nivel algun dia")
            continue

        elif "modo norteño" in pedido:
            hablar("¡Échale ganas, compa! Que no se diga que te rajaste, tú dale recio.")
            continue

        elif "modo español" in pedido:
            hablar("Venga tío, no te rayes. A por todas que tú lo petas, ¡hostia ya!")
            continue

        elif "número al azar" in pedido:
            numero_al_azar()
            continue

        elif "cuál es tu canción favorita" in pedido:
            hablar("Muy buena pregunta. soy un asistente virtual pero mi cancion favorita es Not Like Us de Kendrick Lamar. A mi programador tambien le gusta esa cancion")
            continue

        elif "dónde vives" in pedido:
            hablar("Eres bastante curioso. Yo vivo en Pycharm. mi pequeña casita llena de codigo")
            continue

        elif "pumas" in pedido:
            hablar("Ni me hables de ellos jaja. los pumas de la UNAM van cada vez peor en el futbol")
            continue

        elif "qué te hace enojar" in pedido:
            hablar("Como asistente virtual no puedo transmitir emociones. pero a mi programador le enoja que por un parentesis mal puesto el codigo no funcione JAJA")
            continue

        elif "apple" in pedido or "samsung" in pedido:
            hablar("Imagina ser creado por alguno de ellos. pura excelencia informatica")
            continue

        elif "dato curioso" in pedido:
            hablar("Que bueno que quieras aprender,  aqui esta tu dato bien curioso")
            dato_curioso()
            continue

        elif "palabra del día" in pedido:
            hablar("Ya estoy preparando la palabra")
            palabra_del_dia()
            print(palabra_del_dia())
            hablar("Que interesante")
            continue

        elif "dime un secreto" in pedido:
            hablar("ssshhhh no lo puedo decir a nadie, pero si descifras el codigo secreto si")
            continue


        elif "mi certificado" in pedido or "certificado fibonacci" in pedido or "maestro fibonacci" in pedido:
            try:
                archivo_certificado = os.path.join(os.getcwd(), "certificado_fibonacci.html")
                if os.path.exists(archivo_certificado):
                    hablar("Abriendo tu certificado de Maestro Fibonacci")
                    webbrowser.open(f"file://{archivo_certificado}")
                    print("🏅 Certificado abierto en tu navegador")
                else:
                    hablar("Primero debes completar el desafío del código secreto para obtener tu certificado")
            except Exception as e:
                hablar("Hubo un problema al abrir el certificado")
            continue

        elif "código" in pedido:
            hablar("Si la logras descifrar obtendrás un secreto")
            print("1, 2, 3, 5, 8")
            intento = input("¿Cómo se llama esta serie?: ").lower().strip()
            if intento == "fibonacci" or intento == "numero aureo":
                hablar("Lo has descifrado, muchas felicidades, aquí está tu recompensa")
                time.sleep(1)
                hablar("Eres oficialmente un Maestro Fibonacci honorífico. ¡Que nunca te falte la secuencia!")
                print("🏅 Certificado de Maestro Fibonacci 🏅")
                
                # Abrir certificado HTML
                try:
                    archivo_certificado = os.path.join(os.getcwd(), "certificado_fibonacci.html")
                    hablar("Abriendo tu certificado oficial de Maestro Fibonacci")
                    webbrowser.open(f"file://{archivo_certificado}")
                    print("🎉 ¡Certificado abierto en tu navegador!")
                except Exception as e:
                    print(f"Error al abrir certificado: {e}")
                    hablar("Tu certificado está en el archivo certificado_fibonacci.html")
            else:
                hablar("No es correcto, inténtalo de nuevo la próxima vez.")
                print("💡 Pista: Es una famosa secuencia matemática donde cada número es la suma de los dos anteriores")

        elif "mate" in pedido:
            hablar("mmm, Que rico, ya te tomaste tu mate de hoy?, que yerba usaste?")
            continue

        elif "carta" in pedido or "Dime una carta" in pedido:
            hablar("Te diré una carta")
            time.sleep(1.2)
            carta_seleccionada = random.choice(carta)
            hablar(carta_seleccionada)


        # ========== NUEVAS FUNCIONALIDADES ==========
        
        elif "abrir spotify" in pedido or "spotify" in pedido:
            abrir_spotify()
            continue

        elif "estado del sistema" in pedido or "cómo está mi computadora" in pedido:
            estado_sistema()
            continue

        elif "crear recordatorio" in pedido or "recordatorio" in pedido:
            crear_recordatorio()
            continue

        elif "adivinanza" in pedido or "juego de adivinanza" in pedido:
            juego_adivinanza()
            continue

        elif "trabalenguas" in pedido:
            decir_trabalenguas()
            continue

        elif "cita filosófica" in pedido or "frase filosófica" in pedido or "filosofía" in pedido:
            cita_filosofica()
            continue

        elif "consejo de salud" in pedido or "cuidar mi salud" in pedido:
            consejo_salud()
            continue

        elif "chiste nuevo" in pedido or "otro chiste" in pedido:
            chiste_propio()
            continue

        elif "clima" in pedido or "tiempo" in pedido:
            obtener_clima()
            continue

        elif "cuenta hasta" in pedido or "contar números" in pedido:
            contar_hasta_numero()
            continue

        elif "piedra papel tijeras" in pedido or "juguemos" in pedido:
            juego_piedra_papel_tijeras()
            continue

        elif "generar contraseña" in pedido or "contraseña segura" in pedido:
            generar_contrasena()
            continue

        elif "mis tareas" in pedido or "tareas pendientes" in pedido:
            tareas_pendientes()
            continue

        elif "dato matemático" in pedido or "matemáticas" in pedido:
            dato_matematico()
            continue

        elif "abrir terminal" in pedido:
            hablar("Abriendo la terminal para ti")
            subprocess.run(["open", "-a", "Terminal"])
            continue

        elif "abrir notas" in pedido:
            hablar("Abriendo la aplicación de notas")
            subprocess.run(["open", "-a", "Notes"])
            continue

        elif "cerrar aplicación" in pedido:
            hablar("¿Qué aplicación quieres cerrar?")
            app = input("Aplicación a cerrar: ")
            try:
                subprocess.run(["pkill", app])
                hablar(f"He cerrado {app}")
            except:
                hablar("No pude cerrar esa aplicación")
            continue

        elif "crear archivo" in pedido:
            hablar("¿Cómo quieres llamar al archivo?")
            nombre = input("Nombre del archivo: ")
            try:
                with open(f"{nombre}.txt", "w", encoding="utf-8") as f:
                    f.write("# Archivo creado por tu asistente virtual\n")
                hablar(f"He creado el archivo {nombre}.txt")
            except:
                hablar("No pude crear el archivo")
            continue

        elif "cuéntame sobre ti" in pedido:
            hablar("Soy Jorge, tu asistente virtual creado por Álvaro. Puedo ayudarte con muchas tareas: contar chistes, buscar información, reproducir música, jugar contigo, darte consejos de salud, crear recordatorios y mucho más. ¡Estoy aquí para hacer tu día mejor!")
            continue

        elif "qué puedes hacer" in pedido or "ayuda" in pedido:
            hablar("Puedo hacer muchas cosas: reproducir música, buscar en internet, contar chistes, dar el clima, jugar contigo, crear recordatorios, generar contraseñas, darte consejos de salud, citas filosóficas, trabalenguas, adivinanzas, administrar tareas, y mucho más. ¡Solo pídeme lo que necesites!")
            continue

        elif "meme" in pedido:
            hablar("Ahí te va un meme")
            try:
                archivo_audio = os.path.join(os.getcwd(), "ya-llegaron-las-pipsash.mp3")
                if os.path.exists(archivo_audio):
                    subprocess.run(["open", archivo_audio])
                    print("🎵 Reproduciendo audio...")
                else:
                    hablar("No encuentro el archivo de audio")
                    print("❌ Archivo ya-llegaron-las-pipsash.mp3 no encontrado")
            except Exception as e:
                print(f"Error al reproducir: {e}")
                hablar("Hubo un problema al reproducir el meme")
            continue


        elif "adiós" in pedido or "salir" in pedido or "terminar" in pedido:
            hablar("Ha sido un placer ayudarte hoy. Nos vemos pronto. ¡Que tengas un excelente día!")
            print("\n" + "="*50)
            print("👋 ¡Hasta luego!")
            print("🤖 Asistente Jorge desactivado")
            print("="*50)
            break

if __name__ == "__main__":
    pedir_cosas()