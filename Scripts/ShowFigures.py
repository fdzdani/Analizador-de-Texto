import matplotlib.pyplot as plt
import os
import xml.etree.cElementTree as ET
import textwrap

xmlfiles = "./SalidaGrobid/"
output = "./Salida/"
figuras = {}

for xml in os.listdir(xmlfiles):
    path = os.path.join(xmlfiles, xml)
    if os.path.isfile(path) and path.endswith(".xml"):
        with open(path, 'r') as file:
            xml_data = file.read()
        root = ET.fromstring(xml_data)
        namespaces = {'tei':'http://www.tei-c.org/ns/1.0'}
        figura = root.findall('.//tei:figure', namespaces)
        xml = os.path.splitext(xml)[0].replace(".tei","").replace(".grobid", "")
        figuras[xml] = len(figura)
        
archivo_pdf = "Figuras.pdf"
path_pdf = os.path.join(output, archivo_pdf) 

wrapped_labels = ['\n'.join(textwrap.wrap(label,20)) for label in figuras.keys()]        
plt.bar(range(len(figuras)), list(figuras.values()), align='center')
plt.xticks(range(len(figuras)), wrapped_labels, rotation=90)
plt.tight_layout()

plt.savefig(path_pdf, bbox_inches='tight', format='pdf')
plt.close()
