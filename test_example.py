#!/usr/bin/env python3
"""
Script de exemplo para testar o Backlink Checker
Execute este script para ver como o backlink_checker.py funciona
"""

import subprocess
import sys
import os

def test_backlink_checker():
    """Testa o backlink checker com um domínio de exemplo"""
    
    print("🧪 TESTE DO BACKLINK CHECKER")
    print("="*50)
    
    # Verifica se o arquivo principal existe
    if not os.path.exists('backlink_checker.py'):
        print("❌ Arquivo backlink_checker.py não encontrado!")
        return False
    
    # Verifica se o arquivo .env existe
    if not os.path.exists('.env'):
        print("⚠️  Arquivo .env não encontrado!")
        print("💡 Crie um arquivo .env com sua chave da API:")
        print("   SE_RANKING_API_TOKEN=sua_chave_aqui")
        return False
    
    # Domínio de teste
    test_domain = "google.com"
    
    print(f"🔍 Testando com domínio: {test_domain}")
    print("⏳ Executando análise...")
    print()
    
    try:
        # Executa o backlink checker
        result = subprocess.run([
            sys.executable, 'backlink_checker.py', test_domain
        ], capture_output=True, text=True, timeout=60)
        
        # Exibe a saída
        if result.stdout:
            print("📤 SAÍDA:")
            print(result.stdout)
        
        if result.stderr:
            print("⚠️  ERROS:")
            print(result.stderr)
        
        if result.returncode == 0:
            print("✅ Teste executado com sucesso!")
            return True
        else:
            print(f"❌ Teste falhou com código de saída: {result.returncode}")
            return False
            
    except subprocess.TimeoutExpired:
        print("⏰ Teste expirou (timeout de 60 segundos)")
        return False
    except Exception as e:
        print(f"❌ Erro durante o teste: {e}")
        return False

def show_usage_examples():
    """Mostra exemplos de uso do backlink checker"""
    
    print("\n📚 EXEMPLOS DE USO:")
    print("="*50)
    
    examples = [
        "python backlink_checker.py google.com",
        "python backlink_checker.py moz.com", 
        "python backlink_checker.py seranking.com",
        "python backlink_checker.py --help"
    ]
    
    for i, example in enumerate(examples, 1):
        print(f"{i}. {example}")
    
    print("\n💡 DICAS:")
    print("- O domínio pode ser com ou sem 'www'")
    print("- O script remove automaticamente 'http://' e 'https://'")
    print("- Use --help para ver todas as opções disponíveis")

if __name__ == "__main__":
    print("🚀 BACKLINK CHECKER - SCRIPT DE TESTE")
    print("="*50)
    
    # Executa o teste
    success = test_backlink_checker()
    
    # Mostra exemplos de uso
    show_usage_examples()
    
    print("\n" + "="*50)
    if success:
        print("🎉 Tudo funcionando perfeitamente!")
    else:
        print("🔧 Verifique a configuração e tente novamente")
    print("="*50)

