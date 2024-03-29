# Instalacion
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
