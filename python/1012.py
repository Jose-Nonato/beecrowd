A, B, C = input().split()

A = float(A)
B = float(B)
C = float(C)

triangulo = A * C / 2
circulo = 3.14159 * C ** 2
trapezio = ((A + B) * C) / 2
quadrado = B ** 2
retangulo = A * B

print(f'TRINGULO: {triangulo:.3f}\nCIRCULO: {circulo:.3f}\nTRAPEZIO: {trapezio:.3f}\nQUADRADO: {quadrado:.3f}\nRETANGULO: {retangulo:.3f}')
