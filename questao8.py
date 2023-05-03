def media_anual(temperaturas):
    '''MEDIA DAS TEMPERATURAS'''
    media = sum(temperaturas)/len(temperaturas)
    '''LISTA DAS TEMPERATURAS ACIMA DA MÉDIA'''
    acima = []
    '''LOOP QUE CHECA TODAS AS TEMPERATURAS E ADICIONA AS MAIORES A LISTA acima'''
    for i in range(0, len(temperaturas)):
        if temperaturas[i]>media:
            acima.append(i)
        else:
            continue
    return acima
    '''Receba uma lista com as temperaturas médias de cada mês
    e devolva uma lista com os números correspondentes aos meses que 
    possuem temperatura superior á média anual.'''

def maiores_13(idades,alturas):
    '''MEDIA DAS ALTURAS'''
    mediah = sum(alturas)/len(alturas)
    '''LISTA DAS ALTURAS DOS MENORES ACIMA DE 13'''
    minors = []
    '''LOOP QUE PERCORRE TODA A LISTA alturas E QUE ADICIONA O TERMO DESEJADO
    A LISTA minors'''
    for i in range(0, len(alturas)):
        if alturas[i]<mediah and idades[i]>13:
            minors.append(alturas[i])
        else:
            continue
    return minors
    '''Esta função recebe as idades e alturas de diversas pessoas, em duas
    listas separadas e de igual comprimento.
    Calcule a media das alturas e retorne as alturas daqueles que possuem 
    'idades' maior que 13 e altura inferior a media da turma'''

def media_saltos_lista(saltos):
    saltos.sort()

    saltos.remove(saltos[0])
    saltos.remove(saltos[3])
 
    return sum(saltos)/len(saltos)
    '''Receba uma lista com os saltos de um atleta e calcule a média dos 
    seus saltos, sabendo que o melhor e o pior saltos são desconsiderados.'''

def lista_de_primos(inicio,fim):
    '''LISTA DOS RESULTADOS'''
    result=[]
    '''VALIDAÇÃO UNITÁRIA SOBRE A DIVISIBILIDADE DE UM NÚMERO'''
    def primos_unit(n):
        '''DIVISORES'''
        divs = 0
        '''LOOP QUE PERCORRE OS LIMITES'''
        for i in range(1,n):
            if n%i==0:
                divs+=1
            else:
                continue
        '''VALIDAÇÃO AO TÉRMINO DO LOOP'''
        if divs ==1:
            return True
        else:
            return False
    '''LOOP QUE CHAMA A FUNÇÃO E ADICIONA OS VALORES VÁLIDOS NA LISTA'''
    for j in range(inicio,fim+1):
        if j!=0 and primos_unit(j):
            result.append(j)
        else:
            continue
    return result
    '''Retorne uma lista de primos entre os valores informados, incluindo
    os limites'''

def Fibonacci(n):
    '''DECLARAMOS UM CONTADOR I E UMA LISTA QUE RECEBERÁ OS NÚEMROS'''
    nums =[]
    i=n
    def Fibonacci_unit(s):
        '''UNITARIAMENTE É FEITO O FIBONACCI'''
        if s==1:
            return 1
        if s ==2:
            return 1
        else:
            return Fibonacci_unit(s-1)+Fibonacci_unit(s-2)
    '''UM LOOP PARA QUE OS VALORES SEJAM ADICIONADOS RECURSIVAMENTE E UMA FUNÇÃO PARA ORDENAR OS VALORES'''
    while i>0:
        nums.append(Fibonacci_unit(i))
        i-=1
    nums = sorted(nums)
    return nums 


    ''' Retorne uma lista com os n primeiros valores da série de Fibonacci.
    Fibonacci = 1,1,2,3,5,8,13,...'''

