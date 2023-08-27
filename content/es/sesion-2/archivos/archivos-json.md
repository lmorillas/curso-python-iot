---
title: "Archivos JSON"
linkTitle: "JSON"
weight: 20
#isFolder: true

---


{{% pageinfo color="primary" %}}
## Documentación
* https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

## Notebook Base
* <a target="_blank" href="https://colab.research.google.com/github/lmorillas/curso-python-iot/blob/sesiones/notebooks/archivos-json.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

* <a target="_blank" href="https://colab.research.google.com/github/lmorillas/curso-python-iot/blob/sesiones/notebooks/archivos-json-ejercicio.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>


{{% /pageinfo %}}


## ¿Qué es JSON?

JSON (JavaScript Object Notation) es un formato de intercambio de datos ligero y de fácil lectura para humanos. Está basado en un subconjunto del lenguaje de programación JavaScript y es muy similar a los diccionarios en Python. Aunque fue originado en JavaScript, se ha convertido en un formato estándar para el intercambio de datos entre diferentes lenguajes y aplicaciones.

## ¿Por qué es importante JSON en Python?

1. **Interoperabilidad**: JSON es un formato ampliamente aceptado para el intercambio de datos en aplicaciones web.
2. **Facilidad de Uso**: La sintaxis de JSON es sencilla y fácil de leer/escribir.
3. **Estructura de Datos Anidados**: Permite anidar arrays y objetos, lo cual es especialmente útil para almacenar datos más complejos.

## Bibliotecas para manipular JSON en Python

La biblioteca estándar de Python incluye el módulo `json`, que permite codificar y decodificar datos en formato JSON.

- `json.dump() / json.dumps()`: Para escribir datos en JSON.
- `json.load() / json.loads()`: Para leer datos en JSON.



## Ejercicios Propuestos

### Ejercicio 1: Leer y modificar datos JSON

1. Leer un archivo JSON que contiene una lista de productos. Cada producto debe tener un `nombre`, `precio` y `cantidad_en_stock`.
2. Incrementar el `precio` de cada producto en un 10%.
3. Guardar los datos modificados en un nuevo archivo JSON.

### Ejercicio 2: Análisis de Datos JSON

1. Leer un archivo JSON que contiene datos sobre diversas ciudades, incluyendo el `nombre`, `población`, y `altitud`.
2. Encontrar y mostrar la ciudad con la mayor y la menor población.
3. Guardar esta información en un nuevo archivo JSON titulado `analisis_ciudades.json`.

Estos elementos deberían proporcionar una base sólida para enseñar la manipulación de archivos JSON en Python. Puedes adaptar los ejemplos y ejercicios según las necesidades de tus alumnos.