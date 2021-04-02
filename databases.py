"""Charts positions"""



# Generamos importacion de librerias y creamos database

import sqlite3 as sql

#Generamos funcion de conexion a server y creacion de base de datos


def generateDatabase():
    try:
        #Intentamos abrir y conectarnos, si no existe la DB, la creara python
        conn = sql.connect('Payrolls.db')

        #Retornamos objeto de conexion
        return conn

    except:

        print("Ha ocurrido un error al momento de conectarse a al DB:")

generateDatabase()