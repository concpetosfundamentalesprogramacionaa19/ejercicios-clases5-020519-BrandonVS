"""
	file: Room.py
	autor: BrandonVS

	Se desea obtener el costo de una carrera universitaria. El valor promedio 
	de cada ciclo es de 1200 dolares, el valor promedio del seguro educativo 
	es de 100 dolares si la edad del estudiante es menor o igual a 20 caso 
	contrario sera de 150 dolares. Si el estudiante tiene una modalidad 
	a distancia el numero de ciclos a seguir es de 10 caso contrario debera 
	seguir 8 ciclos. Obtener la proyeccion del costo de la carrera del 
	estudiante.

"""
# Se piden los datos al usuario
ciclos = input("Ingrese la modalidad (Presencial o Distancia): ")
edad = input("Ingrese la edad del estudiante: ")
edad = float(edad)
costo = 0
# Se calcula el costo del ciclo mas el seguro 
if edad <= 20:
	costociclo = 1300
else:
	costociclo = 1350
# Se calcula el costo total de la carrera
if ciclos == "Presencial":
	costo = (float(costociclo) * 8)
	
if ciclos == "Distancia":
	costo = (float(costociclo) * 10)
# Se imprimen los datos
print ("El costo total de la carrera del estudiante sera: %.2f" % (costo))