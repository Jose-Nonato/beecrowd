id1, quantidade1, valor1 = input().split()
id2, quantidade2, valor2 = input().split()

total = (int(quantidade1) * float(valor1)) + (int(quantidade2) * float(valor2))

print(f'VALOR A PAGAR: R$ {total:.2f}')