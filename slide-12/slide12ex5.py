#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Coding by: Marllon Rodrigues

# Função responsável por verificar a quantidade de vezes que um determinado
# numero aparece dentro da minha matriz, excluindo o indice ao qual não desejo verificar
def repetido(matriz, dimensao, n, indice):
	quantidade = 0

	for i in range(dimensao[0]):
		for j in range(dimensao[1]):
			# Verifica se o valor atual da minha matriz eh igual o valor
			# passado para a minha funcao
			if (matriz[i][j] == n) and ((i,j) != indice):
				quantidade += 1

	return quantidade

def mostrar_repetidos(numeros, quantidade):
	for i in range(len(numeros)):
		print("Numero: {} repetiu {} vezes".format(numeros[i],quantidade[i]))

def verifica_repetido(matriz, dimensao):

	numeros_repetidos = []
	quantidade_repetidos = []

	for i in range(dimensao[0]):
		for j in range(dimensao[1]):
			# Verifica se meu elemento ja esta na minha lista de numeros repetidos
			if matriz[i][j] not in numeros_repetidos:
				# Pega a quantidade de vezes que uma determinado numero se repetiu
				busca = repetido(matriz, dimensao, matriz[i][j], (i,j))

				if busca:
					numeros_repetidos.append(matriz[i][j])
					quantidade_repetidos.append(busca + 1)

	mostrar_repetidos(numeros_repetidos, quantidade_repetidos)

dimensao = input()
dimensao = [int(x) for x in dimensao.split()]

matriz = []

for i in range(dimensao[0]):
	linha = [int(x) for x in input().split()]
	matriz.append(linha)

verifica_repetido(matriz, dimensao)
