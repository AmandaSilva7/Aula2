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

#25
n1 = int(input('Digite um numero '))
n2 = int(input('Digite outro numero :)'))

soma = (n1+n2)

print(soma)

#26

def potencia(base, expoente = 2):
    return base ** expoente
user_number = int(input('Digite o numero base: '))
user_expoente = int(input('Digite o expoente: '))

if user_expoente:
  print(f'O resultado é:{potencia(user_number,int(user_expoente))}')
else:
  print(f'O resultado é:{potencia(user_number)}')

#28

n1 = int(input('digite um numero: '))
f1 = n1*2
print(f1)

n2 = int(input('digite outro numero: '))
f2 = n2**2
print(f2)

retotno = f1**2
print(retotno)
