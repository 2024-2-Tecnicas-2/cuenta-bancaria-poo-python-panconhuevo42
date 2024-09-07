import unittest
import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


from src.cuenta_bancaria import CuentaBancaria

class TestCuentaBancaria(unittest.TestCase):
    def setUp(self):
        self.cuenta = CuentaBancaria("Nicolas", "123456789", 10000)
    
    def test_ingresar_dinero(self):
        self.cuenta.ingresar(5000)
        self.assertEqual(self.cuenta.get_saldo(), 15000)
    
    def test_ingresar_dinero2(self):
        self.cuenta.ingresar(7000)
        self.assertEqual(self.cuenta.get_saldo(), 17000)

    def test_retirar_dinero(self):
        self.cuenta.retirar(3000)
        self.assertEqual(self.cuenta.get_saldo(), 7000)

    def test_retirar_dinero_insuficiente(self):
        with self.assertRaises(ValueError):
            self.cuenta.retirar(20000)

    def test_calcular_interes(self):
        self.cuenta.calcular_interes(10)
        interes_esperado = self.cuenta.get_saldo() * 0.1
        interes_esperado = self.cuenta.get_saldo() + interes_esperado
        interes_calculado = self.cuenta.calcular_interes(10)
        self.assertEqual(interes_calculado, interes_esperado)
    
    def test_calcular_interes2(self):
        self.cuenta.calcular_interes(9)
        interes_esperado = self.cuenta.get_saldo() * 0.09
        interes_esperado = self.cuenta.get_saldo() + interes_esperado
        interes_calculado = self.cuenta.calcular_interes(9)
        self.assertEqual(interes_calculado, interes_esperado)
