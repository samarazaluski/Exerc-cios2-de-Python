Gd_Hora = float(input("Digite a quantidade de horas no estacionamento"))

valor_pagar = Gd_Hora * 5.00

if (Gd_Hora >= 7):
    print("valor a pagar: $RS 35.00")

else:
    print(f"valor a pagar: {valor_pagar:.2f}")