class Tools:
    def replace_texto(self, texto):
        texto = texto.replace(" ", "")
        texto = texto.replace(".", "")
        texto = texto.replace(",", "")
        texto = texto.replace("”", "")
        texto = texto.replace("“", "")
        texto = texto.replace("—", "")
        texto = texto.replace("-", "")
        texto = texto.replace("_", "")
        texto = texto.replace(":", "")
        texto = texto.replace(";", "")
        texto = texto.replace("?", "")
        texto = texto.replace("!", "")
        texto = texto.replace("/", "")
        texto = texto.replace("\\", "")
        texto = texto.replace("'", "")
        texto = texto.replace('"', "")
        texto = texto.replace("(", "")
        texto = texto.replace(")", "")
        texto = texto.replace("[", "")
        texto = texto.replace("]", "")
        texto = texto.replace("{", "")
        texto = texto.replace("}", "")
        texto = texto.replace("`", "")
        texto = texto.replace("'", "")
        texto = texto.replace("*", "")
        texto = texto.replace("&", "")
        texto = texto.replace("%", "")
        texto = texto.replace("$", "")
        texto = texto.replace("#", "")
        texto = texto.replace("@", "")
        texto = texto.replace("<", "")
        texto = texto.replace(">", "")
        texto = texto.replace("\n", "")
        texto = texto.replace("\t", "")
        texto = texto.replace("ç", "c")
        texto = ''.join([palavra for palavra in texto if not palavra.isdigit()])
        return texto.lower()
            
    def deslocar_alfabeto(self, alfabeto, deslocamento):
        return alfabeto[deslocamento:] + alfabeto[:deslocamento]
    
    def processar_senha(self):
        if len(self.senha) < len(self.texto):
            nova_senha = self.senha * int((len(self.texto) / len(self.senha)))
            if len(nova_senha):
                nova_senha = nova_senha + self.senha[: len(nova_senha)]
            return nova_senha.lower()
        return self.senha.lower()
        