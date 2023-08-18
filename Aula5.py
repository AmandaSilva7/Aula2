'''
#operadores logicos
#and = precisa de 2 True

renda_acima_5mil = True
nome_limpo = False

if renda_acima_5mil and nome_limpo:
    print('Financiamento aprovado')
else:
    print('Financiamento negado')    

#or = aceita 1 True

renda_acima_5mil = True
nome_limpo = False

if renda_acima_5mil or nome_limpo:
     print('Financiamento aprovado')
else:
      print('Financiamento negado')    


idade_lucas = 21
idade_carolina = 19

#operador or 
 
if idade_lucas >=18 or idade_carolina >=18:
    print('Pelo menos um dos dois é maior de idade')
else:
     print('lucas e carolina nao sao  maiores de idade')

#operador and   

if idade_lucas >=18 and idade_carolina >=18:
    print('lucas e carolina não são  maiores de idade')
else:
     print('Pelo menos um dos dois é maior de idade')  


#Multiplos operadores de comparaçao

valor = 20

if 20<= valor <40:

#if valor >=20 and valor <40:
     print('produto foi aceito')
else:
     print('produto não aceito')     

#for numeros
# imprimir de 1 a 5

for numero in range(1,20, 2): #contar de 1 a 20 com intervalo de 2 numeros
    print(numero)

lojas = ['rio', 'sampa', 'belo', 'curitiba']   
for loja in lojas :
    print(loja)
    print('Acabou for')

for i in range(4):
    print(i)
    print(lojas[i])

#for pra Strings

for letra in 'google':
    print(letra)


palavra  = 'google'
for letra in palavra:

    print(letra + ' esta dentro da palavra google')
'''
  '''  

#Desafio 
#6

from itertools import count


frutas = ['maça', 'banana', 'manga', 'uva']
print(frutas)

#7

print(frutas[0])
print(frutas[-1])

#10

for fruta in range(4):
  print(frutas)
  print(f' eu gosto de {frutas}')

#11

for i in range(11):
  
  print(i)

  #12
  
frutas = ['maça', 'banana', 'manga', 'uva']
vegetais = ['chuchu','brocolis','alface','couve']

print(frutas + vegetais + frutas + vegetais) 



#13

for num in range (1,11):
  print(num)


#14
print('loop com break :')
for numero in range(1,11):
  if numero > 5:
    break
print(numero)

#15xxx

if __name__ == ' __main__ ':
  frutas2 = ['maça', 'banana', 'maça', 'uva', 'maça']
  'maça' == 3
  freq = frutas2.count('maça')
'''
#16

b =('Digite um numero')

if b > 10:
  print('O número é maior que 10')
else:
  print('O número é igual ou menor que 10')

#17
  
a = input('Digite sua idade:')
idade = int(a)
if idade < 13:
  print('voce é uma criança')
elif idade >13 and idade <19:
  print('voce é um adolescente')
elif idade > 20:
  print('voce é um adulto')    

#18
dados = ['BMW X6','BMW i5','BMW i8']
modelo = input('Qual modelo deseja comprar?')


if modelo not in dados:
  print('modelo indisponivel')
else:
  print('disponivel')

 #24

i = int(input('digite um numero'))
retotno = i**2
print(retotno)







