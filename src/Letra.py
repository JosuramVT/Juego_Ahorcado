__authors__ = ["Joseph H. C.", "Stheban Danilo H. V.", "Drako David S. T."]
__lisense__ = "GPL"
__version__ = "1.0"
__emails__ = ["joseph.herrera@campusucc.edu.co","stheban.hoyos@campusucc.edu.co", "drako.salazar@campusucc.edu.co"]

class Letra:

    ###############################
    # constructor
    ###############################

    def __init__(self, p_letra: str):
        self.__letra = p_letra.lower()
       
    ###############################
    # metodos
    ###############################

    __method__= "dar_letra"
    __params__= "ninguno"
    __returns__= "letra"
    __description__= "metodo que sirve para dar la letra"
    def dar_letra(self) -> str:
        assert len(self.__letra) == 1, "La letra debe ser un solo caracter"
        return self.__letra

    __method__= "es_igual"
    __params__= "otra_letra"
    __returns__= "bool"
    __description__= "metodo que sirve para saber si la letra es igual"
    def es_igual(self, otra_letra: 'Letra') -> bool:
        return self.__letra == otra_letra.dar_letra()