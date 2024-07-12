# GEOCIUD

### Descripcion
El repositorio cuenta con un software para ver informacion de ciudades

Este software contiene multiples funciones para un usuarios
***
## Tabla de contenido
| Indice |  |
|--|--|
| 1 | [Descripcion](#Descripcion) |
| 2 | [Informacion general](#Informacion-general)|
| 3 | [Instalacion](#Instalacion) |
| 4 | [Tecnologias utilizadas](#Tecnologias-utilizadas) |
| 5 | [Hecho por](#Desarrolladores)|
| 6 | [Mensaje del desarrollador](#Mensaje-de-los-desarrolladores)|

***
> [!IMPORTANT]  
>
>### Informacion-general
> El desarrollo del software cuenta con un modulo de usuario el cual cuenta con requerimientos basicos como
>
>* registrar ciudades
>* Actualizacion de la informacion de ciudades
>* visualizacion de informacion de ciudades
>* filtrar busqueda por ciudades 
>
> **El menu de usuario le permite realizar las siguentes funciones**
>
> 
> para cargar los datos y guardar se uso la siguentes funciones
> 
```bash
>import json
>
>def cargar_datos(archivo):
>    datos = {}
>    with open(archivo,"r") as file:
>        datos=json.load(file)
>    return datos
>        
>        
>
>def guardar_datos(datos, archivo):
>    datos = dict(datos)
>    
>    diccionario=json.dumps(datos, indent=4)
>    file=open(archivo,"w")
>    file.write(diccionario)
>    file.close()
```
> [!IMPORTANT]
> La cual se encarga de utilizar archivos json para guardar diccionarios con informacion esta funcion se utiliza en fuciones como
>   
```bash
>from datos import *
>
>RUTA_BASE_DE_DATOS = "tienda.json"
>datos = cargar_datos(RUTA_BASE_DE_DATOS)
>#Menu para escoger que producto se va a añadir
```
> [!IMPORTANT]
> no se busca continuar con el proyecto o solucionar problemas que presenta actualmente en base a esta informacion no recibira actualizaciones el repositorio
>
>### Instalacion
>
>1. Descargar el archivo zip desde el repositorio
>2. Descomprimir el archivo zip
>3. Abrir la carpeta desde visual estudio code
>4. Iniciar el terminal desde el archivo main.py  
>### Tecnologias-utilizadas
>Lista de lenguajes en los cuales se desarrollo
>* [Python](Python): Version: 3.12.2 
>

***
> [!WARNING]  
> 
>### Desarrolladores
>* [Carlos Cotes](https://gist.github.com/CarlosCotes)
>* [Nicolas Ruiz](https://gist.github.com/Nicolas-ruizg)
>
***
> [!NOTE]
>### Mensaje-de-los-desarrolladores
>Gracias por ver este repositorio

