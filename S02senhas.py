"""Adicionei uma verificação de segurança sobre dados pessoais
"""

MINUSCULAS=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
MAIUSCULAS=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITOS=["0","1","2","3","4","5","6","7","8","9"]
ESPECIAIS=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", """, """, ",", ".", "<", ">", "?", "/", "`", "~"]


def procurar_palavra(palavra, nome_do_arquivo, maiusculas_e_minusculas=False):
    if not maiusculas_e_minusculas:
        palavra = palavra.lower()

    with open(nome_do_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            palavra_arquivo = linha.strip()
            if not maiusculas_e_minusculas:
                palavra_arquivo = palavra_arquivo.lower()

            if palavra_arquivo == palavra:
                return True

    return False


def palavra_tem_caractere(palavra, lista_caracteres):
    for caractere in palavra:
        if caractere in lista_caracteres:
            return True
    return False


def calcular_complexidade(palavra):
    complexidade = 0

    if palavra_tem_caractere(palavra, MINUSCULAS):
        complexidade += 1
    if palavra_tem_caractere(palavra, MAIUSCULAS):
        complexidade += 1
    if palavra_tem_caractere(palavra, DIGITOS):
        complexidade += 1
    if palavra_tem_caractere(palavra, ESPECIAIS):
        complexidade += 1

    return complexidade


def contem_dados_pessoais(senha, nome_usuario):
    if not nome_usuario:
        return False

    senha_lower = senha.lower()
    partes_nome = nome_usuario.lower().split()

    for parte in partes_nome:
        if len(parte) >= 3 and parte in senha_lower:
            return True

    return False


def validar_senha(senha, comprimento_min=10, comprimento_forte=16, nome_usuario=""):
    if contem_dados_pessoais(senha, nome_usuario):
        print("A senha contém seu nome")
        return 0

    if procurar_palavra(senha, "dicionario.txt", maiusculas_e_minusculas=False):
        print("A senha está no dicionário")
        return 0

    if procurar_palavra(senha, "senhas_mais_comuns.txt", maiusculas_e_minusculas=True):
        print("A senha é comum não é segura.")
        return 0

    comprimento = len(senha)
    if comprimento < comprimento_min:
        print("A senha é muito curta")
        return 1

    if comprimento > comprimento_forte:
        print("A senha é longa")
        return 5

    complexidade = calcular_complexidade(senha)
    forca = 1 + complexidade
    return forca


def main():
    nome_usuario = input("Digite seu nome completo para iniciar: ")
    senha = ""

    while senha != "q" and senha != "Q":
        senha = input("Digite uma senha (ou 'q' para sair): ")

        if senha != "q" and senha != "Q":
            forca = validar_senha(senha, nome_usuario=nome_usuario)
            print(f"Força da senha: {forca}\n")


if __name__ == "__main__":
    main()