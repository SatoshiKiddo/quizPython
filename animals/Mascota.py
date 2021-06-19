from .Animal import Animal

class Mascota(Animal):

	def __init__(self, nombre, fecha_ingreso, fecha_salida, precio, alimento, raza):
		super(Mascota,self).__init__(fecha_ingreso, fecha_salida, precio, alimento, raza)
		self.nombre=nombre

	def imprimirAtributos(self):
		super(Animal,self).imprimirAtributos()
		print (self.nombre)
           