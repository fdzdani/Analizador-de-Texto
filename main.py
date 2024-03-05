from grobid_client.grobid_client import GrobidClient
import os

cliente = GrobidClient(config_path="./grobid_client_python/config.json")

documentos = "./Entrada"

for documento in os.listdir(documentos):

    path = os.path.join(documentos, documento)
    
    cliente.process("processFulltextDocument", documentos, output="./SalidaGrobid", consolidate_citations=True,
                        tei_coordinates=True, force=True)

print("Ejecutando WordCloud.py desde el subdirectorio /Scripts")
exec(open("WordCloud.py").read())
print("Ejecutando ShowFigures.py desde el subdirectorio /Scripts")
exec(open("ShowFigures.py").read())
print("Ejecutando ListLinks.py desde el subdirectorio /Scripts")
exec(open("ListLinks.py").read())
print("Resultados guardados en el subdirectorio de /Salida")
