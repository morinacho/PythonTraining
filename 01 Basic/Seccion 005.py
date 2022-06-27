#Ejercicio: Conversion de numeros a texto
numero = int(input("Ingrese un numero entre 1 y 3: "))
if numero == 1:
    print("Numero uno")
elif numero == 2:
    print("Numero dos")
elif numero == 3:
    print("Numero tres")
else: print("Fuera de rango")

#Ejercicio: Estacion segun el mes
mes = input("Ingrese un mes: ")
if mes == "enero" or mes == "febrero" or mes == "marzo":
    print("Estacion: Invierno")
elif mes == "abril" or mes == "mayo" or mes == "junio":
    print("Estacion: Primavera")
elif mes == "julio" or mes == "agosto" or mes == "septiembre":
    print("Estacion: Verano")
elif mes == "octubre" or mes == "noviembre" or mes == "diciembre":
    print("Estacion: Otono")
else: print("Mes no valido")

#Ejercicio: Etapa de la vida segun la edad
edad = int(input("Ingrese su edad: "))
if edad < 0:
    print("Edad no valida")
elif edad < 15:
    print("Etapa de la vida: Infancia")
elif edad < 18:
    print("Etapa de la vida: Adolescencia")
elif edad < 21:
    print("Etapa de la vida: Joven")
elif edad < 65:
    print("Etapa de la vida: Adulto")
elif edad < 75:
    print("Etapa de la vida: Maduro")
elif edad < 100:
    print("Etapa de la vida: Anciano")
else: print("Edad no valida")

#Ejercicio: Sistema de calificaciones
nota = int(input("Ingrese una nota: "))
if 0 <= nota < 6:
    print("F")
elif 6 <= nota < 7:
    print("D")
elif 7 <= nota < 8:
    print("C")
elif 8 <= nota < 9:
    print("B")
elif 9 <= nota < 10:
    print("A")
else: print("Nota no valida")
