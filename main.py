from animals import Mamifero, Ave, Reptil, Mascota, Animal

if __name__ == "__main__":
	perro = Mamifero("cocky", "04/03/2021", "04/03/2021", 500, "perrarina", "cocker", 'p')
	gato = Mamifero("gatius", "04/03/2021", "04/03/2021", 500, "gatarina", "Maine Coon", 'g')
	perico = Ave("04/03/2021", "04/03/2021", 500, "maiz", "Periquito", 'p')
	canario = Ave("04/03/2021", "04/03/2021", 500, "maiz", "canario", 'c')
	iguana = Reptil("cockyt", "04/03/2021", "04/03/2021", 500, "bichos", "Crestada de Fiyi", 'i')
	serpiente = Reptil("cockyo", "04/03/2021", "04/03/2021", 500, "bichos", "Cascabel", 's')

	perro.imprimirAtributos()
	gato.imprimirAtributos()
	perico.imprimirAtributos()
	canario.imprimirAtributos()
	iguana.imprimirAtributos()
	serpiente.imprimirAtributos()