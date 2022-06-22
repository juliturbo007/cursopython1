
def genera_lista():
    participantes = ['julio', 'jamal', "cesar"]

    print(participantes)

    return participantes

def genera_diccionario():
    diccionario = { "nombre" : 'julio', "apellido": "briones" }
    return diccionario

part = genera_lista()

part[0] = "lucien"

print(genera_lista)

part = genera_lista


def ejecute_generator(funcion):
    return funcion()

print(ejecute_generator(genera_lista))
print(ejecute_generator(genera_diccionario))


