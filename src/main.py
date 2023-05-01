from cypher.vigenere import Cifrador, Decifrador

if __name__ == "__main__":
  option = 0
  while option != 4:
    print("MENU")
    print("="*12)
    print("1-Cifrar mensagem")
    print("2-Decifrar mensagem")
    print("3-Encerrar programa")
    
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
        break
    else:
      print("Opção não cadastrada! Tente novamente.")
