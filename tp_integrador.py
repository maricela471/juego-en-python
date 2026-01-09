"""
Materia: Programación 1
TRABAJO PRACTICO N°2 - INTEGRADOR
Alumnos:
	-Maricela Ramirez
	-Ojeda Silvestre Javier
"""


import random
import time
import os




# =============================================================================
# Funciones de Animaciones
# =============================================================================
# --- Para mejorar la experiencia de usuario se utilizo ASCII Art ---
BANER_MENU = """
||==============================||
||  /\/\    ___  _ __   _   _   ||
|| /    \  / _ \| '_ \ | | | |  ||
||/ /\/\ \|  __/| | | || |_| |  ||
||\/    \/ \___||_| |_| \__,_|  ||
||==============================||
"""

# Título de Bienvenida
BIENVENIDO_ART = """
██████╗ ██╗███████╗███╗   ██╗██╗   ██╗███████╗███╗   ██╗██╗██████╗  ██████╗ ███████╗
██╔══██╗██║██╔════╝████╗  ██║██║   ██║██╔════╝████╗  ██║██║██╔══██╗██╔═══██╗██╔════╝
██████╔╝██║█████╗  ██╔██╗ ██║██║   ██║█████╗  ██╔██╗ ██║██║██║  ██║██║   ██║███████╗
██╔══██╗██║██╔══╝  ██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║██║  ██║██║   ██║╚════██║
██████╔╝██║███████╗██║ ╚████║ ╚████╔╝ ███████╗██║ ╚████║██║██████╔╝╚██████╔╝███████║
╚═════╝ ╚═╝╚══════╝╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝╚═╝╚═════╝  ╚═════╝ ╚══════╝
"""

# Suerte ..!!!
COMIENZA_ART = """
============================================================================== 
 ||  ██████╗  ██████╗  ██████╗ ██████╗     ██╗     ██╗   ██╗ ██████╗██╗  ██╗ |   | 
 || ██╔════╝ ██╔═══██╗██╔═══██╗██╔══██╗    ██║     ██║   ██║██╔════╝██║ ██╔╝ |   | 
 || ██║  ███╗██║   ██║██║   ██║██║  ██║    ██║     ██║   ██║██║     █████╔╝  |   | 
 || ██║   ██║██║   ██║██║   ██║██║  ██║    ██║     ██║   ██║██║     ██╔═██╗  |   | 
 || ╚██████╔╝╚██████╔╝╚██████╔╝██████╔╝    ███████╗╚██████╔╝╚██████╗██║  ██╗ |   | 
 ||  ╚═════╝  ╚═════╝  ╚═════╝ ╚═════╝     ╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝ |   | 
==============================================================================
"""

GAMEOVER_ART = """
==============================================================================
|| ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ ||
||██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗||
||██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝||
||██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗||
||╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║||
|| ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝||
==============================================================================

"""
FELICITACIONES_ART = """
░█▀▀░█▀▀░█░░░▀█▀░█▀▀░▀█▀░▀█▀░█▀█░█▀▀░▀█▀░█▀█░█▀█░█▀▀░█▀▀
░█▀▀░█▀▀░█░░░░█░░█░░░░█░░░█░░█▀█░█░░░░█░░█░█░█░█░█▀▀░▀▀█
░▀░░░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░░▀░░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀▀▀
"""

INTENTA_ART = """
░▀█▀░█▀█░▀█▀░█▀▀░█▀█░▀█▀░█▀█░█░░░█▀█░░░█▀▄░█▀▀░░░█▀█░█░█░█▀▀░█░█░█▀█
░░█░░█░█░░█░░█▀▀░█░█░░█░░█▀█░█░░░█░█░░░█░█░█▀▀░░░█░█░█░█░█▀▀░▀▄▀░█░█
░▀▀▀░▀░▀░░▀░░▀▀▀░▀░▀░░▀░░▀░▀░▀▀▀░▀▀▀░░░▀▀░░▀▀▀░░░▀░▀░▀▀▀░▀▀▀░░▀░░▀▀▀
"""

