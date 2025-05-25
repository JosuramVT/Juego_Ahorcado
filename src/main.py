__authors__ = ["Joseph H. C.", "Stheban Danilo H. V.", "Drako David S. T.", "Claude AI"]
__lisense__ = "GPL"
__version__ = "1.0"
__emails__ = ["joseph.herrera@campusucc.edu.co","stheban.hoyos@campusucc.edu.co", "drako.salazar@campusucc.edu.co"]

import os
import sys
from JuegoAhorcado import JuegoAhorcado, Estado
from Letra import Letra

def limpiar_pantalla():
    """Limpia la pantalla de la consola"""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_ahorcado(intentos_restantes):
    """Muestra el dibujo del ahorcado según los intentos restantes"""
    dibujos = [
        """
        ╔══════╗
        ║      ║
        ║      ☠
        ║     /|\\
        ║     / \\
        ║
        ╚═══════════
        ¡PERDISTE!
        """,
        """
        ╔══════╗
        ║      ║
        ║      ☹
        ║     /|\\
        ║     / 
        ║
        ╚═══════════
        """,
        """
        ╔══════╗
        ║      ║
        ║      ☹
        ║     /|\\
        ║      
        ║
        ╚═══════════
        """,
        """
        ╔══════╗
        ║      ║
        ║      ☹
        ║     /|
        ║      
        ║
        ╚═══════════
        """,
        """
        ╔══════╗
        ║      ║
        ║      ☹
        ║      |
        ║      
        ║
        ╚═══════════
        """,
        """
        ╔══════╗
        ║      ║
        ║      ☹
        ║      
        ║      
        ║
        ╚═══════════
        """,
        """
        ╔══════╗
        ║      ║
        ║      
        ║      
        ║      
        ║
        ╚═══════════
        """
    ]
    return dibujos[intentos_restantes]

def mostrar_estado_juego(juego):
    """Muestra el estado actual del juego"""
    print("=" * 50)
    print("JUEGO DEL AHORCADO")
    print("=" * 50)
    
    # Mostrar el ahorcado
    print(mostrar_ahorcado(juego.dar_intentos_disponibles()))
    
    # Mostrar la palabra con las letras adivinadas
    ocurrencias = juego.dar_ocurrencias()
    palabra_mostrar = ""
    for letra in ocurrencias:
        if letra.dar_letra() == "_":
            palabra_mostrar += "_ "
        else:
            palabra_mostrar += letra.dar_letra().upper() + " "
    
    print(f"\n Palabra: {palabra_mostrar}")
    print(f" Intentos restantes: {juego.dar_intentos_disponibles()}")
    
    # Mostrar letras jugadas
    jugadas = juego.dar_jugadas()
    if jugadas:
        letras_jugadas = [letra.dar_letra().upper() for letra in jugadas]
        print(f" Letras jugadas: {', '.join(letras_jugadas)}")
    
    print("-" * 50)

def obtener_letra_usuario():
    """Obtiene una letra válida del usuario"""
    while True:
        try:
            entrada = input("Ingresa una letra: ").strip()
            
            if len(entrada) != 1:
                print("Por favor, ingresa solo UNA letra.")
                continue
            
            if not entrada.isalpha():
                print("Por favor, ingresa solo LETRAS.")
                continue
                
            return Letra(entrada)
            
        except KeyboardInterrupt:
            print("\n\n¡Gracias por jugar!")
            sys.exit(0)
        except Exception as e:
            print(f"Error: {e}")

def mostrar_resultado_final(juego):
    """Muestra el resultado final del juego"""
    estado = juego.dar_estado()
    palabra_actual = juego.dar_palabra_actual()
    palabra_completa = ''.join([letra.dar_letra() for letra in palabra_actual.dar_letras()]).upper()
    
    if estado == Estado.GANADOR:
        print("\n" + "" * 20)
        print("🏆 ¡FELICIDADES! ¡HAS GANADO! 🏆")
        print(f"La palabra era: {palabra_completa}")
        print(f"Lo lograste con {juego.dar_intentos_disponibles()} intentos restantes")
    
    elif estado == Estado.AHORCADO:
        print(mostrar_ahorcado(0))
        print("💀 ¡GAME OVER! 💀")
        print(f"La palabra era: {palabra_completa}")
        print("¡Inténtalo de nuevo!")

def mostrar_menu_principal():
    """Muestra el menú principal del juego"""
    print("\n" + "#" * 33)
    print("BIENVENIDO AL JUEGO DEL AHORCADO")
    print("#" * 33)
    print("\n INSTRUCCIONES:")
    print("• Adivina la palabra letra por letra")
    print("• Tienes 6 intentos máximo")
    print("• Las palabras son términos de programación")
    print("\n" + "=" * 50)

def jugar_partida():
    """Ejecuta una partida completa del juego"""
    juego = JuegoAhorcado()
    juego.iniciar_juego()
    
    while juego.dar_estado() == Estado.JUGANDO:
        limpiar_pantalla()
        mostrar_estado_juego(juego)
        
        letra = obtener_letra_usuario()
        
        # Verificar si la letra ya fue utilizada
        if juego.letra_utilizada(letra):
            print(f"Ya has usado la letra '{letra.dar_letra().upper()}'. ¡Intenta con otra!")
            input("Presiona Enter para continuar...")
            continue
        
        # Jugar la letra
        resultado = juego.jugar_letra(letra)
        
        if resultado:
            print(f"¡Bien! La letra '{letra.dar_letra().upper()}' está en la palabra.")
        else:
            print(f"Lo siento, la letra '{letra.dar_letra().upper()}' no está en la palabra.")
        
        input("Presiona Enter para continuar...")
    
    # Mostrar resultado final
    limpiar_pantalla()
    mostrar_resultado_final(juego)

def main():
    """Función principal del programa"""
    try:
        while True:
            limpiar_pantalla()
            mostrar_menu_principal()
            
            opcion = input("¿Quieres jugar? (s/n): ").strip().lower()
            
            if opcion in ['s', 'si', 'sí', 'y', 'yes']:
                jugar_partida()
                
                # Preguntar si quiere jugar otra partida
                otra = input("\n¿Quieres jugar otra partida? (s/n): ").strip().lower()
                if otra not in ['s', 'si', 'sí', 'y', 'yes']:
                    break
                    
            elif opcion in ['n', 'no']:
                break
            else:
                print("Opción no válida. Por favor, responde 's' para sí o 'n' para no.")
                input("Presiona Enter para continuar...")
        
        print("\n¡Gracias por jugar al Ahorcado!")
        print("¡Vuelve pronto!")
        
    except KeyboardInterrupt:
        print("\n\n¡Gracias por jugar!")
    except Exception as e:
        print(f"\nError inesperado: {e}")

if __name__ == "__main__":
    main()