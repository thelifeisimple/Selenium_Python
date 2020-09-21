import unittest


class PruebasDeStandars(unittest.TestCase):

    def test_suma(self):
        a = 2 + 2
        b = 3 + 10
        self.assertEqual(a, b)

    def test_otra_suma(self):
        c = 5 + 1
        d = 8
        self.assertNotEqual(c, d)

    def test_algo_verdadero(self):
        a = 2 + 2
        b = 3 + 5
        self.assertTrue(a == b, 'a y b Deberian ser iguales')

    def test_algo_falso(self):
        self.assertFalse(3 + 1 == 4, "Esto debería ser falso")

    def test_algo_mas_grande(self):
        a = 2
        b = 6
        self.assertGreater(a, b)

    def test_algo_mas_menor(self):
        a = 6
        b = 6
        self.assertLess(a, b)

    def test_algo_es_menor_o_igual(self):
        a = 6
        b = 6
        self.assertLessEqual(a, b)

    def test_comparar_listas(self):
        a = [1,4.3,'fruta','hola']
        b = [1,2,'fruta']
        self.assertListEqual(a, b)

    def test_comparar_tuplas(self):
        a = (1, 2, 3, 4)
        b = (1, 2, 3)
        self.assertTupleEqual(a, b)

    def test_comparar_diccionario(self):
        a = {'id':1,'Nombre':'Sun','Apellido':'shin', 'Edad': 31}
        b = {'id':2,'Nombre':'Sun','Apellido':'shin'}
        self.assertDictEqual(a,b)

#crea el main para ejecucion UnitTest
if __name__ == '__main__':
    unittest.main()