def animacion_inicio():
    """Ejecuta la secuencia de animación de inicio."""
    
    # 1. Mostrar BIENVENIDO
    limpia_pantalla()
    print(BIENVENIDO_ART)
    print("\n" * 2) # Saltos de línea para centrar un poco visualmente
    time.sleep(1) # Pausa para ver el primer texto
    # 3. Mostrar CARGANDO TRIVIA
    print(" " * 30 + "CARGANDO TRIVIA...") 
    # 4. Esperar 3 segundos
    time.sleep(3)
    # 5. Borrar la pantalla
    limpia_pantalla()

def limpia_pantalla():
    """Limpia la pantalla de la consola de forma compatible con múltiples OS."""
    # Para Windows usa 'cls', para Unix/Linux/macOS usa 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')

def comienzo_Juego():
    limpia_pantalla()
    print(COMIENZA_ART)
    time.sleep(2)
    limpia_pantalla()


# --------------------------------
# FUNCIONES DE LISTA DE PREGUNTAS
# --------------------------------
# se cargan las listas de de preguntas 
def videojuegos():
    """en esta funcion se cargan las preguntas sobre videojuegos"""
    p1=("¿En qué año fue lanzado Elden Ring?", ["a)2021","b)2022","c)2023"], "b")
    p2=(" ¿Cuál es el nombre del protagonista principal en Spider-Man 2 (2023)?", ["a) Peter Parker solamente","b) Miles Morales solamente","c) Ambos Peter Parker y Miles Morales"], "c")
    p3=("¿Qué estudio desarrolló Baldur's Gate 3?", ["a) BioWare","b) Larian Studios","c) Obsidian Entertainment"], "b")
    p4=("¿En qué planeta se desarrolla principalmente Starfield?", ["a) Marte","b) No hay un planeta principal son múltiples","c) Tierra"], "b")
    p5=("¿Cuál es el nombre del nuevo personaje jugable femenino en Street Fighter 6?", ["a) Kimberly","b) Manon","c) Ambas son correctas"], "c")
    p6=(" ¿Qué empresa desarrolló Hogwarts Legacy?", ["a) Rocksteady Studios","b) Avalanche Software","c) Insomniac Games"], "b")
    p7=(" ¿En The Legend of Zelda: Tears of the Kingdom, cómo se llama la nueva habilidad principal de Link?", ["a) Fuse","b) Ultrahand","c) Ascend"], "b")
    p8=(" ¿Cuál es el nombre del antagonista principal en Resident Evil 4 Remake?", ["a) Albert Wesker","b) Osmund Saddler","c) Jack Krauser"], "b")
    p9=(" ¿Qué tipo de juego es Dead Space Remake (2023)?", ["a) Survival Horror","b) Action RPG","c) Battle Royale"], "a")
    p10=("¿En qué año fue lanzado originalmente Cyberpunk 2077?", ["a) 2019","b) 2020","c) 2021"], "b")
    p11=(" ¿Cuál es el nombre de la protagonista en Horizon Forbidden West?", ["a) Aloy","b) Ellie","c) Lara"], "a")
    p12=(" ¿Qué estudio desarrolló God of War Ragnarök?", ["a) Naughty Dog","b) Santa Monica Studio","c) Sucker Punch"], "b")
    p13=("¿En Fortnite, cómo se llama el modo creativo donde los jugadores pueden construir mapas?", ["a) Creative Mode","b) UEFN (Unreal Editor for Fortnite)","c) Ambas son correctas"], "c")
    p14=("¿Cuál es el nombre del nuevo mapa en Call of Duty: Modern Warfare III (2023)?", ["a) Verdansk","b) Urzikstan","c) Blackout"], "b")
    p15=("¿Qué característica principal tiene Diablo IV comparado con entregas anteriores?", ["a) Es completamente online","b) Es un juego móvil exclusivo","c) No tiene clases de personajes"], "a")
    p16=("¿En qué consola es exclusivo Spider-Man 2 (2023)?", ["a) Xbox Series X/S","b) PlayStation 5","c) Nintendo Switch"], "b")
    p17=(" ¿Cuál es el nombre del nuevo protagonista en Final Fantasy XVI?", ["a) Cloud Strife","b) Clive Rosfield","c) Noctis Lucis"], "b")
    p18=("¿Qué tipo de juego es Pizza Tower?", ["a) Plataformas 2D","b) RPG por turnos","c) Shooter en primera persona"], "a")
    p19=("¿En Tears of the Kingdom, qué nuevo tipo de construcción puede crear Link?", ["a) Solo vehículos terrestres","b) Vehículos terrestres, aéreos y acuáticos","c) Solo estructuras estáticas"], "b")
    p20=(" ¿Cuál es la secuela directa de The Last of Us?", ["a) The Last of Us Part II","b) The Last of Us Part III","c) The Last of Us Remake"], "a")
    return [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20]

