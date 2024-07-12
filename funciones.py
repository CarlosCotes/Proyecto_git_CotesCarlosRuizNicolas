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

    