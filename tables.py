"""tables positions:"""

#Importamos nuestra funcion de conexion a DB
from databases import generateDatabase

#Generamos una nue funcion que nos permitira crear las tablas de nuestra aplicacion

def generateTables(conn):

    DbObj = conn.cursor()


    #Tabla de puestos de empleados
    DbObj.execute("Create Table Positions (id integer PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, paymentNumbers integer, deleted BOOLEAN, createdDate DATETIME, lastModifiedDate DATETIME)")

    #Tabla de Salarios
    DbObj.execute("Create Table Salaries  (id integer PRIMARY KEY AUTOINCREMENT, name TEXT, baseSalary float, isBonusSalary BOOLEAN, BonusAmount FLOAT, taxesPercentage FLOAT, insurancePercentage FLOAT, deleted BOOLEAN, createdDate DATETIME, lastModifiedDate DATETIME)")

    #Tabla de empleados (Tabla Principal)
    DbObj.execute("Create Table Employees (id integer PRIMARY KEY AUTOINCREMENT, firstName TEXT, lastName TEXT, phoneNumber TEXT, address TEXT, email TEXT, socialSecurityNumber TEXT, salaryid TEXT, positionId TEXT, deleted BOOLEAN, createdDate DATETIME, lastModifiedDate DATETIME)")

    conn.commit()

#Generamos una nueva conexion a db
dataconection = generateDatabase()

#A partir de la conexion, detonamos la creacion de tablas
generateTables(dataconection)