# Tomando toda la información almacenada hasta ahora este algorimto devuelve 19 fichero html (web0 el que lo contiene todo)

import os # Librería para gestionar ficheros, carpetas, etc
import pandas # Librería que uso para trabajar con ficheros csv
import numpy # Librería para calcular media y varianza

RECIN = ['      <li><a ', '      <li><a class="active" ']
NUM_TABLAS = 19

# Recogemos la información de todos los ficheros
enlaces_cas = pandas.read_csv('Datos/enlace_cas.csv', header = None, dtype = str)[0]
enlaces_imag = pandas.read_csv('Datos/enlace_imag.csv', header = None, dtype = str)[0]
enlaces_spec = pandas.read_csv('Datos/enlace_spec.csv', header = None, dtype = str)[0]
enlaces_spec_inter = pandas.read_csv('Datos/enlace_spec_inter.csv', header = None, dtype = str)[0]
enlaces_ned = pandas.read_csv('Datos/enlace_ned.csv', header = None, dtype = str)[0]
enlaces_simbad = pandas.read_csv('Datos/enlace_simbad.csv', header = None, dtype = str)[0]
info_sexa = pandas.read_csv('Datos/Galaxias0.csv', header = 0, dtype = str)
info_dec = pandas.read_csv('Datos/Galaxias0dec.csv', header = 0, dtype = str)
info_pos = open('./Datos/posiciones.csv', 'r').read()
info_list = open('./Datos/listas.csv', 'r').read()
inicio = [
  open('./Recursos/recurso_inicio1.htm', 'r').read(),
  open('./Recursos/recurso_inicio2.htm', 'r').read(),
  open('./Recursos/recurso_inicio3.htm', 'r').read()
]
inicio[1] = inicio[1].split('\n')
rareza = inicio[1][:]  # Esto se usa para clonar el array ya que si no me copia el puntero y se me modifica la variable original
for i in range(1,17):
  if i < 10:
    rareza[i] = rareza[i][18:-9]
  else:
    rareza[i] = rareza[i][20:-9]
recurso_fila = open('./Recursos/recurso_fila.htm', 'r').read()
final = open('./Recursos/recurso_final.htm', 'r').read()

ip = list(info_sexa.specobj_id)
ra = list(info_dec.ra)
dec = list(info_dec.dec)
z = list(info_dec.z)
ra_sex = list(info_sexa.ra)
dec_sex = list(info_sexa.dec)

ra_sex_orden = list(map(lambda x: float(x), ra_sex))
dec_sex_vis = list(map(lambda x: float(x), dec_sex))

info_pos = info_pos.split(",\n")
info_pos.pop()
info_pos = list(map(lambda x: x.split(','), info_pos))
info_pos = list(map(lambda x: list(map(lambda y: int(y), x)), info_pos))
for x in info_pos:
  x.sort(key = lambda y: ra_sex_orden[y])

info_list = info_list.split(",\n")
info_list = list(map(lambda x: x.split(","), info_list))

ardilla = []
for i in range(len(ip)):
  ardilla.append('<div class="tooltip">' + info_list[i][0] + '<span class="tooltiptext">' + rareza[int(info_list[i][0])] + '</span></div>')
  for j in range(1, len(info_list[i])):
    ardilla[i] = ardilla[i] + ',\n      <div class="tooltip">' + info_list[i][j] + '<span class="tooltiptext">' + rareza[int(info_list[i][j])] + '</span></div>'

vis_orm = []
vis_paranal = []
nombre_ned = []
cond_cumple = []

for i in range(0,len(ip)):
  nombre_ned.append('SDSS J' + ra_sex[i] + dec_sex[i][:-1])
  ra_sex[i] = ra_sex[i][:2] + 'h' + ra_sex[i][2:4] + 'm' + ra_sex[i][4:] + 's'
  dec_sex[i] = dec_sex[i][:3] + 'd' + dec_sex[i][3:5] + 'm' + dec_sex[i][5:] + 's'
  if dec_sex_vis[i] >= 50000:
    vis_orm.append('YES')
    cond_cumple.append('DEC&nbsp;&ge;&nbsp;5d00m00s')
  else:
    vis_orm.append('NO')
  if dec_sex_vis[i] <= 50000:
    vis_paranal.append('YES')
    cond_cumple.append('DEC&nbsp;&le;&nbsp;5d00m00s')
  else:
    vis_paranal.append('NO')


for j in range(0,NUM_TABLAS):
  fila = []
  for i in info_pos[j]:
    filas = recurso_fila.replace('enlaces_imag[i]',enlaces_imag[i]).replace('str(i)',str(i)).replace('ip[i]',ip[i]).replace('ra_sex[i]',ra_sex[i])
    filas = filas.replace('ra[i]',ra[i]).replace('dec_sex[i]',dec_sex[i]).replace('dec[i]',dec[i]).replace('z[i]',z[i])
    filas = filas.replace('enlaces_spec[i]',enlaces_spec[i]).replace('enlaces_cas[i]',enlaces_cas[i]).replace('enlaces_spec_inter[i]',enlaces_spec_inter[i])
    filas = filas.replace('enlaces_ned[i]',enlaces_ned[i]).replace('vis_orm[i]',vis_orm[i]).replace('vis_paranal[i]',vis_paranal[i])
    filas = filas.replace('enlaces_simbad[i]',enlaces_simbad[i]).replace('nombre_ned[i]',nombre_ned[i])
    filas = filas.replace('cond_cumple[i]',cond_cumple[i]).replace('ardilla[i]',ardilla[i])
    fila.append(filas)

  web = open("./web/web" + str(j) + ".htm", "w")
  web.write(inicio[0])
  for t in range(0,20):
    if t == j:
      web.write(RECIN[1] + inicio[1][t] + '\n')
    else:
      web.write(RECIN[0] + inicio[1][t] + '\n')
  web.write(inicio[2])

  for i in range(0,len(fila)):
    web.write(fila[i])

  web.write(final)

# Ultima tabla: sumario
recurso_tabla = [open('./Recursos/recurso_ultabla1.htm', 'r').read(), open('./Recursos/recurso_ultabla2.htm', 'r').read()]
z = list(map(lambda x: float(x), z))

web = open("./web/web19.htm", "w")
web.write(inicio[0])
for t in range(0,20):
  if t == 19:
    web.write(RECIN[1] + inicio[1][t] + '\n')
  else:
    web.write(RECIN[0] + inicio[1][t] + '\n')
web.write(recurso_tabla[0])
rareza_2 = inicio[1][:]
sumario = []
for i in range(0, NUM_TABLAS):
  if i < 10:
    rareza_2[i] = rareza_2[i][16:-9]
  else:
    rareza_2[i] = rareza_2[i][17:-9]
  info_pos[i].sort(key = lambda y: z[y])
  sumario.append([0, 0])
  for j in range(0, len(info_pos[i])):
    sumario[i].append(z[info_pos[i][j]])
  media = numpy.mean(sumario[i][2:])
  desv = numpy.std(sumario[i][2:])
  recurso_tablas = recurso_tabla[1].replace('rareza_2[i]',rareza_2[i]).replace('z[info_pos[i][0]][:7]',str(z[info_pos[i][0]])[:7])
  recurso_tablas = recurso_tablas.replace('z[info_pos[i][-1]][:7]',str(z[info_pos[i][-1]])[:7]).replace('media[:7]',str(media)[:7]).replace('desv[:7]',str(desv)[:7])
  web.write(recurso_tablas)
web.write(final)
