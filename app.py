# Pixel Crusher Web Dashboard - Developed by elals
import os
from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename
from pixel_crusher import PixelCrusher
import logging

# Configuración de logging para la Web
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("pixel_crusher.log"),
        logging.StreamHandler()
    ]
)

app = Flask(__name__)
app.secret_key = "pixel_crusher_secret"

# Configuración de carpetas
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FOLDER = os.path.join(BASE_DIR, 'inputs')
OUTPUT_FOLDER = os.path.join(BASE_DIR, 'outputs')

app.config['INPUT_FOLDER'] = INPUT_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

# Asegurar directorios
os.makedirs(INPUT_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

crusher = PixelCrusher(input_dir=INPUT_FOLDER, output_dir=OUTPUT_FOLDER)

@app.route('/')
def index():
    # Filtrar archivos ocultos como .gitkeep o .DS_Store
    input_files = [f for f in os.listdir(app.config['INPUT_FOLDER']) 
                   if os.path.isfile(os.path.join(app.config['INPUT_FOLDER'], f)) and not f.startswith('.')]
    output_files = [f for f in os.listdir(app.config['OUTPUT_FOLDER']) 
                    if os.path.isfile(os.path.join(app.config['OUTPUT_FOLDER'], f)) and not f.startswith('.')]
    
    return render_template('index.html', input_files=input_files, output_files=output_files)

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        if 'files' not in request.files:
            print("DEBUG: No se encontró la clave 'files' en request.files")
            return "No files part", 400
        
        files = request.files.getlist('files')
        print(f"DEBUG: Intentando subir {len(files)} archivos...")
        
        for file in files:
            if file.filename == '':
                continue
            filename = secure_filename(file.filename)
            save_path = os.path.join(app.config['INPUT_FOLDER'], filename)
            file.save(save_path)
            print(f"DEBUG: Archivo guardado en {save_path}")
        
        return "OK", 200
    except Exception as e:
        print(f"DEBUG ERROR UPLOAD: {e}")
        return str(e), 500

@app.route('/crush', methods=['POST'])
def crush_images():
    try:
        quality = int(request.form.get('quality', 80))
        scale = request.form.get('scale')
        scale = int(scale) if scale and scale.isdigit() else None
        keywords = request.form.get('keywords', '')

        print(f"DEBUG: Iniciando CRUSH - Q:{quality}, S:{scale}, K:{keywords}")
        count = crusher.crush_all(quality=quality, scale=scale, keywords=keywords)
        
        if count > 0:
            flash(f'¡Éxito! Se procesaron {count} imágenes.')
        else:
            flash('No se encontraron imágenes válidas en /inputs.')
    except Exception as e:
        print(f"DEBUG ERROR CRUSH: {e}")
        flash(f'Error técnico: {e}')
        
    return redirect(url_for('index'))

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER'], filename, as_attachment=True)

@app.route('/preview/<filename>')
def preview_file(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER'], filename)

@app.route('/clear', methods=['POST'])
def clear_folders():
    target = request.form.get('target')
    folder = app.config['INPUT_FOLDER'] if target == 'inputs' else app.config['OUTPUT_FOLDER']
    
    for f in os.listdir(folder):
        file_path = os.path.join(folder, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
            
    flash(f'Carpeta {target} vaciada.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5005)
