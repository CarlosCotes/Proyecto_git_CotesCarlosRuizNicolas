from datos import*
from funciones import*

RUTA_BASE_DE_DATOS = "ciudad.json"


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
                    buscador_ciudades()
                elif opcion == "0":
                    print("--------------------------------------------------")
                    print("Saliendo")
                    print("Gracias por usar GEOCIUD")
                    break
                elif opcion != int:
                    print("--------------------------------------------------")
                    print("opcion invalida")







guardar_datos(datos, RUTA_BASE_DE_DATOS)