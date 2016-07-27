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
def continuar():
    print("¿Desea continuar?")
    print("1.- si")
    print("2.- no")
    x=input("Elija una opcion : ")
    if x=='1':
        opciones()
    elif x=='2':
        salir()
    else :
        print("Intentelo de nuevo")
        continuar()
def salir():
    print("¿Esta seguro de que desea salir?")
    print("1.- si")
    print("2.- no")
    y=input("Elija una opcion : ")
    if y=='2':
        opciones()
    elif y=='1':
        print("El programa se esta cerrando...")
        time.sleep(2)
        sys.exit(1)
    else :
        print("Intentelo de nuevo")
        salir()
def verificar(n):
    for c in n:
        if(ord(c)<65 or  ord(c)>90) and (ord(c)<97 or  ord(c)>122) and (ord(c)!=32):
            return False
    return True
def nnombre():
    global nombre
    nombre=input("Ingrese su nombre: ")
    if (not verificar(nombre)):
        print("Intentelo de nuevo")
        nnombre()
def napellido():
    global apellido
    apellido=input("Ingrese su apellido : ")
    if (not verificar(apellido)):
        print("Intentelo de nuevo")
        napellido()
def ndni():
    global dni
    while True :
        try :
            dni=int(input("Ingrese su DNI : "))
            break
        except :
            print("Intentelo de nuevo")
    dni=str(dni)
    if (len(dni)!=8):
        print("Intentelo de nuevo")
        ndni()

    
    
