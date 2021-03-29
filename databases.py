"""Charts positions"""



# Generamos importacion de librerias y creamos database

import sqlite3 as sql

#from sqlite3 import Error 

#Generamos funcion de conexion a server y creacion de base de datos


def generateDatabase():
    try:
        conn = sql.connect('Payrolls.db')
        return conn
    except :
        print("Ha ocurrido un error al momento de conectarse a al DB:")

generateDatabase()