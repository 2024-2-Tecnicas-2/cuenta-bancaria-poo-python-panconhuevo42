import sys
import os
import unittest

# Add the 'src' directory to the Python path so 'calculadora' can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


class TestCalcular(unittest.TestCase):
    # TODO Adiciona tus pruebas unitarias aquí.
    # Ejemplo:   
    # def test_suma(self):
    #     valor_esperado = 3
    #     valor_actual = calcular(1, 2, '+')
    #     self.assertEqual(valor_esperado, valor_actual)
