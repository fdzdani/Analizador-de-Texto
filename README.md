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
Una vez tengamos el entorno activado debemos descargar los modulos necesarios para correr nuestro programa, para ello utilizaremos el archivo ````modulos.txt```` proporcionado en el repositorio que contiene todas
