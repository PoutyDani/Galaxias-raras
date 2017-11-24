# Algoritmo que nos descarga todos los enlaces CAS acudiento a las coordenadas de las galaxias en galaxias_dec
# y nos lo almacena en enlaces.

import pandas

SDSS_IMAGES_URL = 'http://skyserver.sdss.org/dr14/en/tools/chart/navi.aspx?ra='

data = pandas.read_csv('./galaxias_dec/Galaxias0dec.csv', header = 0, dtype = str)
ra = list(data.ra)
dec = list(data.dec)

urls = []
file = open ("./enlaces.csv", "w")
for j in range(0, len(ra)):
  urls.append(SDSS_IMAGES_URL + ra[j] + '&dec=' + dec[j])
  file.write(urls[j] + '\n')