def actualidad():
    """en esta funcion se cargan las preguntas sobre datos actuales"""
    p1=(" ¿Cuál es la moneda de curso legal en Japón?", ["a) Yuan","b) Dólar","c) Yen"], "c")
    p2=("¿Qué país alberga la sede de las Naciones Unidas?", ["a) Estados Unidos","b) Suiza","c) Francia"], "a")
    p3=("¿Qué empresa lanzó la primera misión tripulada a Marte, anunciada públicamente para la década de 2030?", ["a) SpaceX","b) Blue Origin","c) NASA"], "a")
    p4=("¿Qué continente tiene mayor población?", ["a) Asia","b) África","c) Europa"], "a")
    p5=("¿Qué red social alcanzó una marca de usuarios activos mensuales por encima de 4 mil millones en 2023-2024?", ["a) Instagram","b) Facebook","c) TikTok"], "b")
    p6=(" ¿Cuál es el principal recurso energético no renovable aún más usado a nivel mundial en 2024?", ["a) Petróleo","b) Carbón","c) Gas natural"], "a")
    p7=(" ¿Qué país es el mayor emisor de CO₂ a nivel global en 2023-2024?", ["a) India","b) Estados Unidos","c) China"], "c")
    p8=(" ¿Qué tecnología está detrás de la mayor parte de los avances en IA en los últimos años?", ["a) Algoritmos genéticos","b) Redes neuronales profundas (deep learning)","c) Computación cuántica"], "b")
    p9=(" ¿Qué empresa domina la cuota de mercado de búsquedas en la mayoría de los países?", [" a) Bing","b) Baidu","c) Google"], "c")
    p10=("¿Qué país preside la mayor economía de la región latinoamericana por Producto Interno Bruto (PIB) (2023-2024)?", ["a) México","b) Brasil","c) Argentina"], "b")
    p11=("¿Qué sistema de transporte urbano ha mostrado un crecimiento notable en ciudades europeas durante 2020-2024?", ["a) Autos eléctricos privados","b) Carriles bici y transporte público limpio","c) Motores diésel"], "b")
    p12=("¿Qué país tiene la mayor inversión militar del mundo en 2024?", ["a) China","b) Estados Unidos","c) Rusia"], "b")
    p13=("¿Qué género de música vio un crecimiento masivo en plataformas de streaming durante 2023-2024?", ["a) Música clásica","b) K-pop y música latina","c) Rock clásico"], "b")
    p14=("¿Qué sector tecnológico ha experimentado un crecimiento sustancial en empleo en 2023-2024 en muchos países?", ["a) Inteligencia artificial y ciberseguridad","b) Impresión 3D","c) Tecnología de ficha mecánica"], "a")
    p15=("¿Cuál es la red de transporte terrestre más usada en ciudades para disminuir la congestión (segmento urbano)?", ["a) Microbuses","b) Metro y tren rápido","c) Aviones regionales"], "b")
    p16=("¿Qué país lidera el uso de energías renovables en la generación eléctrica?", ["a) Estados Unidos","b) China","c) Brasil"], "b")
    p17=("¿Qué tecnología de comunicación se está consolidando como base de 5G y más allá?", ["a) Fibra óptica únicamente","b) Antenas MIMO y espectro radioeléctrico","c) Cable coaxial"], "b")
    p18=("¿Cuál es el principal motor de crecimiento económico en muchos países emergentes en 2023-2024?", ["a) Turismo","b) Exportaciones de commodities","c) Servicios financieros digitales"], "c")
    p19=("¿Qué evento climático extremo ha sido más reportado globalmente en 2023-2024?", ["a) Sequías","b) Inundaciones extremas","c) Tornados"], "b")
    p20=(" ¿En qué sector se han visto avances significativos en IA para automatización de oficinas?", ["a) Reconocimiento de voz y procesamiento de lenguaje natural","b) Gráficos por computadora","c) Robótica industrial pesada"], "a")
    return [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20]

