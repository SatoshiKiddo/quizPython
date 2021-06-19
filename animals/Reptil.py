from .Mascota import Mascota

class Reptil(Mascota):

	def __init__(self, nombre, fecha_ingreso, fecha_salida, precio, alimento, tipo, raza):
		super(Reptil,self).__init__(nombre, fecha_ingreso, fecha_salida, precio, alimento, raza)
		switcher = {
			'i': "Iguana",
			's': "Serpiente",
		}
		self.tipo= switcher.get(tipo, "Iguana")

	def imprimirAtributos(self):
		super(Reptil,self).imprimirAtributos()
		print(self.tipo)