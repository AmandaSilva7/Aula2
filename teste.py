#18
dados = ['BMW X6','BMW i5','BMW i8']
modelo = input('Qual modelo deseja comprar?')


if modelo not in dados:
  print('modelo indisponivel')
else:
  print('modelo disponivel')


#17

a = input('Digite sua idade:')
idade =int(a)
if idade < 13:
  print('voce é uma criança')
elif idade >13 and idade <19:
  print('voce é um adolescente')
elif idade > 20:
  print('voce é um adulto')    

#24
i = int(input('digite um numero '))

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


  








