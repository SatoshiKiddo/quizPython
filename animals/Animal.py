

class Animal():

	def __init__(self, fecha_ingreso, fecha_salida, precio, alimento, raza):
		self.fecha_ingreso= fecha_ingreso
		self.fecha_salida= fecha_salida
		self.precio= precio
		self.alimento= alimento
		self.raza= raza

	def imprimirAtributos(self):
		print(self.fecha_ingreso)
		print(self.fecha_salida)
		print(self.precio)
		print(self.alimento)
		print(self.raza)
