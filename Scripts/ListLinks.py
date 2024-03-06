import os
import xml.etree.ElementTree as ET

xmlfiles = "./SalidaGrobid/"
output = "./Salida/"
links = {}

for xml in os.listdir(xmlfiles):
    path = os.path.join(xmlfiles, xml)
    if os.path.isfile(path) and path.endswith(".xml"):
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

with open(os.path.join(output, "Links.txt"),"w") as f:
	for articulo, urls in links.items():
		f.write(f'Articulo: {articulo} \nLinks: {urls}\n')
