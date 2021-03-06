#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Se recoge la información de las galaxias plate, mjd y fiber de galaxias_dec y se almacenan los enlaces interactivos
# de los espectros en enlaces

import pandas # Librería para trabajar con csv

# Constantes

SDSS_IMAGES_URL = 'https://dr14.sdss.org/optical/spectrum/view?plate='

# Tomamos con la librería panda los elementos de csv y los separamos en dos arrays
data = pandas.read_csv('./galaxias_dec/Galaxias0dec.csv', header = 0, dtype = str)
plate = list(data.plate)
mjd = list(data.mjd)
fiber = list(data.fiberid)

# Almacenamos todos los urls y creamos un csv donde vamos guardando a su vez los enlaces
urls = []
file = open ('./enlaces14.csv', 'w')
for j in range(0, len(plate)):
  urls.append(SDSS_IMAGES_URL + plate[j] + '&mjd=' + mjd[j] + '&fiberid=' + fiber[j])
  file.write(urls[j] + '\n')
