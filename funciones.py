def menu_principal():

    print("--------------------------------------------------")
    print("Bienvenido a GEOCIUD")
    print("--------------------------------------------------")
    print("--------------------------------------------------")
    print("--------------------------------------------------")

    print("¿Que desea realizar?")
    print("0. Salir de GEOCIUDAD")
    print("1. agregar ciudad")
    print("2. editar la informacion de una ciudad")
    print("3. buscar ciudad")
    print("--------------------------------------------------")

    while True:
            

            opcion = str(input("Ingrese la opcion que desea: "))
            if opcion == "1":
                print("--------------------------------------------------")
                print("1") 
            elif opcion == "2":
                print("--------------------------------------------------")
                print("2")   
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

print(menu_principal())