#!/usr/bin/env python3
"""
Script de demonstração da aplicação web Backlink Checker Pro
"""

import requests
import json
import time

def test_web_app():
    """Testa a aplicação web com diferentes domínios"""
    
    print("🚀 BACKLINK CHECKER PRO - DEMONSTRAÇÃO WEB")
    print("="*60)
    
    # URL da aplicação
    base_url = "http://localhost:9999"
    
    # Testa se a aplicação está rodando
    try:
        response = requests.get(f"{base_url}/health", timeout=5)
        if response.status_code == 200:
            print("✅ Aplicação web está rodando!")
            print(f"🌐 Acesse: {base_url}")
        else:
            print("❌ Aplicação não está respondendo corretamente")
            return
    except requests.exceptions.RequestException:
        print("❌ Aplicação web não está rodando!")
        print("💡 Execute: python app.py")
        return
    
    print("\n" + "="*60)
    print("📊 TESTANDO ANÁLISE DE BACKLINKS")
    print("="*60)
    
    # Lista de domínios para testar
    test_domains = [
        "google.com",
        "moz.com", 
        "seranking.com"
    ]
    
    for domain in test_domains:
        print(f"\n🔍 Testando domínio: {domain}")
        print("-" * 40)
        
        try:
            # Faz a análise
            response = requests.post(
                f"{base_url}/analyze",
                json={"domain": domain},
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                
                if data.get('success'):
                    print(f"✅ Análise concluída com sucesso!")
                    print(f"📊 Total de backlinks: {data.get('total_backlinks', 0):,}")
                    print(f"🌍 Domínios de referência: {data.get('total_referring_domains', 0):,}")
                    print(f"✅ Dofollow: {data.get('dofollow_count', 0):,}")
                    print(f"🔒 Nofollow: {data.get('nofollow_count', 0):,}")
                    print(f"🖼️ Links de imagem: {data.get('image_links', 0):,}")
                    print(f"📈 Rank médio do domínio: {data.get('avg_domain_rank', 0)}")
                    print(f"🏆 Rank máximo: {data.get('max_domain_rank', 0)}")
                else:
                    print(f"❌ Erro: {data.get('error', 'Erro desconhecido')}")
            else:
                print(f"❌ Erro HTTP: {response.status_code}")
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Erro de conexão: {e}")
        
        time.sleep(1)  # Pausa entre testes
    
    print("\n" + "="*60)
    print("🎉 DEMONSTRAÇÃO CONCLUÍDA!")
    print("="*60)
    print("🌐 Acesse a interface web em: http://localhost:9999")
    print("✨ Funcionalidades disponíveis:")
    print("   • Análise completa de backlinks")
    print("   • Filtros por tipo (dofollow/nofollow/imagem)")
    print("   • Ordenação por rank e data")
    print("   • Busca por texto âncora")
    print("   • Paginação para navegar todos os resultados")
    print("   • Estatísticas detalhadas")
    print("   • Interface responsiva e moderna")

if __name__ == "__main__":
    test_web_app()

