#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Teste Avançado do Chatbot FAQ - Sistema Inteligente
Autor: André Kroetz Berger
Testa o novo sistema de compreensão inteligente
"""

import os
import sys

# Adiciona o diretório do projeto ao path
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_dir)

from chatbot_faq.chatbot_faq import NotebookMaintenanceFAQ

def test_smart_system():
    """Testa o sistema inteligente de compreensão"""
    
    print("=" * 70)
    print("🧠 TESTE DO SISTEMA INTELIGENTE - CHATBOT FAQ")
    print("=" * 70)
    
    # Cria instância do chatbot
    faq_bot = NotebookMaintenanceFAQ()
    
    # Lista de perguntas difíceis de diferentes formas
    challenging_questions = [
        # Perguntas sobre temperatura
        "ta muito quente",
        "esquenta demais", 
        "superaquecendo",
        "muito calor",
        "temperatura alta",
        "forno",
        
        # Perguntas sobre limpeza
        "como limpo",
        "sujo",
        "higienizar",
        "lavar",
        "sujeira",
        
        # Perguntas sobre bateria
        "bateria ruim",
        "não carrega",
        "descarrega rapido",
        "vicia",
        "energia",
        
        # Perguntas sobre velocidade
        "ta lento",
        "demora",
        "travando",
        "lag",
        "devagar",
        "lentidão",
        
        # Perguntas sobre conectividade
        "wifi ruim",
        "internet não pega",
        "conexão",
        "sem rede",
        
        # Perguntas sobre áudio
        "sem som",
        "audio",
        "não escuto",
        "microfone",
        
        # Perguntas sobre tela
        "tela estranha",
        "pontos na tela", 
        "cores",
        "display",
        
        # Perguntas sobre problemas gerais
        "não funciona",
        "pifou",
        "com problema",
        "defeito",
        
        # Perguntas informais/gírias
        "bugado",
        "zoado", 
        "ferrado",
        "estragado",
        "bombou"
    ]
    
    print("\n🔍 TESTANDO SISTEMA INTELIGENTE COM PERGUNTAS DESAFIADORAS:")
    print("-" * 70)
    
    success_count = 0
    total_count = len(challenging_questions)
    
    for i, question in enumerate(challenging_questions, 1):
        try:
            # Testa o sistema inteligente
            smart_response, confidence = faq_bot.smart_response(question)
            
            print(f"\n{i:2d}. Pergunta: '{question}'")
            
            if smart_response and confidence > 0.3:
                print(f"    🧠 Resposta Smart: {smart_response[:80]}...")
                print(f"    📊 Confiança: {confidence:.3f}")
                print(f"    ✅ SUCESSO (Sistema Inteligente)")
                success_count += 1
            else:
                # Tenta o ChatterBot tradicional
                try:
                    traditional_response = faq_bot.chatbot.get_response(question)
                    if "não encontrei informações específicas" in str(traditional_response):
                        print(f"    ❌ FALHOU (Ambos os sistemas)")
                    else:
                        print(f"    🤖 Resposta Tradicional: {traditional_response}")
                        print(f"    ⚠️  SUCESSO (Sistema Tradicional)")
                        success_count += 1
                except:
                    print(f"    ❌ FALHOU (Ambos os sistemas)")
                    
        except Exception as e:
            print(f"    ❌ ERRO: {e}")
    
    # Estatísticas
    success_rate = (success_count / total_count) * 100
    print("\n" + "=" * 70)
    print("📊 ESTATÍSTICAS DO TESTE:")
    print(f"✅ Sucessos: {success_count}/{total_count}")
    print(f"📈 Taxa de Sucesso: {success_rate:.1f}%")
    
    if success_rate >= 80:
        print("🎉 EXCELENTE! Sistema funcionando muito bem!")
    elif success_rate >= 60:
        print("👍 BOM! Sistema funcionando adequadamente.")
    elif success_rate >= 40:
        print("⚠️  REGULAR. Sistema precisa de melhorias.")
    else:
        print("❌ RUIM. Sistema precisa de revisão completa.")
    
    print("\n🎯 TESTE INTERATIVO AVANÇADO:")
    print("Digite perguntas difíceis ou informais para testar o sistema!")
    print("(Digite 'sair' para encerrar)")
    print("-" * 70)
    
    while True:
        try:
            user_question = input("\n👤 Sua pergunta desafiadora: ")
            
            if user_question.lower() in ['sair', 'exit', 'quit']:
                print("\n🧠 Teste avançado finalizado!")
                break
            
            if user_question.strip() == "":
                continue
            
            # Testa sistema inteligente
            smart_response, smart_confidence = faq_bot.smart_response(user_question)
            
            print(f"\n🔍 ANÁLISE DA PERGUNTA: '{user_question}'")
            print("-" * 50)
            
            if smart_response and smart_confidence > 0.3:
                print(f"🧠 Sistema Inteligente:")
                print(f"   Resposta: {smart_response}")
                print(f"   Confiança: {smart_confidence:.3f}")
                print(f"   Status: ✅ SUCESSO")
            else:
                print(f"🧠 Sistema Inteligente:")
                print(f"   Status: ❌ Não encontrou correspondência")
                print(f"   Confiança: {smart_confidence:.3f}")
            
            # Testa sistema tradicional
            try:
                traditional_response = faq_bot.chatbot.get_response(user_question)
                print(f"\n🤖 Sistema Tradicional:")
                if "não encontrei informações específicas" in str(traditional_response):
                    print(f"   Status: ❌ Não entendeu")
                else:
                    print(f"   Resposta: {traditional_response}")
                    print(f"   Status: ✅ SUCESSO")
            except Exception as e:
                print(f"\n🤖 Sistema Tradicional:")
                print(f"   Status: ❌ Erro: {e}")
            
            # Recomendação final
            if smart_response and smart_confidence > 0.3:
                print(f"\n🎯 RESPOSTA FINAL: {smart_response}")
            else:
                print(f"\n💡 SUGESTÃO: Tente palavras como 'quente', 'lento', 'limpar', 'bateria', 'som', 'WiFi'")
                
        except KeyboardInterrupt:
            print("\n\n🧠 Teste avançado interrompido!")
            break
        except Exception as e:
            print(f"\n❌ Erro no teste: {e}")

if __name__ == "__main__":
    test_smart_system()
