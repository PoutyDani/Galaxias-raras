# Galaxias-raras

En este repositorio hay tres directorios principales:

1º **Datos web**: Directorio con programas para descargar enlaces y decargar información. Contiene:

    -**CAS**: Contiene **galaxias_dec/Galaxias0_dec.csv** con la información necesaria de las galaxias (ID, RA, DEC, etc), y un programa **linkcas.py** que genera en un fichero **enlaces.csv** con los enlaces CAS de todas las galaxias.

    -**Galaxia web espectros y sus enlaces**: Contiene **galaxias_sexa/Galaxias0.csv** con la información necesaria de las galaxias, y un programa **images4.py** que genera **images/Galaxias0** con en su interior una imagen del espectro de cada galaxia, además de **enlaces0.csv** que contiene los enlaces de donde se descargaron las imágenes de los espectros.

    -**Galaxia web imagenes y sus enlaces**: Contiene **galaxias_dec/Galaxias0_dec.csv** con la información necesaria de las galaxias, **enlacesdefectuosos.csv** que contiene la posición de las galaxias cuyas imágenes no se muestran con la opción de "Object with spectra" y **images3.2.py** programa que genera **images\Galaxias0dec** con su interior una imagen de cada galaxia, y **enlaces.csv** con los enlaces de donde se descargaron las imágenes.

    -**Interactive Spectrum**: **galaxias_dec/Galaxias0_dec.csv** con la información necesaria de las galaxias, **linkspec12.py** que genera **enlaces12.csv** con los enlaces de los espectros interactivos de las galaxias en DR12 y de igual forma **linkspec14.py** que genera **enlaces14.csv** en DR14.

    -**NED**: Contiene **galaxias_sexa/Galaxias0.csv** con la información necesaria de las galaxias, y un programa **linknedobj.py** que genera **enlacesobjc.csv** con los enlaces a la página NED de las galaxias del objeto y de igual forma con **linknedent.py** que genera **enlacesoent.csv** en un entorno de las coordenadas.

    -**Simbad**: Contiene **galaxias_sexa/Galaxias0.csv** con la información necesaria de las galaxias, y un programa **linksimbad.py** que genera **enlaces.csv** con los enlaces a la página Simbad de las galaxias.

2º **Separador de tablas**: Directorio con programas con todas las tablas de diferentes rarezas de galaxias, y programas que clasifican las galaxias y toman sus posiciones en la tabla total. Contiene:

    -**Galaxias_num_.csv** (num = 0,...,16): Son ficheros csv con todas las tablas de rareza incluyendo la total, 0.

    -**buscador.py**: Contiene un programa que toma todos los ficheros anteriores y devuelve **posiciones.csv** en la que en cada línea se escriben las posiciones de las galaxias de cada tabla en la tabla total (incluyendo si son visibles de paranal o ORM).

    -**buscadorinv.py**: Contiene un programa que toma cada galaxia del total y genera **listas.csv** donde en cada línea se escribe las tablas en las que aparece cada galaxia.

3º **Pagina web**: En ella está el código principal y toda la información necesaria para poderse generar la página web. Contiene:

    - **Datos**: Con toda la información de las galaxias:

      - **enlace_cas.csv**: Contiene los enlaces CAS de las galaxias.

      - **enlace_imag.csv**: Contiene los enlaces de donde se descargaron las imágenes de las galaxias.

      - **enlace_ned.csv**: Contiene los enlaces NED de las galaxias.

      - **enlace_simbad.csv**: Contiene los enlaces SIMBAD de las galaxias.

      - **enlace_spec.csv**: Contiene los enlaces de donde se descargaron los espectros de las galaxias en 'jpg'.

      - **enlace_spec_inter.csv**: Contiene los enlaces a espectros interactivos y más detallados de las galaxias.

      - **Galaxias0.csv**: Contiene la información de las galaxias (en sexagesimal).

      - **Galaxias0dec.csv**: Contiene la información de las galaxias (en decimal).

      - **listas.csv**: Contiene la información de a qué tabla de rarezas pertenece cada galaxia.

      -**posiciones.csv**: Contiene las posiciones en las que están ubicadas las galaxias de cada tabla en la tabla total.

    - **imagenes**: Contiene el directorio **Galaxias0** que contiene todas las imágenes en 'jpg' descargadas de las galaxias.

    - **imagenes_spec**: Contiene el directorio **Galaxias0** que contiene todos los espectros en 'jpg' descargados de las galaxias.

    - **Recursos**: En su interior hay "trozos" de código html que usa el código principal para crear la web además del código 'css'. Contiene:

      - **recurso_estilo.css**: Es un fichero 'css' en el que está el estilo de la web. Cada fichero 'html', una vez creado por el código, accede a este para tomar las características del estilo: márgenes, tipo de letra, color,...

      - **recurso_fila.htm**: Es tomado por el código principal como plantilla para crear cada fila de la tabla, al tiempo que se van sustituyendo las varibales.

      - **recurso_final.htm**: Es tomado por el código principal para escribir la parte final de cada fichero 'html'.

      - **recurso_inicio1.htm**, **recurso_inicio2.htm, **recurso_inicio3.htm**: Son tomados por el código principal para crear el inicio de cada fichero 'html' (a excepción de la tabla del sumario (al crear **web19.htm**) que solo toma **recurso_inicio1.htm** y **recurso_inicio2.htm**.

      - **recurso_ultabla1.htm** y **recurso_ultabla1.htm**: Son tomados por el código principal para crear la tabla del sumario.

    - **web**: Contiene los ficheros 'html' resultantes (**web_num_**) generados por el código principal, es decir la página web.

    - **creahtmls.py**: Código principal que me genera la página web en **web** tomando los datos de **Datos**, **imagenes**, **imagenes_spec** y **Recursos**. Para ejecutar "python creahtmls.py"
