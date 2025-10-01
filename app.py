#!/usr/bin/env python3
"""
Backlink Checker Web App - Interface web para análise de backlinks
"""

from flask import Flask, render_template, request, jsonify
import os
import requests
from dotenv import load_dotenv
from urllib.parse import urlparse
import json

# Carrega variáveis de ambiente
load_dotenv()

app = Flask(__name__)

class BacklinkChecker:
    """Classe para análise de backlinks usando SE Ranking API"""
    
    def __init__(self):
        self.api_token = os.getenv('SE_RANKING_API_TOKEN')
        self.base_url = "https://api.seranking.com"
        self.session = requests.Session()
        
        if not self.api_token:
            raise ValueError("Chave da API não encontrada!")
    
    def _make_request(self, endpoint: str, params: dict) -> dict:
        """Faz uma requisição para a API da SE Ranking"""
        url = f"{self.base_url}{endpoint}"
        params['apiKey'] = self.api_token
        
        try:
            response = self.session.get(url, params=params, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Erro na requisição: {e}")
        except json.JSONDecodeError as e:
            raise Exception(f"Erro ao decodificar resposta JSON: {e}")
    
    def get_backlinks(self, domain: str, limit: int = 1000) -> dict:
        """Obtém backlinks de um domínio"""
        # Remove protocolo se presente
        domain = domain.replace('http://', '').replace('https://', '').replace('www.', '')
        
        params = {
            'target': domain,
            'mode': 'domain',
            'limit': limit,
            'output': 'json'
        }
        
        return self._make_request('/v1/backlinks/raw', params)
    
    def analyze_domain(self, domain: str) -> dict:
        """Analisa um domínio e retorna dados formatados"""
        try:
            # Obtém dados dos backlinks
            backlinks_data = self.get_backlinks(domain)
            backlinks = backlinks_data.get('backlinks', [])
            
            # Conta domínios únicos
            unique_domains = set()
            dofollow_count = 0
            nofollow_count = 0
            image_links = 0
            total_domain_rank = 0
            domain_ranks = []
            
            for backlink in backlinks:
                url_from = backlink.get('url_from', '')
                if url_from:
                    try:
                        domain_name = urlparse(url_from).netloc
                        if domain_name:
                            unique_domains.add(domain_name)
                    except:
                        pass
                
                # Conta tipos de links
                if backlink.get('nofollow', False):
                    nofollow_count += 1
                else:
                    dofollow_count += 1
                
                # Conta links de imagem
                if backlink.get('image', False):
                    image_links += 1
                
                # Coleta ranks de domínio
                domain_rank = backlink.get('domain_inlink_rank', 0)
                if domain_rank > 0:
                    domain_ranks.append(domain_rank)
                    total_domain_rank += domain_rank
            
            # Calcula estatísticas
            avg_domain_rank = total_domain_rank / len(domain_ranks) if domain_ranks else 0
            max_domain_rank = max(domain_ranks) if domain_ranks else 0
            min_domain_rank = min(domain_ranks) if domain_ranks else 0
            
            # Formata dados para exibição (TODOS os backlinks)
            formatted_backlinks = []
            for i, backlink in enumerate(backlinks, 1):
                formatted_backlinks.append({
                    'position': i,
                    'source_url': backlink.get('url_from', 'N/A'),
                    'target_url': backlink.get('url_to', 'N/A'),
                    'title': backlink.get('title', 'N/A'),
                    'anchor_text': backlink.get('anchor', 'N/A'),
                    'alt_text': backlink.get('alt', 'N/A'),
                    'is_nofollow': backlink.get('nofollow', False),
                    'is_image': backlink.get('image', False),
                    'image_source': backlink.get('image_source', ''),
                    'inlink_rank': backlink.get('inlink_rank', 0),
                    'domain_inlink_rank': backlink.get('domain_inlink_rank', 0),
                    'first_seen': backlink.get('first_seen', 'N/A'),
                    'last_visited': backlink.get('last_visited', 'N/A')
                })
            
            return {
                'success': True,
                'domain': domain,
                'total_backlinks': len(backlinks),
                'total_referring_domains': len(unique_domains),
                'dofollow_count': dofollow_count,
                'nofollow_count': nofollow_count,
                'image_links': image_links,
                'avg_domain_rank': round(avg_domain_rank, 2),
                'max_domain_rank': max_domain_rank,
                'min_domain_rank': min_domain_rank,
                'all_backlinks': formatted_backlinks,
                'has_more': 'next' in backlinks_data
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }

# Inicializa o checker (será criado quando necessário)
checker = None

def get_checker():
    """Obtém ou cria uma instância do checker"""
    global checker
    if checker is None:
        try:
            # Verifica se a variável de ambiente existe
            api_token = os.getenv('SE_RANKING_API_TOKEN')
            if not api_token:
                print("❌ SE_RANKING_API_TOKEN não encontrada nas variáveis de ambiente")
                return None
            
            checker = BacklinkChecker()
            print("✅ BacklinkChecker inicializado com sucesso")
        except Exception as e:
            print(f"❌ Erro ao inicializar BacklinkChecker: {e}")
            return None
    return checker

@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    """Endpoint para análise de backlinks"""
    current_checker = get_checker()
    if not current_checker:
        return jsonify({
            'success': False,
            'error': 'Sistema não configurado. Verifique a chave da API.'
        })
    
    data = request.get_json()
    domain = data.get('domain', '').strip()
    
    if not domain:
        return jsonify({
            'success': False,
            'error': 'Domínio é obrigatório'
        })
    
    # Analisa o domínio
    result = current_checker.analyze_domain(domain)
    return jsonify(result)

@app.route('/health')
def health():
    """Endpoint de saúde da aplicação"""
    current_checker = get_checker()
    return jsonify({
        'status': 'ok',
        'api_configured': current_checker is not None,
        'api_token_present': bool(os.getenv('SE_RANKING_API_TOKEN'))
    })

@app.route('/debug')
def debug():
    """Endpoint de debug para verificar configuração"""
    return jsonify({
        'environment_variables': {
            'SE_RANKING_API_TOKEN': '***' if os.getenv('SE_RANKING_API_TOKEN') else 'NOT_SET',
            'PYTHONPATH': os.getenv('PYTHONPATH', 'NOT_SET')
        },
        'checker_status': 'OK' if get_checker() else 'ERROR',
        'working_directory': os.getcwd(),
        'files_present': {
            'app.py': os.path.exists('app.py'),
            'templates/index.html': os.path.exists('templates/index.html'),
            'requirements.txt': os.path.exists('requirements.txt')
        }
    })

# Para desenvolvimento local
if __name__ == '__main__':
    print("🚀 Iniciando Backlink Checker Web App...")
    print("🌐 Acesse: http://localhost:9999")
    print("="*50)
    app.run(debug=True, host='0.0.0.0', port=9999)

# Para produção no Vercel
if __name__ == '__main__':
    app.run()
