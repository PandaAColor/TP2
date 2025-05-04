from Pila import Pila
from Trajes import Traje

pila_de_modelos = Pila()

caso1 = Traje("MarkXLIV", "Capitan America: Civil War", "impecable")
caso2 = Traje("modelo2", "pelicula1", "dañado")
caso3 = Traje("MarkLXXXV", "Capitan America: Civil War", "dañado")
caso4 = Traje("MarkLXXXV", "Capitan America: Civil War", "destruido")
caso5 = Traje("modelo3", "Spider-Man: Homecoming", "destruido")
caso6 = Traje ("MarkXLIV", "Spider-Man: Homecoming", "dañado")

pila_de_modelos.push(caso1)
pila_de_modelos.push(caso2)
pila_de_modelos.push(caso3)
pila_de_modelos.push(caso4)
pila_de_modelos.push(caso5)
pila_de_modelos.push(caso6)

#buscar modelo markXLIV

def flitrar_modelo (busco_modelo, pila_de_modelos = pila_de_modelos):
    pila_local = Pila()
    pila_local2 = Pila()
    lista_peliculas = []
    while pila_de_modelos.size()>0: #pasar la pila original a otras dos pilas locales
        traje_actual = pila_de_modelos.on_top()
        pila_local.push(traje_actual)
        pila_local2.push(traje_actual)
        pila_de_modelos.pop()
    
    while pila_local2.size()>0: #restaurar pila original vaciando una de las locales
        traje_actual = pila_local2.on_top()
        pila_de_modelos.push(traje_actual)
        pila_local2.pop()

    while pila_local.size() > 0:
        traje_actual = pila_local.on_top()
        if traje_actual.modelo == busco_modelo:
            lista_peliculas.append(traje_actual.pelicula)
        pila_local.pop()
    return lista_peliculas

modelo_buscado = flitrar_modelo("MarkXLIV")
print(f"películas del modelo:{modelo_buscado}")

#Segun el nivel de daño

def filtrar_por_estado(pila = pila_de_modelos):
    pila_local = Pila()
    lista_dañados = []
    lista_eliminar = []

    while pila.size() > 0:
        traje_actual = pila.on_top()
        if traje_actual.estado == "dañado":
            lista_dañados.append(traje_actual.modelo)
            pila.pop()
            pila_local.push(traje_actual)

        elif traje_actual.estado == "destruido":
            lista_eliminar.append(traje_actual.modelo)
            pila.pop()
        else:
            pila.pop()
            pila_local.push(traje_actual)
    while pila_local.size() > 0: #restaurar pila original sin los modelos eliminados
        pila.push(pila_local.pop())
    
    return lista_dañados, lista_eliminar

lista_dañados, lista_eliminar = filtrar_por_estado(pila_de_modelos)

print("Modelos dañados:")
for modelo in lista_dañados:
    print("-", modelo)

print("Modelos eliminados (destruidos):")
for modelo in lista_eliminar:
    print("-", modelo)


#filtrar según la película

def filtrar_por_pelicula(pelicula, pila = pila_de_modelos):
    pila_local = Pila()
    pila_aux = Pila()

    lista_trajes = []

    while pila.size() > 0:
        traje_actual = pila.on_top()
        pila.pop()
        pila_local.push(traje_actual)
        pila_aux.push(traje_actual)
    
    while pila_aux.size() > 0:
        traje_actual = pila_aux.on_top()
        pila_aux.pop()  
        pila.push(traje_actual)    
    
    while pila_local.size() >0:
        traje_actual = pila_local.on_top()
        if traje_actual.pelicula == pelicula:
            lista_trajes.append(traje_actual.modelo)
        pila_local.pop()
    return lista_trajes

buscar_peli = "Spider-Man: Homecoming"

trajes_de_peliculas = filtrar_por_pelicula(buscar_peli)

print("trajes usados en: ", buscar_peli)
for traje in trajes_de_peliculas:
    print("-", traje)

buscar_peli = "Capitan America: Civil War"
trajes_de_peliculas = filtrar_por_pelicula(buscar_peli)

print("trajes usados en: ", buscar_peli)
for traje in trajes_de_peliculas:
    print("-", traje)