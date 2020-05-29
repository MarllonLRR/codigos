#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Coding by: Marllon Rodrigues

# ------------------------------------------------
# ----- Calculo do triangulo usando combinacao ---
# ------------------------------------------------

# Calcula o fatorial de um determinado numero
def fatorial(n):
	fatorial = 1

	if(n != 0):
		for i in range(1,n+1):
			fatorial *= i
	return fatorial 

# Faz o calculo de combinacao de um numero
def combinacao(n, p):
	#    n!
	# p!(n-p)!
	return int(fatorial(n)/(fatorial(p)*fatorial(n-p)))

def triangulo_com_combinacao(n):
	for i in range(n + 1):
		for j in range(i+1):
			print(combinacao(i, j), end=' ')
		print()

# ------------------------------------------------
# ----- Calculo do triangulo usando matriz -------
# ------------------------------------------------

# Funcao auxiliar para mostrar a matriz na tela
def mostra_triangulo(triangulo, n):

	for i in range(n):
		for j in triangulo[i]:
			print(j, end=' ')
		print() 

# Função que calcula o triangulo pelo metodo de matriz
def pascal(n):

	# O primeiro valor do meu triangulo sempre é 1
	triangulo = [[1]]

	for i in range(n):
		# O primeiro elemento da minha linha sempre é 1
		linha = [1]

		# Pego o tamanho do meu triangulo anterior ao qual eu quero calcular o meu valor atual
		size_triangulo = len(triangulo[i])
		for j in range(size_triangulo):
			next_value = 0
			# Verifico se o valor do meu triangulo de cima existe
			# caso exista eu pego ele
			if(size_triangulo-1 > j):
				next_value = triangulo[i][j+1]

			soma = triangulo[i][j] + next_value

			linha.append(soma)
		triangulo.append(linha)

	mostra_triangulo(triangulo, n)

# leio o meu N, ao qual é a quantidade de linha que eu quero mostrar
n = int(input())

#----------------------------


# calculo usando combinacao
triangulo_com_combinacao(n)

print("\n\n")

#----------------------------

# calculo usando matrizes

# Como as linhas do meu triangulo sempre começa em 0
# Acrescento 1 a minha entrada
pascal(n+1)
