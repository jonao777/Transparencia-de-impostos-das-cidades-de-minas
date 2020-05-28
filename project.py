import requests
from bs4 import BeautifulSoup


import credenciais
# É nessesário voce criar seu arquivo credencias.py e passar o headers com o seu navegador
# headers = {'User-Agent': 'Mozilla/...

url_transparencia = "http://www.transparencia.mg.gov.br/transferencia-de-impostos-a-municipios"
DOMINIO = "http://www.transparencia.mg.gov.br"


def requisicao(url):
    try:
        resposta = requests.get(url, headers=credenciais.headers)
        return resposta.text
    except Exception as e:
        print("Erro de requisição")
        print(e)


def parsing(resposta_html):
    try:
        soup = BeautifulSoup(resposta_html, 'html.parser')
        return soup
    except Exception as e:
        print("Erro de parsing")
        print(e)


def encontrar_cidade(soup):
    try:
        class_pai = soup.find("div", class_="t3-wrapper")
        class_filha = class_pai.find_all('tbody')
        return class_filha
    except Exception as e:
        print("Erro no soup")
        print(e)


if __name__ == "__main__":
    resposta_requisicao = requisicao(url_transparencia)
    if resposta_requisicao:
        resposta_parcing = parsing(resposta_requisicao)
        if resposta_parcing:
            resposta_soup = encontrar_cidade(resposta_parcing)
            if resposta_soup:
                print(resposta_soup)

