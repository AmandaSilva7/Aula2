#calculando idade de acordo com o nascimento
#varieveis guardam valores
'''
ano_nascimento = 1985
idade = 2020 - ano_nascimento

print(idade)

'''
'''
ano_nascimento = input('Em que ano você nasceu?')
idade = 2020 - int(ano_nascimento)

print(idade)
'''
#exemplos de type
'''
x = 2
y = 'ola'

print(type(x))
print(type(y))

#A slice () funçao retorna um objeto de fatia 

fruta = 'Abacate'

#index   0123456
print(fruta[3]) #da o valor do item[3] da variavel
print(fruta[2:6])# item [2] ate [6]

a =('a', 'b', 'c', 'd', 'e', 'f')
x = slice(3,5)
print(a[x])
#nao le o ultimo
'''
'''
#o marcos silva e um excelente programador 
#formated string

nome = 'Marcos'
sobrenome = 'Silva'
profissao = 'programador'

texto = 'o ' + nome + sobrenome + ' e um excelente ' + '[' + profissao +']'


texto2 = f" o {nome} {sobrenome}  e um excelente [{profissao}]  "  #vai pegar so o que ta na chave{} o resto e frase 
print(texto2)


calculo = 2 + 2 * 3/2
calculo2 = 2 ** (3 + 4)
print (calculo2)

'''
#desafio 1 
print('Olá mundo phyton!' )

#desafio2

nome = str('Amanda')
idade = int(29)

texto = f' Ola meu nome é {nome} e eu tenho {idade} anos'
print(texto)

