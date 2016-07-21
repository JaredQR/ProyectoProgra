import sys
import os
def menu():
    print("")
    print("MENU")
    print("\t[1]  |  (Introducir)")
    print("\t[2]  |  (Introducir)")
    print("\t[3]  |  (Introducir)")
    print("\t[4]  |  (Introducir)")
    print("\t[5]  |  (Introducir)")
    print("")
def op(n,d,e,s):
    while True:
        try:
            o=int(input("Ingres la operacion que desea realizar: "))
            break
        except ValueError:
            print("Ingrese una operacion valida .....")
    if o==1:
        reporte(n,d,e,s)
    elif o==2:
        salir(n,d,e,s)
    else:
        print("Ingrese una opcion segun nuestro Menu")
        pregunta1(n,d,e,s)

def pregunta(n,d,e,s):
    p1=input("Usted desea  realizar otra operacion ?  [si]o[no] :")
    if (p1=='si' or p1=='Si' or p1=='SI'):
        print("")
        menu()
        op(n,d,e,s)
    elif (p1=='no' or p1=='No' or p1=='NO'):
        salir(n,d,e,s)
    else:
        print("Ud debe tomar una decision ...")
        pregunta(n,d,e,s)

def salir(n,d,e,s):
    sal=input("Usted esta seguro que desea SALIR ?  [si]o[no] :")
    if (sal=='si' or sal=='Si' or sal=='SI'):
        print("")
        print("Cerrando Sesion...")
        
    elif (sal=='no' or sal=='No' or sal=='NO'):
        menu()
        salir(n,d,e,s)
    else:
        print("Ud debe tomar una decision ...")
        salir(n,d,e,s)

def verificar(n):
    for c in n:
        if(ord(c)<65 or  ord(c)>90) and (ord(c)<97 or  ord(c)>122) and (ord(c)!=32):
            return False
    return True
    
    
