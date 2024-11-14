import bs4
import requests

#Crear URL sin numero de pagina
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

#Lista de titulos con 4 o 5 estrallas

titulos_rating_alto = []

#Iterar paginas
for p in range(1,10):
    #Crear sopa para cada pagina
    url_pagina = url_base.format(p)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
    #Seleccionar libros 
    libros = sopa.select('.product_pod')
    #Iterar libros
    for l in libros: 
        #Verificar estrallas 
        if len(l.select('.star-rating.Four')) !=0 or len(l.select('.star-rating.Five')) !=0:
            #Guardar titulo en variable
            titulo_libro = l.select('a')[1]['title']
            #Agregar libro a la lista
            titulos_rating_alto.append(titulo_libro)
            
for t in titulos_rating_alto:
    print(t)