#Programa en Python
#Un viaje por el caribe
import sys
import os
import modulo import*

print("\t Viaje por el Caribe")
print("")
print("Usted desea registrarse?.")
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
numtele=""
while True:
    try:
        nt=int(input("Ingrese su numero :"))
        while(len(str(nt))!=9):
            nt=int(input("Los numeros de celular son de 9 cifras numericas:"))
        numtele=str(nt)
        break
    except ValueError:
        print("Ingrese su numero de celular correctamente...")

menu()
op(n,d,e,s)
        





