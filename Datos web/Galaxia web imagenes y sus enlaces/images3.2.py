#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Este algoritmo toma las coordenadas de las galaxias y nos crea images, directorio con las imágenes de las galaxias y enlaces, fichero csv con
# los enlaces de donde se descargaron. Teniendo en cuenta que algunas imágenes no admiten el parámetro S (object with spectra). Donde primero se
# calcularon los enlaces defectuosos (código que se dejó comentado) y posteriormente se añadieron en DEFECT para así poder descargar todas las
# imágenes sin problemas.

import os # Librería para gestionar ficheros, carpetas, etc.
import urllib # Librería para acceder a url y descargar contenido
import pandas # Librería que uso para trabajar con ficheros csv

# Constantes
DIR_NAME = 'galaxias_dec' # Nombre de la carpeta que contiene los CSV con las coordenadas de las galaxias
SDSS_IMAGES_URL = [ # Dirección de la web a la que solicitar los datos
  'http://skyserver.sdss.org/dr14/SkyServerWS/ImgCutout/getjpeg?TaskName=Skyserver.Chart.List&ra=',
  '&scale=0.4&width=500&height=500&opt=GLS', '&scale=0.4&width=500&height=500&opt=GL' # Se puede añadir GLS (G es grid, L label y S object with spectra)
]
IMAGES_FOLDER = 'images'
GALAXY_FILES = 1
DEFECT = [51,94,95,96,99,108,111,115,167,168,170,191,192,213,240,320]

# Función utilizada para crear carpetas. Comprueba si la carpeta con el nombre que le has dado existe, y la crea en caso negativo.
def create_dir(name):
  directory = os.path.dirname(name)
  if not os.path.exists(directory):
    os.makedirs(name)

create_dir('images/') # Creación de la carpeta "images"

# Bucle que nos recorre los diferentes ficheros con galaxias (en este caso solo hay u1)

for i in range(0, GALAXY_FILES):
  urls = [] # Cada vez que empieza un fichero nuevo debe vaciarse
  file_name = 'Galaxias' + str(i) + 'dec.csv'


  # Recogemos las coordenadas de las galaxias del fichero
  data = pandas.read_csv('./galaxias_dec/' + file_name, header = 0, dtype = str)
  ra = list(data.ra)
  dec = list(data.dec)
  for j in range(0, len(ra)):

    # Algunos enlaces dan error por la página debido a S (object with spectra), así que separamos esos casos para obtener las imágenes sin ese parámetro
    if j in DEFECT:
      urls.append(SDSS_IMAGES_URL[0] + ra[j] + '&dec=' + dec[j] + SDSS_IMAGES_URL[2])
    else:
      urls.append(SDSS_IMAGES_URL[0] + ra[j] + '&dec=' + dec[j] + SDSS_IMAGES_URL[1])

  folder_name = file_name.split('.')[0]
  create_dir('images/' + folder_name + '/')
  file = open ("./enlaces.csv", "w")
  # file2 = open("./enlacesdefectuosos.csv", "w")

  # Detectamos con try y expept las galaxias que no podemos obtener con el parámetro S
  for index, url in enumerate(urls):
    file.write(url + '\n')
  # try:
    urllib.request.urlretrieve(url, 'images/' + folder_name + '/' + folder_name + '_' + str(index) + '.jpg')
  # except:
    # file2.write(str(index) + ',')
