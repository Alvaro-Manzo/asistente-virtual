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




# Escuchar mi micrófono y devolver audio a texto
def transformar_audio_en_texto():

    r = sr.Recognizer()

    with sr.Microphone() as origen:
        r.pause_threshold = 0.8
        print("Ya puedes hablar")

        audio = r.listen(origen)
        try:
            pedido = r.recognize_google(audio, language="es-MX")
            print("Dijiste: " + pedido)

            return pedido
        except sr.UnknownValueError:

            print("Ups, no entendí")
            return "sigo esperando"
        except sr.RequestError:

            print("Ups, no hay servicio")
            return "sigo esperando"
        except:

            print("Ups, algo salió mal")
            return "sigo esperando"

# Función para que asistente pueda ser escuchado
def hablar(mensaje):

    engine = pyttsx3.init()

    engine.setProperty("voice", id3)

    engine.say(mensaje)

    engine.runAndWait()

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

    #activar saludo inicial
    saludo_inicial()

    #variable de corte
    comenzar = True

    #loop centra
    while comenzar:

        #activar micro y guardar pedido en str
        pedido = transformar_audio_en_texto().lower()

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

            hablar("Ok, ya lo voy a empezar a reproducir")
            pywhatkit.playonyt(pedido)
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


        elif "código" in pedido:
            hablar("Si la logras descifrar obtendrás un secreto")
            print("1, 2, 3, 5, 8")
            intento = input("¿Cómo se llama esta serie?: ").lower().strip()
            if intento == "fibonacci" or intento == "numero aureo":
                hablar("Lo has descifrado, muchas felicidades, aquí está tu recompensa")
                time.sleep(1)
                hablar("Eres oficialmente un Maestro Fibonacci honorífico. ¡Que nunca te falte la secuencia!")
                print("🏅 Certificado de Maestro Fibonacci 🏅")
            else:
                hablar("No es correcto, inténtalo de nuevo la próxima vez.")

        elif "mate" in pedido:
            hablar("mmm, Que rico, ya te tomaste tu mate de hoy?, que yerba usaste?")
            continue


        elif "adiós" in pedido:
            hablar("Claro que si, me voy a descansar, cualquier cosa me avisas.")
            break



pedir_cosas()