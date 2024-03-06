from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os
import xml.etree.cElementTree as ET

xmlfiles = "./SalidaGrobid/"
output = "./Salida/"

for xml in os.listdir(xmlfiles):
    path = os.path.join(xmlfiles, xml)
    if os.path.isfile(path) and path.endswith(".xml"):
        with open(path, 'r') as file:
            xml_data = file.read()
        root = ET.fromstring(xml_data)
        namespaces = {'tei':'http://www.tei-c.org/ns/1.0'}
        abstracts = root.findall('.//tei:abstract', namespaces)
        for abstract in abstracts:
            div = abstract.find('tei:div', namespaces)
            p = div.find('tei:p', namespaces)
            abstract_info = p.text
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
