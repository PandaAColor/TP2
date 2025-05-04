from Pila import Pila
from personaje import Personaje

pila_personajes = Pila()

personaje1 = Personaje("Capitan América", 14)
personaje2 = Personaje("Rocket Racoon",4)
personaje3 = Personaje("Iron Man",12)
personaje4 = Personaje("Groot", 9)
personaje5 = Personaje("Daredevil", 5)
personaje6 = Personaje("Black Widow", 8)

pila_personajes.push(personaje1)
pila_personajes.push(personaje2)
pila_personajes.push(personaje3)
pila_personajes.push(personaje4)
pila_personajes.push(personaje5)
pila_personajes.push(personaje6)

def buscar_posicion(pila = Pila(), busco_posicion = str):
    pila_aux = Pila()
    contador = 1
    on_top = Personaje()
    on_top = pila.on_top()

    while on_top is not None and busco_posicion != on_top.nombre :
        on_top = pila.on_top()
        pila.pop()
        pila_aux.push(on_top)
        contador +=1
    while pila_aux.size() > 0:
        on_top = pila_aux.on_top()
        pila.push(on_top)
        pila_aux.pop()

    if on_top is None:
        return -1
    else:
        return contador

personaje_a_buscar = "Rocket Racoon"
posicion_personaje = buscar_posicion(pila_personajes, personaje_a_buscar)

print(personaje_a_buscar, " se encuentra en la posición ", posicion_personaje)


def filtrar_por_cantidad_peliculas (pila = Pila(), numero= int):
    lista_personajes = []
    pila_aux = Pila()
    while pila.size() > 0:
        on_top = pila.on_top()
        pila_aux.push(on_top)
        pila.pop()

        if on_top.peliculas >=numero:
            lista_personajes.append(on_top.nombre)
    
    while pila_aux.size()>0:
        on_top = pila_aux.on_top()
        pila.push(on_top)
        pila_aux.pop()
    if len(lista_personajes)> 0:
        return lista_personajes
    else:
        return "no hay personajes con esa cantidad de participaciones en la pila"

cantidad = 5
buscar_por_cantidad = filtrar_por_cantidad_peliculas(pila_personajes, cantidad)

print(f"personajes que aparecen en {cantidad} películas:")
for personaje in buscar_por_cantidad:
    print ("-",personaje)


def cantidad_peliculas (pila=Pila(), nombre_buscado = str):
    pila_aux = Pila()
    on_top = pila.on_top()
    
    while on_top is not None and on_top.nombre != nombre_buscado:
        pila_aux.push(on_top)
        pila.pop()
        on_top = pila.on_top()
    
    while pila_aux.size() > 0:
        on_top_aux = pila_aux.on_top()
        pila.push(on_top_aux) 
        pila_aux.pop()

    if on_top is None:
        return "este personaje no aparece en películas"
    else:
        return on_top.peliculas

buscar_peliculas = "Black Widow"
encontrar_peliculas = cantidad_peliculas(pila_personajes, buscar_peliculas)

print(f"cantidad de películas donde aparece {buscar_peliculas}: {encontrar_peliculas}")


def filtrar_por_inicial(pila= Pila(), inicial= str):
    pila_aux = Pila()
    lista_personajes = []

    while pila.size() > 0:
        on_top = pila.on_top()
        pila_aux.push(on_top)
        nombre = on_top.nombre
        pila.pop()

        if nombre is not None and nombre[0] == inicial:
            lista_personajes.append(nombre)
    
    while pila_aux.size() > 0:
        on_top = pila_aux.on_top()
        pila.push(on_top)
        pila_aux.pop()
    return lista_personajes

buscar_inicial = "C"
busqueda_por_inicial = filtrar_por_inicial(pila_personajes, buscar_inicial)

print(f"personajes con la inicial {buscar_inicial} :")
if not busqueda_por_inicial:
    print ("no se encuentran personajes con esa inicial")
else:
    for personaje in busqueda_por_inicial:
        print("-", personaje)

buscar_inicial = "D"
busqueda_por_inicial = filtrar_por_inicial(pila_personajes, buscar_inicial)
print(f"personajes con la inicial {buscar_inicial} :")
if not busqueda_por_inicial:
    print ("no se encuentran personajes con esa inicial")
else:
    for personaje in busqueda_por_inicial:
        print("-", personaje)

buscar_inicial = "G"
busqueda_por_inicial = filtrar_por_inicial(pila_personajes, buscar_inicial)
print(f"personajes con la inicial {buscar_inicial} :")
if not busqueda_por_inicial:
    print ("no se encuentran personajes con esa inicial")
else:
    for personaje in busqueda_por_inicial:
        print("-", personaje)