#Operadores
#Aritmeticos
a = 2
b = 3
suma = a+b #Lo mismo para - * / 
print(f'suma: {suma}')

# Division entera, potencia y modulo
division = b // a
print(f'Division con resultado entero {division}')
potencia = a ** b
print(f'Potencia {potencia}')
modulo = a % b
print(f'modulo {modulo}')

#Ejercicio: calcular el area y el y el perimetro de un rectangulo
alto = int(input("Ingrese el alto del rectangulo: "))
ancho = int(input("Ingrese el ancho del rectangulo: "))
area = alto * ancho
perimetro = (alto + ancho) * 2
print(f'El area del rectangulo es: {area}')
print(f'El perimetro del rectangulo es: {perimetro}')

# Ejercicio: es par o impar
numero = int(input("Ingrese un numero: "))
if numero % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")

# Ejercicio: Es mayor de edad
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

#Ejercicio: Valor dentro de un rango
numero = int(input("Ingrese un numero: "))
if numero >= 0 and numero <= 10:
    print("El numero esta dentro del rango")
else:
    print("El numero esta fuera del rango")

# Ejercicio : operador Or
vacaciones = False
diaDescanso = False
if vacaciones or diaDescanso:
    print("Puede asistir al juego")
else:
    print("No puede asistir al juego")

# Ejercicio: Aplicando not
vacaciones = False
diaDescanso = False
if not(vacaciones) or not(diaDescanso):
    print("No puede asistir al juego")
else:
    print("Puede asistir al juego")

#Ejercicio: Rango entre los 20 o 30
edad = int(input("Ingrese su edad: "))
veinte = edad >= 20 and edad < 30 # simplificado: 20 <= edad < 30
treinta = edad >= 30 and edad < 40 # simplificado: 30 <= edad < 40
if veinte:
    print("Dentro del rango de 20")
elif treinta:
    print("Dentro del rango de 30")
else:
    print("Fuera del rango de 20 a 30")

#Ejercicio: El mayor de 2 numeros
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
if numero1 > numero2:
    print(f"El numero {numero1} es mayor")
elif numero2 > numero1:
    print(f"El numero {numero2} es mayor")
else:
    print("Los numeros son iguales")

#Ejercicio: Tienda de libros
libro = input("Ingrese el nombre del libro: ")
id = int(input("Ingrese el identificador del libro: "))
precio = float(input("Ingrese el precio del libro: "))
envioGratis = True if(input("Ingrese si el envio es gratis(Si o No): ")) ==  "Si" else False
print(f"El libro {libro} con identificador {id} tiene un precio de {precio} y el envio es {'gratis' if envioGratis else 'no gratis'}")