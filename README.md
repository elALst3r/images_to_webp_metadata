# Pixel Crusher

**Pixel Crusher** es una potente herramienta híbrida (Web & CLI) diseñada para optimizar imágenes. Convierte tus activos a formato **WebP**, ajusta el tamaño y añade metadatos EXIF estratégicos para mejorar el rendimiento web.

## Características
- **Conversión Inteligente:** Transforma JPG/PNG a WebP de alto rendimiento.
- **SEO Ready:** Inyección automática de metadatos SEO (`ImageDescription`).
- **Híbrido:** Úsalo desde tu navegador o desde la terminal.
- **Premium UI:** Interfaz moderna con modo oscuro y efectos de cristal.
- **Batch Processing:** Procesa cientos de imágenes con un solo clic.

## Instalación rápida
1. Clona este repositorio.
2. Configura el entorno ejecutando el script de instalación:
   ```bash
   ./setup_env.sh
   ```
3. Activa el entorno:
   ```bash
   source venv/bin/activate
   ```

## Uso
### Dashboard Web
```bash
python app.py
```
Accede a `http://127.0.0.1:5005`

### Terminal (CLI)
```bash
python cli_crusher.py --all --quality 80 --scale 50
```

## Requisitos
- Python 3.8+
- Pillow
- Flask
- piexif

## Licencia
Este proyecto está bajo la Licencia MIT - mira el archivo [LICENSE](LICENSE) para detalles.

---
Desarrollado para optimización de alto rendimiento.
