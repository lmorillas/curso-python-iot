# Ejemplo de scraping de una SPA (Single Page Application)
# usando requests-html

# recuerda instalar requests-html
# pip install requests-html

import requests_html

session = requests_html.HTMLSession()

url = 'https://react-amazon-bestsellers-books-dy.netlify.app/'
r = session.get(url)

# comprobamos lo que ha tradido parser
print(r.html.html)

# render del js. La primera vez descarga chromium
r.html.render()

print(r.html.html)

# buscamos los títulos de los libros
titulos = [t.text for t in r.html.find('article.book h2')]
