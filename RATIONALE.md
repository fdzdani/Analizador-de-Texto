# Rationale Proyecto de Analisis de Articulos 

## Introduccion 

Este proyecto tiene el objetivo de automatizar el analisis de documentos procesados con Grobid. 

## Generacion de una Nube de palabras 

### Descripcion:

Creamos una nube de palabras para visualizaar la informacion abstracta del documento 

### Justificacion: 

#### Para esta tarea vamos a utilizar distintas herramientas entre las que se encuentran: 

* Biblioteca wordcloud para generar la nube de palabras 

* Biblioteca matplotlib.pyplot como plt para mostrar dicha nube de palabras generada con wordcloud 

* Biblioteca os que permite ejecutar mandatos del sistema operativo dentro de Python 

* Biblioteca xml.etree.cElementTree como ET que nos permite trabajar con documentos XML en Python 

### Verificación de los datos de entrada: 
```python
xmlfiles = "./resources/test_out/"

for xml in os.listdir(xmlfiles):
    path = os.path.join(xmlfiles, xml)
    if os.path.isfile(path) and path.endswith(".xml"):
```
Para verificar los datos de entrada que hemos obtenido del directorio salida, establecido en el pipeline entre python y grobid, fueran documentos XML hemos hecho dos comprobaciones la primera es que el path que hemos obtenido sea un file y la segunda que termine en .xml

### Obtencion de los datos:
```python
with open(path, 'r') as file:
            xml_data = file.read()
        root = ET.fromstring(xml_data)
        namespaces = {'tei':'http://www.tei-c.org/ns/1.0'}
        abstracts = root.findall('.//tei:abstract', namespaces)
        for abstract in abstracts:
            div = abstract.find('tei:div', namespaces)
            p = div.find('tei:p', namespaces)
            if isinstance(p.text, str):
                abstract_info = p.text
```
Para obtener los datos abstractos necesarios para generar la nube de palabras, para ello hemos usados las funciones find de ET para encontrar las etiquetas que buscamos y para navegar dentro de esas etiquetas. Una vez obtenidos los datos que buscamos comprobamos que estos sean en formato de texto para poder crear el wordcloud

### Procesado de los datos:
````python
wordcloud = WordCloud(width = 800, height = 800, background_color = 'white', 
                      stopwords = None, min_font_size = 10).generate(abstract_info)
        plt.figure(figsize = (8, 8), facecolor = None)
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.tight_layout(pad = 0)
    
        plt.title(xml)

        plt.show()
````
Para el procesado de los datos abstractos obtenidos utilizaremos wordcloud para generar la nube de palabras y plt para mostrar los resultados de wordcloud

### Verificacion:
La verificacion de los resultados mostrados por el script se ha hecho de forma manual, puesto que el script muestra una nube de palabras clave se puede comprobar que esta nube es proporcionada por la informacion en los datos abstractos de forma manual

## Visualizacion del numero de figuras por articulo

### Descripcion:
Creamos una visualizacion que nos muestre el numero de figuras contenido en cada articulo

### Justificacion: 

#### Para esta tarea vamos a utilizar distintas herramientas entre las que se encuentran: 

* Biblioteca matplotlib.pyplot como plt para mostrar dicha nube de palabras generada con wordcloud 

* Biblioteca os que permite ejecutar mandatos del sistema operativo dentro de Python 

* Biblioteca xml.etree.cElementTree como ET que nos permite trabajar con documentos XML en Python 
