"""Puestos"""

def positions(conn):

    
    name = str(input("name: "))
    description = str(input("description: "))
    paymentTimes = int(input("veces de pago en el mes: "))
    isActive = int(input("Esta activa esta posicion (1/0): "))

    ##Generamos consulta de insercion de datos

    positionQuery = "INSERT INTO Positions (name, description, paymentNumbers, deleted) VALUES(" + "'" + name + "'," + "'" + description + "'," + "" + str(paymentTimes) + "," + "" + str(isActive) + "" + ")"

    #Generamos cursor a partir de la conexion   
    DbObj = conn.cursor()

    #Ejecutamos consulta
    DbObj.execute(positionQuery)

    #Confirmamos transaccion en db
    conn.commit()
                    
