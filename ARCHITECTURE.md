# 🏗️ Arquitetura do Backlink Checker

## 📊 Fluxo de Funcionamento

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Usuário       │    │  Backlink        │    │  SE Ranking     │
│   (CLI)         │    │  Checker         │    │  API            │
└─────────────────┘    └──────────────────┘    └─────────────────┘
         │                        │                        │
         │ 1. python backlink_    │                        │
         │    checker.py domain   │                        │
         ├───────────────────────►│                        │
         │                        │                        │
         │                        │ 2. GET /v2/backlinks/  │
         │                        │    backlinks_summary   │
         │                        ├───────────────────────►│
         │                        │                        │
         │                        │ 3. Resposta com        │
         │                        │    resumo dos dados    │
         │                        │◄───────────────────────┤
         │                        │                        │
         │ 4. Exibe resumo        │                        │
         │    formatado           │                        │
         │◄───────────────────────┤                        │
         │                        │                        │
         │                        │ 5. GET /v2/backlinks/  │
         │                        │    backlinks_list      │
         │                        ├───────────────────────►│
         │                        │                        │
         │                        │ 6. Resposta com        │
         │                        │    lista de backlinks  │
         │                        │◄───────────────────────┤
         │                        │                        │
         │ 7. Exibe top 10        │                        │
         │    backlinks           │                        │
         │◄───────────────────────┤                        │
```

## 🔧 Componentes do Sistema

### 📁 Estrutura de Arquivos
```
backlinks/
├── backlink_checker.py    # 🎯 Script principal
├── setup.py              # ⚙️  Configuração automática
├── test_example.py       # 🧪 Script de teste
├── run_examples.sh       # 🚀 Execução interativa
├── requirements.txt      # 📦 Dependências Python
├── env.example          # 🔑 Exemplo de configuração
├── README.md            # 📚 Documentação completa
├── QUICKSTART.md        # ⚡ Guia rápido
└── ARCHITECTURE.md      # 🏗️ Este arquivo
```

### 🐍 Classes e Funções Principais

#### `BacklinkChecker` (Classe Principal)
- **`__init__()`**: Inicializa configurações e valida API token
- **`_make_request()`**: Faz requisições HTTP para a API
- **`get_backlinks_summary()`**: Obtém resumo dos backlinks
- **`get_backlinks_list()`**: Obtém lista detalhada de backlinks
- **`display_summary()`**: Formata e exibe resumo
- **`display_backlinks_list()`**: Formata e exibe lista
- **`check_domain()`**: Orquestra análise completa

#### Funções Auxiliares
- **`format_number()`**: Formata números com separadores
- **`main()`**: Ponto de entrada do programa

## 🔄 Fluxo de Dados

### 1. **Entrada**
- Domínio via argumento CLI
- Chave da API via variável de ambiente

### 2. **Processamento**
- Validação da chave da API
- Limpeza do domínio (remove protocolo/www)
- Chamadas sequenciais à API:
  - Resumo de backlinks
  - Lista de backlinks (top 10)

### 3. **Saída**
- Resumo formatado com emojis
- Tabela de backlinks ordenada por Domain Rank
- Tratamento de erros amigável

## 🛡️ Segurança

- ✅ Chave da API em variável de ambiente
- ✅ Arquivo `.env` não versionado
- ✅ Validação de entrada
- ✅ Tratamento de erros robusto
- ✅ Timeout de requisições

## 🚀 Performance

- ⚡ Requisições paralelas quando possível
- ⚡ Cache de sessão HTTP
- ⚡ Timeout configurável (30s)
- ⚡ Formatação otimizada de saída

## 🔌 Integração com API

### Endpoints Utilizados
1. **`/v2/backlinks/backlinks_summary`**
   - Método: GET
   - Parâmetros: domain, date_from, date_to
   - Retorna: Domain Trust, total de backlinks, domínios de referência

2. **`/v2/backlinks/backlinks_list`**
   - Método: GET
   - Parâmetros: domain, date_from, date_to, limit, order_by, order_direction
   - Retorna: Lista de backlinks com detalhes

### Autenticação
- Bearer Token via header `Authorization`
- Token obtido de variável de ambiente `SE_RANKING_API_TOKEN`

## 🎨 Interface do Usuário

### Características
- 🎨 Emojis para melhor visualização
- 📊 Formatação clara e organizada
- 🔢 Números formatados com separadores
- 📋 Tabelas bem estruturadas
- ⚠️ Mensagens de erro amigáveis

### Exemplo de Saída
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
```

## 🔧 Extensibilidade

O sistema foi projetado para ser facilmente extensível:

- ➕ Novos endpoints da API
- ➕ Novos formatos de saída
- ➕ Filtros adicionais
- ➕ Métricas personalizadas
- ➕ Exportação de dados

---

**Desenvolvido com foco em simplicidade, segurança e usabilidade** 🚀

