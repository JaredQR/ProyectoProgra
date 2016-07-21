#Programa en Python
#Un viaje por el caribe
import sys
import os
import modulo import*

print("\t Viaje por el Caribe")
print("")
print("Datos Personales.")
print("")
n=input("Ingresar su nombre completo :")
while(not verificar(n)):
    n=input("Ingres su nombre completo y correctamente :")
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

menu()
op(n,d,e,s)
        





