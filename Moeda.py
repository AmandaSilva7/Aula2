#crie um modulo chamado moeda.py que tenha todas as funçoes
#incorporadas aumentar(), diminuir(), dobro(), e metade().
#faça tambem um programa que importa esse modulo e use algumas 
#dessas funçoes crie modulo teste.py

def aumentar(preço,taxa):
    res = preço + (preço * taxa/100)
    return res

def diminuir (preço,taxa):
    res = preço - (preço * taxa/100)
    return res

def dobro (preço):
    res = preço * 2
    return res

def metade (preço):
    res = preço/2
    return res

    
