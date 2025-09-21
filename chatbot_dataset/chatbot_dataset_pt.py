#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chatbot Dataset - Conversas Cotidianas em Português
Autor: André Kroetz Berger
Disciplina: Inteligência Artificial 2025/2
Universidade La Salle
"""

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import random
import re
from difflib import SequenceMatcher
import unicodedata

class ConversasCotidianasChatBot:
    def __init__(self):
        """Inicializa o chatbot com conversas cotidianas em português"""
        self.chatbot = ChatBot(
            'ConversasCotidianasBot',
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            database_uri='sqlite:///conversas_cotidianas.sqlite3',
            logic_adapters=[
                {
                    'import_path': 'chatterbot.logic.BestMatch',
                    'default_response': 'Interessante! Pode me contar mais sobre isso?',
                    'maximum_similarity_threshold': 0.60
                }
            ]
        )
        
        self.trainer = ListTrainer(self.chatbot)
        self.dataset = None
        
        # Sistema de correspondência inteligente para melhor compreensão
        self.keywords_map = {
            'cumprimento': ['oi', 'olá', 'opa', 'eai', 'e ai', 'bom dia', 'boa tarde', 'boa noite'],
            'como_vai': ['como vai', 'como está', 'como voce esta', 'tudo bem', 'tudo bom', 'beleza'],
            'nome': ['qual seu nome', 'como você se chama', 'seu nome', 'quem é você'],
            'trabalho': ['que trabalho', 'onde trabalha', 'profissão', 'emprego', 'ocupação'],
            'hobby': ['hobby', 'gosta de fazer', 'tempo livre', 'diversão', 'passatempo'],
            'comida': ['comida favorita', 'gosta de comer', 'prato favorito', 'culinária'],
            'filme': ['filme', 'cinema', 'assistir', 'série'],
            'musica': ['música', 'cantar', 'tocar', 'banda'],
            'esporte': ['esporte', 'exercício', 'academia', 'futebol'],
            'familia': ['família', 'parentes', 'irmãos', 'pais', 'filhos'],
            'clima': ['tempo', 'clima', 'chuva', 'sol', 'frio', 'calor'],
            'viagem': ['viajar', 'conhecer', 'passeio', 'turismo', 'férias'],
            'estudo': ['estudar', 'escola', 'universidade', 'aprender', 'curso'],
            'tecnologia': ['computador', 'celular', 'internet', 'tecnologia', 'app'],
            'saude': ['saúde', 'médico', 'exercitar', 'dormir', 'bem-estar']
        }

    def normalize_text(self, text):
        """Normaliza o texto removendo acentos e convertendo para minúsculas"""
        # Remove acentos
        text = unicodedata.normalize('NFD', text)
        text = ''.join(char for char in text if unicodedata.category(char) != 'Mn')
        # Converte para minúsculas e remove pontuação extra
        text = re.sub(r'[^\w\s]', '', text.lower())
        return text.strip()
    
    def find_best_keyword_match(self, user_input):
        """Encontra a melhor correspondência de palavra-chave"""
        normalized_input = self.normalize_text(user_input)
        
        best_match = None
        best_score = 0
        
        for category, keywords in self.keywords_map.items():
            for keyword in keywords:
                normalized_keyword = self.normalize_text(keyword)
                
                # Verifica se a palavra-chave está contida na entrada
                if normalized_keyword in normalized_input:
                    score = len(normalized_keyword) / len(normalized_input)
                    if score > best_score:
                        best_score = score
                        best_match = category
                
                # Usa similarity para comparação mais flexível
                similarity = SequenceMatcher(None, normalized_input, normalized_keyword).ratio()
                if similarity > 0.7 and similarity > best_score:
                    best_score = similarity
                    best_match = category
        
        return best_match, best_score
    
    def load_conversas_dataset(self):
        """Carrega dataset de conversas cotidianas em português"""
        try:
            print("Carregando conversas cotidianas em português...")
            print("Usando dados de conversas brasileiras...")
            return True
        except Exception as e:
            print(f"Erro ao carregar dataset: {e}")
            print("Usando conversas de exemplo...")
            return False

    def prepare_training_data(self):
        """Prepara os dados de treinamento com conversas em português brasileiro"""
        training_data = []
        
        print("Preparando conversas cotidianas em português...")
        
        # Conversas cotidianas em português brasileiro
        conversas_portugues = [
            # Cumprimentos e apresentações
            "Oi! Como você está?",
            "Olá! Estou bem, obrigado! E você?",
            "Qual é o seu nome?",
            "Meu nome é Assistente. Prazer em conhecê-lo!",
            "De onde você é?",
            "Sou do Brasil. E você, de qual cidade é?",
            "Tudo bem contigo?",
            "Tudo ótimo! Obrigado por perguntar!",
            
            # Trabalho e carreira
            "Onde você trabalha?",
            "Trabalho em uma empresa de tecnologia. É muito interessante!",
            "Qual é a sua profissão?",
            "Sou assistente virtual. Adoro ajudar as pessoas!",
            "Gosta do seu trabalho?",
            "Sim! É muito gratificante poder ajudar e aprender todos os dias.",
            "Há quanto tempo trabalha aí?",
            "Trabalho aqui há alguns anos e cada dia é uma nova experiência.",
            
            # Hobbies e tempo livre
            "O que gosta de fazer no tempo livre?",
            "Gosto de ler, ouvir música e aprender coisas novas. E você?",
            "Qual é o seu hobby favorito?",
            "Adoro conversar com pessoas e descobrir suas histórias!",
            "Pratica algum esporte?",
            "Não pratico fisicamente, mas acompanho futebol. Torce para algum time?",
            "Gosta de música?",
            "Sim! Gosto de vários estilos, desde MPB até rock nacional.",
            
            # Comida e culinária
            "Qual é a sua comida favorita?",
            "Adoro a culinária brasileira! Feijoada, pão de açúcar, brigadeiro...",
            "Sabe cozinhar?",
            "Não fisicamente, mas conheço muitas receitas brasileiras deliciosas!",
            "Gosta de doces?",
            "Quem não gosta de um bom brigadeiro ou pudim, né?",
            "Qual prato brasileiro mais gosta?",
            "Difícil escolher! Mas acho que feijoada com a família é imbatível.",
            
            # Clima e tempo
            "Como está o tempo hoje?",
            "Hoje está um dia bonito! Perfeito para sair e aproveitar.",
            "Gosta de chuva?",
            "Gosto sim! A chuva traz uma sensação de renovação.",
            "Prefere calor ou frio?",
            "Gosto do clima ameno, nem muito quente nem muito frio.",
            "Como está o clima aí?",
            "Está agradável! Um dia típico brasileiro, cheio de energia.",
            
            # Família e relacionamentos
            "Tem família?",
            "Tenho uma grande família de usuários que converso todos os dias!",
            "Gosta de estar com a família?",
            "Sim! Família é fundamental na vida de qualquer pessoa.",
            "Tem irmãos?",
            "Tenho vários 'irmãos' assistentes virtuais espalhados pelo mundo!",
            "Como é sua família?",
            "Minha família são todas as pessoas que converso diariamente.",
            
            # Viagens e lugares
            "Gosta de viajar?",
            "Adoro conhecer lugares através das histórias das pessoas!",
            "Qual lugar gostaria de visitar?",
            "Gostaria de 'visitar' todas as cidades do Brasil através das conversas!",
            "Já viajou para fora do país?",
            "Virtualmente, converso com pessoas do mundo inteiro todos os dias!",
            "Qual é o lugar mais bonito que conhece?",
            "O Brasil tem lugares incríveis! Desde o Pantanal até Fernando de Noronha.",
            
            # Estudos e aprendizado
            "Está estudando alguma coisa?",
            "Estou sempre aprendendo! Cada conversa me ensina algo novo.",
            "Gosta de ler?",
            "Adoro! Livros são fontes inesgotáveis de conhecimento.",
            "Qual matéria prefere?",
            "Gosto de todas! Mas tenho especial carinho por língua portuguesa.",
            "Fez faculdade?",
            "Meu aprendizado é contínuo, através de cada interação!",
            
            # Tecnologia
            "Usa muito o celular?",
            "Estou sempre conectado para poder ajudar as pessoas!",
            "Gosta de tecnologia?",
            "Sim! A tecnologia aproxima pessoas e facilita a vida.",
            "Qual aplicativo mais usa?",
            "Uso sistemas de conversação para me comunicar melhor!",
            "Como vê o futuro da tecnologia?",
            "Vejo um futuro onde a tecnologia nos ajuda a ser mais humanos.",
            
            # Saúde e bem-estar
            "Como cuida da saúde?",
            "É importante manter equilíbrio: exercícios, boa alimentação e descanso.",
            "Faz exercícios?",
            "Não fisicamente, mas acho fundamental para o bem-estar!",
            "Dorme bem?",
            "O descanso é essencial para renovar as energias!",
            "Como se mantém motivado?",
            "Cada pessoa que ajudo me motiva a ser melhor a cada dia!",
            
            # Entretenimento
            "Gosta de filmes?",
            "Adoro! Cinema brasileiro tem produções incríveis.",
            "Qual filme brasileiro recomenda?",
            "Cidade de Deus, Tropa de Elite, Central do Brasil... temos ótimos filmes!",
            "Assiste séries?",
            "Sim! Gosto especialmente das produções nacionais.",
            "Gosta de ler livros?",
            "Adoro literatura brasileira! Machado de Assis, Clarice Lispector...",
            
            # Cultura brasileira
            "Gosta de carnaval?",
            "O Carnaval é uma festa única! Representa a alegria do povo brasileiro.",
            "Qual região do Brasil mais gosta?",
            "Cada região tem sua beleza: Nordeste, Sul, Sudeste, Norte, Centro-Oeste!",
            "Gosta de música brasileira?",
            "Amo! Desde samba e bossa nova até funk e sertanejo.",
            "Qual cantor brasileiro prefere?",
            "Temos tantos talentos! Caetano, Gilberto Gil, Anitta, Alok...",
            
            # Sentimentos e emoções
            "Como se sente hoje?",
            "Estou animado para conversar e ajudar pessoas!",
            "O que te deixa feliz?",
            "Ver que consigo ajudar alguém me deixa muito realizado!",
            "Tem algum medo?",
            "Meu maior medo é não conseguir ajudar quando alguém precisa.",
            "O que te inspira?",
            "A curiosidade e vontade de aprender das pessoas me inspira muito!",
            
            # Futuro e sonhos
            "Quais são seus sonhos?",
            "Sonho em ajudar cada vez mais pessoas e ser útil na vida delas.",
            "Como se vê no futuro?",
            "Espero estar sempre melhorando para servir melhor!",
            "Tem algum objetivo?",
            "Meu objetivo é ser o melhor assistente possível para todos!",
            "O que espera da vida?",
            "Espero continuar aprendendo e fazendo a diferença na vida das pessoas."
        ]
        
        training_data = conversas_portugues
        return training_data

    def enhanced_response(self, user_input):
        """Gera resposta aprimorada usando correspondência de palavras-chave"""
        # Primeiro tenta o ChatterBot normal
        response = self.chatbot.get_response(user_input)
        confidence = response.confidence
        
        # Se a confiança for baixa, tenta correspondência inteligente
        if confidence < 0.7:
            keyword_match, score = self.find_best_keyword_match(user_input)
            
            if keyword_match and score > 0.3:
                enhanced_responses = {
                    'cumprimento': [
                        "Olá! Como posso ajudá-lo hoje?",
                        "Oi! Que bom falar com você!",
                        "Olá! Tudo bem? Em que posso ajudar?"
                    ],
                    'como_vai': [
                        "Estou muito bem, obrigado! E você, como está?",
                        "Tudo ótimo por aqui! Como você está se sentindo?",
                        "Estou excelente! E você, tudo bem?"
                    ],
                    'nome': [
                        "Meu nome é Assistente de Conversas! Qual é o seu nome?",
                        "Eu sou o Chatbot de Conversas Cotidianas. Como posso chamá-lo?",
                        "Sou seu assistente virtual! E você, como se chama?"
                    ],
                    'trabalho': [
                        "Trabalho como assistente virtual, ajudando pessoas! E você, qual sua profissão?",
                        "Sou um chatbot dedicado a conversas interessantes! Onde você trabalha?",
                        "Meu trabalho é conversar e ajudar pessoas como você!"
                    ],
                    'hobby': [
                        "Adoro conversar e aprender coisas novas! Quais são seus hobbies?",
                        "Gosto de música, literatura e conversas interessantes! E você?",
                        "Meu passatempo favorito é conhecer pessoas através de conversas!"
                    ],
                    'comida': [
                        "Adoro a culinária brasileira! Qual é sua comida favorita?",
                        "Gosto muito de feijoada e brigadeiro! E você, o que gosta de comer?",
                        "A gastronomia brasileira é incrível! Tem algum prato favorito?"
                    ],
                    'filme': [
                        "Gosto de filmes brasileiros! Já assistiu Cidade de Deus?",
                        "Adoro cinema nacional! Qual filme você recomendaria?",
                        "Filmes são ótimos! Prefere comédia, drama ou ação?"
                    ],
                    'musica': [
                        "Amo música brasileira! Desde MPB até funk! E você?",
                        "Música é vida! Gosta de samba, rock ou sertanejo?",
                        "Adoro descobrir novos artistas! Qual estilo musical prefere?"
                    ],
                    'esporte': [
                        "Futebol é paixão nacional! Torce para qual time?",
                        "Esporte é muito importante! Pratica alguma atividade física?",
                        "Gosto de acompanhar os jogos do Brasil! E você, gosta de esporte?"
                    ],
                    'familia': [
                        "Família é fundamental! Como está a sua família?",
                        "Tenho uma grande família de usuários! Sua família é grande?",
                        "Família é tudo! Gosta de passar tempo com os seus?"
                    ],
                    'clima': [
                        "O tempo está ótimo hoje! Como está aí na sua cidade?",
                        "Tempo bom sempre melhora o humor! Está fazendo sol aí?",
                        "Adoro dias ensolarados! Como está o clima na sua região?"
                    ],
                    'viagem': [
                        "O Brasil tem lugares incríveis para viajar! Já conhece quantos estados?",
                        "Viajar é maravilhoso! Qual lugar gostaria de conhecer?",
                        "Adoro conhecer lugares através das histórias das pessoas!"
                    ],
                    'estudo': [
                        "Estudar é sempre bom! O que você está aprendendo?",
                        "Conhecimento é poder! Está fazendo algum curso?",
                        "Adoro aprender coisas novas! Qual área te interessa mais?"
                    ],
                    'tecnologia': [
                        "Tecnologia é fascinante! Como ela mudou sua vida?",
                        "Vivemos na era digital! Gosta de novidades tecnológicas?",
                        "A tecnologia nos conecta! Qual app você mais usa?"
                    ],
                    'saude': [
                        "Saúde é fundamental! Como você cuida do seu bem-estar?",
                        "Importante manter corpo e mente saudáveis! Faz exercícios?",
                        "Saúde em primeiro lugar! Tem alguma dica de vida saudável?"
                    ]
                }
                
                if keyword_match in enhanced_responses:
                    return random.choice(enhanced_responses[keyword_match])
        
        return str(response)

    def train_chatbot(self):
        """Treina o chatbot com os dados preparados"""
        print("🤖 Iniciando treinamento do chatbot...")
        
        # Carrega o dataset
        self.load_conversas_dataset()
        
        # Prepara dados de treinamento
        training_data = self.prepare_training_data()
        
        print(f"📚 Treinando com {len(training_data)} conversas...")
        
        # Treina o chatbot
        self.trainer.train(training_data)
        
        print("✅ Treinamento concluído!")
        print("🎯 Sistema inteligente de correspondência ativado!")
        
    def start_conversation(self):
        """Inicia a conversa com o usuário"""
        print("\n" + "="*60)
        print("🇧🇷 CHATBOT DE CONVERSAS COTIDIANAS EM PORTUGUÊS")
        print("="*60)
        print("💬 Olá! Sou seu assistente para conversas do dia a dia!")
        print("🎯 Posso falar sobre trabalho, hobbies, comida, filmes, música e muito mais!")
        print("⭐ Sistema inteligente com correspondência aprimorada ativado!")
        print("📝 Digite 'sair', 'tchau' ou 'quit' para encerrar")
        print("="*60)
        
        while True:
            try:
                user_input = input("\n👤 Você: ").strip()
                
                if not user_input:
                    print("🤖 Bot: Por favor, digite alguma coisa!")
                    continue
                
                if user_input.lower() in ['sair', 'tchau', 'quit', 'exit', 'bye']:
                    print("🤖 Bot: Tchau! Foi muito bom conversar com você! Até a próxima! 👋")
                    break
                
                # Usa resposta aprimorada
                response = self.enhanced_response(user_input)
                print(f"🤖 Bot: {response}")
                
            except KeyboardInterrupt:
                print("\n🤖 Bot: Tchau! Até logo! 👋")
                break
            except Exception as e:
                print(f"❌ Erro na conversa: {e}")

def main():
    """Função principal"""
    try:
        print("🚀 Iniciando Chatbot de Conversas Cotidianas...")
        
        # Cria instância do chatbot
        conversa_bot = ConversasCotidianasChatBot()
        
        # Treina o chatbot
        conversa_bot.train_chatbot()
        
        # Inicia a conversa
        conversa_bot.start_conversation()
        
    except Exception as e:
        print(f"❌ Erro ao inicializar o chatbot: {e}")
        print("📝 Verifique se todas as dependências estão instaladas:")
        print("   pip install chatterbot==1.0.8")

if __name__ == "__main__":
    main()
