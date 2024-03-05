# Analisis de articulos
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
## Contenido
- [Instalacion](https://extraccion-de-texto.readthedocs.io/es/latest/installation/)
- [Uso](https://extraccion-de-texto.readthedocs.io/es/latest/usage/)
- [Scripts](https://extraccion-de-texto.readthedocs.io/es/latest/scripts/)
## Licencia y contacto
Distribuido bajo MIT License. Ver LICENSE.txt para mas informacion.

Autor principal y contacto: Daniel Fernandez Gomez (d.fgomez@alumnos.upm.es)
