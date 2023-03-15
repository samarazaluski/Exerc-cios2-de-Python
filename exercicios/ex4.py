Gd_macas = int(input("Digite a quantidade de maças:"))

if (Gd_macas < 12):
    valor_pagar = Gd_macas * 1.30

else:

    valor_pagar = Gd_macas * 1.00

    print(f"voce comprou {Gd_macas} por {valor_pagar:.2f}")