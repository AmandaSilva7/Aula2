#desafio com funcoes
#criar um progarma que aceita um numero e retorna o dobro desse numero 
# a segunda aceita um numro e retorna o quadrado
# a terceira chama a primeira funcao dentro da segunda para retornar o quadrado do dobro do numero


n1 = int(input('Digite um numero: '))
funcao1 = n1 * 2
print(funcao1)
n2= int(input('Digite outro numero: '))
funcao2 = n2 ** 2
print(funcao2)
funcao3 = funcao1**2
print(funcao3)


#programa que calcula a quantidade de tinta necessaria para pintar uma parede
# o usuario devera fornecer as informaçoes: rendimento, altura e largura
#o programa deve mostrar a msg na tela:
# 'Voce necessita de x latas de tinta'


rendimento = int(input("Qual o rendimento da lata?"))
altura = int(input('Qual a altura da parede?'))
largura = int(input('Qual a largura da parede?'))

def calc_tinta():
    area = altura * largura
    total = area / rendimento

    print(f'voce precisa de {total} latas de tinta')

calc_tinta()




