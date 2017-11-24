# Este algoritmo toma las id de las galaxias y nos crea images, directorio con los espectros de las galaxias y enlaces, fichero csv con
# los enlaces de donde se descargaron.

import os # Librería para gestionar ficheros, carpetas, etc.
import urllib # Librería para acceder a url y descargar contenido
import pandas # Librería que uso para trabajar con ficheros csv

DIR_NAME = 'galaxias_sexa'
SDSS_IMAGES_URL = 'http://skyserver.sdss.org/dr14/en/get/SpecById.ashx?id='
IMAGES_FOLDER = 'images'
GALAXY_FILES = 17

def create_dir(name):
  directory = os.path.dirname(name)
  if not os.path.exists(directory):
    os.makedirs(name)

create_dir('images/')

for i in range(0, GALAXY_FILES):
  file_name = 'Galaxias' + str(i) + '.csv'

  data = pandas.read_csv('./galaxias_sexa/' + file_name, header = 0, dtype = str)
  id = list(data.specobj_id)

  urls = []
  for j in range(0, len(id)):
    urls.append(SDSS_IMAGES_URL + id[j])

  folder_name = file_name.split('.')[0]
  create_dir('images/' + folder_name + '/')
  file = open("./enlaces" + str(i) + ".csv", "w")

  for index, url in enumerate(urls):
    urllib.request.urlretrieve(url, 'images/' + folder_name + '/' + folder_name + '_' + str(index) + '.jpg')
    file.write(url + '\n')
