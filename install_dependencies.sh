#!/bin/bash
# Script de instalação das dependências para todos os chatbots
# Autor: André Kroetz Berger

echo "======================================================"
echo "INSTALAÇÃO DAS DEPENDÊNCIAS - PROJETO CHATBOTS"
echo "======================================================"

echo ""
echo "Instalando dependências principais..."
pip install chatterbot==1.0.8
pip install chatterbot-corpus==1.2.0
pip install nltk==3.8.1
pip install PyYAML==6.0.1

echo ""
echo "Instalando dependências para dataset e LLM..."
pip install transformers==4.36.0
pip install datasets==2.14.0
pip install torch==2.1.0
pip install accelerate==0.24.0
pip install tokenizers==0.15.0
pip install numpy==1.24.3

echo ""
echo "======================================================"
echo "INSTALAÇÃO CONCLUÍDA!"
echo "======================================================"
echo ""
echo "Para executar os chatbots:"
echo "- FAQ: python chatbot_faq/chatbot_faq.py"
echo "- Corpora: python chatbot_corpora/chatbot_corpora.py"
echo "- Dataset: python chatbot_dataset/chatbot_dataset.py"
echo "- LLM Conservador: python chatbot_llm/llm_conservative.py"
echo "- LLM Criativo: python chatbot_llm/llm_creative.py"
echo "- Comparação LLM: python chatbot_llm/llm_comparison.py"
echo ""
