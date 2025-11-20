import unittest
from src.procesador import Analizador
import os

class TestAnalizador(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Construir ruta absoluta al CSV, independientemente del directorio actual
        base_dir = os.path.dirname(os.path.dirname(__file__))  # sube a la raíz del proyecto
        ruta_csv = os.path.join(base_dir, "datos", "sri_ventas_2024.csv")
        cls.analizador = Analizador(ruta_csv)

    def test_ventas_totales_como_diccionario(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        self.assertIsInstance(resumen, dict)

    def test_ventas_totales_todas_las_provincias(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        total_provincias = len(resumen)
        self.assertGreaterEqual(total_provincias, 1)

    def test_ventas_totales_mayores_5k(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        self.assertTrue(any(float(v) > 5000 for v in resumen.values()))

    def test_ventas_por_provincia_inexistente(self):
        resultado = self.analizador.ventas_por_provincia("Narnia")
        self.assertEqual(resultado, 0)

    def test_ventas_por_provincia_existente(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        provincia = next((p for p, v in resumen.items() if float(v) > 0), None)
        if provincia is None:
            self.skipTest("No hay provincias con ventas > 0 en el CSV")
        else:
            resultado = self.analizador.ventas_por_provincia(provincia)
            self.assertGreater(resultado, 0)

    def test_exportaciones_totales_por_mes(self):
        analizador = Analizador.__new__(Analizador)
        analizador.datos = [
            {"MES": "Enero", "EXPORTACIONES": "100"},
            {"MES": "Enero", "EXPORTACIONES": "200"},
            {"MES": "Febrero", "EXPORTACIONES": "300"},
        ]
        r = analizador.exportaciones_totales_por_mes()
        self.assertEqual(r["Enero"], 300)
        self.assertEqual(r["Febrero"], 300)

    def test_porcentaje_ventas_tarifa_0(self):
        analizador = Analizador.__new__(Analizador)
        analizador.datos = [
            {"PROVINCIA": "A", "VENTAS_NETAS_TARIFA_0": "100", "TOTAL_VENTAS": "200"},
            {"PROVINCIA": "A", "VENTAS_NETAS_TARIFA_0": "50", "TOTAL_VENTAS": "100"},
            {"PROVINCIA": "B", "VENTAS_NETAS_TARIFA_0": "200", "TOTAL_VENTAS": "400"},
        ]
        r = analizador.porcentaje_ventas_tarifa_0()
        self.assertAlmostEqual(r["A"], 50)
        self.assertAlmostEqual(r["B"], 50)

    def test_provincia_mayor_importacion(self):
        analizador = Analizador.__new__(Analizador)
        analizador.datos = [
            {"PROVINCIA": "A", "IMPORTACIONES": "100"},
            {"PROVINCIA": "A", "IMPORTACIONES": "250"},
            {"PROVINCIA": "B", "IMPORTACIONES": "200"},
        ]
        r = analizador.provincia_mayor_importacion()
        self.assertEqual(r, "A")
