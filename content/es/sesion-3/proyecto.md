---
title: "Proyecto 3"

weight: 120
#isFolder: true

---

## Visualización de canales de TDT con Streamlit

Modifica el proyecto 2 para que use pandas para la gestión de los datos.


## Filtrar y organizar datos climáticos

* Descarga los datos de Zaragoza de este verano (julio y agosto) de la web de AEMET: https://opendata.aemet.es/centrodedescargas/productosAEMET? Necesitarás generarte una API Key. Los datos los tienes también aquí: [julio](https://raw.githubusercontent.com/lmorillas/curso-python-iot/main/notebooks/zaragoza-air-julio.json) [agosto](https://raw.githubusercontent.com/lmorillas/curso-python-iot/main/notebooks/zaragoza-air-agosto.json) [metadatos](https://raw.githubusercontent.com/lmorillas/curso-python-iot/main/notebooks/metadatos-clima.json)

> Ten cuidado con el encoding de los archivos. 
```python

url_metadatos = "https://raw.githubusercontent.com/lmorillas/curso-python-iot/main/notebooks/metadatos-clima.json"

r = requests.get(url_metadatos)

r.encoding = 'ISO-8859-1'  # los datos no están en utf-8
```

Puedes usar `encoding='latin-1'` en `pd.read_csv()` para evitar problemas.

### Tareas
* Analiza los metadatos.
* Crea un DataFrame con los datos de julio y otro con los de agosto.
* Explora los datos
* Crea un DataFrame con los datos de julio y agosto (concaténalos). En este caso usaremos una unión vertical (por filas)

```python
import pandas as pd

# Leer archivos JSON en DataFrames
df1 = pd.read_json("archivo_climatico1.json")
df2 = pd.read_json("archivo_climatico2.json")

df_unido = pd.concat([df1, df2])
```

* Guarda todos los datos unidos en un nuevo archivo JSON.

* Crea una gráfica con los datos de temperatura máxima y mínima de julio y agosto.


## Aplicación con los centros educativos de Aragón

Revisa el listado de centros educativos del portal del Gobierno de Aragón: https://educa.aragon.es/buscador-de-centros Tienes un json en [centros.json](https://github.com/lmorillas/curso-python-iot/blob/main/notebooks/centros.json)

> Crea una aplicación con Streamlit que permita filtrar los centros por provincia y localidad, tipo de centro, tipo de enseñanza, etc y que muestre los resultados en una tabla o en un mapa.
