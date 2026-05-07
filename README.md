# Python Image Converter to WEBP + Metadata Manager

Script en Python para convertir archivos de imagen desde múltiples formatos a **WEBP**, formato moderno desarrollado por Google para compresión y optimización de imágenes web.

Además de convertir las imágenes, el script permite agregar **metadatos personalizados** a la imagen generada para mejorar el control, organización y trazabilidad de los activos digitales.

## Características

- Conversión de imágenes a formato `.webp`
- Compatible con múltiples formatos de entrada:
  - JPG / JPEG
  - PNG
  - BMP
  - TIFF
  - GIF
- Compresión optimizada para web
- Reducción de peso de archivos
- Inserción de metadatos personalizados
- Procesamiento individual o masivo
- Preparado para flujos SEO, eCommerce y performance web

## Objetivo

Optimizar imágenes para mejorar:

- Velocidad de carga
- Performance web
- Core Web Vitals
- SEO técnico
- Organización de assets digitales
- Control interno de imágenes generadas

## Tecnologías

- Python 3
- Pillow
- pathlib
- os
- datetime

## Casos de uso

- Optimización de imágenes para sitios web
- Conversión masiva de imágenes para eCommerce
- Preparación de imágenes para landing pages
- Automatización de assets digitales
- Mejora de rendimiento web
- Control de versiones de imágenes generadas

## Estructura sugerida

```bash
project/
├── input/
│   ├── imagen-1.jpg
│   ├── banner.png
│   └── producto.tiff
│
├── output/
│   ├── imagen-1.webp
│   ├── banner.webp
│   └── producto.webp
│
├── converter.py
└── README.md
