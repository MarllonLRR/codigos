#!/usr/bin/env python3
# -*- coding: utf-8 -*-

x = int(input("Digite n: "))

# pega o comprimento de um determinado numero
def size(x):
	counter = 0

	while(x > 0):
		x = x // 10

		counter += 1

	return counter

def quebra(x, debugg = False):

	# Pego o meu utimo digito
	last = x % 10
	# pego a parte inteira do meu X / 10 ^ (numero de digitos)
	first = x // (10 ** (size(x)- 1))

	# pego agora o meio do meu numero palindromo
	# DIVIDO POR 10
	# DEPOIS SUBTRAIO de X - (PRIMEIRO DIGITO * 10 ^ (NUMERO DE DIGITOS))
	x = x // 10
	x = x - first * (10 ** (size(x) - 1))

	middle = int(x)

	# caso eu queria mostrar os valores encontrados
	if (debugg):
		print(first, last, middle)

	return first, last, middle


# variavel para me dizer se o numero eh palindromo
palindromo = True
nX = x

while palindromo:
	first, last, middle = quebra(nX, debugg = True)

	# caso o meio tenho apenas 1 digito meu laco tem que parar
	if(middle < 10):
		break

	# caso o primeiro e o ultimo digitos sejam diferentes meu numero nao eh palindromo
	if(first != last):
		palindromo = False
		break

	# pego agora o meio meio para o proximo passo de 'quebra' do meu numero
	nX = middle

print(palindromo)