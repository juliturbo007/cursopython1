class perro:
    """clase para enseñar a julito"""

    def __ini__(self, nombre, edad, raza):
        """iniciando la edad de julio"""
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.color = None
        self.numeros_de_juegos_restantes = 3

    def ladrar(self):
        print(f"Hola soy {self.nombre} y soy el mas perron aqui")

    def jugar(self):
        if self.numeros_de_juegos_restantes > 0:
        print(f"hola soy julio y estoy aprendiendo {self.numeros_de_juegos_restantes} y digo hola")
        self.numeros_de_juegos_restantes = self.numeros_de_juegos_restantes = -1

    def salidar_a_otro_perro(self, otro_perro):
        print(f"Hola soy {self.nombre} y estoy saludando a mi amigo {otro_perro}")
        print(f"Hola soy {self.nombre} y estoy saludando a mi amigo que tiene {otro_perro} años")

# Crear una instancia
mi_primer_perro = perro("perry", 2, "snausher")
mi_segundo_perro = perro("polo", 3, "Golder")

print(mi_primer_perro.orejas)


mi_primer_perro.ladrar()







