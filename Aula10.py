#armazenar mais de uma informaçao
#manter a sequencia de dados em uma variavel
#o lower() retorna uma string onde os carcteres sao minusculos
#simbolos e numeros sao ignorados
'''
cor_cliente =input('digite a cor desejada: ')
cores = ['amarelo', 'verde', 'azul', 'vermelho']

if cor_cliente.lower() in cores:
    print('sim')
else:
   print('não temos essa cor em estoque')    




#junta listas
  '''      
cores = ['amarelo', 'verde', 'azul', 'vermelho','roxo']
valores = [10,20,30,40,50]
valor = [53.00, 56.00]

duas_listas = zip(cores, valores,valor)

print(list(duas_listas))



#criar uma lista de frutas a partir do input fornecido por virgulas:
#o split metodo divide uma string em lista
#voce pode especificar o separador, o separador padrao é qualquer espaço em branco


frutas_usuario = input('digite o nome das frutas separadas por virgula: ')
frutas_lista = frutas_usuario.split(', ')

print(frutas_lista)


#Turples
#as turples sao usadas para armazenar varios itens em uma unica variavel
#tuplas sao escritas com parenteses 
#tupla e uma coleçao ordenada e imutavel

cores_list =  ['amarelo', 'verde', 'azul', 'vermelho']
cores_turples= ('amarelo', 'verde', 'azul', 'vermelho','roxo')

cores_list.append('roxo')

#print(type(cores_list))
#print(type(cores_turples))

#duas_listas2 = cores_list * 2
print (cores_list)


