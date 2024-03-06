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
xmlfiles = "./SalidaGrobid/"
output = "./Salida/"

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
            abstract_info = p.text
```
Para obtener los datos abstractos necesarios para generar la nube de palabras, para ello hemos usados las funciones find de ET para encontrar las etiquetas que buscamos y para navegar dentro de esas etiquetas. Una vez obtenidos los datos que buscamos comprobamos que estos sean en formato de texto para poder crear el wordcloud

### Procesado de los datos:
````python
wordcloud = WordCloud(width = 800, height = 800, background_color = 'white', 
                      stopwords = None, min_font_size = 10).generate(abstract_info)
        archivo = os.path.splitext(xml)[0].replace(".tei","")
        archivo_pdf = archivo + ".wordcloud.pdf"
        path_pdf = os.path.join(output, archivo_pdf)
        plt.figure(figsize = (8, 8), facecolor = None)
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.tight_layout(pad = 0)

        plt.title(xml)
        plt.savefig(path_pdf, format='pdf')
        plt.close()
````
Para el procesado de los datos abstractos obtenidos utilizaremos wordcloud para generar la nube de palabras y plt para mostrar los resultados de wordcloud

### Verificacion:
La verificacion de los resultados mostrados por el script se ha hecho de forma manual, puesto que el script muestra una nube de palabras clave se puede comprobar que esta nube es proporcionada por la informacion en los datos abstractos de forma manual

## Visualizacion del numero de figuras por articulo

### Descripcion:
Creamos una visualizacion que nos muestre el numero de figuras contenido en cada articulo

### Justificacion: 

#### Para esta tarea vamos a utilizar distintas herramientas entre las que se encuentran: 

* Biblioteca matplotlib.pyplot como plt para mostrar el numero de figuras

* Biblioteca os que permite ejecutar mandatos del sistema operativo dentro de Python 

* Biblioteca xml.etree.cElementTree como ET que nos permite trabajar con documentos XML en Python

### Verificación de los datos de entrada: 
```python
xmlfiles = "./SalidaGrobid/"
output = "./Salida/"
figuras = {}

for xml in os.listdir(xmlfiles):
    path = os.path.join(xmlfiles, xml)
    if os.path.isfile(path) and path.endswith(".xml"):
```
Para verificar los datos de entrada que hemos obtenido del directorio salida, establecido en el pipeline entre python y grobid, fueran documentos XML hemos hecho dos comprobaciones la primera es que el path que hemos obtenido sea un file y la segunda que termine en .xml, ademas hemos creado el diccionario donde guardaremos el numero de figuras por cada articulo

### Obtencion de los datos:
```python
with open(path, 'r') as file:
            xml_data = file.read()
        root = ET.fromstring(xml_data)
        namespaces = {'tei':'http://www.tei-c.org/ns/1.0'}
        figura = root.findall('.//tei:figure', namespaces)
        xml = os.path.splitext(xml)[0].replace(".tei","").replace(".grobid", "")
        figuras[xml] = len(figura)
```
Para obtener el numero de figuras vamos obtenerlo buscando la etiqueta figure en el XML, para ello hemos usados las funciones find de ET para encontrar la etiqueta y luego contar el numero de objetos contenidos en la lista. Una vez obtenidos los datos los añadimos a nuestro diccionario

### Procesado de los datos:
````python
archivo_pdf = "Figuras.pdf"
path_pdf = os.path.join(output, archivo_pdf) 

wrapped_labels = ['\n'.join(textwrap.wrap(label,20)) for label in figuras.keys()]        
plt.bar(range(len(figuras)), list(figuras.values()), align='center')
plt.xticks(range(len(figuras)), wrapped_labels, rotation=90)
plt.tight_layout()

plt.savefig(path_pdf, bbox_inches='tight', format='pdf')
plt.close()
````
Para el procesado de los datos vamos a crear un diagrama de barras para mostrar el numero de figuras por cada articulo

### Verificacion:
La verificacion de los resultados mostrados por el script se ha hecho de forma manual, puesto que el script muestra un diagrama de barras con todos las figuras por articulos podemos comprobar facilmente si los datos obtenidos corresponden con la realidad

## Lista de links de cada articulo

### Descripcion:
Creamos una lista de links encontrados en cada articulo procesado

### Justificacion: 

#### Para esta tarea vamos a utilizar distintas herramientas entre las que se encuentran: 

* Biblioteca os que permite ejecutar mandatos del sistema operativo dentro de Python 

* Biblioteca xml.etree.cElementTree como ET que nos permite trabajar con documentos XML en Python

### Verificación de los datos de entrada: 
```python
xmlfiles = "./SalidaGrobid/"
output = "./Salida/"
links = {}

for xml in os.listdir(xmlfiles):
    path = os.path.join(xmlfiles, xml)
    if os.path.isfile(path) and path.endswith(".xml"):
```
Para verificar los datos de entrada que hemos obtenido del directorio salida, establecido en el pipeline entre python y grobid, fueran documentos XML hemos hecho dos comprobaciones la primera es que el path que hemos obtenido sea un file y la segunda que termine en .xml, ademas hemos creado el diccionario donde guardaremos la lista de links por cada articulo

### Obtencion de los datos:
```python
with open(path, 'r') as file:
            xml_data = file.read()
        root = ET.fromstring(xml_data)
        namespaces = {'tei':'http://www.tei-c.org/ns/1.0'}
        biblStruct = root.findall('.//tei:biblStruct', namespaces)
        url = []
        for ptr in biblStruct:
            link = ptr.find('.//tei:ptr', namespaces)
            if link is not None:
                url.append(link.attrib['target'])
        links[xml] = url
```
Para obtener los links de cada articulo vamos a buscar la etiqueta ptr dentro de biblStruct en el XML, para ello hemos usados las funciones find de ET para encontrar la etiqueta y luego guardamos cada link encontrado en una lista propia que sera de cada articulo. Una vez obtenidos los datos los añadimos a nuestro diccionario

### Procesado de los datos:
````python
with open(os.path.join(output, "Links.txt"),"w") as f:
	for articulo, urls in links.items():
		f.write(f'Articulo: {articulo} \nLinks: {urls}\n')
````
Para el procesado de los datos vamos a mostrar por pantalla cada articulo con su nombre y cada lista de links encontrados

### Verificacion:
La verificacion de los resultados mostrados por el script se ha hecho de forma manual, puesto que el script muestra por pantalla los links encontrados en cada uno de los articulos procesados
