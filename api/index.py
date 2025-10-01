#!/usr/bin/env python3
"""
Vercel API endpoint for Backlink Checker Pro
"""

import sys
import os

# Adiciona o diretório pai ao path para importar o app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

# Para o Vercel
if __name__ == "__main__":
    app.run()
