import this


def exercicio01():
    A = 10
    B = 20
    msg = "Antes da troca: A = {}, B = {}".format(A,B) # Troca dos {} para A,B
    aux = A
    A = B
    B = aux
    msg = msg + "\nDepois da troca : A = {}, B = {}".format(A,B)
    return msg

def exercicio02():

    num = int(input('escreva o seu valor:'))
    su = num -1
    print('\nO número escolhido foi: {}, seu antecessor é: {}'.format(num, su))

def exercicio03():

    base = int(input('Escreva sua base do retanculo:'))
    if base <= 0:
        return 'Por favor,digite um numero possitivo!'
    altura = int(input('Escreva a altura do retanculo'))
    if altura <= 0:
        return 'Por favor,digite um numero possitivo!'
    area = base * altura / 2.0

    print('Area:',area)

def exercicio04():

    anos = int(input('Digite o valor da sua idade: '))
    dias = int(input('Digite o valor em dias: '))
    meses = int(input('Digite o valor em meses: '))
    total_de_dias = anos * 365 + meses * 30 + dias
    print('O valor do total de dias: ' + repr(total_de_dias))

def exercicio05():

    eleitores = int(input("Digite o número total de eleitores: "))
    votos = int(input('Digite o numero de votos validos:'))
    nulos = int(input('Digite o numero de votos nulos:'))
    brancos = int(input('digite o numeros de votos brancos'))

    A = 100
    B = (votos/eleitores) *A
    C = (nulos/eleitores) *A
    D = (brancos/eleitores) *A

    print('Porcentos em votos ',B ,'%')
    print('Porcentos em nulos',C ,'%')
    print('Porcentos em brancos ',D,'%')

def exercicio06():

    salario = int(input('Digite o seu Salario Mensal:'))
    reajuste = int(input('Digite quantos porcentos você ira ganha:'))

    Valor = (salario/100* reajuste)
    print('Você ira ganhar :',Valor,)

def exercicio07():

    ValordoVeiculo = float(input('Informe o custo de fabrica do veiculo:'))

    Distribuidor = 1.28
    Impostos = 1.45

    Distribuidor1 = (ValordoVeiculo * Distribuidor)

    Impostos1 = (ValordoVeiculo * Impostos)

    Consumidor = (Distribuidor1 + Impostos1)

    valor = Consumidor
    msg = 'O custo ao consumidor é: valor = {}'.format(valor)
    return msg

def exercicio08():

    Aluno = (input('digite nome do aluno que deseja da nota:'))
    Nota1 = float(input('Primeira Nota:'))
    Nota2 = float(input('Segunda Nota:'))
    Nota3 = float(input('Terceira Nota:'))

    Calcular =(Nota1 + Nota2 + Nota3)/3

    print('A media do aluno sera:',Calcular)

#def exercicio09():
 #   print('Me informe quantas maças deseja?')

    #if qut > 0 and qut < 12:
       # Valor = Valor * 1.30

    #else:
      #  Valor = Valor * 1.00
   # msg = ('O valor do produto é : {}'.format(Valor))
    #return msg


def exercicio10():
    lista = []
    for i in range(1, 11):
        valor = float(input('Digite um número: '))
        lista.append(valor)
    return sorted(lista)

def exercicio11():
    salario = float(input('Digite seu salário fixo em R$:'))
    vendas = float(input('Digite o total das suas vendas em R$: '))
    if vendas >= 1500.0:
            c5 = (5*(vendas-1500))/100
            c3 = (3*vendas)/100
            total = salario+c3+c5

            return 'Parabéns, além do comissionamento de 3%, você atigiu o bônus de 5%, seu salário total será R${}'.format(total)
    else:
            c3 = (3/vendas)*100
            total = salario + c3

            return 'Seu salário total será R${}'.format(total)

def exercicio12():
    conta = int(input('Digite o número da sua conta:'))
    saldo = float(input('Digite seu saldo em R$:'))
    debito = float(input('Digite o débito que você possui em R$:'))
    credito = float(input('Digite o seu crédito em R$:'))

    saldoatual = saldo - debito + credito
    if saldoatual >= 0:
        return 'Saldo Positivo, seu saldo atual é de R${}'.format(saldoatual)

    else:
        return 'Saldo Negativo, seu saldo atual é de -R${}' .format(saldoatual)

def exercicio13():
    n = int(input('Digite um valor entre 1 e 10: '))
    if n > 10:
        return 'Opção inválida, digite um valor entre 1 e 10'
    elif n<0:
        return 'Opção inválida, digite um valor entre 1 e 10'
    else:
        for i in range(1, 11):
            resultado = n*i
            print('{} * {} = {}'.format(n, i, resultado))

def exercicio14():
    n = int(input('Digite um número: '))
    for i in range(1, n+1):
        print(i)

def exercicio15():
    lista = 0
    for i in range(1,11):
        n = int(input('Digite um número: '))
        if n<0:
            lista += +1

    return '\nSua lista possui {} números negativos' .format(lista)

def exercicio16():
    lista = 0
    for i in range(1, 11):
        n = float(input('Digite um número: '))
        if n<40:
            lista += n

    return '\nO resultado da sua soma é {}' .format(lista)

def exercicio17():
    aux = 0
    quantidade = 0
    for i in range(1, 101):

        aux += i
        quantidade += +1
        result = aux/quantidade

    return '\n{} / {} = {}' .format(aux, quantidade, result)

def exercicio18():
   n = int(input('Quantos números deseja digitar? '))
   if n<=0:
       print('Obrigado!')
   else:
    aux3 = 0
    quantidade = 1

    maior = float(input('Digite um número: '))
    for i in range(2, n + 1):
        num = float(input('Digite um número: '))

        aux2 = maior
        aux3 += num
        quantidade += +1
        media = (aux2+aux3)/quantidade

        if num>maior:
            maior = num

    print ('O maior número digitado foi {}'.format(maior))
    print('A média dos números digitados foi {}' .format(media))

def exercicio19():
    total = 0
    maior = 0
    lista = []
    for i in range(20):
        notas = float(input('Digita sua nota de 0 a 10: '))
        lista.append(notas)
        if notas>10:
            print('Digite uma nota válida')
        elif notas<0:
            print('Digite uma nota válida')
        else:
            total += notas
            mediag = total / 20

    for i in range(20):
       if lista[i] > mediag:
          maior += 1

    print('A média da turma foi {}.'.format(mediag))
    print('{} aluno(s) tiveram nota maior que a média'.format(maior))

def exercicio20():
    medias = 0
    mediaf = 0
    aux = 0
    abaixo = 0

    habitantes = int(input('Digite a quantidade de habitantes: '))
    for i in range(1, habitantes+1):
        salario = float(input('Digite seu salário em R$: '))
        if salario<=150.0:
            abaixo = +1
        if aux<salario:
            aux = salario
        if salario<0:
            print('Salário inválido')
        filhos = int(input('Digite a quantidade de filhos que você possui: '))
        if filhos<0:
            print('Quantidade inválida')

        medias += salario
        mediaf += filhos
    results = medias/habitantes
    resultf = mediaf/habitantes
    resultmenor = (abaixo/habitantes)*100

    print('Média do salário da população R$:{}' .format(results))
    print('Média número de filhos por habitante: {}' .format(resultf))
    print('Maior salário dos habitantes, R$:{}'.format(aux))
    print('Há {}% de pessoas com salário abaixo de R$150.0'.format(resultmenor))







