alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def cifra_vigenere(mensagem, chave):
    tamanho_chave = len(chave)
    mensagem_cifrada = ''
    indice_chave = 0
    for letra_mensagem in mensagem:
        if letra_mensagem.isalpha():
            letra_mensagem = letra_mensagem.upper()
            letra_chave = chave[indice_chave % tamanho_chave].upper()
            deslocamento = obter_deslocamento(letra_chave, alfabeto)
            letra_cifrada = cifrar_letra(letra_mensagem, deslocamento, alfabeto)
            mensagem_cifrada += letra_cifrada
            indice_chave += 1
        else:
            mensagem_cifrada += letra_mensagem
    return mensagem_cifrada

def decifra_vigenere(mensagem_cifrada, chave):
    tamanho_chave = len(chave)
    mensagem_decifrada = ''
    for i, letra_cifrada in enumerate(mensagem_cifrada):
        if letra_cifrada.isalpha():
            letra_cifrada = letra_cifrada.upper()
            indice_chave = i % tamanho_chave
            letra_chave = chave[indice_chave].upper()
            deslocamento = obter_deslocamento(letra_chave, alfabeto)
            letra_decifrada = decifrar_letra(letra_cifrada, deslocamento, alfabeto)
            mensagem_decifrada += letra_decifrada
        else:
            mensagem_decifrada += letra_cifrada
    return mensagem_decifrada

def obter_deslocamento(letra_chave, alfabeto):
    deslocamento = alfabeto.index(letra_chave)
    if letra_chave.islower():
        deslocamento = deslocamento + 26
    return deslocamento


def cifrar_letra(letra_mensagem, deslocamento, alfabeto):
    indice_letra = alfabeto.index(letra_mensagem.upper())
    letra_cifrada = alfabeto[(indice_letra + deslocamento) % 26]
    if letra_mensagem.islower():
        letra_cifrada = letra_cifrada.lower()
    return letra_cifrada

def decifrar_letra(letra_cifrada, deslocamento, alfabeto):
    indice_letra = alfabeto.index(letra_cifrada.upper())
    indice_letra_decifrada = (indice_letra - deslocamento) % 26
    letra_decifrada = alfabeto[indice_letra_decifrada]
    if letra_cifrada.islower():
        letra_decifrada = letra_decifrada.lower()
    return letra_decifrada


print("decifrando texto =",decifra_vigenere("LBMCOCJMSSDCX", "LIMAOLIMAOLIM"))
