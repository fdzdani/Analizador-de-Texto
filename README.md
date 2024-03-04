# Analisis de articulos
## Descripcion
Este proyecto hace uso de la herramienta grobid para procesar los distintos articulos que se le proporcione mediante un script escrito en Python que hace de pipeline entre nuestro sistema y el servidor de grobid, una vez generados los documentos XML, existen otros 3 scripts para poder generar una nube de palabras o wordcloud mediante la informacion abstracta del XML, mostrar el numero de figuras en cada uno de los articulos procesados, y crear una lista de todos los links encontrados en cada articulo.
## Requisitos
Para poder utilizar las herramientas proporcionadas en este repositorio se necesitara [instalar grobid](https://grobid.readthedocs.io/en/latest/Install-Grobid/) y tener corriendo un [servidor de grobid](https://grobid.readthedocs.io/en/latest/Grobid-service/), ademas tambien se deberia tener instalado el [cliente-python de grobid](https://github.com/kermitt2/grobid_client_python/blob/master/Readme.md) para poder hacer llamadas al servidor de grobid desde el script del pipeline
## Instrucciones de instalacion
Para utilizar los recursos proporcionados en este repositorio se debe descargar el .zip con todo el contenido o realizar un ````git clone```` de este repositorio. Una vez obtengas el repositorio en tu maquina, solo debes crear un entorno virtual con los modulos necesarios para correr los scripts. Para esto tenemos dos opciones:
### Venv
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
Una vez tengamos el entorno activado debemos descargar los modulos necesarios para correr nuestro programa, para ello utilizaremos el archivo [modulos.txt](https://github.com/fdzdani/Extraccion-de-Texto/blob/Develop/modulos.txt) proporcionado en el repositorio para descargar todas las librerias necesarias utilizando:
````
pip install -r modulos.txt
````
### Conda
Para utilizar conda para crear el entorno virtual primero debemos [descargar anaconda](https://www.hostinger.es/tutoriales/instalar-anaconda-python-en-ubuntu). Una vez descargado debemos crearemos el entorno con todas las librerias necesarias a partir del archivo [enviroment.yml](https://github.com/fdzdani/Extraccion-de-Texto/blob/Develop/enviroment.yml) con:
```` 
conda env create -f environment.yml
````
y activarlo:
````
conda activate nombre_entorno
````
Una vez instalado todo podemos hacer en ambos casos un ````pip freeze```` para comprobar que todo se ha instalado correctamente, y pasar a la ejecucion.
## Instrucciones de ejecucion
Para la ejecucion del programa simplemente debemos introducir los articulos que queremos procesar en la carpeta de entrada, tambien tenemos que [activar el servidor de grobid](https://grobid.readthedocs.io/en/latest/Grobid-service/), y por ultimo activar el entorno virtual si no lo tenemos activado ya. Una vez hecho todo lo anterior corremos el script principal mediante el comando:
````bash
python3 main.py
````
Que se ocupara de correr todos los otros scripts.
### Posibles errores durante la ejecucion
Este es un posible error que puede salir durante la ejecucion del programa
````
Warning: Ignoring XDG_SESSION_TYPE=wayland on Gnome. Use QT_QPA_PLATFORM=wayland to run on Wayland anyway.
qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

Available platform plugins are: eglfs, linuxfb, minimal, minimalegl, offscreen, vnc, wayland-egl, wayland, wayland-xcomposite-egl, wayland-xcomposite-glx, webgl, xcb.

Aborted (core dumped)
````
Una posible solucion para este problema es instalar el siguiente plugin en Ubuntu:
````bash
sudo apt install qtwayland5
````
