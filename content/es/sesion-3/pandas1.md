---
title: "Primeros pasos con Pandas"
date: 2021-10-21T10:29:17+02:00
linkTitle: "Pandas 1"
weight: 40
description: >
    Introducción a la gestión de datos con Pandas
notas: > 
    

---
{{% pageinfo %}}
## Documentación
* https://pandas.pydata.org/docs/index.html

* <a target="_blank" href="https://colab.research.google.com/github/lmorillas/curso-python-iot/blob/sesiones/notebooks/introduccion_pandas.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

{{% /pageinfo %}}

# Clase: Introducción a la Librería Pandas en Python

## Introducción Teórica

### ¿Qué es Pandas?

Pandas es una biblioteca de Python que proporciona estructuras de datos de alto rendimiento y herramientas de análisis de datos. Es ideal para manipular y analizar datos, así como para organizar datos en un formato tabular y adjuntar etiquetas descriptivas a las filas y columnas. 

### ¿Por qué usar Pandas?

1. **Facilita el manejo de datos**: Ofrece estructuras como DataFrames y Series para manejar datos de manera eficiente.
2. **Potente para análisis de datos**: Proporciona funciones incorporadas para agrupar, fusionar y resumir datos.
3. **Compatibilidad con diferentes formatos de archivos**: Puedes importar datos desde varios formatos como CSV, Excel, JSON, SQL y muchos otros.

### Componentes principales

1. **Series**: Un array unidimensional etiquetado capaz de contener cualquier tipo de datos.
2. **DataFrame**: Una matriz bidimensional con etiquetas tanto de fila como de columna. Esencialmente, un conjunto de Series que comparten un índice.

## Ejemplo Interesante

### Analizar datos de ventas

Supongamos que tenemos un archivo CSV (`ventas.csv`) con la siguiente información:

```csv
Fecha,Producto,Cantidad,Precio
2023-01-01,Manzana,10,2.5
2023-01-01,Pera,5,3
2023-01-02,Manzana,8,2.5
2023-01-02,Pera,2,3
2023-01-03,Manzana,12,2.5
```

Podemos usar Pandas para responder preguntas como "¿Cuál es el producto más vendido?" o "¿Cuánto ingreso se generó cada día?"

```python
import pandas as pd

# Leer datos desde un archivo CSV
df = pd.read_csv('ventas.csv')

# Calcular el ingreso de cada venta
df['Ingreso'] = df['Cantidad'] * df['Precio']

# Sumar el ingreso por cada producto
ingreso_producto = df.groupby('Producto')['Ingreso'].sum()

# Sumar el ingreso por cada fecha
ingreso_fecha = df.groupby('Fecha')['Ingreso'].sum()

print(f"Ingreso por producto:\n{ingreso_producto}")
print(f"Ingreso por fecha:\n{ingreso_fecha}")
```

## Ejercicio Propuesto

### Filtrar y organizar datos climáticos

1. Suponga que tiene un archivo CSV (`clima.csv`) con datos climáticos que incluyen `Fecha`, `Temperatura` y `Humedad`.
2. Utilice Pandas para filtrar los días en los que la `Temperatura` fue superior a 25 grados y la `Humedad` fue inferior al 50%.
3. Guarde este subconjunto de datos en un nuevo archivo CSV (`dias_calurosos.csv`).

Este ejercicio permitirá a los estudiantes practicar la lectura de archivos, el filtrado basado en condiciones y la escritura en archivos, todo lo cual son tareas comunes en el análisis de datos.