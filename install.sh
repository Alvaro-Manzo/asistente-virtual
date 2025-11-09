#!/bin/bash

# 🤖 Script de instalación para Asistente Virtual Jorge
# Para macOS

echo "🚀 Configurando Asistente Virtual Jorge..."

# Crear entorno virtual si no existe
if [ ! -d ".venv" ]; then
    echo "📦 Creando entorno virtual..."
    python3 -m venv .venv
fi

# Activar entorno virtual
echo "⚡ Activando entorno virtual..."
source .venv/bin/activate

# Actualizar pip
echo "🔧 Actualizando pip..."
pip install --upgrade pip

# Instalar dependencias
echo "📚 Instalando dependencias..."
pip install -r requirements.txt

echo "✅ ¡Instalación completada!"
echo ""
echo "🎯 Para ejecutar el asistente:"
echo "   ./run.sh"
echo ""
echo "🎯 O manualmente:"
echo "   source .venv/bin/activate"
echo "   python main.py"
