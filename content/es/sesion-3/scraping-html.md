---
title: "Scraping HTML"
linkTitle: "HTML"
weight: 10
#isFolder: true
description: >
    Extracción de datos de páginas web

notas: >
  https://awsacademy.instructure.com/courses/55981/modules/items/4907052
  https://github.com/sdelquin/aprendepython
  https://www.scrapingbee.com/blog/python-web-scraping-beautiful-soup/

---


{{% pageinfo color="primary" %}}
## Documentación
* Requests: https://docs.python-requests.org/en/master/  &  https://requests-html.kennethreitz.org/
* Beautiful Soup: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
* LXML: https://lxml.de/
* Selenium: https://selenium-python.readthedocs.io/

## Algunos tutoriales
* https://www.learndatasci.com/tutorials/ultimate-guide-web-scraping-w-python-requests-and-beautifulsoup/
* https://aprendepython.es/pypi/scraping/
* https://realpython.com/beautiful-soup-web-scraper-python/


## Notebook Base
* <a target="_blank" href="https://colab.research.google.com/github/lmorillas/curso-python-iot/blob/main/notebooks/scraping_html.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

{{% /pageinfo %}}

## Motivación

Hay veces que la información no está disponible para descargar en un formato estructurado, como CSV o JSON. En estos casos, es necesario extraer la información de la página web y convertirla a un formato estructurado.

> Nota: Es importante revisar la política de uso de la página web para asegurarnos de que no estamos infringiendo ninguna norma.

## Acceso a los datos

Accedemos a los datos por selectores de `CSS` o expresiones `XPath`.

Para `CSS` aquí tienes un buen resumen de selectores https://gist.github.com/magicznyleszek/809a69dd05e1d5f12d01

Para `XPath` aquí tienes un buen resumen de selectores https://devhints.io/xpath

## requests-html
`requests-html` permite acceder a página generadas con JavaScript (SPA por ejemplo). Pero la gestión de los procesos choca con `Jupyter`.

Echa un vistazo a este ejemplo: https://github.com/lmorillas/curso-python-iot/blob/main/src/scraping-spa.py

> Descárgalo y ejecútalo en tu ordenador.

## TAREA

Genera un archivo `json` con los datos de los libros de alguna de las librerías siguientes:
* http://books.toscrape.com
* https://react-amazon-bestsellers-books-dy.netlify.app/

El primer caso es un scraping normal (html estático). El segundo es un scraping de una SPA (Single Page Application).

Un ejemplo del archivo `json` generado puede ser el siguiente:
```json
[
  {"titulo": "A Light in the Attic",
  "autor": "by Suzanne Collins",
  "precio": "51.77",
  "stock": "true",
  "categoria": "Poetry",
  "imagen": "http://books.toscrape.com/media/cache/fe/72/fe72f0532301ec28892ae79a629a293c.jpg"
  },
  ...
]
```
Si algún dato no está disponible o no se puede extraer, puedes poner `null`.