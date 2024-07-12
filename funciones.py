from datos import*
def registrar_ciudad(datos):
    datos = dict(datos)
    ciudad = {}
    ciudad["nombre"] = input("Ingrese el nombre de la ciudad : ")
    while True:
        try:
            ciudad["cod"] = int(input("Ingrese el codigo postal: "))
            break
        except ValueError:
            print("codigo postal invalido . Por favor, ingrese un codigo válido.")
                    
    ciudad["poblacion"] = input("Ingrese la poblacion total de la ciudad: ")
    ciudad["pais"] = input("Ingrese el pais: ")
    

    datos["clientes"].append(ciudades)
    print("¡Cliente registrado con éxito!")
    return datos

def actualizar_ciudad(datos):
    datos=dict(datos)
    codigo =input("Ingrese el codigo postal: ")
    for i in range(len(datos["ciudades"])):
        if datos["ciudades"][i]["cod"]== codigo:


            while True:
                print("¿que te gustaria cambiar?")
                print("(1) para modificar el nombre: ")
                print("(2) para modificar el codigo postal: ")
                print("(3) para modificar la poblacion total: ")
                print("(4) para modificar la pais: ")
                print("(0) para salir ")
                opc=input("ingrese la opcion: ")

                if opc=="1":
                    datos["ciudades"][i]["nombre"]= input("ingrese el nuevo nombre: ")
                    print("se guardo con exito")
                    print("------------------------------------------------")
                elif opc== "2":
                    datos["ciudades"][i]["cod"]=input("ingrese el nuevo codigo postal: ")
                    print("se guardo con exito")
                    print("------------------------------------------------")

                elif opc=="3":
                    datos["ciudades"][i]["poblacion"]=input("ingrese la nueva poblacion: ")
                    print("se guardo con exito")
                    print("------------------------------------------------")
                elif opc=="4":
                    datos["ciudades"][i]["pais"]=input("ingrese el nuevo pais: ")
                    print("se guardo con exito")
                    print("------------------------------------------------")    
                elif opc=="0":
                    break
            break
    return datos

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