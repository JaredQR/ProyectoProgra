#PUERTOS#

def anadirpuertos():
    import sys, os, sqlite3
    con = sqlite3.connect('DISENHO.s3db')
    puer=input("Ingrese el puerto :" )
    pai=input("Ingrese el pais : ")
    os.system('cls')
    cursor=con.cursor()
    cursor.execute("insert into TABPUERTOS(puertos, pais) values ('"+puer+"','"+pai+"')")
    con.commit()
    con.close()
    
def salir():
    import sys, os
    print("Decidio SALIR")
    sys.exit()

def verpuertos():
    import sys, os, sqlite3
    con = sqlite3.connect('DISENHO.s3db')
    cursor=con.cursor()
    cursor.execute("select * from TABPUERTOS")
    print()
    print ("\t Cod    \t Puerto  \t  Ubicacion")
    print("********************************************************************")
    for TABPUERTOS in cursor:
        verpuer='\t'+str(TABPUERTOS[0])+'\t'+"     "+str(TABPUERTOS[1])+'\t'+'\t'+str(TABPUERTOS[2])
        print(str(verpuer))
    con.close
    print()

def modificarpuerto():
    import sys, os, sqlite3
    llave=[]
    con = sqlite3.connect('DISENHO.s3db')
    cursor=con.cursor()
    cursor.execute("select * from TABPUERTOS")
    print()
    print ("\t Cod    \t Puerto  \t  Ubicacion")
    print("********************************************************************")
    for TABPUERTOS in cursor:
        llave.append(TABPUERTOS)
        verpuer='\t'+str(TABPUERTOS[0])+'\t'+"     "+str(TABPUERTOS[1])+'\t'+'\t'+str(TABPUERTOS[2])
        print(str(verpuer))
        print("")
    cod=input("Ingrese el codigo del puerto que desea modificar :")
    for TABPUERTOS in llave:
        if int(TABPUERTOS[0]==int(cod)):
               P1=TABPUERTOS[1]
               P2=TABPUERTOS[2]
               encontrado=True
               break
    P1=input("Digite el nuevo puerto"+P1+":")
    P2=input("Digite el nuevo lugar"+P2+":")
    sql="update TABPUERTOS set puertos='"+P1+"', pais='"+P2+"' where Cod="+cod
    cursor.execute(sql)
    con.commit()
    con.close()
    os.system("cls")
    print("El producto a sido modificado")


def sacarpuerto():
    import sys, os, sqlite3
    con = sqlite3.connect('DISENHO.s3db')
    cursor=con.cursor()
    cursor.execute("select * from TABPUERTOS")
    print("Aqui puedes eliminar los puertos")
    print()
    print ("\t Cod    \t Puerto  \t  Ubicacion")
    print("********************************************************************")
    for TABPUERTOS in cursor:
        verpuer='\t'+str(TABPUERTOS[0])+'\t'+"     "+str(TABPUERTOS[1])+'\t'+'\t'+str(TABPUERTOS[2])
        print(str(verpuer))
        print("")
    cod=input("Ingrese el codigo que desea eliminar :")
    sql="delete from TABPUERTOS where Cod="+cod
    cursor.execute(sql)
    con.commit()
    con.close()
    os.system('cls')
    print("Elimino un puerto ")

##################################################################################################

#Categorias y precios #
def anadircategoria():
    import sys, os, sqlite3
    con = sqlite3.connect('DISENHO.s3db')
    categ=input("Ingrese la categoria :" )
    TB=input("Ingrese el precio de la temporada baja :  ")
    TM=input("Ingrese el precio de la temporada media :  ")
    TA=input("Ingrese el precio de la temporada alta :  ")
    os.system('cls')
    cursor=con.cursor()
    cursor.execute("insert into TABCATEGORIAS(categoria, tempbaja, tempmed, tempalta) values ('"+categ+"','"+TB+"','"+TM+"','"+TA+"')")
    con.commit()
    con.close()

def vercategoria():
    import sys, os, sqlite3
    con = sqlite3.connect('DISENHO.s3db')
    cursor=con.cursor()
    cursor.execute("select * from TABCATEGORIAS")
    print()
    print ("\t Cod    \t Categoria  \t  TempBaja    \t  TempMed  \t  TempAlta")
    print("********************************************************************")
    for TABCATEGORIAS in cursor:
        vercategorias='\t'+str(TABCATEGORIAS[0])+'\t'+"      "+str(TABCATEGORIAS[1])+'\t'+"     "+str(TABCATEGORIAS[2])+'\t'+"   "+str(TABCATEGORIAS[3])+'\t'+str(TABCATEGORIAS[4])
        print(str(vercategorias))
    con.close
    print()

def modificarcategoria():
    import sys, os, sqlite3
    llave=[]
    con = sqlite3.connect('DISENHO.s3db')
    cursor=con.cursor()
    cursor.execute("select * from TABCATEGORIAS")
    print()
    print ("\t Cod    \t Categoria  \t  TempBaja    \t  TempMed  \t  TempAlta")
    print("********************************************************************")
    for TABCATEGORIAS in cursor:
        llave.append(TABCATEGORIAS)
        vercategorias='\t'+str(TABCATEGORIAS[0])+'\t'+"      "+str(TABCATEGORIAS[1])+'\t'+"     "+str(TABCATEGORIAS[2])+'\t'+"   "+str(TABCATEGORIAS[3])+'\t'+str(TABCATEGORIAS[4])
        print(str(vercategorias))
        print("")
    cod=input("Ingrese el codigo del puerto que desea modificar :")
    for TABCATEGORIAS in llave:
        if int(TABCATEGORIAS[0]==int(cod)):
               C1=TABCATEGORIAS[1]
               Cbaja=TABCATEGORIAS[2]
               Cmed=TABCATEGORIAS[3]
               Calta=TABCATEGORIAS[4]
               jared=True
               break
    C1=input("Digite la nueva categoria  "+C1+":")
    Cbaja=input("Digite el precio de temporada baja "+str(Cbaja)+":")
    Cmed=input("Digite el nuevo precio de temporada media "+str(Cmed)+":")
    Calta=input("Digite el nuevo precio de temporada alta "+str(Calta)+":")
    
    sql="update TABCATEGORIAS set categoria='"+C1+"', tempbaja='"+Cbaja+"' , tempmed='"+Cmed+"' , tempalta='"+Calta+"' where Cod="+cod
    cursor.execute(sql)
    con.commit()
    con.close()
    os.system("cls")
    print("El producto a sido modificado")
    
def sacarcategoria():
    import sys, os, sqlite3
    con = sqlite3.connect('DISENHO.s3db')
    cursor=con.cursor()
    cursor.execute("select * from TABCATEGORIAS")
    print("Aqui puedes eliminar los puertos")
    print()
    print ("\t Cod    \t Categoria  \t  TempBaja    \t  TempMed  \t  TempAlta")
    print("********************************************************************")
    for TABCATEGORIAS in cursor:
        vercategorias='\t'+str(TABCATEGORIAS[0])+'\t'+"      "+str(TABCATEGORIAS[1])+'\t'+"     "+str(TABCATEGORIAS[2])+'\t'+"   "+str(TABCATEGORIAS[3])+'\t'+str(TABCATEGORIAS[4])
        print(str(vercategorias))
        print("")
    cod=input("Ingrese el codigo que desea eliminar :")
    sql="delete from TABCATEGORIAS where Cod="+cod
    cursor.execute(sql)
    con.commit()
    con.close()
    os.system('cls')
    print("Elimino un puerto ")



               
               
               
        
    
    
    
    








    
    
