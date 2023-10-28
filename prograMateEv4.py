#Evaluacion 3&4 Programación matemática
import numpy as np


costos = np.array([[10, 7, 5, 12],[6, 2, 9, 11],[8, 6, 4, 14]])
capacidad = [20, 30, 10]
requerimientos = [15, 25, 20, 10]

asignacion = np.zeros(costos.shape)
i = j = 0

while sum(capacidad) > 0 and sum(requerimientos) > 0:
    asignado = min(capacidad[i], requerimientos[j])
    asignacion[i][j] = asignado
    capacidad[i] -= asignado
    requerimientos[j] -= asignado

    if capacidad[i] == 0 and i < len(capacidad) - 1:
        i += 1
        
    if requerimientos[j] == 0 and j < len(requerimientos) - 1:
        j += 1

costo_total = np.sum(asignacion * costos)
costo_trabajador = np.sum(asignacion * costos, axis=1)

print("Matriz de asignación resultante:")
print(asignacion)
print("\nEl costo total de la asignación es: ", costo_total)
for i in range(len(costo_trabajador)):
    print(f"\nEl costo del Trabajador {i+1} es: ", costo_trabajador[i])
