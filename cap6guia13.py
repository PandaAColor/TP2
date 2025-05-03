from Pila import Pila
from Trajes import Traje

pila_de_modelos = Pila()
pila_extra = Pila()

lista_peliculas = []
lista_dañados = []

caso1 = Traje("MarkXLIV", "pelicula1", "impecable")
caso2 = Traje("modelo2", "pelicula1", "dañado")
caso3 = Traje("MarkLXXXV", "pelicula2", "dañado")
caso4 = Traje("MarkLXXXV", "peluca3", "destruido")
caso5 = Traje("modelo3", "pelicula2", "destruido")
caso6 = Traje ("MarkXLIV", "pelicula3", "dañado")

pila_de_modelos.push(caso1)
pila_de_modelos.push(caso2)
pila_de_modelos.push(caso3)
pila_de_modelos.push(caso4)
pila_de_modelos.push(caso5)
pila_de_modelos.push(caso6)

#buscar modelo markXLIV

def flitrar_modelo (busco_modelo, pila_de_modelos = pila_de_modelos, pila_extra = pila_extra, lista_peliculas =lista_peliculas):
    while pila_de_modelos.size() > 0:
        lista_actual = pila_de_modelos.on_top()
        if lista_actual.modelo == busco_modelo:
            lista_peliculas.append(lista_actual.pelicula)
        pila_extra.push(lista_actual)
        pila_de_modelos.pop()
    pila_de_modelos = pila_extra
    return print(lista_peliculas)

print(flitrar_modelo("MarkXLIV"))

#Segun el nivel de daño

while pila_extra.size() >0:
    pila_extra.pop()

while pila_de_modelos.size() >0:
    lista_actual = pila_de_modelos.on_top()
    if lista_actual.estado == "dañado":
        lista_dañados.append(lista_actual.modelo)
        pila_extra.push(lista_actual)
        pila_de_modelos.pop()
        print ("paso por aca")
    elif lista_actual.estado == "destruido":
        print(f"se eliminó el modelo {lista_actual.modelo}")
        pila_de_modelos.pop()
    else:
        pila_extra.push(lista_actual)
        pila_de_modelos.pop()
        print("otro lado")
        