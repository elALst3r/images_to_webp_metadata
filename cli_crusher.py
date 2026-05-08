import sys
import argparse
from pixel_crusher import PixelCrusher
import logging

# Configuración de logging para CLI
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s'
)

def main():
    parser = argparse.ArgumentParser(description="Pixel Crusher CLI - Optimiza tus imágenes para SEO")
    
    parser.add_argument("--quality", type=int, default=80, help="Calidad del WebP (1-100). Default: 80")
    parser.add_argument("--scale", type=int, default=None, help="Porcentaje de escala (ej. 80, 50).")
    parser.add_argument("--keywords", type=str, default=None, help="Palabras clave para SEO (entre comillas).")
    parser.add_argument("--all", action="store_true", help="Procesar todas las imágenes en /inputs")

    args = parser.parse_args()

    crusher = PixelCrusher()

    if args.all:
        print(f"Crushing images in /inputs...")
        crusher.crush_all(quality=args.quality, scale=args.scale, keywords=args.keywords)
    else:
        # Si no se pasa --all, preguntar interactivamente si hay archivos
        import os
        files = os.listdir("inputs")
        if not files:
            print("La carpeta /inputs está vacía. Agregue imágenes y use --all")
            sys.exit(0)
            
        print(f"Se encontraron {len(files)} archivos. ¿Deseas procesarlos todos? (s/n)")
        confirm = input().lower()
        if confirm == 's':
            crusher.crush_all(quality=args.quality, scale=args.scale, keywords=args.keywords)
        else:
            print("Operación cancelada.")

if __name__ == "__main__":
    main()
