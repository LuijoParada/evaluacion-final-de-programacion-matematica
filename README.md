# Evaluación de Programación Matemática

Este repositorio contiene un script de Python para resolver un problema de asignación. El problema consiste en asignar trabajadores a tareas de manera que se minimice el costo total.

## Descripción del Código

El script utiliza la biblioteca `numpy` para manipular matrices y vectores. Se define una matriz de costos donde cada elemento representa el costo de asignar un trabajador a una tarea. También se definen dos vectores: uno para la capacidad de cada trabajador y otro para los requerimientos de cada tarea.

El script luego realiza un bucle hasta que todas las capacidades y requerimientos se hayan satisfecho. En cada iteración del bucle, se asigna la cantidad mínima entre la capacidad del trabajador y el requerimiento de la tarea. Luego se actualizan la capacidad y el requerimiento después de la asignación.

Finalmente, el script calcula el costo total de la asignación y el costo por trabajador y los imprime.
