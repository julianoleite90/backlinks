# 🔧 Configuração de Variáveis de Ambiente no Vercel

## ❌ **Problema: "Sistema não configurado. Verifique a chave da API."**

Este erro acontece quando a variável de ambiente `SE_RANKING_API_TOKEN` não está configurada no Vercel.

## ✅ **Solução: Configurar Variáveis de Ambiente**

### **Método 1: Via Painel do Vercel (Recomendado)**

1. **Acesse o painel do Vercel:**
   - Vá para [vercel.com](https://vercel.com)
   - Faça login na sua conta

2. **Selecione seu projeto:**
   - Clique no projeto "backlinks"

3. **Vá para Settings:**
   - Clique na aba "Settings"
   - Clique em "Environment Variables"

4. **Adicione a variável:**
   ```
   Name: SE_RANKING_API_TOKEN
   Value: 386fa52e-64c3-0a18-b7bd-935bc9d82496
   Environment: Production, Preview, Development
   ```

5. **Salve e faça redeploy:**
   - Clique em "Save"
   - Vá para "Deployments"
   - Clique em "Redeploy" no último deploy

### **Método 2: Via Vercel CLI**

```bash
# Instalar Vercel CLI
npm i -g vercel

# Login
vercel login

# Configurar variável de ambiente
vercel env add SE_RANKING_API_TOKEN

# Quando solicitado, digite sua chave da API
# 386fa52e-64c3-0a18-b7bd-935bc9d82496

# Deploy
vercel --prod
```

## 🔍 **Verificar se Está Funcionando**

### **1. Endpoint de Debug:**
Acesse: `https://seu-projeto.vercel.app/debug`

Deve retornar:
```json
{
  "environment_variables": {
    "SE_RANKING_API_TOKEN": "***",
    "PYTHONPATH": "."
  },
  "checker_status": "OK",
  "working_directory": "/var/task",
  "files_present": {
    "app.py": true,
    "templates/index.html": true,
    "requirements.txt": true
  }
}
```

### **2. Endpoint de Health:**
Acesse: `https://seu-projeto.vercel.app/health`

Deve retornar:
```json
{
  "status": "ok",
  "api_configured": true,
  "api_token_present": true
}
```

## 🚨 **Problemas Comuns**

### **"api_token_present": false**
- ❌ Variável de ambiente não configurada
- ✅ Configure `SE_RANKING_API_TOKEN` no painel do Vercel

### **"checker_status": "ERROR"**
- ❌ Erro ao inicializar o checker
- ✅ Verifique os logs no painel do Vercel

### **404 Error**
- ❌ Estrutura de arquivos incorreta
- ✅ Verifique se `api/index.py` existe

## 📋 **Checklist de Deploy**

- [ ] Repositório conectado ao Vercel
- [ ] `vercel.json` configurado corretamente
- [ ] `api/index.py` existe
- [ ] `SE_RANKING_API_TOKEN` configurada
- [ ] Deploy realizado
- [ ] Teste no endpoint `/debug`
- [ ] Teste no endpoint `/health`
- [ ] Teste na interface principal

## 🎯 **URLs de Teste**

Após configurar tudo, teste estas URLs:

1. **Interface Principal:** `https://seu-projeto.vercel.app/`
2. **Debug:** `https://seu-projeto.vercel.app/debug`
3. **Health:** `https://seu-projeto.vercel.app/health`

---

**🎉 Após seguir estes passos, sua aplicação funcionará perfeitamente!**
