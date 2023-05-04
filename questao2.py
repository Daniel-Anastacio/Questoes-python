import unittest


def verbing(s):
    #SEU CODIGO AQUI
    '''CONDICIONAIS QUE RECORTAM O FINAL
    DA STRING E COMPARAM'''
    if s[len(s)-1]=="l":
       return s + "ing"
    elif s[len(s)-3:] == "ing":
       return s + "ly"
    else: 
       return s
    pass


# Dado um astring, procurar a primeira ocorrência da substring 'not' e 'bad'
# Se 'bad' vier após o 'not'
# substituir todo o trecho "not ... bad" por 'good'
# Retorne a string resultante.
def not_bad(s): 
  '''CONDICIONAL QUE CHECA A EXISTÊNCIA DOS TERMOS
  PEDIDOS'''
  if 'bad' in s and 'not' in s and ' is ' in s :
       x = s.index('not')
       y = s.index('bad')
       z = s.index(' is ')
       '''TRATAMENTO DE STRING E RECORTE'''
       if x<y:
        return s[:z+4] + "good"
       else:
          return s
  else:
     return s
  pass
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

class MyTest(unittest.TestCase):

  def test_verbing(self):
    self.assertEqual(verbing('hail'), 'hailing')
    self.assertEqual(verbing('swiming'), 'swimingly')
    self.assertEqual(verbing('do'), 'do')

  def test_not_bad(self):
    self.assertEqual(not_bad('This movie is not so bad'), 'This movie is good')
    self.assertEqual(not_bad('This dinner is not that bad!'), 'This dinner is good')
    self.assertEqual(not_bad('This tea is not hot'), 'This tea is not hot')
    self.assertEqual(not_bad("It's bad yet not"), "It's bad yet not")

  def test_front_back(self):
    self.assertEqual(front_back('abcd', 'xy'), 'abxcdy')
    self.assertEqual(front_back('abcde', 'xyz'), 'abcxydez')
    self.assertEqual(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  unittest.main()