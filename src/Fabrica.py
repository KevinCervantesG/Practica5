from Objeto import Objeto

t = 0 #Variable t que representa los segundos
id_objeto = 0 #id de los objetos
banda_transAB = []
banda_transC = []
paquetes = []

#Produce objetos A cada 5 segundos
def productorA():
	global t
	global id_objeto
	while t <= 500: #La maquina solo trabajara por 500 segundos
		t += 1
		if t%5 == 0:
			id_objeto += 1
			A = Objeto(id_objeto, 1)
			banda_transAB.append(A)

#Produce objetos B cada 5 segundos
def productorB():
	global t
	global id_objeto
	while t <= 500: #La maquina solo trabajara por 500 segundos
		t += 1
		if t%5 == 0:
			id_objeto += 1
			B = Objeto(id_objeto, 2)
			banda_transAB.append(B)

#Ensambla objetos C cada 2 objetos A y 3 objetos B
def ensamblador():
	global id_objeto
	contA = 0
	contB = 0
	for x in banda_transAB:
		if Objeto.getTipo(x) == 1:
			contA += 1
		elif Objeto.getTipo(x) == 2:
			contB += 1
		if (contA%2 == 0) and (contB%3 == 0):
			id_objeto += 1
			C = Objeto(id_objeto, 3)
			banda_transC.append(C)

#Empaqueta dado el limite de piezas por paquete
def empaquetador(piezas_limite):
	cont_piezasC = 0
	for x in banda_transC:
		cont_piezasC += 1
		if cont_piezasC % piezas_limite == 0:
			paquetes.append(1) #Solo decimos que se ha creado un paquete

if __name__ == "__main__":
	productorA()
	print(len(banda_transAB))
	productorB()
	print(len(banda_transAB))
	ensamblador()
	print(len(banda_transC))
	empaquetador(5)
	print(len(paquetes))
	while len(paquetes) <= 5:
		print("Se ha creado un paquete de piezas C")
		#El while no sirve aunque se crean la cantidad de paquetes necesarios
	
	


