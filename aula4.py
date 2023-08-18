'''
numero_1 = 5
numero_2 = 2

soma = numero_1 + numero_2
subtracao = numero_1 - numero_2
multiplicacao = numero_1 * numero_2
divisao = numero_1 / numero_2
divisao_inteira = numero_1 // numero_2
modulo = numero_1 % numero_2
exponenciacao = numero_1 ** numero_2

print(soma)
print(subtracao)
print(multiplicacao)
print(divisao)
print(divisao_inteira)
print(modulo)
print(exponenciacao)

#precedencia = ordem de operacao quando ocorre mais de uma operacao 


print(1 + 5 ** 2)#precedencia **

print(5 * 3 + 8)#precedencia*

#os operadores de atribuicao possuem o valoe de uma variavel
#x + 1 
#x +=1 
x = 10
#x = x + 5
x += 5 #soma 5 + 10 

print(x)
'''
'''
#operadores de comparacao > (maior que)    < (menor que)... etc

operadores = 10>=5
print(operadores)
'''
'''
numero_1 = 2
numero_2 = 4

soma = numero_1 + numero_2

if soma < 10:
    print('soma não é maior que 10') 
else:
    print('soma é igual ou maior que 10')    

soma_1 = 7 + 7
soma_2 = 10 + 5

if soma_1==soma_2:
    print('os resultados são iguais')
else:
    print('os resultados são diferentes')


soma3 = 1 + 5
soma4 = 5 + 5

if soma3!=soma4:
    print('os resultados são diferentes :)')
else:
    print('os resultados são iguais :)')
'''
'''

from tokenize import String


velocidade = 50

if velocidade >110:
    print('Acima da velocidade permitida')
    print('Favor reduzir a velocidade')
elif velocidade <60:
    print('favor dirigir acima de 80km/h')    
else:
    print('velocidade ok')    
'''
#desafio 3 4 e 5
 
 
 #3
num1 = int (10)
num2 = float (3.5)

divisao = num1/num2

print (divisao)


#4

nome = input('qual é o seu nome')
idade = input('Qual é a sua idade?')

texto = f"Olá , {nome}! Você tem {idade} anos."
print(texto)

#5

n1 = int (input('Digite um numero'))
n2 = int(input('Digite outro numero :)'))

soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1/n2
exponenciacao = n1**n2

print (soma) 
print (subtracao) 
print (multiplicacao)
print (divisao) 
print (exponenciacao)




