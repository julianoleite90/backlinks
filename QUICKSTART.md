# 🚀 Quick Start - Backlink Checker

## ⚡ Configuração Rápida (3 passos)

### 1️⃣ Instalar e Configurar
```bash
# Instalar dependências
pip install -r requirements.txt

# Configurar automaticamente
python setup.py
```

### 2️⃣ Adicionar sua Chave da API
Edite o arquivo `.env` e adicione sua chave:
```
SE_RANKING_API_TOKEN=sua_chave_aqui
```

**Como obter a chave:**
1. Acesse [SE Ranking](https://seranking.com)
2. Menu superior direito → **API**
3. Copie seu **API Token**

### 3️⃣ Executar
```bash
# Análise básica
python backlink_checker.py google.com

# Ou use o script interativo
./run_examples.sh
```

## 🎯 Exemplos Rápidos

```bash
# Sites populares para teste
python backlink_checker.py google.com
python backlink_checker.py moz.com
python backlink_checker.py seranking.com
python backlink_checker.py ahrefs.com
```

## 🔧 Solução de Problemas

| Problema | Solução |
|----------|---------|
| `❌ Chave da API não encontrada` | Verifique se o arquivo `.env` existe e tem a chave correta |
| `❌ Erro na requisição` | Verifique sua conexão com a internet |
| `❌ Domínio não encontrado` | Tente sem `www` ou `https://` |
| `❌ Timeout` | A API pode estar lenta, tente novamente |

## 📚 Mais Informações

- **README completo**: `README.md`
- **Teste automatizado**: `python test_example.py`
- **Configuração manual**: `env.example`

---

**🎉 Pronto! Seu Backlink Checker está funcionando!**

