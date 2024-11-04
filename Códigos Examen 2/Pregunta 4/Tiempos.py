import time
import csv
from Pregunta4 import f_3_3, f_3_3_cola, f_3_3_iterativo

# Generar los valores de prueba
valores_pruebas = [i for i in range(86)]
tiempos_rec_normal = []
tiempos_rec_cola = []
tiempos_it = []

# Medir los tiempos de ejecución promediados
for k in valores_pruebas:
    inicio_rec = time.time_ns() / 1_000_000
    f_3_3(k)
    final_rec = time.time_ns() / 1_000_000
    tiempos_rec_normal.append(final_rec-inicio_rec)
    
    inicio_cola = time.time_ns() / 1_000_000
    f_3_3_cola(k)
    final_cola = time.time_ns() / 1_000_000
    tiempos_rec_cola.append(final_cola-inicio_cola)
    
    inicio_it = time.time_ns() / 1_000_000
    f_3_3_iterativo(k)
    final_it = time.time_ns() / 1_000_000
    tiempos_it.append(final_it-inicio_it)

# Exportar los tiempos a un archivo CSV
with open('tiempos_ejecucion.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['n', 'rec_normal', 'rec_cola', 'iterativo'])
    for i in range(len(valores_pruebas)):
        writer.writerow([valores_pruebas[i], tiempos_rec_normal[i], tiempos_rec_cola[i], tiempos_it[i]])

print("Datos exportados a tiempos_ejecucion.csv")
