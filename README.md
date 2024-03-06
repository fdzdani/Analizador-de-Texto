# Analisis de Articulos
[![Documentation Status](https://readthedocs.org/projects/analizador-de-texto/badge/?version=latest)](https://analizador-de-texto.readthedocs.io/es/latest/?badge=latest)
## Descripcion  
Este proyecto hace uso de la herramienta grobid para procesar los distintos articulos que se le proporcione mediante un script escrito en Python que hace de pipeline entre nuestro sistema y el servidor de grobid, una vez generados los documentos XML, existen otros 3 scripts para poder generar una nube de palabras o wordcloud mediante la informacion abstracta del XML, mostrar el numero de figuras en cada uno de los articulos procesados, y crear una lista de todos los links encontrados en cada articulo.
## Requisitos
* Python 3.10.12
* Grobid
* Python-client-grobid
  
Para poder utilizar las herramientas proporcionadas en este repositorio se necesitara tener [instalado pyhton 3.10.12](), [instalar grobid](https://grobid.readthedocs.io/en/latest/Install-Grobid/) y tener corriendo un [servidor de grobid](https://grobid.readthedocs.io/en/latest/Grobid-service/), ademas tambien se deberia tener instalado el [cliente-python de grobid](https://github.com/kermitt2/grobid_client_python/blob/master/Readme.md) para poder hacer llamadas al servidor de grobid desde el script del pipeline.
## Recomendaciones
* Ubuntu 22.04

Para el uso de estas herramientas se recomienda el uso de Ubuntu Linux por su facilida para la instalacion y puesta en marcha de todos los recursos proporcionados.
## Instrucciones de instalacion
### Instalacion mediante GitHub
Para utilizar los recursos proporcionados en este repositorio se debe descargar el .zip con todo el contenido o realizar un ````git clone```` de este repositorio. 

````
git clone https://github.com/fdzdani/Analizador-de-Texto.git
````

Una vez obtengas el repositorio en tu maquina, solo debes crear un entorno virtual con los modulos necesarios para correr los scripts. Para esto tenemos dos opciones utilizar venv o conda.
### Instalacion mediante Docker
Se provee de una imagen de Docker ya instalada. Para ejecutar los recursos mediante Docker, podras usar el Dockerfile que se proporciona en este repositorio:

```
docker build -t analizador .
```
## Preparacion del entorno
### Entorno virtual con Venv
Para utilizar venv para crear el entorno virtual primero debemos descargar esta herramienta con:
```` 
python3 -m pip install --user virtualenv
````
Una vez descargado debemos crear el entorno:
```` 
python3 -m venv nombre_entorno
````
y activarlo:
````
source nombre_entorno/bin/activate
````
Una vez tengamos el entorno activado debemos descargar los modulos necesarios para correr nuestro programa, para ello utilizaremos el archivo [modulos.txt](https://github.com/fdzdani/Analizador-de-Texto/blob/main/modulos.txt) proporcionado en el repositorio para descargar todas las librerias necesarias utilizando:
````
pip install -r modulos.txt
````
### Entorno virtual con Conda
Para utilizar conda para crear el entorno virtual primero debemos [descargar anaconda](https://www.hostinger.es/tutoriales/instalar-anaconda-python-en-ubuntu). Una vez descargado debemos crearemos el entorno con todas las librerias necesarias a partir del archivo [enviroment.yml](https://github.com/fdzdani/Analizador-de-Texto/blob/main/enviroment.yml) con:
```` 
conda env create -f environment.yml
````
y activarlo:
````
conda activate nombre_entorno
````
Una vez instalado todo podemos hacer en ambos casos un ````pip freeze```` para comprobar que todo se ha instalado correctamente, y pasar a la ejecucion.
## Instrucciones de ejecucion
Para la ejecucion del programa simplemente debemos introducir los articulos que queremos procesar en la carpeta de entrada, tambien tenemos que [activar el servidor de grobid](https://grobid.readthedocs.io/en/latest/Grobid-service/), y por ultimo activar el entorno virtual si no lo tenemos activado ya. 
Tras esto y si no lo hemos hecho nos movemos a la carpeta principal del proyecto haciendo un:
```
cd Analizador-de-Texto
````
Una vez hecho todo lo anterior corremos el script principal mediante el comando:
````
python3 main.py
````
Que se ocupara de correr todos los otros scripts. Despues de esto podremos consultar los resultados de la ejecucion en el subdirectorio de salida correspondiente.
### Posibles errores durante la ejecucion
Este es un posible error que puede salir durante la ejecucion del programa:
````
Warning: Ignoring XDG_SESSION_TYPE=wayland on Gnome. Use QT_QPA_PLATFORM=wayland to run on Wayland anyway.
qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

Available platform plugins are: eglfs, linuxfb, minimal, minimalegl, offscreen, vnc, wayland-egl, wayland, wayland-xcomposite-egl, wayland-xcomposite-glx, webgl, xcb.

Aborted (core dumped)
````
Una posible solucion para este problema es instalar el siguiente plugin en Ubuntu:
````
sudo apt install qtwayland5
````
## Ejemplos de ejecucion
Primero ponemos el servidor de grobid en marcha:

![image](https://github.com/fdzdani/Analizador-de-Texto/assets/115399394/8835f016-72dd-4062-bc50-53d95cd04546)

Tras esto activamos el entorno para empezar a trabajar:

![image](https://github.com/fdzdani/Analizador-de-Texto/assets/115399394/9476f9d0-6943-4459-a608-be837c30f43c)

A continuacion llamamos al script principal, el cual sirve de pipeline con grobid y llama a los demas scripts, y nos indica si esta funcionando el servidor de grobid:

![image](https://github.com/fdzdani/Analizador-de-Texto/assets/115399394/16cc959a-27dd-47cf-9513-3f26ac36895b)

Nos encontraremos con los siguientes documentos generados en el subdirectorio correspondiente:

![image](https://github.com/fdzdani/Analizador-de-Texto/assets/115399394/3fa70aa4-30e6-4ff0-835b-363fe2c87fb9)

### Resultados de ejecucion
WordCloud:

![image](https://github.com/fdzdani/Analizador-de-Texto/assets/115399394/24fc0404-a6f3-4ca2-981d-c7852b1f5196)

ShowFigures:

![image](https://github.com/fdzdani/Analizador-de-Texto/assets/115399394/df2e2198-8a44-4c91-92c7-4aeedd67de3c)

ListLinks:

![image](https://github.com/fdzdani/Analizador-de-Texto/assets/115399394/4cda5699-32ef-48da-a066-5cdbf3a8e956)

## Como citar
Si se quiere citar este repositorio, puedes hacerlo por ejemplo con BibTeX:

```bibtex
@misc{
    author = {Daniel Fernandez Gomez},
    year = {2024},
    title = {Analizador-de-Texto},
    publisher = {GitHub},
    url = {https://github.com/fdzdani/Analizador-de-Texto}
}
```
## Donde buscar ayuda
Para cualquier problema con la descarga, instalacion o puesta en marcha de grobid, acudir a la pagina principal de [documentacion de grobid](https://grobid.readthedocs.io/en/latest/Introduction/) o a su [repositorio de GitHub](https://github.com/kermitt2/grobid). Para cualquier problema con el cliente de python de grobid acudir a su [repositorio de GitHub](https://github.com/kermitt2/grobid_client_python).

## Licencia
Distribuido bajo [MIT License](https://opensource.org/license/mit). Ver [LICENSE](https://github.com/fdzdani/Analizador-de-Texto/blob/main/LICENSE) para mas informacion.

Autor principal y contacto: Daniel Fernandez Gomez (d.fgomez@alumnos.upm.es)
