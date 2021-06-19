from .Mascota import Mascota

class Mamifero(Mascota):

	def __init__(self, nombre, fecha_ingreso, fecha_salida, precio, alimento, raza, tipo):
		super(Mamifero,self).__init__(nombre, fecha_ingreso, fecha_salida, precio, alimento, raza)
		switcher = {
			'g': "Gato",
			'p': "Perro",
		}
		self.tipo= switcher.get(tipo, "Gato")

	def imprimirAtributos(self):
		super(Mamifero,self).imprimirAtributos()
		print(self.tipo)