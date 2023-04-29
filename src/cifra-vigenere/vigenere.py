from tools.cifra_tools import Tools

class Cifra(Tools):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    CRIPTOGRAFAR = False
    texto_processado = ""
    alfabeto_deslocado = ""

    def __init__(self, texto, senha):
        self.senha = senha
        self.texto = self.replace_texto(texto)
        self.processar_texto()

    def __str__(self):
        return self.texto_processado

    def processar_texto(self):
        senha = self.processar_senha()

        for indice, caracter in enumerate(self.texto):
            caracter_indice = self.alfabeto.find(senha[indice])
            self.alfabeto_deslocado = self.deslocar_alfabeto(
                self.alfabeto, caracter_indice
            )
            self.adaptador(caracter)

    def adaptador(self, caracter):
        if self.CRIPTOGRAFAR:
            self.criptografar(caracter)

    def criptografar(self, caracter):
        indice_p = self.alfabeto.find(caracter)
        self.texto_processado = (
            self.texto_processado + self.alfabeto_deslocado[indice_p]
        )
        
class Cifrador(Cifra):
    def __init__(self, texto, senha):
        self.CRIPTOGRAFAR = True
        super().__init__(senha, texto)


# teste de entradas    
texto = input("insira o texto: ")
senha = input("insira a senha: ")

cifra = Cifrador(texto, senha)
print(f"texto: {cifra}")