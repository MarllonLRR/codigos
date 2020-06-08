#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input("Numero de estudantes: "))
contador = 0

soma_das_notas = 0
numero_de_aprovados = 0
numero_de_reprovados = 0

while(contador < n):

	n1 = int(input("Digite a nota 1 para o aluno {}: ".format(contador + 1)))
	n2 = int(input("Digite a nota 2 para o aluno {}: ".format(contador + 1)))
	n3 = int(input("Digite a nota 3 para o aluno {}: ".format(contador + 1)))

	media_estudante = (n1 + n2 + n3) / 3

	print("Media do estudante {} eh: {}".format((contador+1), media_estudante))

	if (media_estudante >= 5):
		numero_de_aprovados += 1
	else:
		numero_de_reprovados += 1

	soma_das_notas = soma_das_notas + n1 + n2 + n3

	contador += 1


# media das notas
media_turma = soma_das_notas /( n * 3)


print("Media da turma eh de: {}".format(media_turma))
print("Numero de aprovador: {}".format(numero_de_aprovados))
print("Numero de reprovador: {}".format(numero_de_reprovados))