import math
import matplotlib.pyplot as plt
import numpy as np

def _main_():

	while(1):
		raiz1 = []
		raiz2 = []
		vertices = []
		interc_y = []

		print('Esse código tem a capacidade de resolver calculos de Báskara\n')
		a = int(input('Insira o valor de "A": '))
		b = int(input('Insira o valor de "B": '))
		c = int(input('Insira o valor de "C": '))

		if a == 0:
			print('Não é uma função do segundo grau')
			_main_()
		elif a > 0:
			valueA = 'função tem concavidade voltada para cima'
		elif a < 0:
			valueA = 'função tem concavidade voltada para baixo'

		delta = b**2 - 4*a*c

		if delta < 0:
			raiz3 = ('Não existe raiz no conjunto dos reais')

		elif delta == 0:
			raiz1.append(- b/(2*a))
			raiz1.append(0)
		
		elif delta > 0:
			bask1 = (-b + math.sqrt(delta))/(2 * a)
			raiz1.append(bask1)
			raiz1.append(0)

			bask2 = (-b -math.sqrt(delta))/(2 * a)
			raiz2.append(bask2)
			raiz2.append(0)


		xv = -b/(2*a)
		yv = -delta/(4*a)

		vertices.append(xv)
		vertices.append(yv)

		interc_y.append(0)
		interc_y.append(c)

		print(valueA)
		if delta > 0:
			print('A primeira raiz vale: ' + str(raiz1))
			print('A segunda raiz vale: ' + str(raiz2))
		if delta < 0:
			print(raiz3)
		else:
			print('A raiz vale: ' + str(raiz1))

		print('A vertice de x é: ' + str(xv))
		print('A vertice de y é: ' + str(yv))
		print('O intercepto em y é: ' + str(interc_y))



		while(1):
			shazam = input('Deseja continuar? (S/n):')
			if(shazam == 'S' or shazam == 's' or shazam == ''):
				break
			if(shazam =='N' or shazam == 'n'):
				exit()
			else:
				print('número não válido')


_main_()