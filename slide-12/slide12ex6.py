#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Função para mostrar a minha matriz resultante
def show_matrix(matrix, dimension):
	for i in range(dimension[0]):
		print(" ".join([str(i) for i in matrix[i]]))

# Função que cria uma matriz transposta apenas com zeros
# Pela definição: Mnxm -> MTmxn ------ MT = Matriz transposta
def create_matrix_zeros(dimension):
	matrix = []
	for i in range(dimension[1]):
		line = []
		for j in range(dimension[0]):
			line.append(0)
		matrix.append(line)

	return matrix

# Função que faz a copia dos valores de uma matriz para a sua matriz transposta
# Pela definição: a(i,j) = a'(j,i) ---- onde a' é um elemento da minha matriz transposta
def transposed(matrix, dimension):
	tranposed_matrix = create_matrix_zeros(dimension)
	# Usando a definição para determinar o tamanho da nova matriz
	new_dimension = (dimension[1], dimension[0])
	
	for i in range(dimension[0]):
		for j in range(dimension[1]):
			tranposed_matrix[j][i] = matrix[i][j]

	show_matrix(tranposed_matrix, new_dimension)


# Pega as dimensoes da minha matriz
entry = [int(i) for i in input().split()]
matrix = []

# Para cada linha eu lei os valores das minhas colunas
for i in range(entry[0]):
	line = [ int(x) for x in input().split() ]
	matrix.append(line)

transposed(matrix, entry)