def curiosidades():
  
    p1=("¿Qué animal duerme de pie?", ["a) Elefante","b) Flamenco","c) Jirafa"], "b")
    p2=("¿Cuántos corazones tiene un pulpo?", ["a) 1","b) 2","c) 3"], "c")
    p3=("¿Qué fruta es técnicamente una baya?", ["a) Fresa","b) Plátano","c) Cereza"], "b")
    p4=("¿Cuál es el único mamífero capaz de volar?", ["a) Ardilla voladora","b) Murciélago","c) Pez volador"], "b")
    p5=("¿Qué planeta gira al revés comparado con los demás?", ["a) Venus","b) Urano","c) Neptuno"], "a")
    p6=("¿Cuántos huesos tiene un tiburón?", ["a) 206","b) 100","c) 0"], "c")
    p7=("¿Qué animal puede vivir sin cabeza durante varias semanas?", ["a) Cucaracha","b) Lagartija","c) Serpiente"], "a")
    p8=("¿Cuál es el único alimento que nunca se pudre?", ["a) Sal","b) Miel","c) Arroz"], "b")
    p9=("¿Qué órgano del cuerpo humano sigue creciendo toda la vida?", ["a) Nariz y orejas","b) Ojos","c) Lengua"], "a")
    p10=("¿Cuántas veces puede batir sus alas un colibrí por segundo?", ["a) 20","b) 50","c) 80"], "c")
    p11=("¿Qué animal tiene la lengua más larga en proporción a su cuerpo?", ["a) Camaleón","b) Oso hormiguero","c) Jirafa"], "a")
    p12=("¿Cuántos años puede vivir una tortuga gigante?", ["a) 50 años","b) 100 años","c) Más de 150 años"], "c")
    p13=("¿Qué inventó primero la humanidad?", ["a) La rueda","b) La flauta","c) El fuego controlado"], "b")
    p14=("¿Cuántos cerebros tiene un pulpo?", ["a) 1","b) 3","c) 9"], "c")
    p15=("¿Qué país tiene más volcanes activos?", ["a) Islandia","b) Indonesia","c) Japón"], "b")
    p16=("¿Cuánto pesa la lengua de una ballena azul?", ["a) Como un elefante","b) Como un auto","c) Como una persona"], "a")
    p17=("¿Qué animal puede correr sobre el agua?", ["a) Basilisco","b) Rana","c) Cangrejo"], "a")
    p18=("¿Cuántas horas duerme un koala al día?", ["a) 12 horas","b) 18 horas","c) 22 horas"], "c")
    p19=("¿Qué país consume más chocolate per cápita?", ["a) Bélgica","b) Suiza","c) Alemania"], "b")
    p20=("¿Cuántos dientes puede tener un caracol?", ["a) 0","b) 50","c) Más de 20,000"], "c")
    return [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20]


# -----------------------------
# FUNCIONES
# -----------------------------


resultados=[]

def menu_principal():
    #mediante esta funcion se podra cargar el menu y hacer los llamados a las funciones del juego  
    while True:
        limpia_pantalla
        print(BANER_MENU)
        print("="*34)
        print("1) Jugar")
        print("2) Resultados anteriores")
        print("3) Salir")
        print("=" * 34)
    
        opcion_menu = input("Elige una opción (1-3): ")
    
        match opcion_menu:
            case "1":
                comienzo_Juego()
                juego()
            case "2":
                limpia_pantalla()
                mostrar_resultados()
            case "3":
                limpia_pantalla()
                print(GAMEOVER_ART)
                print(" " * 30 + "Saliendo...")
                time.sleep(3)
                break  # Sale del while
            case _:
                limpia_pantalla()
                print("Opción no válida")    
          

