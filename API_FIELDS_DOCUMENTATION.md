# 📊 Documentação Completa dos Campos da API SE Ranking

## 🔍 **Estrutura Completa de um Backlink**

A API da SE Ranking retorna **12 campos** para cada backlink, organizados nas seguintes categorias:

---

## 🌐 **1. INFORMAÇÕES DE URL**

### `url_from` (string)
- **Descrição**: URL de origem do backlink (página que contém o link)
- **Exemplo**: `"https://example.com/article"`
- **Uso**: Identificar a página que está linkando para o seu site

### `url_to` (string)
- **Descrição**: URL de destino do backlink (para onde o link aponta)
- **Exemplo**: `"https://meusite.com"`
- **Uso**: Confirmar para qual página específica o link está direcionando

---

## 📝 **2. CONTEÚDO E TEXTO**

### `title` (string)
- **Descrição**: Título da página de origem
- **Exemplo**: `"Como Otimizar SEO em 2024"`
- **Uso**: Entender o contexto e relevância da página que está linkando
- **Nota**: Pode estar vazio se a página não tiver título

### `anchor` (string)
- **Descrição**: Texto âncora do link (texto clicável)
- **Exemplo**: `"melhor ferramenta de SEO"`
- **Uso**: Analisar a qualidade e relevância do texto âncora
- **Nota**: Campo mais importante para SEO

### `alt` (string)
- **Descrição**: Texto alternativo (para links de imagem)
- **Exemplo**: `"Logo da empresa"`
- **Uso**: Acessibilidade e contexto para links de imagem
- **Nota**: Só é relevante quando `image: true`

---

## 🔗 **3. TIPO E ATRIBUTOS DO LINK**

### `nofollow` (boolean)
- **Descrição**: Se o link tem atributo `rel="nofollow"`
- **Valores**: `true` ou `false`
- **Uso**: Determinar se o link passa "link juice" (autoridade)
- **SEO**: Links dofollow são mais valiosos

### `image` (boolean)
- **Descrição**: Se é um link de imagem
- **Valores**: `true` ou `false`
- **Uso**: Identificar se o backlink é através de uma imagem
- **Nota**: Quando `true`, o campo `image_source` é preenchido

### `image_source` (string)
- **Descrição**: URL da imagem (quando `image: true`)
- **Exemplo**: `"https://example.com/logo.png"`
- **Uso**: Acessar a imagem que está sendo linkada
- **Nota**: Só preenchido quando `image: true`

---

## 📊 **4. MÉTRICAS DE RANK**

### `inlink_rank` (integer)
- **Descrição**: Rank do link específico
- **Valores**: Número inteiro (geralmente 0)
- **Uso**: Autoridade do link individual
- **Nota**: Na maioria dos casos é 0

### `domain_inlink_rank` (integer)
- **Descrição**: Rank do domínio de origem
- **Valores**: 0-100 (quanto maior, melhor)
- **Uso**: **MÉTRICA MAIS IMPORTANTE** - autoridade do domínio
- **SEO**: Domínios com rank alto passam mais autoridade

---

## 📅 **5. DATAS**

### `first_seen` (string)
- **Descrição**: Primeira vez que o backlink foi descoberto
- **Formato**: `"YYYY-MM-DD"`
- **Exemplo**: `"2024-01-15"`
- **Uso**: Analisar a idade e evolução dos backlinks

### `last_visited` (string)
- **Descrição**: Última vez que foi visitado/verificado
- **Formato**: `"YYYY-MM-DD"`
- **Exemplo**: `"2024-12-30"`
- **Uso**: Verificar se o backlink ainda está ativo

---

## 🎯 **CAMPOS MAIS IMPORTANTES PARA SEO**

### **1. `domain_inlink_rank`** ⭐⭐⭐
- **Por quê**: Mede a autoridade do domínio de origem
- **Uso**: Priorizar backlinks de domínios com rank alto
- **Meta**: Buscar backlinks de domínios com rank > 50

### **2. `anchor`** ⭐⭐⭐
- **Por quê**: Texto âncora é crucial para SEO
- **Uso**: Analisar relevância e qualidade do texto
- **Meta**: Textos âncora relevantes e naturais

### **3. `nofollow`** ⭐⭐
- **Por quê**: Determina se o link passa autoridade
- **Uso**: Focar em links dofollow para SEO
- **Meta**: Maximizar links dofollow

### **4. `title`** ⭐⭐
- **Por quê**: Contexto da página que está linkando
- **Uso**: Entender relevância temática
- **Meta**: Backlinks de páginas relevantes

---

## 📈 **ESTATÍSTICAS TÍPICAS**

Com base em análises reais:

- **Dofollow vs Nofollow**: ~60% dofollow, ~40% nofollow
- **Links de Imagem**: ~5-10% do total
- **Com Título**: ~80-90% das páginas
- **Com Rank de Domínio**: ~70-80% dos backlinks
- **Rank Médio**: 20-50 (varia por domínio)

---

## 🔧 **COMO USAR NA PRÁTICA**

### **Filtros Recomendados:**
1. **Rank Alto**: `domain_inlink_rank > 50`
2. **Dofollow**: `nofollow = false`
3. **Relevantes**: `title` contém palavras-chave
4. **Recentes**: `first_seen` nos últimos 6 meses

### **Métricas para Acompanhar:**
- Total de backlinks
- Percentual dofollow vs nofollow
- Rank médio dos domínios
- Evolução ao longo do tempo
- Qualidade dos textos âncora

---

## 🚀 **IMPLEMENTAÇÃO NA APLICAÇÃO**

A aplicação web já utiliza **TODOS** os campos disponíveis:

✅ **Exibição**: Todos os 12 campos são mostrados na interface
✅ **Filtros**: Por tipo, rank, data, texto âncora
✅ **Estatísticas**: Contadores e métricas avançadas
✅ **Ordenação**: Por rank, data, posição
✅ **Busca**: Por texto âncora e outros campos

---

**🎉 A API da SE Ranking fornece dados muito completos para análise de backlinks!**

