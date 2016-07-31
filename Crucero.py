import os
import sys
import sqlite3

def salida():
    con=sqlite3.connect("Crucero.s3db")
    cursor=con.cursor()
    cursor.execute("SELECT * FROM Pais")
    for i in cursor:
        print("Codigo: ", i[0],"Nombre: ", i[1])
salida()
    
