import unittest,re

# Dado um `count` como sendo o números de donuts, retornar uma string
# na forma "Número de donuts: <count>", caso `count` seja
# maior ou igual a 10 retornar "many".
def donuts(count):
  '''Usando IF para checar variável'''
  if count >=10:
    '''Maior que dez funciona melhor pois printa qualquer valor menor 10'''
    return 'Number of donuts: many'
  else:
    return f'Number of donuts: {count}'
    pass


# Outra versão
def donutsV2(count):
  '''USANDO WHILE COMO SE FOSSE UM IF NO FIM TUDO SE TRATA DE UMA OPERAÇÃO LÓGICA'''
  while count >= 10:
    print(f'Number of donuts: many')
    break
  while count<10:
    print('Number of donuts: ', count)
    break
    pass





# Dado uma string qualquer `s`, retonar uma string
# composta dos 2 primeiros e os 2 últimos caracteres, exemplo:
#
# panela ----> pala
# bala   ----> bala
# mao    ----> maao
# ja     ----> jaja
#
# Caso a string `s` contenha menos que 2 caracteres,
# retornar "" (string de cumprimento zero).
def both_ends(s):
  '''AQUI VAMOS SEPARAR OS CASOS POSSÍVEIS'''
  if len(s) >= 2:
    '''APARTIR DO TAMANHO DA STRING PODEMOS CHEGAR A SUAS SUBSTRINGS E SELECIONAR O AS DUAS INICIAIS E AS DUAS FINAIS'''
    return s[:2]+s[len(s)-2:]
  else :
    '''SE FOR MENOR QUE DOIS VAI RETORNAR UM STRING VAZIA'''
    return ''
    pass


  
# Dado uma string `s`, retornar uma string onde
# todas as ocorrências de seu primeiro caractere
# seja alterado para '*', exceto o primeiro caracter. Exemplo:
#
# babble ---> ba**le
#
# Presuma que o tamanho da string seja 1 ou mais.
# Dica: s.replace (strA, strB) retorna uma versão da string s
def fix_start(s):
  '''SALVAMOS A LETRA INICIAL EM UMA VARIÁVEL LOCAL'''
  x= s[0]
  '''TROCAMOS TODAS AS LETRAS IGUAIS A PRIMEIRA POR ASTERISCO INCLUSIVE ESTA'''
  s = s.replace(s[0], "*")
  '''AQUI PERCORREMOS DE MODO INDIRETO A STRING EXCETO A PRIMEIRA LETRA'''
  for i in range(1, len(s)):
    '''AGORA ACESSAMOS A VARIÁVEL SALVA E CONCATENAMOS FORMANDO A PALAVRA DESEJADA'''
    x = x+s[i]
  return x
  pass

# Dado duas string `a` e `b`,  trocar os 2 primeiros caracteres entre as variáveis
# e retornar uma única string separada por espaço como no exemplo:
#
# "pezzy", "firm" ----> "fizzy perm"
def mix_up(a, b):
  '''TROCAMOS AS SUBSTRINGS USANDO REPLACE, ENTRANTO SE A STRING FOR MONOCARACTERE ISSO NÃO VAI FUNCIONAR DIREITO'''
  a,b = a.replace(a[:2], b[:2],1), b.replace(b[:2], a[:2], 1)
  '''SOLUCIONANDO O PROBLEMA RELATADO'''
  if len(a)<2 or len(b)<2:
    '''COLOCA-SE OS VALORES EM UMA LISTA'''
    list= [a,b]
    '''DEPOIS ORDENAMOS USANDO O COMPRIMENTO DE COMO PARÂMETROS'''
    list = sorted(list, key=len)
    '''AGORA É POSSÍVEL SABER QUAL DAS VARIÁVEIS É A MENOR E REATRIBUIR AOS PARÂMETROS'''
    a = list[0]
    b = list[1]
    '''USANDO O REPLACE O PROCESSO É FINALIZADO'''
    a,b = a.replace(a[0], b[:2], 1), b.replace(b[:2], a[0],1)
  return f'{a} {b}'
  pass




class MyTest(unittest.TestCase):

    def test_donuts(self):
      self.assertEqual(donuts(4), 'Number of donuts: 4')
      self.assertEqual(donuts(9), 'Number of donuts: 9')
      self.assertEqual(donuts(10), 'Number of donuts: many')
      self.assertEqual(donuts(99), 'Number of donuts: many')

    def test_both_ends(self):
      self.assertEqual(both_ends('spring'), 'spng')
      self.assertEqual(both_ends('Hello'), 'Helo')
      self.assertEqual(both_ends('a'), '')
      self.assertEqual(both_ends('xyz'), 'xyyz')
      self.assertEqual(both_ends('xy'), 'xyxy')

    def test_fix_start(self):
      self.assertEqual(both_ends('xy'), 'xyxy')
      self.assertEqual(fix_start('babble'), 'ba**le')
      self.assertEqual(fix_start('aardvark'), 'a*rdv*rk')
      self.assertEqual(fix_start('google'), 'goo*le')
      self.assertEqual(fix_start('donut'), 'donut')

    def test_mix_up(self):
      self.assertEqual(mix_up('mix', 'pod'), 'pox mid')
      self.assertEqual(mix_up('dog', 'dinner'), 'dig donner')
      self.assertEqual(mix_up('gnash', 'sport'), 'spash gnort')
      self.assertEqual(mix_up('pezzy', 'firm'), 'fizzy perm')



if __name__=="__main__":
    #Questão 1
    unittest.main()