import re


class ExtratorURL:
    def __init__(self, url: str):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url: str):
        return url.strip()

    def valida_url(self) -> bool:
        # tanto None quanto String vazia retorna False
        if not self.url:
            raise ValueError("URL vazia")

        expressao_regular = re.compile(
            '(http(s)?://)?(wwww.)?[A-z]+.com(.br)?(.*)')
        match = expressao_regular.match(self.url)
        if not match:
            raise ValueError("URL não é válida")
        return True

    def get_url_base(self) -> str:
        i = self.url.find("?")
        return self.url[:i]

    def get_url_parametros(self) -> str:
        i = self.url.find("?")
        return self.url[i+1:]

    def get_valor_parametro(self, nome_parametro: str) -> str:
        i = self.get_url_parametros().find(nome_parametro)
        iValor = i + len(nome_parametro)
        iEcomercial = self.get_url_parametros().find('&', iValor)
        if iEcomercial == -1:
            valor = self.get_url_parametros[iValor]
        else:
            valor = self.get_url_parametros()[iValor:iEcomercial]
        return valor

    def __str__(self) -> str:
        return self.url

    def __eq__(self, other):
        return self.url == other.url
