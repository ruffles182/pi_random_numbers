##Trataremos de encontrar el valor de pi con numeros aleatorios
#como lo explican en el video de youtube https://www.youtube.com/watch?v=RZBhSi_PwHU
#importamos librerias necesaria
import math
from random import randint
import os

clearStr = 'cls' if os.name == 'nt' else 'clear'

cantidadAleatorio = int(input("defina el Maximo repeticiones: "))
maxAleatorio = int(input("defina el max de numero aleatorio (de 0 hasta ?): "))
cantidadMuestras = int(input("defina el numero de muestras (para el promedio): "))

numeroMuchiflistico = cantidadAleatorio*cantidadMuestras

def coprime2(a, b):
    return math.gcd(a, b) == 1

def generarRNG():
    return randint(0,maxAleatorio)

def generarResultados(totalCoprimos):
    x = totalCoprimos/cantidadAleatorio

    return math.sqrt(6/x)

promedio = 0.0
totalCalculos = 0
sumaPromedio = 0
for j in range(0, cantidadMuestras):
    contadorCoprimos = 0
    for i in range(0,cantidadAleatorio):
        a = generarRNG()
        b = generarRNG()

        if coprime2(a,b):
            contadorCoprimos += 1

        totalCalculos +=1

    pi = generarResultados(contadorCoprimos)
    sumaPromedio += pi
    promedio = float(sumaPromedio)/(j+1)
    os.system(clearStr)

    print("---------------------------------------------------------")
    print("Calculando... esto puede tomar un tiempo...")
    print("muestra no: "+str(j+1)+" de: "+str(cantidadMuestras))
    print("Se han realizado "+str(totalCalculos)+" calculos!! D:  de: "+str(numeroMuchiflistico))
    print("completado: "+"%.0f%%" % (100 * float(totalCalculos)/numeroMuchiflistico))
    print("---------------------------------------------------------")

print("")
print("el valor promedio de las muestras es de: "+str(promedio))
print("le fallamos a pi por tan solo: "+str(promedio-math.pi))
print("")
print("---------------------------------------------------------")
print("")
input("Presione Enter para continuar...")