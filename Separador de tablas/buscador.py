#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Este algoritmo toma las posiciones de todas las galaxias y las de cada tabla y devuelve posiciones, un csv donde se almacena en
# cada línea la posición donde están las galaxias de cada tabla en la total. Luego hacemos exactamente lo mismo pero para las
# posiciones de las galaxias que son observables o no desde Paranal y ORM.

import pandas # Librería para trabajar con csv

info_sexa = []
ip = []
file = open ("./posiciones.csv", "w")

for i in range(0,17):
  info_sexa.append(pandas.read_csv('Galaxias' + str(i) + '.csv', header = 0, dtype = str))
  ip.append(list(info_sexa[i].specobj_id))

for j in range(0,17):
  for index, element in enumerate(ip[0]):
    if element in ip[j]:
      file.write(str(index) + ',')
  file.write('\n')


dec_sex = list(info_sexa[0].dec)
for i in range(0,382):
  dec_sex[i] = dec_sex[i].replace(':', '').replace('\'','')
  dec_sex[i] = float(dec_sex[i])
  if dec_sex[i] >= 50000:
    file.write(str(i) + ',')
file.write('\n')
for i in range(0,382):
  if dec_sex[i] <= 50000:
    file.write(str(i) + ',')