def verificar_resultado(porcentaje):
    if porcentaje < 50:
        print (INTENTA_ART)
        print("\n Necesitas al menos 50% para aprobar.")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        juego()  # Vuelve a jugar automáticamente
        return
    else:
        print(FELICITACIONES_ART)
        print("\n  Aprobaste")
        opcion = input("¿Quieres jugar de nuevo? (s/n): ")
        if opcion.lower() == 's':
            juego()
        return
    
def juego():
    """lista que  contiene todas las funciones con los temas de preguntas"""
    funciones_temas=[videojuegos,actualidad,curiosidades] 
    """obtenemos todas las preguntas de las distintas funciones"""
    todas_preguntas=[]
    for funcion in funciones_temas:
     todas_preguntas+=funcion()
     """elegimos las preguntas"""
    random.shuffle(todas_preguntas)
    elegidas=todas_preguntas[:10]
    correctas=0 #acumulador para preguntas correctas
    incorrectas=0 #acumulador para preguntas incorrectas

    for pregunta in elegidas:
        print(f"{'*' * 100}\n")
        print(f"{pregunta[0]}\n")  # Acceso al primer elemento de la tupla (pregunta)
        print(f"{'*' * 100}\n")
        for opcion in pregunta[1]:  # Acceso al segundo elemento (opciones)
            print(opcion)
        
        respuesta=input("¿cual es la respuesta correcta?:") 
        if respuesta.strip().lower()==pregunta[2].strip():  # Acceso al tercer elemento (respuesta correcta)
            correctas+=1
            print("respuesta correcta 😆")
            print("Siguiente pregunta... ¡Sigue asi! ➡️💡")
        else:
            incorrectas+=1
            print("respuesta incorrecta 😢")
            print("Siguiente pregunta... ¡Vamos tu Puedes! ➡️💡")
        time.sleep(2)

        os.system('cls' if os.name == 'nt' else 'clear')
    
    porcentaje_correctas=correctas*100/10
    resultados.append((correctas,incorrectas, porcentaje_correctas))
    print(f"{'*' * 100}\n")
    print(f"su porcentaje de preguntas correctas es de {porcentaje_correctas}%\n")
    print(f"{'*' * 100}\n")
    verificar_resultado(porcentaje_correctas)
    input("Presione Enter para continuar...")
    verificar_resultado(porcentaje_correctas)
    limpia_pantalla()

def mostrar_resultados():
    limpia_pantalla()
    if not resultados:
        print("\n" + "=" * 75)
        print("   ¡Aún no hay resultados de partidas! 😞")
        print("   Juega una partida para empezar a acumular estadísticas.")
        print("=" * 75)
        input("\nPresione Enter para volver al menú principal...")
        return
    print("\n" + "=" * 55)
    print("      🏆 HISTORIAL DE PARTIDAS DE TRIVIA 🏆")
    print("=" * 55)
    #print("\n--- RESULTADOS ANTERIORES ---")
    for i, (aciertos, errores, porcentaje) in enumerate(resultados, 1):
        print(f"Partida {i}: Aciertos: {aciertos}, Errores: {errores}, Porcentaje: {porcentaje}%")
    
    lista_aciertos = [resultado[0] for resultado in resultados]
    
    print("\n" + "-" * 55)
    print("      📊 ESTADÍSTICAS GENERALES")
    print("-" * 55 + "\n")
    print(f"Máximo puntaje obtenido(Record): {max(lista_aciertos)} aciertos")
    print(f"Mínimo puntaje obtenido: {min(lista_aciertos)} aciertos")
    print(f"Promedio de aciertos: {sum(lista_aciertos) / len(lista_aciertos):.2f}\n") 
    print("\n" + "-" * 55+ "\n")
    input("\nPresione Enter para volver al menú principal...")   


# -----------------------------
# PROGRAMA PRINCIPAL
# -----------------------------

# Ejecutar la animación inicial y llamada a menu
if __name__ == "__main__":
    animacion_inicio()
    menu_principal()
