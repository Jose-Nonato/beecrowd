# Fórmula de Bhaskara
'''
Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara.
Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, 
caso haja uma divisão por 0 ou raiz de numero negativo.
'''

a, b, c = list(map(float, input().split()))

delta = ((b**2)-4*a*c)

if( (delta < 0) or a == 0):
	print( "Impossivel calcular")
	
elif ( delta == 0 ):
	r1 = (-b + delta **(1/2))/(2*a)
	r2 = r1
	print("R1 = %.5f" %(r1))
	print("R2 = %.5f" %(r2))

else:
	r1 = (-b + delta **(1/2))/(2*a)
	r2 = (-b - delta **(1/2))/(2*a)
	print("R1 = %.5f" %(r1))
	print("R2 = %.5f" %(r2))