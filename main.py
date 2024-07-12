from datos import*
from funciones import*

RUTA_BASE_DE_DATOS = "ciudades.json"


datos = cargar_datos(RUTA_BASE_DE_DATOS)


while True:
                print(menu_principal())                
                opcion = str(input("Ingrese la opcion que desea: "))
                if opcion == "1":
                    print("--------------------------------------------------")
                    registrar_ciudad(datos) 
                elif opcion == "2":
                    print("--------------------------------------------------")
                    actualizar_ciudad(datos)
                elif opcion == "3":
                    print("--------------------------------------------------")
                    print("3")
                elif opcion != int:
                    print("--------------------------------------------------")
                    print("opcion invalida")
                elif opcion == "0":
                    print("--------------------------------------------------")
                    print("Saliendo")
                    

                    print("Gracias por usar GEOCIUD")
                    break








guardar_datos(datos, RUTA_BASE_DE_DATOS)