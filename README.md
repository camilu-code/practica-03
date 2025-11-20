📊 PRACTICA-03 — Análisis de Datos Tributarios del SRI con Pruebas Unitarias
🎯 Objetivo

Desarrollar un analizador de datos tributarios utilizando Python, aplicando pruebas unitarias para garantizar la confiabilidad de los cálculos realizados sobre el archivo real sri_ventas_2024.csv.

Este proyecto corresponde al trabajo de un estudiante de 7mo semestre de Ingeniería en Software, aplicando buenas prácticas en procesamiento de datos, testing y control de versiones.

🧰 Tecnologías utilizadas

Python 3.10+

VSCode

unittest

coverage.py

Entorno virtual venv/

Git & GitHub

📂 Estructura del proyecto (real)
PRACTICA-03/
│── app.py
│── .gitignore
│── .coverage
│── datos/
│   └── sri_ventas_2024.csv
│── src/
│   ├── __init__.py
│   └── procesador.py
│── test/
│   ├── __init__.py
│   └── test_analizador.py
│── venv/     (ignorado por Git)

📝 Descripción general

El archivo CSV contiene información tributaria del SRI:
ventas, compras, exportaciones, importaciones y valores con tarifa 0%.

El proyecto implementa una clase Analizador que procesa estos datos y ejecuta funciones como:

✔ Ventas totales por provincia
✔ Ventas por provincia específica
✔ Exportaciones totales por mes
✔ Porcentaje de ventas con tarifa 0%
✔ Provincia con mayor volumen de importaciones
🧪 Pruebas unitarias

Las pruebas se encuentran en:

test/test_analizador.py


Validan:

Correctos totales por provincia

Existencia y valores de ventas

Cálculo de exportaciones

Porcentaje de tarifa 0%

Provincia con mayor importación

Tipos de datos y comportamiento esperado

Ejecutar pruebas:
python -m unittest discover -s test

📈 Cobertura del código
Instalación:
pip install coverage

Ejecutar cobertura:
coverage run -m unittest discover -s test

Ver reporte:
coverage report

Crear reporte HTML:
coverage html


Esto genera la carpeta htmlcov/.

🔧 Trabajo autónomo realizado
1️⃣ Descarga del repositorio

Se descargó/clonó desde GitHub.

2️⃣ Creación del entorno virtual
python -m venv venv

3️⃣ Activación del entorno

Windows:

venv\Scripts\activate


Linux:

source venv/bin/activate

4️⃣ Instalación de coverage
pip install coverage

5️⃣ Ejecución de pruebas con cobertura

Incluye reporte en consola y HTML.

6️⃣ Configuración del .gitignore

Se agregó el entorno virtual y archivos temporales.

7️⃣ Creación del README profesional

(este documento)

8️⃣ Actualización del repositorio

Push final:

git add .
git commit -m "Proyecto final PRACTICA-03 con pruebas, cobertura y README"
git push

▶ Ejecución del programa principal

Solo correr:

python app.py

👨‍💻 Autor: Camila Segovia 👨‍💻
Práctica 03 – Procesamiento de Datos con Testing
