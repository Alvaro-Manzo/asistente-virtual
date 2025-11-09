#!/bin/bash

# 🤖 Script para ejecutar el Asistente Virtual Jorge

# Verificar si existe el entorno virtual
if [ ! -d ".venv" ]; then
    echo "❌ Entorno virtual no encontrado."
    echo "🔧 Ejecuta primero: ./install.sh"
    exit 1
fi

# Activar entorno virtual y ejecutar
echo "🚀 Iniciando Asistente Virtual Jorge..."
source .venv/bin/activate
python main.py
