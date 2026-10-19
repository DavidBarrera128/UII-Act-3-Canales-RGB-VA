import cv2
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt

# -----------------------------------------
# 1. Definir las rutas del proyecto
# -----------------------------------------
# David Barrera NC  = 1388
# -----------------------------------------

CARPETA_PROYECTO = Path(__file__).resolve().parent.parent

RUTA_IMAGEN = (
    CARPETA_PROYECTO
    / "img-original-1388"
    / "img-Chevrolet-1388.jpg"
)

CARPETA_RESULTADOS = (
    CARPETA_PROYECTO / "resultados-img-1388"
)

# Crear la carpeta de resultados si no existe
CARPETA_RESULTADOS.mkdir(parents=True, exist_ok=True)

# -----------------------------------------
# 2. Comprobar que existe la imagen
# -----------------------------------------

if not RUTA_IMAGEN.is_file():
    print("ERROR: No se encontro la imagen.")
    print("Coloca img-Chevrolet-1388.jpg en:")
    print(RUTA_IMAGEN)
    raise SystemExit(1)

# -----------------------------------------
# 3. Obtener el tamaño del archivo
# -----------------------------------------

tamano_bytes = RUTA_IMAGEN.stat().st_size
tamano_kb = tamano_bytes / 1024
tamano_mb = tamano_bytes / (1024 * 1024)

# -----------------------------------------
# 4. Leer la imagen con OpenCV
# -----------------------------------------

imagen = cv2.imread(str(RUTA_IMAGEN), cv2.IMREAD_COLOR)

if imagen is None:
    print("ERROR: El archivo no es una imagen valida")
    print("o el formato no se pudo interpretar.")
    raise SystemExit(1)

# -----------------------------------------
# 5. Obtener dimensiones y canales
# -----------------------------------------

alto, ancho, canales = imagen.shape

total_pixeles = ancho * alto
resolucion = f"{ancho} x {alto}"

# -----------------------------------------
# 6. Consultar propiedades de los pixeles
# -----------------------------------------

tipo_datos = str(imagen.dtype)
valor_minimo = int(np.min(imagen))
valor_maximo = int(np.max(imagen))
promedio = float(np.mean(imagen))

promedio_b = float(np.mean(imagen[:, :, 0]))
promedio_g = float(np.mean(imagen[:, :, 1]))
promedio_r = float(np.mean(imagen[:, :, 2]))

# -----------------------------------------
# 7. Preparar el informe
# -----------------------------------------

informe = f"""
INFORME DE METADATOS Y PROPIEDADES
==================================

Nombre del archivo: {RUTA_IMAGEN.name}
Ruta del archivo: {RUTA_IMAGEN}
Formato por extension: {RUTA_IMAGEN.suffix.upper()}
Tamano en bytes: {tamano_bytes}
Tamano en KB: {tamano_kb:.2f}
Tamano en MB: {tamano_mb:.4f}

DIMENSIONES
-----------
Ancho: {ancho} pixeles
Alto: {alto} pixeles
Resolucion: {resolucion}
Total de pixeles: {total_pixeles:,}

CANALES Y DATOS
---------------
Numero de canales: {canales}
Orden de canales: BGR
Tipo de datos: {tipo_datos}
Valor minimo de pixel: {valor_minimo}
Valor maximo de pixel: {valor_maximo}
Promedio general de los valores: {promedio:.2f}

PROMEDIO POR CANAL
------------------
Azul (B): {promedio_b:.2f}
Verde (G): {promedio_g:.2f}
Rojo (R): {promedio_r:.2f}

Nota: el formato se identifica por la extension
del archivo. La resolucion indica las dimensiones
en pixeles y no los puntos por pulgada (DPI).
"""

# -----------------------------------------
# 8. Mostrar el informe en la terminal
# -----------------------------------------

print(informe)

# -----------------------------------------
# 9. Guardar el informe automaticamente
# -----------------------------------------

ruta_informe = CARPETA_RESULTADOS / "metadatos-img-1388.txt"
ruta_informe.write_text(informe, encoding="utf-8")

# -----------------------------------------
# 10. Guardar una copia de la imagen
# -----------------------------------------

ruta_copia = CARPETA_RESULTADOS / "copia-img-Chevrolet-1388.jpg"

if not cv2.imwrite(str(ruta_copia), imagen):
    print("No se pudo guardar la copia de la imagen.")
    raise SystemExit(1)

# -----------------------------------------
# 11. Mostrar la imagen en pantalla con Matplotlib
# -----------------------------------------

imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

plt.figure("resultado-Chevrolet-1388")
plt.imshow(imagen_rgb)
plt.title("resultado-Chevrolet-1388")
plt.axis("off")
plt.show()

# -----------------------------------------
# 12. Finalizar
# -----------------------------------------

print("Practica completada correctamente.")
print("Informe:", ruta_informe)
print("Copia de imagen:", ruta_copia)

print("David Barrera NC  = 1388")