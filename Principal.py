from archivo.elarchivo import *
from modelado.modelo import *
archivo = MiArchivo()

arry = archivo.obtener_informacion()
arry = [l.split(",") for l in arry]
ordenada = []

for i in arry:
	for n in i :
		ordenada.append(int(n))

ordenada.sort()
print(ordenada)

op = ArregloBinario(ordenada)

elem = int(input("Que numero desea buscar?\n"))
pos = (op.Busqueda(elem) )
print("El numero ingresado se encuentra en la posicion: %d" %(pos))