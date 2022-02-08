import sys
import MySQLdb

def Conectar_BD(host,usuario,password,nombrebd):
    try:
        db = MySQLdb.connect(host,usuario,password,nombrebd)
        return db
    except MySQLdb.Error as e:
        print("No puedo conectar a la base de datos:",e)
        sys.exit(1)

def Desconectar_BD(db):
    db.close()


def Insertar_BD(db,alumno):
    cursor = db.cursor()
    sql="insert into Alumnos values (%d, '%s', '%s', %d )" % (alumno["identificador"],alumno["nombre"],alumno["apellidos"],alumno["edad"])
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print("Error al insertar.")
        db.rollback()

def MostrarMenu():
    menu='''
    1. Insertar Alumnos
    0. Salir
    '''
    print(menu)
    while True:
        try:
            opcion=int(input("Opción:"))
            return opcion
        except:
            print("Opción incorrecta, debe ser un número")
