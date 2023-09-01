---
title: "Proyecto 2"

weight: 120
#isFolder: true

---

## Visualizador de canales de TDT a partir de un archivo JSON

En este repositorio https://github.com/LaQuay/TDTChannels tienes información sobre canales de TDT de España en formato JSON.

Usa el archivo https://www.tdtchannels.com/lists/tv.json para crear un visualizador de los canales de TDT.

Si lo quieres ver en el navegador, necesitarás una extensión para ver archivos `m3u`.


<a target="_blank" href="https://colab.research.google.com/github/lmorillas/curso-python-iot/blob/main/notebooks/proyecto2.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>


### Variante: uso de streamlit

> no podrás ejecutarlo en colab, sino en tu equipo. Para ejecutarlo en colab, tendrías que usar alguna herramienta como [ngrok](https://lmorillas.github.io/intro-django/docs/extra/ngrok/).

> Aquí tienes un ejemplo de aplicación que usa [streamlit](https://streamlit.io/) https://github.com/lmorillas/streamlit-tdt/
>
> Para ejecutar en tu equipo, tienes que
* clonar el repositorio
```bash
$ git clone c

* crear entorno virtual
```bash
$ cd streamlit-tdt
$ python3 -m venv env
$ source env/bin/activate
```

* instalar dependencias
```bash
$ pip install -r requirements.txt
```

* ejecutar la aplicación
```bash
$ streamlit run tdt.py
```

#### Modifica el programa
* Que muestre los canales
* Que permita otras búsquedas directas.

#### Ejercicios propuestos
* Añade una caja de búsqueda para filtrar los canales por nombre.

```python
text_search = st.text_input("Buscar canal de TV", value="")

```