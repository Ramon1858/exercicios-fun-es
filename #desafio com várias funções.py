 #1.crie uam função para comparar 2 numeros
def comparar():
    n1 = float(input('digite um numero:'))
    n2 = float(input('digite o outro numero:'))
    if n1 > n2:
        print('o numero um é maior ')
    elif n1 < n2:
         print('o numero um é menor')
comparar()
#2. crie uma função com 3 numeros
def multiplicar_numeros():
    n1 = float(input('digite um numero:'))
    n2 = float(input('digite o segundo numero:'))
    n3 = float(input('digite o ultimo numero:'))
    multiplicacao = n1 * n2 * n3
    print(multiplicacao)
multiplicar_numeros()
# 3.cria uma função para descobrir o valor elevado de um numero
def elevarn():
    numero1 = float(input('digite um numero:'))
    numero = float(input('digite um numeropara elevar:'))
    elevar = numero ** numero1 
    print(elevar)
elevarn()
#4 .crie uma função para mostrar uma mensagem na tela se o usuario digitar 18
def idade():
    idade1 = int(input('digite sua idade:'))
    if idade1 >= 18:
        print('acesso liberado')
    elif idade1 <= 18:
        print('não pode acessar')
idade()
#5.crie uma função para descobrir a idade de uma pessoa
def nascimento():
    ano = int(input('ano de nascimento:'))
    ano_atual = int(input('ano atual:'))
    calc = ano_atual - ano
    print(calc)    
nascimento()
#6.desenvolva uma função para ver se o Brasil ganhou a copa de 1999
def copa():
    resposta = input('o Brasil ganhou a copa américa de 1999(sim ou não)?:')
    if resposta == 'sim':
        print('conhecor dos conhecimentos')
    elif resposta =='não':
        print('errorroouu')
copa()