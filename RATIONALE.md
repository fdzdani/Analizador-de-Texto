Rationale Proyecto de Analisis de Articulos 

Introduccion 

Este proyecto tiene el objetivo de automatizar el analisis de documentos procesados con Grobid. 

Generacion de una Nube de palabras:

  Descripcion:
  Vamos a crear una nube de palabras para visualizaar la informacion abstracta del documento 

  Justificacion: 
  Para esta tarea vamos a utilizar distintas herramientas entre las que se encuentran: 
    Biblioteca wordcloud para generar la nube de palabras 
    Biblioteca matplotlib.pyplot para mostrar dicha nube de palabras generada con wordcloud 
    Biblioteca os que permite ejecutar mandatos del sistema operativo dentro de Python 
    Biblioteca xml.etree.cElementTree que nos permite trabajar con documentos XML en Python 
    
  Verificación de los datos: 
  Para verificar los datos de entrada que hemos obtenido del directorio ... fueran documentos xml hemos hecho dos comprobaciones la primera es que el path que hemos obtenido que fuera un file y la segunda que terminen en .xml () 
