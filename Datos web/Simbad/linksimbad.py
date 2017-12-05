# Tomando las coordenadas de las galaxias de galaxias_sexag devuelve los enlaces de la página web en enlaces.

import pandas # Librería para trabajar con csv

# Constantes

SDSS_IMAGES_URL = ['http://simbad.u-strasbg.fr/simbad/sim-coo?Coord=', '+', '&Radius=0.5&Radius.unit=arcmin&submit=submit+query']

# Tomamos con la librería panda los elementos de csv y los separamos en dos arrays
data = pandas.read_csv('./galaxias_sexa/Galaxias0.csv', header = 0, dtype = str)
ra = list(data.ra)
dec = list(data.dec)

# Quitamos los : de las coordenadas para introducirlo en la pagina web sin problemas
ra = list(map(lambda x: x.replace(':','+'), ra))
dec = list(map(lambda x: x.replace(':','+'), dec))

# Almacenamos todos los urls y creamos un csv donde vamos guardando a su vez los enlaces
urls = []
file = open ("./enlaces.csv", "w")
for j in range(0, len(ra)):
  urls.append(SDSS_IMAGES_URL[0] + ra[j] + SDSS_IMAGES_URL[1] + dec[j] + SDSS_IMAGES_URL[2])
  file.write(urls[j] + '\n')
