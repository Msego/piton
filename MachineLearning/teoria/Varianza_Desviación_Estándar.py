 edades = [13, 14, 15, 15, 15, 16, 17, 18, 20]
 len(edades)
9
 suma = sum(edades)
 suma
143
 media = 1.0*(suma / len(edades))
 media
15.0
 media = (1.0*suma / len(edades))
 media
15.88888888888889
 residuos = [x-media for x in edades]
 residuos2 = [x**2 for x in residuos]
 desviacion = sum(residuos2) / len(edades)
 desviacion
4.098765432098765
 import math
 desv_std = math.sqrt(desviacion)
 desv_std
2.0245407953653998