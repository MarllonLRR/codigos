#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Coding by: Marllon Rodrigues

# Função que percorre a minha diagonal principal 
# e verifica se a minha linha e minha coluna contem apenas UM elemento 1
def check_premises(matrix, dimension):
	result = True

	# Percorro a minha minha diagonal principal da minha matriz para verifica se em cada
	# elemento contem APENAS um unico elemento '1'
	for i in range(dimension):
		if not (check(matrix, dimension, i)):
			result = False

	return result 

# Função que faz a verificação dado um indice se a coluna e a linha daquele elemento contém
# Apenas um unico elemento '1'
def check(matrix, dimension, index):

	count_col = 0
	count_row = 0

	for i in range(dimension):
		# Faços a soma dos valores absolutos das minhas linhas e colunas
		count_row += abs(matrix[index][i]) 
		count_col += abs(matrix[i][index])

	# Verifico se os meus contadores estão com os valores iguais a '1'
	return (count_col == count_row) and (count_col == 1)
		
# Leio a dimenção da minha matriz
entry = int(input())
matrix = []

# Faço a leitura dos valores da minha matriz
for i in range(entry):
	line = [ int(x) for x in input().split() ]
	matrix.append(line)

if(check_premises(matrix, entry)):
	print("É uma matriz de permutação")
else:
	print("Não é uma matriz de permutação")