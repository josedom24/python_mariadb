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

def Borrar_Alumno(db,id):
    sql="delete from Alumnos where id=%d" % id
    cursor = db.cursor()
    resp=input("¿Ralmente quieres borrar al alumno %d? (pulsa 's' para si)" % id)
    if resp=="s":
        try:
            cursor.execute(sql)
            db.commit()
            if cursor.rowcount==0:
                print("No hay alumnos con ese id")
        except:
            print("Error al borrar.")
            db.rollback()


def Listar_BD(db):
    sql="select * from Alumnos"
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
       cursor.execute(sql)
       registros = cursor.fetchall()
       for registro in registros:
          print(registro["id"]," --- ",registro["nombre"],registro["apellidos"],"-- Edad:",registro["edad"])
    except:
       print("Error en la consulta")

def Buscar_alumno_edad(db,edad):
    sql="select * from Alumnos where edad=%d" % edad
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute(sql)
        if cursor.rowcount==0:
            print("No hay alumnos con esa edad.")
        else:
            registros = cursor.fetchall()
            for registro in registros:
                print(registro["nombre"])
    except:
       print("Error en la consulta")

def MostrarMenu():
    menu='''
    1. Insertar Alumnos
    2. Listas Alumnos
    3. Buscar alumnos por edad
    4. Borrar alumno por id
    0. Salir
    '''
    print(menu)
    while True:
        try:
            opcion=int(input("Opción:"))
            return opcion
        except:
            print("Opción incorrecta, debe ser un número")
