#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Este algoritmo toma todas las tablas de las galaxias y devuelve a que tabla pertence cada galaxia en listas.

import pandas # Librería para trabajar con csv

info_sexa = []
ip = []
file = open ("./listas.csv", "w")

for i in range(0,17):
  info_sexa.append(pandas.read_csv('Galaxias' + str(i) + '.csv', header = 0, dtype = str))
  ip.append(list(info_sexa[i].specobj_id))

for element in ip[0]:
  for j in range(1,17):
    if element in ip[j]:
      file.write(str(j) + ',')
  file.write('\n')
