#Tipos de datos
#int
from sympy import numer


variable = 10
print(type(variable), variable) #Para saber el tipo de dato que guarda
#string bool flat
variable = "string"
variable = True
variable = 10.5

#Manejo de cadenas (string)
#Concatenacion 
grupoMusical = "Aerosmith" 
comentario = "Rock Band"
print("Banda musical: " + grupoMusical + " " + comentario)
#Otra forma
print("Banda musical:", grupoMusical,comentario)

#String a enteros
numero1 = "1"
numero2 = "2"
print(numero1 + numero2)
print(int(numero1) + int(numero2))

#Booleanos
variable = 3>2 #True
print(variable)

#Input: entrada del usuario
entrada = input("Ingresar datos")
print(entrada)

#Sumando entradas por input
num1 = int(input("Ingresar el primer numero "))
num2 = int(input("Ingrese el segundo numero "))
print("Suma resultado = ", num1 + num2)

#Ejercicio: Preguntarle al usuario como estuvo su dia del 1 al 10
dia = input("Califica tu dia del 1 al 10 ")
print("Mi dia estuvo de: ", dia)

#Ejecicio: pedir titulo del libro y nombre del autor e imprimir en el siguiente formato = <titulo> fue escrito por <autor>
titulo = input("Proporciona el titulo: ")
autor = input ("Proporciona el autor: ")
print(titulo + " fue escrito por " + autor)