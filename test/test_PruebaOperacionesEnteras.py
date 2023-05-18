import unittest
from src.logic.OperacionesEnteros import OperacionesEnteros

class PruebaOperacionesEnteros(unittest.TestCase):
    def test_MCD_dosNumerosPositivos_retornaMCD(self):
         # Arrange
         numero1 = 18
         numero2 = 24
         resultadoEsperado = 6
         operacion = OperacionesEnteros([numero1, numero2])

         # Do
         resultadoActual = operacion.calcularMCD()

         # Assert
         self.assertEqual(resultadoEsperado, resultadoActual)
    def test_MCD_tresNumerosPositivos_retornaMCD(self):
         # Arrange
         numero1 = 24679
         numero2 = 20387
         numero3 = 16169
         resultadoEsperado = 37
         operacion = OperacionesEnteros([numero1, numero2, numero3])

         # Do
         resultadoActual = operacion.calcularMCD()

         # Assert
         self.assertEqual(resultadoEsperado, resultadoActual)

    def test_MCD_cuatroNumerosPositivos_retornaMCD(self):
        # Arrange
        numero1 = 27
        numero2 = 15
        numero3 = 6
        numero4 = 21
        resultadoEsperado = 3
        operacion = OperacionesEnteros([numero1, numero2, numero3, numero4])

        # Do
        resultadoActual = operacion.calcularMCD()

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)