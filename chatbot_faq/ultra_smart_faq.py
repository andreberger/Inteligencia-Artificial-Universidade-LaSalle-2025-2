#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chatbot FAQ Ultra Inteligente - Versão Robusta
Autor: André Kroetz Berger
Sistema com múltiplas camadas de compreensão
"""

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import re
from difflib import SequenceMatcher
import unicodedata

class UltraSmartFAQ:
    def __init__(self):
        """Inicializa o chatbot com sistema ultra inteligente"""
        self.chatbot = ChatBot(
            'UltraSmartFAQ',
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            database_uri='sqlite:///ultra_smart_faq.sqlite3',
            logic_adapters=[
                {
                    'import_path': 'chatterbot.logic.BestMatch',
                    'default_response': 'Vou tentar entender melhor sua pergunta...',
                    'maximum_similarity_threshold': 0.50
                }
            ]
        )
        
        self.trainer = ListTrainer(self.chatbot)
        self.responses_database = self._create_responses_database()
        
    def _normalize_text(self, text):
        """Normaliza texto removendo acentos, pontuação e convertendo para minúsculas"""
        # Remove acentos
        text = unicodedata.normalize('NFD', text)
        text = ''.join(char for char in text if unicodedata.category(char) != 'Mn')
        
        # Converte para minúsculas
        text = text.lower()
        
        # Remove pontuação e caracteres especiais
        text = re.sub(r'[^\w\s]', ' ', text)
        
        # Remove múltiplos espaços
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text
    
    def _create_responses_database(self):
        """Cria base de respostas com múltiplas formas de expressão"""
        return {
            'temperatura_alta': {
                'keywords': [
                    'quente', 'esquenta', 'esquentando', 'calor', 'temperatura', 'forno', 
                    'muito calor', 'ta quente', 'esta quente', 'superaquecimento', 
                    'aquecendo', 'fervendo', 'pegando fogo', 'ardendo'
                ],
                'response': "🌡️ Seu notebook está superaquecendo! Verifique se as ventoinhas estão funcionando, limpe-as com ar comprimido, use uma base refrigerada e evite superfícies que bloqueiem a ventilação. Se continuar, verifique a pasta térmica."
            },
            
            'limpeza': {
                'keywords': [
                    'limpar', 'limpeza', 'sujo', 'suja', 'limpo', 'higiene', 'lavar',
                    'sujeira', 'poeira', 'como limpo', 'limpe', 'higienizar'
                ],
                'response': "🧹 Para limpeza: Use pano de microfibra levemente úmido para a tela, ar comprimido para o teclado e álcool isopropílico 70% apenas no gabinete externo. Nunca use líquido diretamente na tela!"
            },
            
            'bateria_problemas': {
                'keywords': [
                    'bateria', 'battery', 'carga', 'carrega', 'carregando', 'energia',
                    'nao carrega', 'não carrega', 'vicia', 'viciada', 'descarrega',
                    'rapido', 'rápido', 'durando pouco', 'autonomia'
                ],
                'response': "🔋 Problemas de bateria: Evite descargas completas, mantenha entre 20-80%, não deixe sempre na tomada. Se a autonomia diminuiu muito, pode precisar trocar a bateria."
            },
            
            'velocidade_lenta': {
                'keywords': [
                    'lento', 'devagar', 'demora', 'travando', 'trava', 'lag', 'lentidao',
                    'lentidão', 'ta lento', 'esta lento', 'muito lento', 'lerdo'
                ],
                'response': "🐌 Notebook lento: Limpe arquivos temporários, desinstale programas desnecessários, verifique por malware, considere adicionar RAM ou trocar por SSD. Execute limpeza de disco."
            },
            
            'wifi_internet': {
                'keywords': [
                    'wifi', 'wi-fi', 'internet', 'rede', 'conexao', 'conexão', 'conectar',
                    'sem internet', 'nao conecta', 'não conecta', 'wifi ruim', 'rede lenta'
                ],
                'response': "📶 Problemas de WiFi: Reinicie o roteador, esqueça e reconecte a rede, atualize drivers de rede, verifique se está próximo do roteador ou redefina configurações de rede."
            },
            
            'audio_som': {
                'keywords': [
                    'som', 'audio', 'áudio', 'sem som', 'mudo', 'silencioso', 'nao escuto',
                    'não escuto', 'microfone', 'alto falante', 'som baixo', 'volume'
                ],
                'response': "🔊 Problemas de áudio: Verifique o volume, dispositivos de reprodução padrão, drivers de áudio, se não está no mudo e teste com fones de ouvido."
            },
            
            'tela_display': {
                'keywords': [
                    'tela', 'display', 'monitor', 'pixel', 'pixels mortos', 'pontos',
                    'manchas', 'amarela', 'amarelada', 'cores', 'cor estranha', 'brilho'
                ],
                'response': "🖥️ Problemas de tela: Pixels mortos são defeitos permanentes. Tela amarelada pode ser filtro de luz azul. Ajuste brilho para economizar bateria. Para riscos, evite pressão na tela."
            },
            
            'nao_liga': {
                'keywords': [
                    'nao liga', 'não liga', 'nao funciona', 'não funciona', 'morto',
                    'pifou', 'bugado', 'zoado', 'ferrado', 'estragado', 'bombou', 'defeito'
                ],
                'response': "⚡ Notebook não liga: Teste o carregador, pressione o botão power por 15 segundos, remova a bateria se possível, teste só na tomada. Verifique se há sinais de vida (LEDs, sons)."
            },
            
            'hardware_upgrade': {
                'keywords': [
                    'ram', 'memoria', 'memória', 'ssd', 'hd', 'disco', 'storage',
                    'armazenamento', 'pouca ram', 'adicionar memoria', 'trocar ssd'
                ],
                'response': "💾 Hardware: SSD é muito mais rápido que HD. Se usa muita RAM (>80%), considere adicionar mais. Verifique compatibilidade antes de comprar. Backup antes de trocar HD/SSD!"
            },
            
            'manutencao_preventiva': {
                'keywords': [
                    'manutencao', 'manutenção', 'cuidados', 'preventiva', 'conservar',
                    'durar mais', 'vida util', 'vida útil', 'preservar'
                ],
                'response': "🔧 Manutenção preventiva: Limpeza regular (6-12 meses), backup de dados, atualizações do sistema, antivírus atualizado, cuidados físicos e evitar temperaturas extremas."
            },
            
            'virus_seguranca': {
                'keywords': [
                    'virus', 'vírus', 'malware', 'antivirus', 'antivírus', 'segurança',
                    'infectado', 'lento por virus', 'proteção'
                ],
                'response': "🛡️ Segurança: Use antivírus atualizado, evite sites suspeitos, não baixe arquivos duvidosos, mantenha sistema atualizado. Windows Defender já oferece boa proteção básica."
            }
        }
    
    def ultra_smart_response(self, user_input):
        """Sistema ultra inteligente de análise e resposta"""
        normalized_input = self._normalize_text(user_input)
        
        best_match_score = 0
        best_response = None
        best_category = None
        
        # Analisa cada categoria de resposta
        for category, data in self.responses_database.items():
            keywords = data['keywords']
            response = data['response']
            
            # Calcula score para esta categoria
            category_score = 0
            matched_keywords = []
            
            for keyword in keywords:
                normalized_keyword = self._normalize_text(keyword)
                
                # Verifica correspondência exata
                if normalized_keyword in normalized_input:
                    category_score += 1.0
                    matched_keywords.append(keyword)
                    continue
                
                # Verifica correspondência parcial
                similarity = SequenceMatcher(None, normalized_keyword, normalized_input).ratio()
                if similarity > 0.6:
                    category_score += similarity * 0.8
                    matched_keywords.append(keyword)
                    continue
                
                # Verifica se palavras do keyword estão na entrada
                keyword_words = normalized_keyword.split()
                input_words = normalized_input.split()
                
                word_matches = 0
                for kw_word in keyword_words:
                    for inp_word in input_words:
                        word_sim = SequenceMatcher(None, kw_word, inp_word).ratio()
                        if word_sim > 0.7:
                            word_matches += 1
                            break
                
                if word_matches > 0:
                    word_score = word_matches / len(keyword_words)
                    category_score += word_score * 0.6
                    if word_score > 0.5:
                        matched_keywords.append(keyword)
            
            # Normaliza o score pela quantidade de palavras-chave
            if len(keywords) > 0:
                normalized_score = category_score / len(keywords)
                
                if normalized_score > best_match_score:
                    best_match_score = normalized_score
                    best_response = response
                    best_category = category
        
        return best_response, best_match_score, best_category
    
    def get_response(self, user_input):
        """Método principal para obter resposta"""
        # Primeiro tenta o sistema ultra inteligente
        smart_response, confidence, category = self.ultra_smart_response(user_input)
        
        if smart_response and confidence > 0.2:
            return {
                'response': smart_response,
                'confidence': confidence,
                'method': 'ultra_smart',
                'category': category
            }
        
        # Se não encontrar, tenta o ChatterBot tradicional
        try:
            traditional_response = self.chatbot.get_response(user_input)
            if "Vou tentar entender melhor" not in str(traditional_response):
                return {
                    'response': str(traditional_response),
                    'confidence': 0.5,
                    'method': 'traditional',
                    'category': 'chatterbot'
                }
        except:
            pass
        
        # Resposta padrão mais útil
        return {
            'response': "🤔 Não consegui entender sua pergunta específica. Posso ajudar com: 🌡️ superaquecimento, 🧹 limpeza, 🔋 bateria, 🐌 lentidão, 📶 WiFi, 🔊 áudio, 🖥️ tela, ⚡ não liga, 💾 hardware, 🔧 manutenção. Tente ser mais específico!",
            'confidence': 0.1,
            'method': 'default',
            'category': 'unknown'
        }
    
    def interactive_mode(self):
        """Modo interativo melhorado"""
        print("=" * 70)
        print("🧠 CHATBOT FAQ ULTRA INTELIGENTE - MANUTENÇÃO DE NOTEBOOKS 🧠")
        print("=" * 70)
        print("Olá! Sou seu assistente ultra inteligente para manutenção de notebooks!")
        print("🎯 Agora entendo perguntas de forma muito mais natural e flexível!")
        print("💡 Experimente perguntas como: 'ta quente', 'muito lento', 'não liga'")
        print("Digite 'sair' para encerrar.")
        print("-" * 70)
        
        while True:
            try:
                user_input = input("\n👤 Você: ")
                
                if user_input.lower() in ['sair', 'exit', 'quit', 'tchau', 'bye']:
                    print("\n🧠 Obrigado por usar o FAQ Ultra Inteligente! Até mais! 👋")
                    break
                
                if user_input.strip() == "":
                    print("\n🧠 Digite sua pergunta sobre notebooks e eu tentarei ajudar!")
                    continue
                
                # Obtém resposta do sistema ultra inteligente
                result = self.get_response(user_input)
                
                # Mostra a resposta com informações de debug
                print(f"\n🧠 Bot: {result['response']}")
                print(f"📊 Confiança: {result['confidence']:.3f} | Método: {result['method']} | Categoria: {result['category']}")
                
            except KeyboardInterrupt:
                print("\n\n🧠 Conversa interrompida. Até mais!")
                break
            except Exception as e:
                print(f"\n❌ Erro: {e}")

def main():
    """Função principal"""
    try:
        ultra_faq = UltraSmartFAQ()
        ultra_faq.interactive_mode()
    except Exception as e:
        print(f"❌ Erro ao inicializar: {e}")

if __name__ == "__main__":
    main()
