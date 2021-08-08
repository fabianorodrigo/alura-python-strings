import re


class ExtratorCEP:
    def __init__(self, endereco: str):
        self.endereco = endereco

    def get_cep(self):
        expressaoRegular = re.compile("[0-9]{5}-?[0-9]{3}")
        resultado = expressaoRegular.search(
            self.endereco)  # retorna Match se achar
        if resultado:
            cep = resultado.group()
            return cep
        return None
