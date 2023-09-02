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

* <a target="_blank" href="https://colab.research.google.com/github/lmorillas/curso-python-iot/blob/main/notebooks/introduccion_pandas.ipynb">
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

* Descarga los datos de Zaragoza de este verano (julio y agosto) de la web de AEMET: https://opendata.aemet.es/centrodedescargas/productosAEMET? Necesitarás generarte una API Key. Los datos los tienes también aquí: [julio](https://raw.githubusercontent.com/lmorillas/curso-python-iot/main/notebooks/zaragoza-air-julio.json) [agosto](https://raw.githubusercontent.com/lmorillas/curso-python-iot/main/notebooks/zaragoza-air-agosto.json) [metadatos](https://raw.githubusercontent.com/lmorillas/curso-python-iot/main/notebooks/metadatos-clima.json)
> Ten cuidado con el encoding de los archivos. 
```python

url_metadatos = "https://raw.githubusercontent.com/lmorillas/curso-python-iot/main/notebooks/metadatos-clima.json"

r = requests.get(url_metadatos)

r.encoding = 'ISO-8859-1'  # los datos no están en utf-8
```


Puedes usar `encoding='latin-1'` en `pd.read_csv()` para evitar problemas.

* Analiza los metadatos.



1. Suponga que tiene un archivo CSV (`clima.csv`) con datos climáticos que incluyen `Fecha`, `Temperatura` y `Humedad`.
2. Utilice Pandas para filtrar los días en los que la `Temperatura` fue superior a 25 grados y la `Humedad` fue inferior al 50%.
3. Guarde este subconjunto de datos en un nuevo archivo CSV (`dias_calurosos.csv`).




## Unir Datos Climáticos en JSON con DataFrames de Pandas

Cuando tienes múltiples archivos JSON con datos climáticos y quieres unirlos en un solo DataFrame de Pandas, hay varias estrategias que podrías seguir. La elección del método dependerá del formato de tus datos y de cómo deseas unirlos (por ejemplo, unión por columnas o filas, unión interna, unión externa, etc.).

### Carga de Datos JSON en DataFrames

Primero, necesitas cargar tus archivos JSON en DataFrames individuales. Para ello, puedes usar la función `read_json` de Pandas.

```python
import pandas as pd

# Leer archivos JSON en DataFrames
df1 = pd.read_json("archivo_climatico1.json")
df2 = pd.read_json("archivo_climatico2.json")
```

### Unir DataFrames

Una vez que tienes los DataFrames, puedes usar métodos como `concat` o `merge` para unirlos.

#### Unión Vertical (Unión por Filas)

Si los archivos tienen las mismas columnas y deseas unirlos verticalmente (añadir filas de uno al otro), puedes utilizar `pd.concat`.

```python
# Unir DataFrames verticalmente
df_unido = pd.concat([df1, df2])
```

#### Unión Horizontal (Unión por Columnas)

Si los archivos tienen una columna en común (por ejemplo, `fecha`), y deseas unirlos horizontalmente (añadir nuevas columnas), puedes utilizar `pd.merge`.

```python
# Unir DataFrames horizontalmente basado en una columna común 'fecha'
df_unido = pd.merge(df1, df2, on='fecha')
```

También puedes hacer una unión externa, interna, a la izquierda o a la derecha dependiendo de tus necesidades.

```python
# Unión externa
df_unido = pd.merge(df1, df2, on='fecha', how='outer')

# Unión interna
df_unido = pd.merge(df1, df2, on='fecha', how='inner')

# Unión a la izquierda
df_unido = pd.merge(df1, df2, on='fecha', how='left')

# Unión a la derecha
df_unido = pd.merge(df1, df2, on='fecha', how='right')
```

### Guardar el DataFrame Unido

Una vez que tienes tu DataFrame unido, podrías querer guardarlo en un nuevo archivo para futuros análisis.

```python
# Guardar el DataFrame unido como un nuevo archivo JSON
df_unido.to_json("archivo_climatico_unido.json")
```

Espero que esto te sea de ayuda para unir tus archivos de datos climáticos en un solo DataFrame utilizando Pandas.