#!/usr/bin/env python3
"""
Script de configuração para o Backlink Checker
Facilita a instalação e configuração inicial
"""

import os
import subprocess
import sys
from pathlib import Path

def install_dependencies():
    """Instala as dependências necessárias"""
    print("📦 Instalando dependências...")
    
    try:
        subprocess.check_call([
            sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'
        ])
        print("✅ Dependências instaladas com sucesso!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao instalar dependências: {e}")
        return False

def create_env_file():
    """Cria o arquivo .env se não existir"""
    env_file = Path('.env')
    
    if env_file.exists():
        print("✅ Arquivo .env já existe!")
        return True
    
    print("📝 Criando arquivo .env...")
    
    # Copia do arquivo de exemplo
    try:
        with open('env.example', 'r') as src:
            content = src.read()
        
        with open('.env', 'w') as dst:
            dst.write(content)
        
        print("✅ Arquivo .env criado!")
        print("⚠️  IMPORTANTE: Edite o arquivo .env e adicione sua chave da API!")
        return True
        
    except FileNotFoundError:
        print("❌ Arquivo env.example não encontrado!")
        return False
    except Exception as e:
        print(f"❌ Erro ao criar arquivo .env: {e}")
        return False

def make_executable():
    """Torna o script principal executável"""
    script_file = Path('backlink_checker.py')
    
    if not script_file.exists():
        print("❌ Arquivo backlink_checker.py não encontrado!")
        return False
    
    try:
        # No Windows, não precisamos fazer isso
        if os.name != 'nt':
            os.chmod(script_file, 0o755)
            print("✅ Script principal configurado como executável!")
        else:
            print("✅ Script principal pronto para uso!")
        return True
    except Exception as e:
        print(f"⚠️  Aviso: Não foi possível tornar o script executável: {e}")
        return True  # Não é crítico

def show_next_steps():
    """Mostra os próximos passos para o usuário"""
    print("\n🎯 PRÓXIMOS PASSOS:")
    print("="*50)
    print("1. 📝 Edite o arquivo .env e adicione sua chave da API da SE Ranking")
    print("2. 🔑 Obtenha sua chave em: https://seranking.com (menu API)")
    print("3. 🚀 Execute: python backlink_checker.py google.com")
    print("4. 📚 Leia o README.md para mais informações")
    print("\n💡 Exemplo de configuração no .env:")
    print("   SE_RANKING_API_TOKEN=sua_chave_aqui")

def main():
    """Função principal de configuração"""
    print("🚀 BACKLINK CHECKER - CONFIGURAÇÃO INICIAL")
    print("="*50)
    
    # Lista de tarefas
    tasks = [
        ("Instalando dependências", install_dependencies),
        ("Criando arquivo de configuração", create_env_file),
        ("Configurando script principal", make_executable),
    ]
    
    # Executa as tarefas
    success_count = 0
    for task_name, task_func in tasks:
        print(f"\n🔧 {task_name}...")
        if task_func():
            success_count += 1
        else:
            print(f"❌ Falha em: {task_name}")
    
    # Resultado final
    print("\n" + "="*50)
    if success_count == len(tasks):
        print("🎉 Configuração concluída com sucesso!")
        show_next_steps()
    else:
        print("⚠️  Configuração parcialmente concluída.")
        print("🔧 Verifique os erros acima e execute novamente se necessário.")
    print("="*50)

if __name__ == "__main__":
    main()

