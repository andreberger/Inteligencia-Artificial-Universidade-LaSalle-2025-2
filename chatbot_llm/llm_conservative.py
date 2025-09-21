#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LLM Conservador - Respostas Menores e Coerentes
Autor: André Kroetz Berger
Disciplina: Inteligência Artificial 2025/2
Universidade La Salle
"""

from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

class ConservativeLLM:
    def __init__(self):
        """Inicializa o LLM com configurações conservadoras"""
        print("Carregando modelo GPT-2 para versão conservadora...")
        
        # Carrega modelo e tokenizer
        self.model_name = "gpt2"
        self.tokenizer = GPT2Tokenizer.from_pretrained(self.model_name)
        self.model = GPT2LMHeadModel.from_pretrained(self.model_name)
        
        # Adiciona token de padding se não existir
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token
        
        # Configurações conservadoras
        self.generation_config = {
            'temperature': 0.3,          # Baixa temperatura = mais determinístico
            'max_length': 50,            # Respostas curtas
            'top_p': 0.8,               # Vocabulário mais restrito
            'repetition_penalty': 1.2,   # Evita repetições
            'do_sample': True,
            'pad_token_id': self.tokenizer.eos_token_id
        }
        
        print("Modelo carregado com configurações conservadoras!")
        self.print_configuration()
    
    def print_configuration(self):
        """Imprime as configurações utilizadas"""
        print("\n🎛️ CONFIGURAÇÕES CONSERVADORAS:")
        print(f"Temperature: {self.generation_config['temperature']} (baixa - mais determinístico)")
        print(f"Max Length: {self.generation_config['max_length']} tokens (respostas curtas)")
        print(f"Top-p: {self.generation_config['top_p']} (vocabulário restrito)")
        print(f"Repetition Penalty: {self.generation_config['repetition_penalty']} (evita repetições)")
        print("-" * 60)
    
    def generate_response(self, prompt):
        """Gera resposta usando configurações conservadoras"""
        try:
            # Codifica o prompt
            inputs = self.tokenizer.encode(prompt, return_tensors='pt')
            
            # Gera resposta
            with torch.no_grad():
                outputs = self.model.generate(
                    inputs,
                    **self.generation_config
                )
            
            # Decodifica apenas a parte nova (sem o prompt original)
            response = self.tokenizer.decode(
                outputs[0][len(inputs[0]):], 
                skip_special_tokens=True
            ).strip()
            
            return response if response else "I understand, but I need more context to provide a helpful response."
            
        except Exception as e:
            return f"Error generating response: {e}"
    
    def start_conversation(self):
        """Inicia conversa com o usuário"""
        print("=" * 60)
        print("🤖 LLM CONSERVADOR - RESPOSTAS COERENTES E CONCISAS 🤖")
        print("=" * 60)
        print("Olá! Sou um assistente com configurações conservadoras.")
        print("Forneço respostas curtas, diretas e coerentes.")
        print("Digite 'sair' para encerrar.")
        print("-" * 60)
        
        while True:
            try:
                user_input = input("\n👤 Você: ")
                
                if user_input.lower() in ['sair', 'exit', 'quit', 'bye']:
                    print("\n🤖 Bot: Obrigado pela conversa! Até mais!")
                    break
                
                if user_input.strip() == "":
                    print("\n🤖 Bot: Por favor, digite sua pergunta.")
                    continue
                
                # Gera resposta
                print("\n🤖 Bot: ", end="", flush=True)
                response = self.generate_response(user_input)
                print(response)
                
            except KeyboardInterrupt:
                print("\n\nConversa interrompida. Até mais!")
                break
            except Exception as e:
                print(f"\n❌ Erro: {e}")

def main():
    """Função principal"""
    try:
        # Cria instância do LLM conservador
        conservative_llm = ConservativeLLM()
        
        # Inicia conversa
        conservative_llm.start_conversation()
        
    except Exception as e:
        print(f"❌ Erro ao inicializar LLM: {e}")
        print("Verifique se o PyTorch e Transformers estão instalados.")

if __name__ == "__main__":
    main()
