#Programa en Python
#Un viaje por el caribe
import sys
import os
from modulo import*

print("\t Viaje por el Caribe")
print("\t Disfruta de un tour en tierra mientras viajas en crucero")
print("")
#Registro de persona
print("\tRegistrate para recibir novedades.")
print("")
print("Inscribete y se el primero en conocer nuestras ultimas promociones de cruceros, los destinos mas populares y aprende a planificar mejor tu viajes")
print("")
print(" (*) Campos obligatorios ")
print("")
n=input("Nombre :")
while(not verificar(n)):
    n=input("Ingres su nombre completo y correctamente :")
ape=input("Apellido :")
while(not verificar(ape)):
    n=input("Ingres su apellido completo y correctamente (*) :")
dni=""
while True:
    try:
        d=int(input("Ingrese su n° de su DNI:"))
        while(len(str(d))!=8):
            d=int(input("Ingrese su n° de su DNI de 8 digitos:"))
        dni=str(d)
        break
    except ValueError:
        print("Ingrese su n° de su DNI correctamente...")
numtele=""
while True:
    try:
        nt=int(input("Ingrese su numero de celular:"))
        while(len(str(nt))!=9):
            nt=int(input("Los numeros de celular son de 9 cifras numericas:"))
        numtele=str(nt)
        break
    except ValueError:
        print("Ingrese su numero de celular correctamente...")

menu()
op(n,a,d,nt)
        





