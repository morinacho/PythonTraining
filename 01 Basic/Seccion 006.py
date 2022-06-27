#Ejercicio: Imprimir numeros del 0 al 5
numero = 0
while numero <= 5:
    print(numero)
    numero += 1
#Ejercicio: Imprimir numeros del 0 al 5 desendente
numero = 5
while numero >= 0:
    print(numero)
    numero -= 1

#Ciclo for
cadena = "Hola mundo"
for letra in cadena:
    print(letra)
else:
    print("Fin del ciclo")

#Palabra break

for letra in "Holanda":
    if letra == "a":
        print(f"letra encontrada: {letra}")
        break
else:
    print("Fin del ciclo")

#Palabra continue
for i in range(10):
    if i % 2 != 0:
        continue
    else:
        print(i)
