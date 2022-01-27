import requests
from bs4 import BeautifulSoup
import urllib
import urllib.request
import os
from string import ascii_lowercase

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}

page = requests.get('https://www.delicor.com/sbgroup.php?idg=1', headers=headers)

url_base = 'https://www.delicor.com/'

soup = BeautifulSoup(page.content, 'html.parser')

cartillas = soup.find_all('section', class_='product spad') # 1 #busca las 23 categorias de tragos que tiene la web
#arriba tenemos una lista de 23 categorias de alcoholes

for cartilla in cartillas: # 1 de cada 23 #itera cada uno de los elementos de la lista cartillas

    items = cartilla.find_all('div', class_='featured__item') # 23 #busca la cartilla del producto dentro de cada una de las categorias

    for item in items:

        nombres_y_precios = item.find_all('div', class_='featured__item__text') #busca el nombre y el precio del prodcuto dentro de cada cartilla
        titulo = cartilla.h2 #titulo de la categoria de alcohol
        bebida = item.h6     #nombre de la bebida
        precio = item.h4     #precio de la bebida
        imagen = item.div.get('data-setbg')

        print(titulo.text + '|' + bebida.text + '|' + precio.text)
        
        nombre_archivo = f'{titulo.text} {bebida.text}'
        url_imagen = url_base + imagen
        imagefile = open(nombre_archivo.replace('/', '') + '.jpeg', 'wb')
        imagefile.write(urllib.request.urlopen(url_imagen)
            .read())
        imagefile.close()