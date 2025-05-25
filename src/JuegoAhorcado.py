__authors__ = ["Joseph H. C.", "Stheban Danilo H. V.", "Drako David S. T."]
__lisense__ = "GPL"
__version__ = "1.0"
__emails__ = ["joseph.herrera@campusucc.edu.co","stheban.hoyos@campusucc.edu.co", "drako.salazar@campusucc.edu.co"]

    ####################################
    # importaciones
    ####################################

import random
from enum import Enum
from typing import List
from Palabra import Palabra
from Letra import Letra

    ################################
    # constantes
    ################################

class Estado(Enum):
    NO_INICIADO = 1
    JUGANDO = 2
    GANADOR = 3
    AHORCADO = 4

class JuegoAhorcado:
    TOTAL_PALABRAS = 12
    MAX_INTENTOS = 6

    ###############################
    # constructor
    ###############################

    def __init__(self):
        self.diccionario: List[Palabra] = [
            Palabra("algoritmo"),
            Palabra("contenedora"),
            Palabra("avance"),
            Palabra("ciclo"),
            Palabra("indice"),
            Palabra("instrucciones"),
            Palabra("arreglo"),
            Palabra("vector"),
            Palabra("inicio"),
            Palabra("cuerpo"),
            Palabra("recorrido"),
            Palabra("patron"),
        ]
        self.__estado = Estado.NO_INICIADO
        self.__intentos_disponibles = self.MAX_INTENTOS
        self.__jugadas: List[Letra] = []
        self.__palabra_actual: Palabra = None

    ###############################
    # metodos
    ###############################

    __method__= "iniciar_juego"
    __params__= "ninguno"
    __returns__= "ninguno"
    __description__= "metodo que sirve para iniciar el juego"
    def iniciar_juego(self):
        self.__estado = Estado.JUGANDO
        self.__intentos_disponibles = self.MAX_INTENTOS
        self.__jugadas = []
        posicion_aleatoria = random.randint(0, self.TOTAL_PALABRAS - 1)
        self.__palabra_actual = self.diccionario[posicion_aleatoria]

    __method__= "jugar_letra"
    __params__= "letra"
    __returns__= "bool"
    __description__= "metodo que sirve para jugar una letra"
    def jugar_letra(self, letra: Letra) -> bool:
        if self.__estado != Estado.JUGANDO:
            return False
        
        if self.letra_utilizada(letra):
            return False
        
        self.__jugadas.append(letra)
        
        if self.__palabra_actual.esta_letra(letra):
            if self.__palabra_actual.esta_completa(self.__jugadas):
                self.__estado = Estado.GANADOR
            return True
        else:
            self.__intentos_disponibles -= 1
            if self.__intentos_disponibles == 0:
                self.__estado = Estado.AHORCADO
            return False
        
    __method__= "dar_palabra_actual"
    __params__= "ninguno"
    __returns__= "palabra"
    __description__= "metodo que sirve para dar la palabra actual"
    def dar_palabra_actual(self) -> Palabra:
        return self.__palabra_actual

    __method__= "dar_palabra"
    __params__= "posicion"
    __returns__= "palabra/nada"
    __description__= "metodo que sirve para dar la palabra"
    def dar_palabra(self, posicion: int) -> Palabra:
        if 0 <= posicion < len(self.diccionario):
            return self.diccionario[posicion]
        return None
    
    __method__= "dar_intentos_disponibles"
    __params__= "ninguno"
    __returns__= "intentos_disponibles"
    __description__= "metodo que sirve para dar los intentos disponibles"
    def dar_intentos_disponibles(self) -> int:
        return self.__intentos_disponibles

    __method__= "dar_jugadas"
    __params__= "ninguno"
    __returns__= "jugadas"
    __description__= "metodo que sirve para dar las jugadas"
    def dar_jugadas(self) -> List[Letra]:
        return self.__jugadas.copy()

    __method__= "dar_ocurrencias"
    __params__= "ninguno"
    __returns__= "ocurrencias"
    __description__= "metodo que sirve para dar las ocurrencias"
    def dar_ocurrencias(self) -> List[str]:
        if self.__palabra_actual is None:
            return []
        return self.__palabra_actual.dar_ocurrencias(self.__jugadas)
    
    __method__= "dar_estado"
    __params__= "ninguno"
    __returns__= "estado"
    __description__= "metodo que sirve para dar el estado"
    def dar_estado(self) -> Estado:
        return self.__estado

    __method__= "letra_utilizada"
    __params__= "letra"
    __returns__= "bool"
    __description__= "metodo que sirve para saber si la letra fue utilizada"
    def letra_utilizada(self, letra: Letra) -> bool:
        for jugada in self.__jugadas:
            if jugada.es_igual(letra):
                return True
        return False

    def metodo1(self) -> str:
        return "Respuesta 1"

    def metodo2(self) -> str:
        return "Respuesta 2"