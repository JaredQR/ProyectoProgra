import sys
import os
import time

def menu():
    print("")
    print("MENU")
    print("\t[1]  |  Diseña tu Viaje")
    print("\t[2]  |  Promociones")
    print("\t[3]  |  Registrate")
    print("\t[4]  |  Contactanos")
    print("\t[5]  |  Ayuda")
    print("\t[6]  |  Salir")
    print("")
def op(n,ape,d,nt):
    while True:
        try:
            o=int(input("Ingres la operacion que desea realizar: "))
            break
        except ValueError:
            print("Ingrese una operacion valida .....")
    if o==1:
        diseña(n,ape,d,nt)
    if o==2:
        promociones(n,ape,d,nt)
    if o==3:
        registrare(n,ape,d,nt)
    if o==4:
        contactanos(n,ape,d,nt)
    if o==5:
        ayuda(n,ape,d,nt)
    if o==6:
        salir(n,ape,d,nt)
    else:
        print("Ingrese una opcion segun nuestro Menu")
        pregunta1(n,ape,d,nt)
def pregunta(n,ape,d,nt):
    p1=input("Usted desea  realizar otra operacion ?  [si]o[no] :")
    if (p1=='si' or p1=='Si' or p1=='SI'):
        print("")
        menu()
        op(n,ape,d,nt)
    elif (p1=='no' or p1=='No' or p1=='NO'):
        salir(n,ape,d,nt)
    else:
        print("Ud debe tomar una decision ...")
        pregunta(n,ape,d,nt)
        
def salir(n,ape,d,nt):
    sal=input("Usted esta seguro que desea SALIR ?  [si]o[no] :")
    if (sal=='si' or sal=='Si' or sal=='SI'):
        print("")
        print("Cerrando Sesion...")

    elif (sal=='no' or sal=='No' or sal=='NO'):
        menu()
        salir(n,ape,d,nt)
    else:
        print("Ud debe tomar una decision ...")
        salir(n,ape,d,nt)


def verificar(n):
    for c in n:
        if(ord(c)<65 or  ord(c)>90) and (ord(c)<97 or  ord(c)>122) and (ord(c)!=32):
            return False
    return True

def verificar(ape):
    for c in ape:
        if(ord(c)<65 or  ord(c)>90) and (ord(c)<97 or  ord(c)>122) and (ord(c)!=32):
            return False
    return True


    
    
