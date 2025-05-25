__authors__ = ["Joseph H. C.", "Stheban Danilo H. V.", "Drako David S. T."]
__lisense__ = "GPL"
__version__ = "1.0"
__emails__ = ["joseph.herrera@campusucc.edu.co","stheban.hoyos@campusucc.edu.co", "drako.salazar@campusucc.edu.co"]

    ####################################
    # importaciones
    ####################################

from typing import List
from Letra import Letra

class Palabra:
    
    ###############################
    # constructor
    ###############################

    def __init__(self, p_palabra: str):
        self.__palabra = p_palabra.lower()

    ###############################
    # metodos
    ###############################

    __method__="esta_completa"
    __params__="p_jugadas"
    __returns__="bool"
    __description__="metodo que sirve para saber si la palabra esta completa"
    def esta_completa(self, p_jugadas: List[Letra]) -> bool:
        for letra in self.dar_letras():
            if not self._buscar_letra_en_lista(letra, p_jugadas):
                return False
        return True
    
    __method__="_buscar_letra_en_lista"
    __params__="p_letra, lista_letras"
    __returns__="bool"
    __description__="metodo que sirve para buscar una letra en una lista"
    def _buscar_letra_en_lista(self, p_letra: Letra, lista_letras: List[Letra]) -> bool:
        for letra in lista_letras:
            if p_letra.es_igual(letra):
                return True
        return False

    __method__="esta_letra"
    __params__="p_letra"
    __returns__="bool"
    __description__="metodo que sirve para saber si la letra esta en la palabra"
    def esta_letra(self, p_letra: Letra) -> bool:
        for letra in self.dar_letras():
            if letra.es_igual(p_letra):
                return True
        return False

    __method__="dar_ocurrencias"
    __params__="p_jugadas"
    __returns__="List[Letra]"
    __description__="metodo que sirve para dar las ocurrencias"
    def dar_ocurrencias(self, p_jugadas: List[Letra]) -> List[Letra]:
        resultado = []
        for letra in self.dar_letras():
            if self._buscar_letra_en_lista(letra, p_jugadas):
                resultado.append(letra)
            else:
                resultado.append(Letra("_"))
        return resultado

    __method__="dar_letras"
    __params__="ninguno"
    __returns__="List[Letra]"
    __description__="metodo que sirve para dar las letras"
    def dar_letras(self) -> List[Letra]:
        return [Letra(l) for l in self.__palabra]