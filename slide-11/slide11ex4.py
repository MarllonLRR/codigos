#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Coding by: Marllon Rodrigues

# Função que fara a minha lista que contém a diferença dos valores
# consecutivos da minha lista
def calc_diff(entry):
	diff = []
	for i in range(1,len(entry)):
		# A funcao 'abs' retorna um valor positivo caso o numero seja negativo
		diff.append(abs(entry[i-1] - entry[i]))

	# Ordeno a minha lista criada
	diff.sort()

	return diff

# Função que verificara se a minha sequencia contem numeros de 1 até n-1
def check_sequence(entry):
	result = True
	for i in range(1, len(entry)):

		# Faço a diferencia entre o meu numero atual e o meu numero
		# anterior + 1, caso o numero seja igual a '0', então significa
		# que o mesmos é uma sequencia do tipo 1,2,...,n
		check = abs((entry[i-1] + 1) - entry[i])
		
		# Caso o meu numero seja algo diferente de '0', então a minha
		# sequencia não contém o padrao que eu quero
		if(check):
			result = False

	return result

list_entry = [int(i) for i in input().split()]
# Crio a minha lista com as diferenças
new_list = calc_diff(list_entry)

if(check_sequence(new_list)): 
	print("Sequencia cheia")
else:
	print("Sequencia não cheia")