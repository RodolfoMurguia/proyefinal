"""programa principal"""

from position import positions
from salary import salaries
from employee import employees

print("Bienvenido al programa de nóminas")
print("Opciones de búsqueda")
print("a: Puestos")
print("b: Salarios")
print("c: Empleados")

option = input("Qué quieres consultar?: ")

if option == "a":
    positions()
elif option == "b":
    salary()
elif option == "c":
    employees()
else:
    print("no existe esa opcion")