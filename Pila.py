from typing import Any, Optional

class Pila:

    def __init__(self):
        self.__elementos= []

    def push (self, value: Any)->None: #agrega elementos a la lista
        self.__elementos.append(value)

    def pop(self): #elimina el último elemento
        return{
            self.__elementos.pop()
            if self.__elementos
            else None
        }

    def on_top(self):
        if self.__elementos:
            return self.__elementos[-1]
        else:
            return None


    def size(self)-> int : #tamaño de la lista
        return len(self.__elementos)

    def show(self): #muestra la lista
        lista_auxiliar= Pila()
        while self.size()>0:
            value = self.pop()
            print(value)
            lista_auxiliar.push(value)
        
