#!/bin/bash

# Script de exemplo para executar o Backlink Checker
# Facilita o teste com diferentes domínios

echo "🚀 BACKLINK CHECKER - EXEMPLOS DE EXECUÇÃO"
echo "=========================================="

# Verifica se o Python está disponível
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 não encontrado!"
    exit 1
fi

# Verifica se o arquivo principal existe
if [ ! -f "backlink_checker.py" ]; then
    echo "❌ Arquivo backlink_checker.py não encontrado!"
    exit 1
fi

# Verifica se o arquivo .env existe
if [ ! -f ".env" ]; then
    echo "⚠️  Arquivo .env não encontrado!"
    echo "💡 Execute: python setup.py"
    exit 1
fi

echo "✅ Ambiente configurado corretamente!"
echo ""

# Lista de domínios para teste
domains=(
    "google.com"
    "moz.com"
    "seranking.com"
    "ahrefs.com"
    "semrush.com"
)

echo "📋 Domínios disponíveis para teste:"
for i in "${!domains[@]}"; do
    echo "  $((i+1)). ${domains[$i]}"
done

echo ""
echo "🎯 Escolha uma opção:"
echo "1-${#domains[@]}. Analisar um domínio específico"
echo "0. Sair"
echo ""

read -p "Digite sua escolha: " choice

# Valida a escolha
if [[ "$choice" =~ ^[0-9]+$ ]] && [ "$choice" -ge 0 ] && [ "$choice" -le "${#domains[@]}" ]; then
    if [ "$choice" -eq 0 ]; then
        echo "👋 Até logo!"
        exit 0
    else
        selected_domain="${domains[$((choice-1))]}"
        echo ""
        echo "🔍 Analisando: $selected_domain"
        echo "=========================================="
        python3 backlink_checker.py "$selected_domain"
    fi
else
    echo "❌ Opção inválida!"
    exit 1
fi

