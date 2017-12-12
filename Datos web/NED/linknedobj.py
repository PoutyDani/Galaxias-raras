#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Tomando las coordenadas de las galaxias de galaxias_sexag devuelve los enlaces de la página web en enlaces.

import pandas # Librería para trabajar con csv

# Constantes

SDSS_IMAGES_URL = ['https://ned.ipac.caltech.edu/cgi-bin/objsearch?objname=SDSS+',
'&extend=no&hconst=73&omegam=0.27&omegav=0.73&corr_z=1&out_csys=Equatorial&out_equinox=J2000.0&obj_sort=RA+or+Longitude&of=pre_text&zv_breaker=30000.0&list_limit=5&img_stamp=YES']

# Tomamos con la librería panda los elementos de csv y los separamos en dos arrays
data = pandas.read_csv('./galaxias_sexag/Galaxias0.csv', header = 0, dtype = str)
ra = list(data.ra)
dec = list(data.dec)

# Quitamos los : de las coordenadas para introducirlo en la pagina web sin problemas
dec = list(map(lambda x: x[:-1], dec))
dec = list(map(lambda x: x.replace('+','%2B'), dec))

# Almacenamos todos los urls y creamos un csv donde vamos guardando a su vez los enlaces
urls = []
file = open ("./enlacesobj.csv", "w")
for j in range(0, len(ra)):
  urls.append(SDSS_IMAGES_URL[0] + ra[j] + dec[j] + SDSS_IMAGES_URL[1])
  file.write(urls[j] + '\n')
