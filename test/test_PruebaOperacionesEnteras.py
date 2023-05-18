import unittest
from src.logic.OperacionesEnteros import OperacionesEnteras

class test_OperacionesEnteras(unittest.TestCase):
    def setUp(self):
        self.operacion = OperacionesEnteras()

    def tearDown(self):
        self.operacion = None


    def test_MCD_dosNumerosPositivos_retornaMCD(self):

        # Arrange
        numero1 = 18
        numero2 = 24
        resultadoEsperado = 6

        # Do
        resultadoActual = self.operacion.MCD(numero1, numero2)

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)