def altera_salarios(salarios):
    '''LISTA QUE ARMAZENARÁ OS RESULTADOS'''
    result=[]
    '''SALÁRIO MÍNIMO'''
    sm = 724.0
    '''LOOP QUE PERCORRERÁ A LISTA DE SALÁRIOS'''
    for i in range(0, len(salarios)):
        '''CONDICIONAIS QUE CHECAM OS SALÁRIOS DE CADA UM'''
        if salarios[i]<=sm:
            result.append(salarios[i]+salarios[i]*0.2)
        elif sm < salarios[i] <= 2*sm:
            result.append(salarios[i]+salarios[i]*0.15)
        elif 2*sm < salarios[i] <= 5*sm:
            result.append(salarios[i]+salarios[i]*0.10)
        else:
            result.append(salarios[i]+salarios[i]*0.05)
    return result
    ''' Calcule o aumento de salário de acordo com a seguinte tabela:
    - até 1 SM(inclusive): aumento de 20%
    - de 1 até 2 SM(inclusive): aumento de 15%
    - de 2 até 5 SM(inclusive): aumento de 10%
    - acima de 5 SM: aumento de 5% 
    Salário mínimo para referência: R$ 724,00
    Retorna a lista com os salários alterados
    '''

# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0 

def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = ' Falhou.'
    else:
        prefixo = ' Passou.'
        acertos += 1
    print ('%s Esperado: %s \tObtido: %s' % (prefixo,repr(esperado), 
        repr(obtido)))

def main():
    print(' Meses acima da média:')
    test(media_anual([20,20,20,20,20,20,20,20,20,20,20,20]), [])
    test(media_anual([25,20,20,20,20,20,20,20,20,20,20,20]), [0])
    test(media_anual([23,25,26,24,21,22,26,24,25,22,23,19]), [1,2,3,6,7,8])
    test(media_anual([19,20,21,20,17,18,19,20,22,21,20]), [1, 2, 3, 7, 8, 9, 10])
    test(media_anual([21,22,23,21,22,22,23,21,23,22,21,23,21]), [1,2,4,5,6,8,9,11])
    
    print(' Alturas abaixo da media:')
    test(maiores_13([13,13,14],[1.7,1.7,1.5]), [1.5])
    test(maiores_13([13,13,14,13],[1.7,1.7,1.5,1.6]), [1.5])
    test(maiores_13([14,20],[1.6,2]), [1.6])
    test(maiores_13([10,7,13,15,20,21],[1.7,1.21,1.65,2,1.9,1.5]), [1.5])
    test(maiores_13([14,15,16,17,18,30],[1.9,1.89,1.85,1.95,2,1.99]), [1.9,1.89,1.85])
    test(maiores_13([10,9,90,9,13,14,15],[1.25,1.3,1.7,1.41,1.5,1.55,1.7]), [])

    print(' Média dos saltos em lista:')
    test(media_saltos_lista([10,10,10,10,10]), 10)
    test(media_saltos_lista([9,9.1,8,7,6.9]), 8)
    test(media_saltos_lista([1,1,3,5,5]), 3)
    test(media_saltos_lista([10,10,9.9,10,10]), 10)

    print(' Lista de primos:')
    test(lista_de_primos(0,1), [])
    test(lista_de_primos(5,10), [5,7])
    test(lista_de_primos(10,20), [11,13,17,19])
    test(lista_de_primos(0,21), [2,3,5,7,11,13,17,19])
    test(lista_de_primos(43,102), [43,47,53,59,61,67,71,73,79,83,89,97,101])

    print(' Fibonacci:')
    test(Fibonacci(1), [1])
    test(Fibonacci(2), [1,1])
    test(Fibonacci(3), [1,1,2])
    test(Fibonacci(4), [1,1,2,3])

    print(' Aumenta salários:')
    test(altera_salarios([500,724.0,725.00,1448.00,1449.00,3620.00,3621.00,4000.00]), 
        [600.0, 868.8, 833.75, 1665.2, 1593.9, 3982.0, 3802.05, 4200.0])

if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" %(total, acertos,
     total-acertos, float(acertos*10)/total))
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")