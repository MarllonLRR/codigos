#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def cedulas(valor):

	# Pego a parte inteira da divisao das notas por 20
	n20 = valor // 20 
	# Pego o valor restante da divisao anterior e divido ele por 10
	n10 = (valor % 20) // 10
	# Pego o valor restante da divisao anterior e divido ele por 05
	n05 = ((valor % 20) % 10) // 5
	# Pego o valor restante da divisao anterior e divido ele por 01
	n01 = (((valor % 20) % 10) % 5) // 1

	return n20, n10, n05, n01

# Pego o valor de entrada e ja jogo para minha funcao que calcula as notas
result = notas(int(input()))

# Resposta do exercicio A)
print("%d nota de R$20, %d nota de R$10, %d nota de R$5, %d nota de R$1" % result)

# Resposta do exercicio B)
print("O menor numero de cedulas para se pagar eh %d cedulas" % sum(result))