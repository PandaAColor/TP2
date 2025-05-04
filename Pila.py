from typing import Any, Optional

class Pila:

    def __init__(self):
        self.__elementos= []

    def push (self, value: Any)->None: #agrega elementos a la lista
        self.__elementos.append(value)

    def pop(self): 
        if self.size() > 0:
            return self.__elementos.pop()
        else:
            return None 


    def on_top(self):
        if self.__elementos:
            return self.__elementos[-1]
        else:
            return None


    def size(self)-> int : #tamaño de la lista
        return len(self.__elementos)

        
