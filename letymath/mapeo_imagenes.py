#!/usr/bin/env python3
"""
Script para mapear imágenes antiguas (JPG) a tópicos nuevos.

Uso:
    python3 mapeo_imagenes.py > mapeo_imagenes.csv

Este script ayuda a correlacionar las ~300 imágenes antiguas
con los tópicos nuevos de LetyMath.

Basado en:
- Análisis de nombres de archivos (pag_X_foto_Y.jpg)
- Mapeo manual de páginas a tópicos
"""

import os
import csv
from collections import defaultdict

# Mapeo manual de páginas a tópicos
# (página_inicio, página_fin, topico, curso)
MAPEO_PAGINAS = [
    # Matemáticas 1
    (1, 5, "operaciones-basicas", "matematicas-1"),
    (6, 10, "jerarquia", "matematicas-1"),
    (11, 17, "ecuaciones", "matematicas-1"),
    (18, 25, "monomios", "matematicas-1"),
    (26, 32, "expresiones-algebraicas", "matematicas-1"),
    (33, 40, "grafica-tabulacion", "matematicas-1"),
    (41, 47, "pendiente-ordenada", "matematicas-1"),
    (48, 54, "area-perimetro", "matematicas-1"),
    (55, 60, "ecuaciones-angulos", "matematicas-1"),

    # Matemáticas 2 (estimado)
    (61, 70, "operaciones-con-fracciones", "matematicas-2"),
    (71, 80, "jerarquia-con-fracciones", "matematicas-2"),

    # Matemáticas 3
    (81, 97, "[REVISAR - Sistemas, Cuadráticas, Cónicas]", "matematicas-3"),
]

def get_topico_for_page(page_num):
    """Obtener el tópico para una página específica."""
    for inicio, fin, topico, curso in MAPEO_PAGINAS:
        if inicio <= page_num <= fin:
            return topico, curso
    return "[DESCONOCIDO]", "[DESCONOCIDO]"

def main():
    # Ruta a la carpeta de imágenes
    folder = "/sessions/hopeful-funny-cori/mnt/ capturas y sitios letymath"

    # Obtener todas las imágenes
    try:
        images = sorted([f for f in os.listdir(folder) if f.endswith('.jpg')])
    except FileNotFoundError:
        print("Error: No se encuentra la carpeta de imágenes")
        return

    # Agrupar por página
    by_page = defaultdict(list)
    for img in images:
        # Patrón: pag_X_foto_Y.jpg
        parts = img.split('_')
        if len(parts) >= 2 and parts[0] == 'pag':
            page_num = int(parts[1])
            by_page[page_num].append(img)

    # Generar CSV
    writer = csv.writer(__import__('sys').stdout)
    writer.writerow(['página', 'num_fotos', 'topico', 'curso', 'archivos'])

    for page in sorted(by_page.keys()):
        images_list = by_page[page]
        topico, curso = get_topico_for_page(page)
        files = '; '.join(sorted(images_list))
        writer.writerow([
            page,
            len(images_list),
            topico,
            curso,
            files
        ])

    print(f"\n# Total de imágenes: {len(images)}", file=__import__('sys').stderr)
    print(f"# Páginas identificadas: {len(by_page)}", file=__import__('sys').stderr)

if __name__ == '__main__':
    main()
