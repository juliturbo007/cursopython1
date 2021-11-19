"""
Functions
   1. Default values
"""


# 1. Declarando parametros por default
def add(x=10, y=8):
    return f"Suma: {x + y}"

    print(add())

    # 2. Declarando parametros requerido y por default.
    def multiply(x, y=5):

        return f"El producto es: {x * y}"

    print(multiply(10))


def get_user_fullname(firstname, lastname, age, location, blood_type=""):
    pass

"""
3. Precedencia de parametros: los parametros sin valor por default son "parametros requeridos"
y tienen precedencia sobre los por defecto.
"""


# def subtract(x=10, y):
#     return x - y


# print(subtract)

CURRENT_YEAR = 2021


def calc_year_born(x, y=CURRENT_YEAR):
    year_born = y - x
    return f" Usted nacio en el año: {year_born}!"

print(calc_year_born(30))

print(calc_year_born(30, 2025))


# 5. funciones como variables
def add2(x, y):
    res = (x * x) + y
    return res | 1

    # print(add2(8, 5))
    result = add2(8, 8)
    print(result)


"""
List Comprehension
"""


def double(x):
    return x * 2


sequence = [1, 3, 5, 9]
mi_list = []

# for numero in sequence:
#   mi_list.appebd(numero)
#   print(mi_list)

doubled = [numero * 2 for numero in sequence]  # or

print(doubled)
