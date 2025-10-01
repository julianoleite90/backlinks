#!/usr/bin/env python3
"""
Backlink Checker - Ferramenta CLI para análise de backlinks usando SE Ranking API
Autor: Assistente de Programação
Versão: 1.0.0
"""

import argparse
import os
import sys
import requests
from dotenv import load_dotenv
from typing import Dict, List, Optional, Tuple
import json
from datetime import datetime


class BacklinkChecker:
    """Classe principal para análise de backlinks usando SE Ranking API"""
    
    def __init__(self):
        """Inicializa o checker e carrega configurações"""
        load_dotenv()
        self.api_token = os.getenv('SE_RANKING_API_TOKEN')
        self.base_url = "https://api.seranking.com"
        self.session = requests.Session()
        
        if not self.api_token:
            print("❌ ERRO: Chave da API não encontrada!")
            print("💡 Dica: Crie um arquivo .env com SE_RANKING_API_TOKEN=sua_chave_aqui")
            sys.exit(1)
    
    def _make_request(self, endpoint: str, params: Dict) -> Optional[Dict]:
        """Faz uma requisição para a API da SE Ranking"""
        url = f"{self.base_url}{endpoint}"
        
        # Adiciona a chave da API como parâmetro para a API v1
        params['apiKey'] = self.api_token
        
        try:
            response = self.session.get(url, params=params, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"❌ Erro na requisição: {e}")
            return None
        except json.JSONDecodeError as e:
            print(f"❌ Erro ao decodificar resposta JSON: {e}")
            return None
    
    def get_backlinks_summary(self, domain: str) -> Optional[Dict]:
        """Obtém resumo dos backlinks de um domínio"""
        print(f"🔍 Analisando o domínio: {domain}")
        print("⏳ Buscando dados de resumo...")
        
        params = {
            'target': domain,
            'mode': 'domain',
            'limit': 100,
            'output': 'json'
        }
        
        return self._make_request('/v1/backlinks/raw', params)
    
    def get_backlinks_list(self, domain: str, limit: int = 10) -> Optional[Dict]:
        """Obtém lista de backlinks de um domínio"""
        print("⏳ Buscando lista de backlinks...")
        
        params = {
            'target': domain,
            'mode': 'domain',
            'limit': limit,
            'output': 'json'
        }
        
        return self._make_request('/v1/backlinks/raw', params)
    
    def format_number(self, number: int) -> str:
        """Formata números com separadores de milhares"""
        return f"{number:,}".replace(',', '.')
    
    def display_summary(self, domain: str, backlinks_data: Dict):
        """Exibe resumo dos backlinks de forma formatada"""
        print("\n" + "="*50)
        print("📊 RESUMO DOS BACKLINKS")
        print("="*50)
        
        # Extrai dados dos backlinks
        backlinks = backlinks_data.get('backlinks', [])
        total_backlinks = len(backlinks)
        
        # Conta domínios únicos
        unique_domains = set()
        for backlink in backlinks:
            url_from = backlink.get('url_from', '')
            if url_from:
                try:
                    from urllib.parse import urlparse
                    domain_name = urlparse(url_from).netloc
                    if domain_name:
                        unique_domains.add(domain_name)
                except:
                    pass
        
        total_referring_domains = len(unique_domains)
        
        print(f"🌐 Domínio Analisado: {domain}")
        print(f"🔗 Total de Backlinks: {self.format_number(total_backlinks)}")
        print(f"🌍 Total de Domínios de Referência: {self.format_number(total_referring_domains)}")
    
    def display_backlinks_list(self, backlinks_data: Dict):
        """Exibe lista de backlinks de forma formatada"""
        print("\n" + "="*50)
        print("🏅 TOP 10 BACKLINKS ENCONTRADOS")
        print("="*50)
        
        backlinks = backlinks_data.get('backlinks', [])
        
        if not backlinks:
            print("❌ Nenhum backlink encontrado para este domínio.")
            return
        
        for i, backlink in enumerate(backlinks[:10], 1):
            source_url = backlink.get('url_from', 'N/A')
            target_url = backlink.get('url_to', 'N/A')
            anchor_text = backlink.get('anchor', 'N/A')
            nofollow = backlink.get('nofollow', False)
            first_seen = backlink.get('first_seen', 'N/A')
            
            # Formata o tipo de link
            type_emoji = "🔒" if nofollow else "✅"
            type_text = "Nofollow" if nofollow else "Dofollow"
            
            # Trunca URLs muito longas
            if len(source_url) > 60:
                source_url = source_url[:57] + "..."
            
            # Trunca texto âncora muito longo
            if len(anchor_text) > 40:
                anchor_text = anchor_text[:37] + "..."
            
            print(f"{i:2d}. Origem: {source_url}")
            print(f"    Destino: {target_url}")
            print(f"    Âncora: \"{anchor_text}\" | Tipo: {type_emoji} {type_text}")
            print(f"    Primeira vez visto: {first_seen}")
            print()
    
    def check_domain(self, domain: str):
        """Executa análise completa de um domínio"""
        print("🚀 Iniciando análise de backlinks...")
        print("="*50)
        
        # Remove protocolo se presente
        domain = domain.replace('http://', '').replace('https://', '').replace('www.', '')
        
        # Obtém dados dos backlinks
        backlinks_data = self.get_backlinks_summary(domain)
        if not backlinks_data:
            print("❌ Falha ao obter dados dos backlinks.")
            return
        
        # Exibe resumo
        self.display_summary(domain, backlinks_data)
        
        # Exibe lista de backlinks
        self.display_backlinks_list(backlinks_data)
        
        print("="*50)
        print("✅ Análise concluída com sucesso!")
        print("="*50)


def main():
    """Função principal do programa"""
    parser = argparse.ArgumentParser(
        description="Backlink Checker - Analise backlinks usando SE Ranking API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos de uso:
  python backlink_checker.py google.com
  python backlink_checker.py moz.com
  python backlink_checker.py seranking.com

Configuração:
  1. Crie um arquivo .env na pasta do projeto
  2. Adicione: SE_RANKING_API_TOKEN=sua_chave_aqui
  3. Instale dependências: pip install -r requirements.txt
        """
    )
    
    parser.add_argument(
        'domain',
        help='Domínio para análise (ex: google.com)'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='Backlink Checker v1.0.0'
    )
    
    args = parser.parse_args()
    
    # Cria e executa o checker
    checker = BacklinkChecker()
    checker.check_domain(args.domain)


if __name__ == "__main__":
    main()
