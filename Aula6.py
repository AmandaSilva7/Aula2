#For loop - utilisando If e Else

#enviar um email com detalhes da compra online(Maximo 3 tentativas)
# para compras confirmadas
'''
compra_confirmada = True
dados_compra = 'Compra no valor de R$ 12.50 e entrega confirmada'



for enviar in range(3): 
   if compra_confirmada:
    print(dados_compra)
    print('Detalhes enviados para seu email')
    break #parar o looping
else:
    print('falha na compra')

# For loop - Nested loops (Laços aninhados)
#outer loop

#inner loop(laço externo)
#inner loop(laço interno)

#interno
for numero1 in range(5):
   print(numero1)
   for numero2 in range(5):
      print(numero2)

#externo

for numero1 in range(5):
   print(numero1)
   for numero2 in range(5):
      print(numero1,numero2)



'''
'''
for numero1 in range(1,6):
   print('produto'+str(numero1))
   for numero2 in range(5):
      print(numero1,numero2)

#modificar de FANTASTICO PARA F A N T A S T I C O       

palavra = 'FANTASTICO'
for spaco in palavra:
        print(f' {spaco}', end='')

        '''
'''
# criar um retangulo 6x6

linha = 6
coluna = 6
simbolo = '@'

for l in range(linha):
    for c in range (coluna):
        print(simbolo, end='')
    print()

 '''   

#== while loops ===
#excelente para loops depementes de uma condicao
'''
valor = 100
dia = 1

while valor > 20:
    dia += 1
    print(f'no dia {dia} o produto vai ser vendido por {valor}' )
    
    valor -= 5

#operador ternario

idade = 20

if idade >=16:
    resultado = print('voto nao permitido')
else:
    resultado = print('voto nao permitido')

resultado = 'voto permitido' if idade >=16 else'voto nao permitido'
print(resultado)      
'''
#publicar um produto com comissao de 10% se for acima de R$:20 

valor = int(input('digite o valor do seu produto em R$:'))
while valor > 20: 
      valor = (valor *0.10) + valor
      print(f' o valor final do seu produto sera de R${valor}')       
      break



              
