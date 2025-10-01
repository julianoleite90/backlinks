# 🚀 Deploy no Vercel - Backlink Checker Pro

## 📋 **Passos para Deploy**

### 1. **Preparar o Repositório**
```bash
# Clone o repositório
git clone https://github.com/julianoleite90/backlinks.git
cd backlinks

# Instalar Vercel CLI
npm i -g vercel
```

### 2. **Configurar Variáveis de Ambiente**
No painel do Vercel, adicione as variáveis de ambiente:
- `SE_RANKING_API_TOKEN` = sua_chave_da_api_aqui

### 3. **Deploy via CLI**
```bash
# Login no Vercel
vercel login

# Deploy
vercel

# Para produção
vercel --prod
```

### 4. **Deploy via GitHub (Recomendado)**
1. Conecte o repositório GitHub ao Vercel
2. Configure as variáveis de ambiente
3. Deploy automático a cada push

## 🔧 **Arquivos de Configuração**

### `vercel.json`
```json
{
  "version": 2,
  "builds": [
    {
      "src": "api/index.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "api/index.py"
    }
  ],
  "env": {
    "PYTHONPATH": "."
  }
}
```

### `api/index.py`
- Entry point para o Vercel
- Importa o app Flask principal

## ⚠️ **Problemas Comuns e Soluções**

### **404 Error**
- ✅ Verifique se `api/index.py` existe
- ✅ Confirme se `vercel.json` está correto
- ✅ Verifique se as rotas estão configuradas

### **500 Error**
- ✅ Verifique as variáveis de ambiente
- ✅ Confirme se `SE_RANKING_API_TOKEN` está configurada
- ✅ Verifique os logs no painel do Vercel

### **Import Error**
- ✅ Confirme se `PYTHONPATH` está configurado
- ✅ Verifique se todos os arquivos estão no repositório

## 🌐 **URLs de Acesso**

Após o deploy, sua aplicação estará disponível em:
- **Desenvolvimento**: `https://seu-projeto.vercel.app`
- **Produção**: `https://seu-projeto.vercel.app`

## 📊 **Monitoramento**

- Acesse o painel do Vercel para ver logs
- Monitore performance e erros
- Configure alertas se necessário

## 🔄 **Atualizações**

Para atualizar a aplicação:
```bash
git add .
git commit -m "Atualização"
git push origin main
# Deploy automático via GitHub
```

---

**🎉 Sua aplicação estará online e funcionando!**
