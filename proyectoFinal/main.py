import cv2
from function1 import opcion1
from function2 import opcion2
from function3 import opcion3
from function4 import opcion4
from function5 import opcion5
from function6 import opcion6
from function7 import opcion7
from function8 import opcion8
from function9 import opcion9
from function10 import opcion10

while True:
    print("----")
    print("Menu")
    print("----")
    print("1. Titulo")
    print("2. Problema a resolver")
    print("3. Justificación")
    print("4. Objetivos")
    print("5. Marco teórico")
    print("6. Metodologia")
    print("7. Desarrollo del proyecto")
    print("8. Conclusiones")
    print("9. Referencias")
    print("10. Equipo")
    print("11. Salir")
    

    eleccion = int(input("ingresa una opción del menu:"))

    if eleccion == 1:
        opcion1()

    elif eleccion == 2:
        opcion2()

    elif eleccion == 3:
        opcion3()

    elif eleccion == 4:
        opcion4()

    elif eleccion == 5:
        opcion5()

    elif eleccion == 6:
        opcion6()

    elif eleccion == 7:
        opcion7()

    elif eleccion == 8:
        opcion8()

    elif eleccion == 9:
        opcion9()

    elif eleccion == 10:
        opcion10()

    elif eleccion == 11:
        break

    else:
        print("Opción no válida, vuelva a intentar")



        
