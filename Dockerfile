from python:3.10.12

RUN git clone https://github.com/fdzdani/Extraccion-de-Texto.git

RUN conda env create -f enviroment.yml

RUN conda activate analizador

