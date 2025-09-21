#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Teste do Chatbot FAQ - Manutenção de Notebooks
Autor: André Kroetz Berger
Script para testar a compreensão do chatbot
"""

import os
import sys

# Adiciona o diretório do projeto ao path
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_dir)

from chatbot_faq.chatbot_faq import NotebookMaintenanceFAQ

def test_chatbot_understanding():
    """Testa a compreensão do chatbot com diferentes tipos de perguntas"""
    
    print("=" * 60)
    print("🧪 TESTE DE COMPREENSÃO - CHATBOT FAQ")
    print("=" * 60)
    
    # Cria instância do chatbot
    faq_bot = NotebookMaintenanceFAQ()
    
    # Verifica se precisa treinar
    db_path = "notebook_faq.sqlite3"
    if not os.path.exists(db_path):
        print("Treinando chatbot...")
        faq_bot.train_chatbot()
    
    # Lista de perguntas de teste
    test_questions = [
        "notebook quente",
        "limpar tela",
        "bateria viciada", 
        "não liga",
        "wifi lento",
        "sem som",
        "tela amarela",
        "trocar SSD",
        "pasta termica",
        "superaquecimento",
        "esquentando muito",
        "notebook devagar",
        "internet não funciona",
        "pixels mortos",
        "como limpo o teclado",
        "deixar sempre carregando",
        "backup importante",
        "adicionar memoria"
    ]
    
    print("\n🔍 TESTANDO COMPREENSÃO COM PERGUNTAS VARIADAS:")
    print("-" * 60)
    
    for i, question in enumerate(test_questions, 1):
        try:
            response = faq_bot.chatbot.get_response(question)
            confidence = response.confidence if hasattr(response, 'confidence') else 'N/A'
            
            print(f"\n{i:2d}. Pergunta: '{question}'")
            print(f"    Resposta: {response}")
            print(f"    Confiança: {confidence}")
            
            # Verifica se é a resposta padrão (não entendeu)
            if "não encontrei informações específicas" in str(response).lower():
                print("    ❌ NÃO ENTENDEU")
            else:
                print("    ✅ ENTENDEU")
                
        except Exception as e:
            print(f"    ❌ ERRO: {e}")
    
    print("\n" + "=" * 60)
    print("🎯 TESTE INTERATIVO - Digite suas próprias perguntas:")
    print("(Digite 'sair' para encerrar)")
    print("-" * 60)
    
    while True:
        try:
            user_question = input("\n👤 Sua pergunta: ")
            
            if user_question.lower() in ['sair', 'exit', 'quit']:
                print("\n🧪 Teste finalizado!")
                break
            
            if user_question.strip() == "":
                continue
            
            response = faq_bot.chatbot.get_response(user_question)
            confidence = response.confidence if hasattr(response, 'confidence') else 'N/A'
            
            print(f"\n🤖 Resposta: {response}")
            print(f"📊 Confiança: {confidence}")
            
            # Feedback sobre compreensão
            if "não encontrei informações específicas" in str(response).lower():
                print("❌ O chatbot não conseguiu entender sua pergunta.")
                print("💡 Tente usar palavras-chave como: limpeza, bateria, quente, lento, WiFi, som, tela")
            else:
                print("✅ Pergunta compreendida com sucesso!")
                
        except KeyboardInterrupt:
            print("\n\n🧪 Teste interrompido!")
            break
        except Exception as e:
            print(f"\n❌ Erro no teste: {e}")

if __name__ == "__main__":
    test_chatbot_understanding()
