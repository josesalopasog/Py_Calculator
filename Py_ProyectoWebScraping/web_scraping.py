import bs4
import requests

resultado = requests.get('https://escueladirecta.com/')

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

#print(sopa.select('title')[0].getText())

imagenes = sopa.select('.course-box-image')[0]['src']

#for i in imagenes:#
#    print(i)

imagen_curso_1 = requests.get(imagenes)

f = open('mi_imagen.jpg', 'wb')
f.write(imagen_curso_1.content)
f.close()