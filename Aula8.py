#criar uma funçao que soma varios numeros

def soma (*numeros): # * significa recebendo varios numeros
  resultado = 0
  for num in numeros:
    resultado += num
  return resultado

x = soma (2,3,4,7)

print(x)


###



#defina funçao
def somador(valor1, valor2):
  soma = valor1 + valor2
  return soma
#chama funçao
res = somador(3,4)
print(f'valor é {res}')

###




#declaraçao da funçao 
def imprime_msg(nomePessoa):
  print(f'o usuario {nomePessoa} escreveu uma mensagem')
#chamando a funçao
nome = input('digite seu nome: ')  
imprime_msg(nome)


###
#criar uma funcao que armazena numeros e srings(dados) 

#varios argumentos 
def agencia (**carro):  # ** recebe parametro e argumento
  return carro 

print (agencia(marca='gol',cor= 'branca',motor= 1.0))


###


#qual e o numero fatorial de quatro
# 4 * 3 * 2 * 1 = 24

import math

print(math.factorial(4))
print(math.floor(2.7))
print(math.ceil(4))






fatorial = 4 * 3 * 2 * 1 
print(fatorial)



  

