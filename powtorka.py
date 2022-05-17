import requests
import sys, os

def pobierz_strone_www_jako_text(url):

    surowe_info = requests.get(url)
    text = surowe_info.text
    return text

def stworz_liste_flag(url):

    text_strony_www = pobierz_strone_www_jako_text(url)

    lista_linii = text_strony_www.split('</p>')


    linki = []
    for linia in lista_linii:
        link = linia.replace('<p>', '')
        link = link.replace('- ', '') 
        link = link.strip()
        linki.append(link)
       

    return linki


if __name__=='__main__':
    argument = sys.argv[1]
    lista_flag = stworz_liste_flag(argument)
    print(lista_flag)
    

    
    








