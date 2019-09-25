#Clase objeto para simular objetos de tipo A,B y C
#el traibuto tipo es de tipo entero
#si tipo = 1 entonces el objeto es de tipo A
#si tipo = 2 entonces el objeto es de tipo B
#si tipo = 3 entonces el objeto es de tipo C
class Objeto:

	def __init__(self, id, tipo):
		self.id = id
		self.tipo = tipo

	def getTipo(self): 
		return self.tipo  
