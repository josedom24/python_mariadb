from funciones import *

db = Conectar_BD("localhost","usuario","asdasd","testdb")
Desconectar_BD(db)
opcion=Mostrar_menu()
while opcion!=0:
    if opcion==1:
        alumno={}
        alumno["identificador"]=int(input("Identificador:"))
        alumno["nombre"]=input("Nombre:")
        alumno["apellidos"]=input("Apellidos:")
        alumno["edad"]=int(input("Edad:"))
        Insertar_BD(db,alumno)
        
