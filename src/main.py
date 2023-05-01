from cypher.vigenere import Cifrador, Decifrador
from cypher.attack import AtaqueAnaliseFrequenciaENG, AtaqueAnaliseFrequenciaPT

if __name__ == "__main__":
  option = 0
  while option != 4:
    print("MENU")
    print("="*12)
    print("1-Cifrar mensagem")
    print("2-Decifrar mensagem")
    print("3-Atacar a cifra")
    print("4-Encerrar programa")
    
    option= input("Escolha uma opção: ")
    if option == "1":
      string_ofc = input("Insira a mensagem decifrada: ")
      keyword = input("Insira a chave: ")
      print("Mensagem criptografada:", Cifrador(string_ofc, keyword).texto_processado)
    elif option == "2":
      string_ofc = input("Insira uma cifra: ")
      keyword = input("Insira a senha: ")
      print("Mensagem descriptografada:", Decifrador(string_ofc, keyword))
    elif option == "3":
      language = ""
      while language != "p" or language != "i":
        print("Opções: Português, Inglês ou Menu (voltar)")
        language = input("Escolha a linguagem: ")[0].lower()
        if language == "p":
          string_ofc = input("Insira uma cifra: ")
          for key in reversed(AtaqueAnaliseFrequenciaPT(string_ofc).get_keys()):
            print("")
            print("Found key: {!r}".format(key))
        if language == "i":
          string_ofc = input("enter a cipher: ")
          for key in reversed(AtaqueAnaliseFrequenciaENG(string_ofc).get_keys()):
            print("")
            print("Found key: {!r}".format(key))  
        if language == "m": 
          break
    elif option == "4":
        break
    else:
      print("Opção não cadastrada! Tente novamente.")
