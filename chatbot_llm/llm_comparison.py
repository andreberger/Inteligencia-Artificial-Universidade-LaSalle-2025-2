#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Comparação entre LLM Conservador vs Criativo
Autor: André Kroetz Berger
Disciplina: Inteligência Artificial 2025/2
Universidade La Salle
"""

from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

class LLMComparison:
    def __init__(self):
        """Inicializa ambas as versões do LLM para comparação"""
        print("Carregando modelo GPT-2 para comparação...")
        
        # Carrega modelo e tokenizer
        self.model_name = "gpt2"
        self.tokenizer = GPT2Tokenizer.from_pretrained(self.model_name)
        self.model = GPT2LMHeadModel.from_pretrained(self.model_name)
        
        # Adiciona token de padding se não existir
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token
        
        # Configurações conservadoras
        self.conservative_config = {
            'temperature': 0.3,
            'max_length': 50,
            'top_p': 0.8,
            'repetition_penalty': 1.2,
            'do_sample': True,
            'pad_token_id': self.tokenizer.eos_token_id
        }
        
        # Configurações criativas
        self.creative_config = {
            'temperature': 0.9,
            'max_length': 150,
            'top_p': 0.95,
            'repetition_penalty': 1.1,
            'do_sample': True,
            'pad_token_id': self.tokenizer.eos_token_id
        }
        
        print("Modelo carregado para comparação!")
    
    def generate_response(self, prompt, config):
        """Gera resposta usando configuração específica"""
        try:
            inputs = self.tokenizer.encode(prompt, return_tensors='pt')
            
            with torch.no_grad():
                outputs = self.model.generate(inputs, **config)
            
            response = self.tokenizer.decode(
                outputs[0][len(inputs[0]):], 
                skip_special_tokens=True
            ).strip()
            
            return response if response else "I need more context to provide a helpful response."
            
        except Exception as e:
            return f"Error: {e}"
    
    def compare_responses(self, prompt):
        """Compara respostas entre as duas configurações"""
        print(f"\n📝 PROMPT: {prompt}")
        print("=" * 60)
        
        # Gera resposta conservadora
        print("🤖 VERSÃO CONSERVADORA:")
        conservative_response = self.generate_response(prompt, self.conservative_config)
        print(f"   {conservative_response}")
        
        print("\n🎨 VERSÃO CRIATIVA:")
        creative_response = self.generate_response(prompt, self.creative_config)
        print(f"   {creative_response}")
        
        print("-" * 60)
        
        # Análise das diferenças
        print("📊 ANÁLISE:")
        print(f"   Tamanho conservador: {len(conservative_response.split())} palavras")
        print(f"   Tamanho criativo: {len(creative_response.split())} palavras")
        print(f"   Diferença: {abs(len(creative_response.split()) - len(conservative_response.split()))} palavras")
    
    def run_demonstrations(self):
        """Executa demonstrações com prompts pré-definidos"""
        print("=" * 60)
        print("🔬 COMPARAÇÃO LLM: CONSERVADOR vs CRIATIVO 🔬")
        print("=" * 60)
        
        print("\n🎛️ CONFIGURAÇÕES:")
        print("CONSERVADOR - Temp: 0.3, Max: 50, Top-p: 0.8, Rep: 1.2")
        print("CRIATIVO    - Temp: 0.9, Max: 150, Top-p: 0.95, Rep: 1.1")
        
        # Lista de prompts para demonstração
        demo_prompts = [
            "What is artificial intelligence?",
            "Tell me about the future of technology.",
            "How can we solve climate change?",
            "What makes a good leader?",
            "Describe your ideal vacation."
        ]
        
        for prompt in demo_prompts:
            self.compare_responses(prompt)
            input("\nPressione Enter para continuar...")
    
    def interactive_mode(self):
        """Modo interativo para comparação"""
        print("\n🔄 MODO INTERATIVO - COMPARAÇÃO EM TEMPO REAL")
        print("Digite seus próprios prompts para ver as diferenças!")
        print("Digite 'demo' para ver demonstrações ou 'sair' para encerrar.")
        print("-" * 60)
        
        while True:
            try:
                user_input = input("\n👤 Digite seu prompt: ")
                
                if user_input.lower() in ['sair', 'exit', 'quit']:
                    print("\n🔬 Obrigado por explorar as diferenças entre LLMs! Até mais!")
                    break
                
                if user_input.lower() == 'demo':
                    self.run_demonstrations()
                    continue
                
                if user_input.strip() == "":
                    print("Por favor, digite um prompt para comparação.")
                    continue
                
                self.compare_responses(user_input)
                
            except KeyboardInterrupt:
                print("\n\nComparação interrompida. Até mais!")
                break

def main():
    """Função principal"""
    try:
        # Cria instância de comparação
        comparison = LLMComparison()
        
        # Pergunta ao usuário qual modo usar
        print("\nEscolha o modo:")
        print("1. Demonstrações automáticas")
        print("2. Modo interativo")
        print("3. Ambos")
        
        choice = input("\nDigite sua escolha (1/2/3): ").strip()
        
        if choice == "1":
            comparison.run_demonstrations()
        elif choice == "2":
            comparison.interactive_mode()
        elif choice == "3":
            comparison.run_demonstrations()
            comparison.interactive_mode()
        else:
            print("Opção inválida. Executando modo interativo...")
            comparison.interactive_mode()
        
    except Exception as e:
        print(f"❌ Erro ao inicializar comparação: {e}")
        print("Verifique se o PyTorch e Transformers estão instalados.")

if __name__ == "__main__":
    main()
