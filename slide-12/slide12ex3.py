#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Coding by: Marllon Rodrigues

# Funcao responsavel por fazer o calculo da soma de uma lista
def soma_lista(lista):
	soma = 0

	for i in range(len(lista)):
		soma += lista[i]

	return soma

def varifica_linha(matriz, dimensao, diagonal = False, valor_diagonal = 0):

	soma_de_linhas = []

	# Para cada linha da minha matriz
	for i in range(dimensao):
		# faz a soma da minha lista
		soma = soma_lista(matriz[i])
		soma_de_linhas.append(soma)

	# Pego o primeiro valor da minha lista
	valor = soma_de_linhas[0]
	# Faço a media de valores da minha lista de somas
	media = soma_lista(soma_de_linhas) / dimensao

	# Caso preciso fazer a comparacao com a diagonal
	if(diagonal):
		return valor == media == valor_diagonal

	return valor == media

def soma_coluna(matriz, dimensao):

	soma_de_colunas = []

	# Iterador que passa por fora da minha matriz
	# |a00| a01 a02
	# |a10| a11 a12 => [a00, a10, a20]
	# |a20| a21 a22
	# Fixo um iterador e ando com o outro iterador

	for i in range(dimensao):

		lista_aux = []
		# caminho sobre as colunas da minha matriz pegado 1 valor de cada linha
		for j in range(dimensao):
			lista_aux.append(matriz[j][i])

	
		soma = soma_lista(lista_aux)
		soma_de_colunas.append(soma)

	valor = soma_de_colunas[0]
	media = soma_lista(soma_de_colunas) / dimensao

	return valor == media

def verifica_diagonal_principal(matriz, dimensao):

	soma_de_diagonal = []

	# Pego os valores da matriz da diagonal principal
	# |a00| a01  a02
	#  a10 |a11| a12 => [a00, a11, a22]
	#  a20  a21 |a22|
	# M[i][i]
	for i in range(dimensao):
		soma_de_diagonal.append(matriz[i][i])

	soma = soma_lista(soma_de_diagonal)

	return varifica_linha(matriz, dimensao, diagonal=True, valor_diagonal=soma)

def verifica_diagonal_secundaria(matriz, dimensao):
	soma_de_diagonal = []

	# Pego os valores da matriz com idices iguais
	#  a00  a01 |a02|
	#  a10 |a11| a12 => [a02, a11, a20]
	# |a20| a21  a22
	# M[i][dimensao-i-1] -> i = indice da minha linha

	for i in range(dimensao):
		soma_de_diagonal.append(matriz[i][dimensao-i-1])

	soma = soma_lista(soma_de_diagonal)
	return varifica_linha(matriz, dimensao, diagonal=True, valor_diagonal=soma)

# Funcao que faz as comparações das propriedades da matriz
def verifica_quadrado(matriz, dimensao):
	flag = soma_coluna(matriz, dimensao) == verifica_diagonal_principal(matriz, dimensao)
	flag = flag == verifica_diagonal_secundaria(matriz, dimensao)

	return flag 

entrada = int(input())

matriz = []

# Faco a minha leitura da matriz
# Suponto de eu NUNCA vo passar uma matriz errada para meu programa
# Em casos reais deve se verificar se a quantidade de elementos bate com a dimensao
for i in range(entrada):
	linha = [ int(x) for x in input().split() ]
	matriz.append(linha)


if(verifica_quadrado(matriz, entrada)):
	print("Eh quadrado magico")
else:
	print("Nao eh quadrado magico")