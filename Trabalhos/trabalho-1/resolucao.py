###################################
#!/usr/bin/env python3           
# -*- coding: utf-8 -*-
# developed by: Marllon Rodrigues 
###################################

# Funcao que retonar a quantidade de cedulas dado um valor
def result_currency(value):
  
  v_100 = value // 100 
  v_10  = (value % 100) // 10
  v_1   = (value % 100) % 10

  return value, v_100, v_10, v_1

# Funcao que me retornar em qual grupo determinado valor pertence
def detect_group(number):
  if(number == 0):
    number = 100
  
  result = number // 4

  if(number % 4 == 0):
    result -= 1

  return result

# Funcao que calcula o valor do premio do participante
def result_price(value, n, m):
  N_4 = n % 10000
  M_4 = m % 10000

  N_3 = n % 1000
  M_3 = m % 1000

  N_2 = n % 100
  M_2 = m % 100

  if(N_4 == M_4):
    value *= 3000
  elif(N_3 == M_3):
    value *= 500
  elif(N_2 == M_2):
    value *= 50
  elif(detect_group(N_2) == detect_group(M_2)):
    value *= 16
  else:
    value = 0

  return result_currency(value)


value = input().split()
value = [int(x) for x in value]

while sum(value) > 0:
  result = result_price(value[0], value[1], value[2])
  print("{} {}x100 {}x10 {}x1".format(result[0], result[1], result[2], result[3]))

  value = input().split()
  value = [int(x) for x in value]
