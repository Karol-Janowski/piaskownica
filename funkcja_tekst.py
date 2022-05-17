import requests
import sys

def stworz_liste_flag():

    url = 'https://zajecia-programowania-xd.pl/flagi'
    surowe_info = requests.get(url)
    text = surowe_info.text

    lista_linii = text.split('</p>')


    linki = []
    for linia in lista_linii:
        link = linia.replace('<p>', '')
        link = link.replace('- ', '') 
        link = link.strip()

    if ' ' in link or '<' in link:
        
    linki.append(link)
    

    return linki


lista = stworz_liste_flag()   
print(lista)