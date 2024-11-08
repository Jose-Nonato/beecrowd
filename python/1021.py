# Notas e moedas
'''
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número 
de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis 
são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.
'''

valor = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.5, 0.25, 0.1, 0.05, 0.01]

print('NOTAS:')
for nota in notas:
    qt_notas = int(valor / nota)
    print(f'{qt_notas} nota(s) de R$ {nota:.2f}')
    valor -= qt_notas * nota

print('MOEDAS:')
for moeda in moedas:
    valor = round(valor, 2)
    qt_moedas = int(valor / moeda)
    print(f'{qt_moedas} moeda(s) de R$ {moeda:.2f}')
    valor -= qt_moedas * moeda
