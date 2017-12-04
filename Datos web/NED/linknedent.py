# Tomando las coordenadas de las galaxias de galaxias_sexag devuelve los enlaces de la página web en enlaces.

import pandas # Librería para trabajar con csv

# Constantes

SDSS_IMAGES_URL = ['https://ned.ipac.caltech.edu/cgi-bin/objsearch?search_type=Near+Position+Search&in_csys=Equatorial&in_equinox=J2000.0&lon=', 's&lat=',
's&radius=0.1&hconst=73&omegam=0.27&omegav=0.73&corr_z=1&z_constraint=Unconstrained&z_value1=&z_value2=&z_unit=z&ot_include=ANY&nmp_op=ANY&out_csys=Equatorial&out_equinox=J2000.0&obj_sort=Distance+to+search+center&of=pre_text&zv_breaker=30000.0&list_limit=5&img_stamp=YES']
# Tomamos con la librería panda los elementos de csv y los separamos en dos arrays
data = pandas.read_csv('./galaxias_sexag/Galaxias0.csv', header = 0, dtype = str)
ra = list(data.ra)
dec = list(data.dec)

# Quitamos los : de las coordenadas para introducirlo en la pagina web sin problemas
dec = list(map(lambda x: x.replace('+','%2B'), dec))

# Almacenamos todos los urls y creamos un csv donde vamos guardando a su vez los enlaces
urls = []
file = open ("./enlacesent.csv", "w")
for j in range(0, len(ra)):
  urls.append(SDSS_IMAGES_URL[0] + ra[j][:2]+ 'h' + ra[j][2:4] + 'm' + ra[j][4:] + SDSS_IMAGES_URL[1] + dec[j][:-7] + 'd' + dec[j][-7:-5] + 'm' + dec[j][-5:] + SDSS_IMAGES_URL[2])
  file.write(urls[j] + '\n')
