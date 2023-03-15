valor_mercadoria = float(input("Digite o valor da mercadoria: "))
valor_usuario = float(input("Digite o valor que possui em mãos: "))
if (valor_mercadoria <= valor_usuario):
    print("O valor que possui em mãos é suficiente")
    else:
    print("O valor que tem em mãos não é suficiente")