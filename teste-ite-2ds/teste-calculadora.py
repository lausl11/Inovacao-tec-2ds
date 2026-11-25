# test_calculadora.py
import unittest
from calculadora import soma, subtrai, multiplica, divide

class TestCalculadora(unittest.TestCase):

    def test_soma(self):
        casos = [
            (1, 2, 3),
            (-1, 1, 0),
            (-1, -1, -2),
        ]
        for a, b, esperado in casos:
            with self.subTest(a=a, b=b):
                resultado = soma(a, b)
                self.assertEqual(
                    resultado,
                    esperado,
                    msg=f"Falha: soma({a}, {b}) retornou {resultado}, esperado {esperado}"
                )
                print(f"[OK] Teste de soma passou: {a} + {b} = {resultado}")

    def test_subtrai(self):
        casos = [
            (10, 5, 5),
            (-1, -1, 0),
            (0, 1, -1),
        ]
        for a, b, esperado in casos:
            with self.subTest(a=a, b=b):
                resultado = subtrai(a, b)
                self.assertEqual(
                    resultado,
                    esperado,
                    msg=f"Falha: subtrai({a}, {b}) retornou {resultado}, esperado {esperado}"
                )
                print(f"[OK] Teste de subtração passou: {a} - {b} = {resultado}")

    def test_multiplica(self):
        casos = [
            (3, 7, 21),
            (-1, 1, -1),
            (0, 10, 0),
        ]
        for a, b, esperado in casos:
            with self.subTest(a=a, b=b):
                resultado = multiplica(a, b)
                self.assertEqual(
                    resultado,
                    esperado,
                    msg=f"Falha: multiplica({a}, {b}) retornou {resultado}, esperado {esperado}"
                )
                print(f"[OK] Teste de multiplicação passou: {a} * {b} = {resultado}")

    def test_divide(self):
        casos = [
            (10, 2, 5),
            (-10, 2, -5),
        ]
        for a, b, esperado in casos:
            with self.subTest(a=a, b=b):
                resultado = divide(a, b)
                self.assertEqual(
                    resultado,
                    esperado,
                    msg=f"Falha: divide({a}, {b}) retornou {resultado}, esperado {esperado}"
                )
                print(f"[OK] Teste de divisão passou: {a} / {b} = {resultado}")

        # Teste de exceção para divisão por zero
        with self.subTest(a=10, b=0):
            with self.assertRaises(ValueError, msg="Falha: divide(10, 0) não levantou ValueError"):
                divide(10, 0)
            print("[OK] Teste de divisão por zero passou: ValueError levantado corretamente")

if __name__ == '__main__':
    unittest.main(verbosity=2)