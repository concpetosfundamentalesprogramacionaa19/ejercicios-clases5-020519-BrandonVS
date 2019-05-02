"""
	file: Room.py
	autor: BrandonVS
"""

from MisVariables import *

# Uso de condicional simple

nota = input("Ingrese nota 1: ")
nota2 = input("Ingrese la nota 2: ")

nota = int(nota)
nota2 = int(nota2)

if nota >= 18:
	print ("%s, su valor de nota es %d" % (mensaje, nota))
else:
	print ("%s, su valor de nota es %d" % (mensaje2, nota))

if nota2 >= 18:
	print ("%s, su valor de nota es %d" % (mensaje, nota2))
else:
	print ("%s, su valor de nota es %d" % (mensaje2, nota2))