# 🔗 Backlink Checker

Uma ferramenta CLI em Python para análise de backlinks usando a API da SE Ranking.

## ✨ Funcionalidades

- 📊 **Resumo de Backlinks**: Domain Trust, total de backlinks e domínios de referência
- 🏅 **Top 10 Backlinks**: Lista dos backlinks mais fortes ordenados por Domain Rank
- 🎨 **Interface Amigável**: Saída formatada e colorida no terminal
- 🔒 **Segurança**: Chave da API armazenada em variável de ambiente
- ⚡ **Rápido**: Análise completa em segundos

## 🚀 Instalação

### 1. Clone ou baixe o projeto
```bash
git clone <seu-repositorio>
cd backlinks
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Configure sua chave da API

#### Obter a chave da API:
1. Acesse sua conta na [SE Ranking](https://seranking.com)
2. No menu superior direito, clique em **API**
3. Copie seu **API Token**

#### Configurar o ambiente:
1. Copie o arquivo de exemplo:
   ```bash
   cp env.example .env
   ```

2. Edite o arquivo `.env` e adicione sua chave:
   ```
   SE_RANKING_API_TOKEN=sua_chave_api_aqui
   ```

## 📖 Como Usar

### Uso Básico
```bash
python backlink_checker.py google.com
```

### Exemplos
```bash
# Analisar o site da Google
python backlink_checker.py google.com

# Analisar o site da Moz
python backlink_checker.py moz.com

# Analisar o site da SE Ranking
python backlink_checker.py seranking.com
```

### Ajuda
```bash
python backlink_checker.py --help
```

## 📋 Exemplo de Saída

```
🚀 Iniciando análise de backlinks...
==================================================
🔍 Analisando o domínio: google.com
⏳ Buscando dados de resumo...
⏳ Buscando lista de backlinks...

==================================================
📊 RESUMO DOS BACKLINKS
==================================================
🌐 Domínio Analisado: google.com
🏆 Domain Trust: 95
🔗 Total de Backlinks: 15.700.000
🌍 Total de Domínios de Referência: 68.200

==================================================
🏅 TOP 10 BACKLINKS POR DOMAIN RANK
==================================================
 1. Origem: https://www.example.com/article
    Âncora: "melhor ferramenta de seo" | Rank: 92 | Tipo: ✅ Dofollow

 2. Origem: https://www.anotherblog.org/post
    Âncora: "SE Ranking review" | Rank: 90 | Tipo: ✅ Dofollow

 3. Origem: https://www.techblog.net/news
    Âncora: "ferramentas de marketing digital" | Rank: 88 | Tipo: 🔒 Nofollow

...

==================================================
✅ Análise concluída com sucesso!
==================================================
```

## 🛠️ Tecnologias Utilizadas

- **Python 3.7+**
- **requests**: Para chamadas HTTP à API
- **python-dotenv**: Para gerenciamento de variáveis de ambiente
- **argparse**: Para interface de linha de comando

## 🔧 Estrutura do Projeto

```
backlinks/
├── backlink_checker.py    # Script principal
├── requirements.txt       # Dependências Python
├── env.example           # Exemplo de configuração
├── .env                  # Suas configurações (não versionado)
└── README.md             # Este arquivo
```

## 🚨 Tratamento de Erros

O script inclui tratamento robusto para:
- ❌ Chave da API inválida ou ausente
- ❌ Domínio não encontrado
- ❌ Problemas de conectividade
- ❌ Respostas inválidas da API
- ❌ Timeouts de requisição

## 📝 Notas Importantes

- A chave da API deve ter permissões para acessar os endpoints de backlinks
- O arquivo `.env` não deve ser versionado por segurança
- O script funciona com domínios com ou sem protocolo (http/https)
- Os dados são obtidos em tempo real da API da SE Ranking

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 🆘 Suporte

Se encontrar algum problema:

1. Verifique se sua chave da API está correta
2. Confirme se o domínio existe e está acessível
3. Verifique sua conexão com a internet
4. Abra uma issue no repositório

---

**Desenvolvido com ❤️ para análise eficiente de backlinks**

