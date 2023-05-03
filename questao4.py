import unittest

# Dado um a lista de números, retorna uma lista onde
# todo elemento adjacente e repetido será deletado reduzindo a um único elemento.
# Então, [1, 2, 2, 3] retornará [1, 2, 3]
# Você pode criar uma nova lista ou modificar a lista atual.
def remove_adjacent(nums):
    '''LISTA QUE RECEBERÁ OS VALORES DE RESULTADO'''
    x = list()
    '''ÚLTIMO DIGITO ADICIONADO'''
    p = 0
    '''LOOP QUE PERCORRE TODA A LISTA nums'''
    for i in nums:
        '''CHECA SE O NÚMERO NÃO FOI REPETIDO E SE NÃO É 
        IGUAL AO ÚLTIMO ADICIONADO'''
        if i not in x or i != p:
          x.append(i)
        p = x[len(x)-1]
    '''RETORNA A LISTA CONCERTADA'''
    return x
    pass

# Dado duas listas ordenadas em ordem crescente, criar e retornar uma
# lista de todos os elementos em ordem algabética.
# Você pode modificar as listas passadas.
# Idealmente, a solução deve trabalhar em tempo "linear", que passa uma única vez em ambas as listas.
def linear_merge(list1, list2):
  '''CHECA SE AS LISTAS TEM VALOR E COLOCA
  ELAS EM ORDEM '''
  if list1!=[None] and list2!=[None]:
    return sorted(list1+list2, reverse=False)
  else:
    return None
    pass
linear_merge([1,2,3],[None])
class MyTest(unittest.TestCase):
  def test_remove_adjacent(self):
    self.assertEqual(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    self.assertEqual(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    # Repare que são excluídos apenas os valores repetidos e adjacentes
    self.assertEqual(remove_adjacent([1, 2, 3, 2, 3]), [1, 2, 3, 2, 3])
    self.assertEqual(remove_adjacent([]), [])

  def test_linear_merge(self):
    self.assertEqual(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']), ['aa', 'bb', 'cc', 'xx', 'zz'])
    self.assertEqual(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']), ['aa', 'bb', 'cc', 'xx', 'zz'])
    self.assertEqual(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']), ['aa', 'aa', 'aa', 'bb', 'bb'])

if __name__ == '__main__':
  unittest.main()