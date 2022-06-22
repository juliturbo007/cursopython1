"""nombre del usuario"""


def obtener_nombre_completo():
    nombre = input("escriba su nombre: ")
    apellido1 = input("escriba su primer apellido: ")
    apellido2 = input("escriba su segundo apellido: ")

    return f"usted se llama {nombre.lower()} {apellido1.lower()} {apellido2.lower()}"


def contar_letras():
    s = "Hola mundo"
    print(s.count("x"))


def regresar_find():
    s = "hola mundo"
    print(s.find("o"))


def suspender_index():
    s = "Hola mundo"
    print(s.index("l"))


suspender_index()



