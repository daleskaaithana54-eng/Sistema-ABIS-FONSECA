import unittest
from clientes import validar_dni, validar_nombre, validar_telefono


class TestValidaciones(unittest.TestCase):
    def test_dni_correcto(self):
        self.assertTrue(validar_dni("12345678"))

    def test_dni_incorrecto(self):
        self.assertFalse(validar_dni("1234"))

    def test_nombre_correcto(self):
        self.assertTrue(validar_nombre("Ana Maria"))

    def test_nombre_incorrecto(self):
        self.assertFalse(validar_nombre("Ana123"))

    def test_telefono_correcto(self):
        self.assertTrue(validar_telefono("987654321"))

    def test_telefono_incorrecto(self):
        self.assertFalse(validar_telefono("12345"))

if __name__ == "__main__":
    unittest.main()