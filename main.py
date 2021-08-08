from ExtratorCEP import ExtratorCEP
from ExtratorURL import ExtratorURL


url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"


extrator = ExtratorURL(url)

# fatiamento
url_base = extrator.get_url_base()[0:21]
# find e fatiamento
indice_interrogacao = url.find('?')
url_parametros = url[indice_interrogacao+1:]  # o índice final é opcional

print(url_base)
print(url_parametros)

extratorCEP = ExtratorCEP("Rua SaoSalva, 77 - apto 777 - 22231-130 - Flamengo")
print(extratorCEP.get_cep())
print("THE END")
