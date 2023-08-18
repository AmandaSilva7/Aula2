#Listas

#Armazenar mais de uma informaçao em variaveis 
#Manter a sequencia de dados em uma variavel

cidade1 = 'rio de janeiro'
cidade2 = 'sao paulo'
cidade3 = 'salvador'
                     #itens
cidades = ['rio de janeiro', 'sao paulo', 'salvador']
#              0                   1           2

#cidades.append('santa catarina') #append = adicionar item 
#cidades.remove('salvador') #remover
#cidades.insert(1,'manaus') #troca item 1 por manaus e bota pro item 2
#cidades.pop(0)
cidades.sort() # coloca em ordem alfabetica

print(cidades)
#

numeros = [ 2,3,4,5]
letras = ['a', 'b','c','d']
#final = numeros + letras 
numeros.extend(letras) #extend = juntar listas
print(numeros)
#              0                 1
itens= [['item1','item2'],['item3','item4']] #lista dentro de lista
#           0      1          2       3
print(itens[1][0])


