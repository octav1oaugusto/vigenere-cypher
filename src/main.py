from cypher.vigenere import Cifrador, Decifrador
from cypher.attack import AtaqueAnaliseFrequenciaENG, AtaqueAnaliseFrequenciaPT

if __name__ == "__main__":
  option = 0
  separator = "=" * 20
  space = ""
  while option != 4:
    print(space)
    print(separator)
    print("MENU")
    print(separator)
    print("1-Cifrar mensagem")
    print("2-Decifrar mensagem")
    print("3-Atacar a cifra")
    print("4-Encerrar programa")
    print(separator)
    print(space)    
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
          key = AtaqueAnaliseFrequenciaPT(string_ofc).get_keys()[-1]
          print(space)
          print(separator)
          print(f"Chave encontrada: {key}")
          print(separator)
          print(space)
          decipher = input("Você deseja decifrar a cifra com essa chave? (Sim/Não) ")[0].lower()  
          if decipher == "s":
            print(space)
            print(separator)
            print("Mensagem decifrada: ")
            print(separator)
            print(Decifrador(string_ofc, key))
            print(separator)
          elif decipher == "n":
            break
        if language == "i":
          string_ofc = input("enter a cipher: ")
          key = AtaqueAnaliseFrequenciaENG(string_ofc).get_keys()[-1]
          print(space)
          print(separator)
          print(f"Found key: {key}")
          print(separator)
          print(space)
          decipher = input("Do you want to decrypt the cipher with that key? (Yes/Not) ")[0].lower()
          if decipher == "y":
            print(space)
            print(separator)
            print("Decrypted message: ")
            print(separator)
            print(Decifrador(string_ofc, key))
            print(separator)
          elif decipher == "n":
            break
        if language == "m": 
          break
    elif option == "4":
        break
    else:
      print("Opção não cadastrada! Tente novamente.")
