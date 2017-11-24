# Galaxias-raras

En este repositorio hay tres directorios principales:

- 1º "Datos web": donde están los programas que nos generan los cinco enlaces de cada galaxia además de descargar una imagen y un espectro de cada una de ellas. Tres de ellos, de los que solo generan enlaces, se pueden observar los ficheros resultantes, pero los otros dos no, ya que generan demasiadas imágenes para ser subidas a esta plataforma.
- 2º "Separador de tablas": donde además de estar la información de las diferentes galaxias obtenidas desde https://dr12.sdss.org/optical/spectrum/search, hay dos pequeños programas de los que uno detecta las posiciones donde están las galaxias de cada tabla en la tabla principal (cada tabla tiene asignada una rareza para la galaxia). Y el otro nos devuelve en qué tabla aparece cada galaxia, ya que algunas aparecen en más de una. También están en este directorio los ficheros resultantes de los programas ("listas" y "posiciones").
- 3º "Pagina web": Donde se toman todos los datos resultantes de los programas anteriores, a excepción de las imágenes. El programa "creahtmls" nos genera, usando python y con ayuda de los ficheros "recurso_inicio", "recurso_fila" y "recurso_final", 17 códigos html para todas las galaxias (la principal y las diferentes tablas). También se pueden ver los códigos resultantes.
