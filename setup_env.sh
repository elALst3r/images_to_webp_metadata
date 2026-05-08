#!/bin/bash

echo "🚀 Iniciando configuración de Pixel Crusher..."

# 1. Crear entorno virtual si no existe
if [ ! -d "venv" ]; then
    echo "📦 Creando entorno virtual (venv)..."
    python3 -m venv venv
else
    echo "✅ El entorno virtual ya existe."
fi

# 2. Activar el entorno virtual
echo "🔌 Activando entorno..."
source venv/bin/activate

# 3. Instalar/Actualizar pip
echo "🆙 Actualizando pip..."
pip install --upgrade pip

# 4. Instalar dependencias
if [ -f "requirements.txt" ]; then
    echo "📚 Instalando dependencias desde requirements.txt..."
    pip install -r requirements.txt
else
    echo "❌ Error: requirements.txt no encontrado."
    exit 1
fi

echo "-----------------------------------------------"
echo "✨ ¡Listo! Para usar Pixel Crusher, recuerda activar el entorno con:"
echo "   source venv/bin/activate"
echo ""
echo "Luego puedes ejecutar:"
echo "   python app.py      (Para el Dashboard Web)"
echo "   python cli_crusher.py --all  (Para la Terminal)"
echo "-----------------------------------------------"
