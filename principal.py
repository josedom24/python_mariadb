from funciones import *

db = Conectar_BD("localhost","usuario","asdasd","testdb")
opcion=MostrarMenu()
while opcion!=0:
    if opcion==1:
        alumno={}
        alumno["identificador"]=int(input("Identificador:"))
        alumno["nombre"]=input("Nombre:")
        alumno["apellidos"]=input("Apellidos:")
        alumno["edad"]=int(input("Edad:"))
        Insertar_BD(db,alumno)
    elif opcion==2:
        Listar_BD(db)
    elif opcion==3:
        miedad=int(input("Edad:"))
        Buscar_alumno_edad(db,miedad)
    elif opcion==4:
        miid=int(input("Id:"))
        Borrar_Alumno(db,miid)
    else:
        print("Opción incorrecta.")
    opcion=MostrarMenu()
Desconectar_BD(db)
