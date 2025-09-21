#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Menu Principal - Projeto Chatbots
Autor: André Kroetz Berger
Disciplina: Inteligência Artificial 2025/2
Universidade La Salle
"""

import os
import subprocess
import sys

class ChatbotMenu:
    def __init__(self):
        """Inicializa o menu principal"""
        self.project_path = os.path.dirname(os.path.abspath(__file__))
    
    def show_header(self):
        """Exibe cabeçalho do projeto"""
        print("=" * 70)
        print("🤖 PROJETO CHATBOTS - INTELIGÊNCIA ARTIFICIAL 2025/2 🤖")
        print("=" * 70)
        print("Autor: André Kroetz Berger")
        print("Universidade La Salle")
        print("GitHub: https://github.com/andreberger/Inteligencia-Artificial-Universidade-LaSalle-2025-2")
        print("=" * 70)
    
    def show_menu(self):
        """Exibe menu de opções"""
        print("\n📋 ESCOLHA UM CHATBOT PARA EXECUTAR:")
        print("-" * 40)
        print("1. 🔧 Chatbot FAQ - Manutenção de Notebooks")
        print("2. 💬 Chatbot Corpora - Conversação Natural") 
        print("3. 📅 Chatbot Dataset - Daily Dialog")
        print("4. 🤖 LLM Conservador - Respostas Concisas")
        print("5. 🎨 LLM Criativo - Respostas Elaboradas")
        print("6. 🔬 Comparação LLM - Lado a Lado")
        print("7. 📚 Ver Documentação")
        print("8. ⚙️  Instalar Dependências")
        print("0. ❌ Sair")
        print("-" * 40)
    
    def run_chatbot(self, script_path):
        """Executa um chatbot específico"""
        try:
            full_path = os.path.join(self.project_path, script_path)
            if os.path.exists(full_path):
                print(f"\n🚀 Executando: {script_path}")
                print("=" * 50)
                subprocess.run([sys.executable, full_path])
            else:
                print(f"❌ Arquivo não encontrado: {script_path}")
        except Exception as e:
            print(f"❌ Erro ao executar: {e}")
    
    def show_documentation(self):
        """Exibe informações sobre a documentação"""
        print("\n📚 DOCUMENTAÇÃO DO PROJETO")
        print("=" * 50)
        print("Cada chatbot possui sua própria documentação:")
        print()
        print("📁 chatbot_faq/README.md")
        print("   - FAQ sobre manutenção de notebooks")
        print("   - 50+ pares pergunta/resposta")
        print()
        print("📁 chatbot_corpora/README.md")
        print("   - Conversação usando corpora")
        print("   - Treinamento com diálogos estruturados")
        print()
        print("📁 chatbot_dataset/README.md")
        print("   - Dataset Daily Dialog do Hugging Face")
        print("   - Conversas cotidianas reais")
        print()
        print("📁 chatbot_llm/README.md")
        print("   - Experimento com duas configurações LLM")
        print("   - Comparação entre conservador e criativo")
        print()
        print("🔗 GitHub: https://github.com/andreberger/Inteligencia-Artificial-Universidade-LaSalle-2025-2")
    
    def install_dependencies(self):
        """Instala dependências do projeto"""
        print("\n⚙️ INSTALANDO DEPENDÊNCIAS...")
        print("=" * 50)
        
        dependencies = [
            "chatterbot==1.0.8",
            "chatterbot-corpus==1.2.0", 
            "nltk==3.8.1",
            "PyYAML==6.0.1",
            "transformers==4.36.0",
            "datasets==2.14.0",
            "torch==2.1.0",
            "accelerate==0.24.0",
            "numpy==1.24.3"
        ]
        
        for dep in dependencies:
            try:
                print(f"Instalando {dep}...")
                subprocess.run([sys.executable, "-m", "pip", "install", dep], check=True)
            except subprocess.CalledProcessError as e:
                print(f"❌ Erro ao instalar {dep}: {e}")
        
        print("✅ Instalação concluída!")
    
    def run(self):
        """Executa o menu principal"""
        while True:
            self.show_header()
            self.show_menu()
            
            try:
                choice = input("\n👤 Digite sua escolha (0-8): ").strip()
                
                if choice == "1":
                    self.run_chatbot("chatbot_faq/chatbot_faq.py")
                elif choice == "2":
                    self.run_chatbot("chatbot_corpora/chatbot_corpora.py")
                elif choice == "3":
                    self.run_chatbot("chatbot_dataset/chatbot_dataset.py")
                elif choice == "4":
                    self.run_chatbot("chatbot_llm/llm_conservative.py")
                elif choice == "5":
                    self.run_chatbot("chatbot_llm/llm_creative.py")
                elif choice == "6":
                    self.run_chatbot("chatbot_llm/llm_comparison.py")
                elif choice == "7":
                    self.show_documentation()
                    input("\nPressione Enter para continuar...")
                elif choice == "8":
                    self.install_dependencies()
                    input("\nPressione Enter para continuar...")
                elif choice == "0":
                    print("\n👋 Obrigado por usar o projeto de chatbots!")
                    print("🎓 Universidade La Salle - IA 2025/2")
                    break
                else:
                    print("\n❌ Opção inválida! Tente novamente.")
                    input("Pressione Enter para continuar...")
                    
            except KeyboardInterrupt:
                print("\n\n👋 Saindo do menu. Até mais!")
                break
            except Exception as e:
                print(f"\n❌ Erro: {e}")
                input("Pressione Enter para continuar...")

def main():
    """Função principal"""
    menu = ChatbotMenu()
    menu.run()

if __name__ == "__main__":
    main()
