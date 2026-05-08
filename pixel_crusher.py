# Pixel Crusher Core - Developed by elals
import os
import logging
# pyrefly: ignore [missing-import]
from PIL import Image
# pyrefly: ignore [missing-import]
import piexif

__version__ = "1.0.0"

# Configuración de logger para el módulo
logger = logging.getLogger(__name__)

class PixelCrusher:
    def __init__(self, input_dir="inputs", output_dir="outputs"):
        """Inicializa el motor con rutas absolutas."""
        self.input_dir = os.path.abspath(input_dir)
        self.output_dir = os.path.abspath(output_dir)
        
        # Crear directorios con permisos
        try:
            os.makedirs(self.input_dir, exist_ok=True)
            os.makedirs(self.output_dir, exist_ok=True)
            logger.info(f"Pixel Crusher activo en: {self.input_dir}")
        except Exception as e:
            print(f"ERROR CRÍTICO: No se pudieron crear los directorios: {e}")

    def log(self, message, level="info"):
        if level == "info":
            logger.info(message)
        elif level == "error":
            logger.error(message)

    def _add_metadata(self, keywords):
        """Genera bytes de metadatos EXIF de forma robusta."""
        if not keywords or not isinstance(keywords, str):
            return None
        try:
            exif_dict = {
                "0th": {
                    piexif.ImageIFD.ImageDescription: keywords.encode('utf-8'),
                    piexif.ImageIFD.Software: b"Pixel Crusher"
                },
                "Exif": {},
                "GPS": {},
                "1st": {},
                "thumbnail": None
            }
            return piexif.dump(exif_dict)
        except Exception as e:
            self.log(f"Error en metadatos: {e}", "error")
            return None

    def _resize_image(self, img, scale_percent):
        """Redimensiona la imagen usando el filtro de mayor calidad disponible."""
        width, height = img.size
        new_size = (int(width * scale_percent / 100), int(height * scale_percent / 100))
        
        # Intentar usar el nuevo estándar de Pillow 10+
        if hasattr(Image, 'Resampling'):
            resample_mode = Image.Resampling.LANCZOS
        else:
            resample_mode = Image.LANCZOS
            
        return img.resize(new_size, resample_mode)

    def process_image(self, filename, quality=80, scale=None, keywords=None):
        """Convierte una imagen a WebP con optimizaciones."""
        input_path = os.path.join(self.input_dir, filename)
        output_filename = os.path.splitext(filename)[0] + ".webp"
        output_path = os.path.join(self.output_dir, output_filename)

        if not os.path.exists(input_path):
            return False

        try:
            with Image.open(input_path) as img:
                # Normalizar modo de color
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")
                
                # Escalar si es necesario
                if scale and 0 < scale < 100:
                    img = self._resize_image(img, scale)
                
                # Preparar metadatos
                exif_bytes = self._add_metadata(keywords)
                
                # Guardar con fallback de seguridad
                try:
                    img.save(output_path, "WEBP", quality=quality, exif=exif_bytes)
                except Exception:
                    # Si falla con metadatos, guardar solo la imagen
                    img.save(output_path, "WEBP", quality=quality)
                
                self.log(f"Convertido: {filename} -> {output_filename}")
                return True
        except Exception as e:
            self.log(f"Fallo en {filename}: {e}", "error")
            return False

    def crush_all(self, quality=80, scale=None, keywords=None):
        """Procesa todas las imágenes compatibles en la carpeta de entrada."""
        exts = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.PNG', '.JPG', '.JPEG')
        files = [f for f in os.listdir(self.input_dir) if f.endswith(exts)]
        
        if not files:
            self.log(f"No hay imágenes válidas en {self.input_dir}")
            return 0

        count = 0
        for f in files:
            if self.process_image(f, quality, scale, keywords):
                count += 1
        return count

if __name__ == "__main__":
    crusher = PixelCrusher()
    print(f"Pixel Crusher v{__version__} listo.")
