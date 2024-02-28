# Analisis de articulos
## Descripcion
Este proyecto hace uso de la herramienta grobid para procesar los distintos articulos que se le proporcione mediante un script escrito en Python que hace de pipeline entre nuestro sistema y el servidor de grobid, una vez generados los documentos XML, existen otros 3 scripts para poder generar una nube de palabras o wordcloud mediante la informacion abstracta del XML, mostrar el numero de figuras en cada uno de los articulos procesados, y crear una lista de todos los links encontrados en cada articulo.
## Requisitos
Para poder utilizar las herramientas proporcionadas en este repositorio se necesitara tener instalado y corriendo un servidor de grobid, y tener instalado el cliente de python de grobid para poder hacer uso del pipeline
