#qt1 
#O TRATAMENTO DE EXCEÇÕES É IMPORTANTE PARA QUE O CÓDIGO NÃO QUEBRE
# DE QUALQUER MODO E PARA QUE SE SAIBA A CAUSA DO CRASH. ACREDITO QUE 
# SEJA IMPORTANTE PARA A CONSTRUÇÃO DE PEQUENAS FUNÇÕES EM CÓDIGOS 
# GRANDES POIS ASSIM AS FALHAS NÃO IRIAM PARAR TUDO. VEJAMOS UMA SIMPLES
# FUNÇÃO QUE FOI PASSADA COMO ATIVIDADE


# Considere dividir uma string em duas metades.
# Se o comprimento for par, a parte da frete (front) e a parte de trás (back) são do mesmo tamanho.
# Se o comprimento for ímpar, o caracter extra irá para a aprte da frente.
#
# Dado 2 strings, 'a' e 'b', retornar um string na forma
# a front + b front + a back + b back
def front_back(a, b):
  '''DECLARA OS VALROES QUE CORRESPONDEM A METADE DA PALAVRA
  E SOMA COM ALGUM RESTO QUE HAJA NESSA DIVISÃO
  CUMPRINDO A REQUISIÇÃO'''
  index_a = int(len(a)/2)+len(a)%2
  index_b = int(len(b)/2)+len(b)%2
  return a[:index_a]+ b[:index_b] +a[index_a-len(a)%2:]+b[index_b-len(a)%2:]
  pass

# SABE-SE QUE OS PARAMETROS DA FUNÇÃO DEVEM SER STRINGS
# ENTRETANTO É POSSÍVEL QUE OS PARAMETROS PASSADOS SEJAM 
# TIPO INTEIRO E SE ACONTECER O CÓDIGO IRÁ QUEBRAR
# PODEMOS ENTÃO USAR O try except

try:
  print(front_back(1,"all"))
except Exception as erro:
  print("O valor recebido em um dos parâmetros não é válido", erro.__class__)

#qt2
# A FUNÇÃO map() FUNCIONA COMO UM LOOP for QUE PERCORRE TODA
# UMA LISTA DE ITENS OU BASE DADOS. A CADA ITEM PERCORRIDO A
# MESMA EXECUTA UMA FUNÇÃO COLOCADA COMO PARÂMETRO, TAL FUNÇÃO
# EXECUTADA DEVE TER APENAS UM PARÂMETRO DE ENTRADA QUE 
# SERÁ PREENCHIDO PELO ITEM QUE MAP PERCORRE. A FUNÇÃO map()
# RETORNA UM OBJETO DO TIPO map
# RESUMO: A FUNÇÃO map() RECEBE DOIS PARÂMETROS(UM AGRUPAMENTO DE ITENS E UMA FUNÇÃO)
# E DEVOLVE UM OBJETO DO TIPO map.

#qt3
primos = [2, 3, 5, 7, 11, 13]
primos_1 = list(map(lambda a : a + 1, primos))
print(f'{primos_1}')
#qt4
primos_1 = []
for i in primos:
  primos_1.append(i+1)
print(f'{primos_1}')
#qt5
# O match case FUNCIONA COMO UMA CONDICIONAL QUE CHECA OS 
# POSSÍVEIS VALORES DE UMA OU MAIS VARIÁVEIS. É PRECISO INFORMAR QUAL
# VARIÁVEL SERÁ OBSERVADA EM match E O QUE IRÁ SER EXECUTADO
# EM CADA case, É OPCIONAL QUE SEJA DECLARADA UMA
# EXCEÇÃO CASO NENHUM DOS VALORES NOS case's SEJAM CORRESPONDENTES.
# O match case NÃO FAZ OPERAÇÕES LÓGICAS ALÉM DA CHECAGEM DE VALOR
a = 1
b = 2
match a,b:
  case 1, 2:
    print("deu certo")
  case _:
    print("Nenhum valor previsto")

#qt6
# O QUE assert BASICAMENTE FAZ É CHECA UMA OPERAÇÃO LÓGICA
# SE A OPERAÇÃO FOR VERDADEIRA O CÓDIGO SEGUE NORMALMENTE
# SE NÃO O CÓDIGO PARA. O USO DELE É INDICADO PARA FAZER 
# DEBUGS E ENCONTRAR CAUSAS DE ERRO APARENTEMENTE INVISÍVEIS
# BUSCANDO MANTER A SANIDADE INTERNA DO CÓDIGO.
# NÃO HÁ UM CONSENSO GERAL PARA QUAIS TIPOS DE ERRO SE DEVE
# USAR O assert ALGUMAS FONTES DIZEM QUE SERIA PARA VERIFICAR
# OS TIPOS DOS PARÂMETROS DE UMA FUNÇÃO OU MÉTODO, JÁ OUTRAS
# DIZEM QUE O assert DEVERIA SER USADO PARA SE VERIFICAR O VALOR
# DE ALGUMA VARIÁVEL IMPORTANTE OU ALGUMA COISA DO GÊNERO QUE
# PODE ESTAR ACARRETANDO O ERRO

import random

lista = [1,2,3,4,5]
index = random.randint(0,6)
assert index < 4
print(lista[index])