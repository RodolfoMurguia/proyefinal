"""programa principal"""
import time

from position import positions
from salary import salaries
from employee import employees
from tables import generateTables, dataconection

print("Configurando Ambiente")

data = generateTables(dataconection)

print("Bienvenido al programa de nóminas")
print("Opciones de búsqueda")
print("a: Puestos")
print("b: Salarios")
print("c: Empleados")

option = input("Qué quieres consultar?: ")

if option == "a":

    positions(dataconection)

elif option == "b":

    salary(dataconection)

elif option == "c":

    employees(dataconection)

else:
    
    print("no existe esa opcion")