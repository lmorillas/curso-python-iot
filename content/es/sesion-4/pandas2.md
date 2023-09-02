---
title: "Pandas"
linkTitle: "Pandas"

#isFolder: true

weight: 20
description: >
    Profundizando en el trabajo con Pandas 

data: >
  https://mljar.com/blog/jupyter-notebook-widgets/
  https://www.kaggle.com/datasets/jolenech/netflixdata-viewingactivity
  https://www.kaggle.com/datasets/enviouscodefellow/viewingactivity
  https://www.kaggle.com/datasets/jolenech/netflixdata-viewingactivity
  https://infografia-netflix.streamlit.app/
  https://github.com/mkfnx/netflix-activity-infographic
  https://bjolko.github.io/netflix-analysis/
  https://dev.to/shittu_olumide_/build-your-first-data-science-project-from-your-netflix-data-4gi0
  https://himanshi-png.github.io/Netflix-Data-Analysis/
  https://bjolko.github.io/netflix-analysis/  **

  https://www.learndatasci.com/tutorials/python-pandas-tutorial-complete-introduction-for-beginners/


  ** https://www.kaggle.com/code/edwardtoledolpez/beer-stadistics


  https://bjolko.github.io/netflix-analysis/

  click  https://click.palletsprojects.com/
  fabric https://www.fabfile.org/
  

---




# Uso de Pivot Tables con Pandas en Python

## Introducción Teórica

Las tablas dinámicas (o `pivot_tables`) son una de las técnicas más útiles en el análisis de datos. Sirven para resumir, analizar, explorar y presentar los datos de origen en un formato fácil de entender. Pandas ofrece una función llamada `pivot_table` que es extremadamente versátil y potente para realizar este tipo de operaciones.

### ¿Para qué sirven las tablas dinámicas?

1. **Resumir Datos**: Pueden resumir un conjunto de datos grande y complicado en un formato más simple.
2. **Analizar y Explorar**: Ayudan a explorar las relaciones entre variables y pueden ayudarte a responder preguntas específicas sobre tus datos.
3. **Presentación de Datos**: Facilitan la representación gráfica de los datos resumidos.

### Sintaxis Básica

La sintaxis básica de `pivot_table` en Pandas es la siguiente:

```python
pandas.pivot_table(data, values=None, index=None, columns=None, aggfunc='mean', ...)
```

- `data`: DataFrame que contiene los datos.
- `values`: Columna o columnas para agregar.
- `index`: Columna, o lista de columnas, para usar como índices de la tabla dinámica.
- `columns`: Columna o columnas para pivotar en nuevas columnas.
- `aggfunc`: Función para aplicar a `values` si hay más de una entrada (por defecto es 'mean').

## Ejemplo Interesante: Ventas por Departamento y Mes

Supongamos que tenemos un DataFrame que representa las ventas de una tienda con varias columnas: `Fecha`, `Departamento`, y `Ventas`:

```python
import pandas as pd
import numpy as np

# Crear un DataFrame de ejemplo
df = pd.DataFrame({
    'Fecha': pd.date_range(start='2022-01-01', periods=20, freq='7D'),
    'Departamento': np.random.choice(['Electrónica', 'Ropa', 'Alimentos'], 20),
    'Ventas': np.random.randint(100, 2000, 20)
})

# Crear una nueva columna 'Mes' basada en la columna 'Fecha'
df['Mes'] = df['Fecha'].dt.month_name()

print(df)
```

Podemos crear una tabla dinámica para resumir las ventas por `Departamento` y `Mes`:

```python
# Crear una tabla dinámica
pivot_table = pd.pivot_table(df, values='Ventas', index='Mes', columns='Departamento', aggfunc=np.sum)

print(pivot_table)
```

Esta tabla dinámica nos dará una idea clara de cómo las ventas varían entre diferentes departamentos a lo largo de los meses.

## Ejercicio Propuesto

1. Supongamos que además del DataFrame anterior, tenemos una columna adicional que representa el `Vendedor` para cada venta.
2. Utiliza `pivot_table` para crear una tabla dinámica que muestre las ventas totales por `Departamento` y `Vendedor`.
3. Guarda esta tabla dinámica en un nuevo archivo CSV.

Este ejercicio permitirá a los estudiantes practicar la creación de tablas dinámicas más complejas que involucren múltiples variables.


# Generar Gráficos con Plotly Usando Pivot Tables en Pandas

## Introducción

Plotly es una biblioteca de gráficos que facilita la creación de visualizaciones interactivas. A menudo, las tablas dinámicas creadas con Pandas pueden ser un excelente punto de partida para generar gráficos de alta calidad con Plotly.

## Ejemplo: Ventas por Departamento y Mes

Supongamos que tenemos el mismo DataFrame que en el ejemplo anterior y hemos creado una tabla dinámica para resumir las ventas por `Departamento` y `Mes`.

Primero, instalamos e importamos las bibliotecas necesarias:

```bash
pip install pandas plotly
```

Luego, generamos un DataFrame y una tabla dinámica con Pandas:

```python
import pandas as pd
import numpy as np

# Crear un DataFrame de ejemplo
df = pd.DataFrame({
    'Fecha': pd.date_range(start='2022-01-01', periods=20, freq='7D'),
    'Departamento': np.random.choice(['Electrónica', 'Ropa', 'Alimentos'], 20),
    'Ventas': np.random.randint(100, 2000, 20)
})

# Crear una nueva columna 'Mes' basada en la columna 'Fecha'
df['Mes'] = df['Fecha'].dt.month_name()

# Crear una tabla dinámica
pivot_table = pd.pivot_table(df, values='Ventas', index='Mes', columns='Departamento', aggfunc=np.sum, fill_value=0)

print(pivot_table)
```

Ahora, vamos a utilizar Plotly para generar un gráfico de barras basado en esta tabla dinámica:

```python
import plotly.express as px

# Generar el gráfico de barras
fig = px.bar(pivot_table.reset_index(), x='Mes', y=pivot_table.columns,
             title="Ventas Mensuales por Departamento")

# Mostrar el gráfico
fig.show()
```

Este gráfico mostrará las ventas totales de cada departamento para cada mes, en forma de barras apiladas o agrupadas, dependiendo de cómo configuremos Plotly.

## Tareas Propuestas para los Alumnos

1. Modifica el código anterior para crear un gráfico de línea en lugar de un gráfico de barras.
2. Utiliza una tabla dinámica diferente como base para un nuevo gráfico. Podría ser ventas por vendedor y día de la semana, por ejemplo.

Esta actividad permitirá a los estudiantes explorar la poderosa combinación de Pandas para el análisis de datos y Plotly para la visualización.