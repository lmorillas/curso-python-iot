---
title: "Streamlit"
date: 2021-10-21T10:29:17+02:00
linkTitle: "Streamlit"
weight: 30
description: >
    Introducción a la creación de apps y cuadros de mando con Streamlit
notas: > 
    * https://blog.jcharistech.com/2019/10/20/streamlit-python-tutorial-crash-course/
    * https://seraph13.medium.com/tutorial-introductorio-de-streamlit-be78f225b434

---
{{% pageinfo %}}
* https://streamlit.io/
* https://docs.streamlit.io/library/get-started/create-an-app
* Tutorial de ejemplo: https://docs.streamlit.io/library/get-started/create-an-app
{{% /pageinfo %}}

## ¿Qué es Streamlit?
Es un framework para crear aplicaciones web de datos con Python.

## Ventajas
* Visualización en tiempo real
* Paneles interactivos
* Facilidad de uso
* Integración con el conjunto de herramientas de ciencia de datos de Python: Pandas, NumPy, Plotly

## Instalar
> mejor en un entorno virtual
```bash
pip install streamlit
```
## Demo
```bash
streamlit hello
```

## Ejecutar
```bash
 streamlit run your_script.py [-- script args]
```
También se puede ejecutar una aplicación remota
```bash
$ streamlit run https://raw.githubusercontent.com/streamlit/demo-uber-nyc-pickups/master/streamlit_app.py
```

## Primeros recursos
### Texto
```python
import streamlit as st

# Text/Title
st.title("Streamlit Tutorial")

# Header/Subheader
st.header("Encabezado de la app")
st.subheader("Segundo nivel de encabezado")

# Text
st.text("Texto normal de la app")

# Markdown
st.markdown("### Texto en markdown")
```

### Texto en colores y errores
```python
st.success("Successful")

st.info("Information!")

st.warning("This is a warning")

st.error("This is an error Danger")

st.exception("NameError('name three not defined')")
```
## Widgets
```python
# Checkbox
if st.checkbox("Show/Hide"):
	st.text("Showing or Hiding Widget")

# Radio Buttons
status = st.radio("What is your status",("Active","Inactive"))

if status == 'Active':
	st.success("You are Active")
else:
	st.warning("Inactive, Activate")

# SelectBox
occupation = st.selectbox("Your Occupation",["Programmer","DataScientist","Doctor","Businessman"])
st.write("You selected this option ",occupation)


# MultiSelect
location = st.multiselect("Where do you work?",("London","New York","Accra","Kiev","Nepal"))
st.write("You selected",len(location),"locations")

# Slider
level = st.slider("What is your level",1,5)

# Buttons
st.button("Simple Button")

if st.button("About"):
	st.text("Streamlit is Cool")
```

## Input del usuario
```python
# Receiving User Text Input
firstname = st.text_input("Enter Your Firstname","Type Here..")
if st.button("Submit"):
	result = firstname.title()
	st.success(result)


# Text Area
message = st.text_area("Enter Your message","Type Here..")
if st.button("Submit"):
	result = message.title()
	st.success(result)

```
## Sidebar
```python
with st.sidebar:
    st.title("Título de la barra lateral")

    st.markdown(":+1: Introducción a la biblioteca `streamlit`. :sunglasses:")

    tech = st.selectbox(
        "Selecciona un color",
		["red", "orange", "yellow", "green", "blue", "indigo", "violet"],
    )

    start, end = st.slider(
        "Curso", 1990, 2023, (1990, 2023), step=1, help="Selecciona el año de inicio y fin del curso"
    )
```
## Configuración 
En el archivo `~/.streamlit/config.toml` se puede configurar el puerto, el ancho de la página, etc.
https://docs.streamlit.io/library/advanced-features/configuration

### Tema

https://docs.streamlit.io/library/advanced-features/theming

## Más
* https://blog.jcharistech.com/2019/10/20/streamlit-python-tutorial-crash-course/

## Primer ejemplo

https://github.com/lmorillas/streamlit-tdt/blob/main/tdt.py

* requisitos: instalar `streamlit` y `requests`
