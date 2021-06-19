from .Animal import Animal

class Ave(Animal):

	def __init__(self, fecha_ingreso, fecha_salida, precio, alimento, tipo, raza):
		super(Ave,self).__init__(fecha_ingreso, fecha_salida, precio, alimento, raza)
		switcher = {
			'c': "Canario",
			'p': "Perico",
		}
		self.tipo= switcher.get(tipo, "Canario")
		
	def imprimirAtributos(self):
		super(Ave,self).imprimirAtributos()
		print(self.tipo)