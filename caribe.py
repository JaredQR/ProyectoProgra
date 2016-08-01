import os
import sys
import sqlite3
import modulo

def administrador():
    os.system("cls")
    print("")
    print("   > MENU   >  Administrador")
    print("")
    print("Bienvenido al administrador donde usted puede configurar los paquetes de viaje")
    print("")
    print("\t[1]   |    Agregar ")
    print("\t[2]   |    Modificar")
    print("\t[3]   |    Eliminar")
    print("\t[4]   |    Visualizar")
    print("")
    print("")
    while True:
        try:
            opcion=int(input("Ingrese una opcion: "))
            break
        except ValueError:
            print("Opcion incorrecta...")
            administrador()
    if opcion==1:
        agregar()
    elif opcion==2:
        modificar()
    elif opcion==3:
        eliminar()
    elif opcion==4:
        visualizar()
    else:
        print("Opcion incorrecta...")
        administrador()
administrador()
