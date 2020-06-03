#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Coding by: Marllon Rodrigues

import math

# Função que faz a retirada de elementos multiplos do elemento C[i]
def remove_element(C, i):
	j = i+1

	while(len(C) > j):
		
		# Faço o calculo de modulo para determinar se um numero é multiplo de outro
		multiple = C[j] % C[i]

		if(multiple == 0):
			# Caso seja multiplo faço a remoção do elemento na minha lista
			del C[j]

		j += 1 

def clac_clive(C, n):
	# Calculo o piso da raiz quadrado do meu numero	
	floor = math.floor(math.sqrt(n))

	# Para cada elemento indo de 0 até a raiz quadrade de N
	for i in range(floor):
		# Faço a remoção dos meus numeros multiplos
		remove_element(C, i)

	return C

def create_list(n):
	return [i for i in range(2,n+1)]

# Pego o meu N
entry = int(input())
# Crio a minha lista de numeros
prime_numbers = create_list(entry)
# Chamo a minha função que retorna todos os numeros primos em uma determinada sequencia
prime_numbers = clac_clive(prime_numbers, entry)

print(prime_numbers)