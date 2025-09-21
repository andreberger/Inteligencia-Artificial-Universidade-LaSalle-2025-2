#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LLM Criativo - Respostas Abertas e Criativas
Autor: André Kroetz Berger
Disciplina: Inteligência Artificial 2025/2
Universidade La Salle
"""

from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

class CreativeLLM:
    def __init__(self):
        """Inicializa o LLM com configurações criativas"""
        print("Carregando modelo GPT-2 para versão criativa...")
        
        # Carrega modelo e tokenizer
        self.model_name = "gpt2"
        self.tokenizer = GPT2Tokenizer.from_pretrained(self.model_name)
        self.model = GPT2LMHeadModel.from_pretrained(self.model_name)
        
        # Adiciona token de padding se não existir
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token
        
        # Configurações criativas
        self.generation_config = {
            'temperature': 0.9,          # Alta temperatura = mais criativo
            'max_length': 150,           # Respostas mais longas
            'top_p': 0.95,              # Vocabulário mais amplo
            'repetition_penalty': 1.1,   # Penalização suave
            'do_sample': True,
            'pad_token_id': self.tokenizer.eos_token_id
        }
        
        print("Modelo carregado com configurações criativas!")
        self.print_configuration()
    
    def print_configuration(self):
        """Imprime as configurações utilizadas"""
        print("\n🎨 CONFIGURAÇÕES CRIATIVAS:")
        print(f"Temperature: {self.generation_config['temperature']} (alta - mais criativo)")
        print(f"Max Length: {self.generation_config['max_length']} tokens (respostas longas)")
        print(f"Top-p: {self.generation_config['top_p']} (vocabulário amplo)")
        print(f"Repetition Penalty: {self.generation_config['repetition_penalty']} (penalização suave)")
        print("-" * 60)
    
    def generate_response(self, prompt):
        """Gera resposta usando configurações criativas"""
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
            
            return response if response else "That's a fascinating topic! Let me explore that idea with you in a creative way..."
            
        except Exception as e:
            return f"Error generating response: {e}"
    
    def start_conversation(self):
        """Inicia conversa com o usuário"""
        print("=" * 60)
        print("🎨 LLM CRIATIVO - RESPOSTAS ABERTAS E CRIATIVAS 🎨")
        print("=" * 60)
        print("Olá! Sou um assistente com configurações criativas.")
        print("Gero respostas mais elaboradas, imaginativas e abertas.")
        print("Digite 'sair' para encerrar.")
        print("-" * 60)
        
        while True:
            try:
                user_input = input("\n👤 Você: ")
                
                if user_input.lower() in ['sair', 'exit', 'quit', 'bye']:
                    print("\n🎨 Bot: Foi uma jornada criativa incrível! Até nossa próxima aventura intelectual!")
                    break
                
                if user_input.strip() == "":
                    print("\n🎨 Bot: Compartilhe seus pensamentos comigo! Estou ansioso para explorar ideias criativas.")
                    continue
                
                # Gera resposta
                print("\n🎨 Bot: ", end="", flush=True)
                response = self.generate_response(user_input)
                print(response)
                
            except KeyboardInterrupt:
                print("\n\nConversa criativa interrompida. Que nossa imaginação continue fluindo!")
                break
            except Exception as e:
                print(f"\n❌ Erro: {e}")

def main():
    """Função principal"""
    try:
        # Cria instância do LLM criativo
        creative_llm = CreativeLLM()
        
        # Inicia conversa
        creative_llm.start_conversation()
        
    except Exception as e:
        print(f"❌ Erro ao inicializar LLM: {e}")
        print("Verifique se o PyTorch e Transformers estão instalados.")

if __name__ == "__main__":
    main()
