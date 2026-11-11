def main():
    valor_inicial = float(input("Qual o valor inicial do odômetro em quilômetros? "))
    valor_final = float(input("Qual o valor final do odômetro em quilômetros? "))
    combustivel_consumido = float(input("Qual a quantidade de combustível consumida em litros? "))

    kml = quilometros_por_litro(valor_inicial, valor_final, combustivel_consumido)
    mpg = milhas_por_galao(valor_inicial, valor_final, combustivel_consumido)

    print(f"{kml:.2f} quilometros por litro")
    print(f"{mpg:.2f} milhas por galao")

    pass

def quilometros_por_litro(valor_inicial, valor_final, combustivel_consumido):
    consumo_litro = (valor_final - valor_inicial) / combustivel_consumido

    return consumo_litro

def milhas_por_galao(valor_inicial, valor_final, combustivel_consumido):
    galoes = combustivel_consumido * 0.26417
    milhas = (valor_final - valor_inicial) / 1.609
    consulmo_mpg = milhas / galoes

    return consulmo_mpg


main()