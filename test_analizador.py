import csv

class Analizador:
    def __init__(self, ruta_csv):
        self.ruta_csv = ruta_csv
        self.datos = self.leer_csv()

    # ===============================================================
    # LECTURA DEL CSV
    # ===============================================================
    def leer_csv(self):
        """Lee el archivo CSV y devuelve una lista de filas."""
        datos = []
        try:
            with open(self.ruta_csv, "r", encoding="utf-8") as archivo:
                lector = csv.DictReader(archivo, delimiter='|')
                for fila in lector:
                    datos.append(fila)
            return datos
        except FileNotFoundError:
            print(f"Error: El archivo {self.ruta_csv} no fue encontrado.")
            return []

    # ===============================================================
    # PROVINCIAS ÚNICAS
    # ===============================================================
    def provincias_unicas(self):
        """Devuelve un conjunto con las provincias en minúsculas."""
        return {fila["PROVINCIA"].lower() for fila in self.datos}

    # ===============================================================
    # VENTAS TOTALES POR PROVINCIA
    # ===============================================================
    def ventas_totales_por_provincia(self):
        """Devuelve las ventas totales agrupadas por provincia."""
        totales = {}
        for fila in self.datos:
            try:
                provincia = fila["PROVINCIA"].upper()
                total_venta = float(fila["TOTAL_VENTAS"])
                totales[provincia] = totales.get(provincia, 0.0) + total_venta
            except (ValueError, KeyError):
                continue
        return totales

    # ===============================================================
    # VENTAS DE UNA PROVINCIA
    # ===============================================================
    def ventas_por_provincia(self, nombre):
        """
        Devuelve las ventas totales para una provincia.
        Si no existe, debe lanzar KeyError (exigencia del test).
        """
        nombre = nombre.upper()
        resumen = self.ventas_totales_por_provincia()

        if nombre not in resumen:
            raise KeyError(f"Provincia '{nombre}' no encontrada.")

        return resumen[nombre]

    # ===============================================================
    # EXPORTACIONES POR MES
    # ===============================================================
    def exportaciones_totales_por_mes(self):
        """Suma exportaciones agrupadas por mes."""
        totales = {}
        for fila in self.datos:
            try:
                mes = fila["MES"]
                valor = float(fila["EXPORTACIONES"])
                totales[mes] = totales.get(mes, 0.0) + valor
            except (KeyError, ValueError):
                continue
        return totales

    # ===============================================================
    # PROVINCIA CON MAYOR IMPORTACIÓN
    # ===============================================================
    def provincia_mayor_importacion(self):
        """Devuelve la provincia con mayor total de importaciones."""
        totales = {}
        for fila in self.datos:
            try:
                provincia = fila["PROVINCIA"].upper()
                valor = float(fila["IMPORTACIONES"])
                totales[provincia] = totales.get(provincia, 0.0) + valor
            except (KeyError, ValueError):
                continue

        if not totales:
            raise ValueError("No existen datos válidos de importaciones.")

        return max(totales, key=totales.get)
