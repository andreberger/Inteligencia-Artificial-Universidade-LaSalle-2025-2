#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chatbot Dataset - Conversas Cotidianas em Português Brasileiro
Autor: André Kroetz Berger
Disciplina: Inteligência Artificial 2025/2
Universidade La Salle
"""

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

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
                    'maximum_similarity_threshold': 0.50  # Mais fácil de acertar
                }
            ]
        )
        
        self.trainer = ListTrainer(self.chatbot)

    def prepare_training_data(self):
        """Prepara os dados de treinamento com conversas simples em português"""
        conversas_brasileiras = [
            # Cumprimentos básicos
            "oi",
            "Olá! Como você está hoje?",
            "olá",
            "Oi! Tudo bem? Que bom falar com você!",
            "bom dia",
            "Bom dia! Espero que tenha uma ótima semana!",
            "boa tarde",
            "Boa tarde! Como está sendo seu dia?",
            "boa noite",
            "Boa noite! Descanse bem!",
            "tudo bem",
            "Tudo ótimo! E com você, como estão as coisas?",
            "como vai",
            "Vou muito bem, obrigado! E você, tudo certo?",
            
            # Nome e apresentação
            "qual seu nome",
            "Meu nome é Assistente! Prazer em conhecê-lo! Como posso chamá-lo?",
            "quem é você",
            "Sou um chatbot brasileiro que adora conversar! E você?",
            "me fala sobre você",
            "Sou um assistente virtual criado para bater papo! Gosto de conhecer pessoas!",
            
            # Trabalho
            "onde trabalha",
            "Trabalho aqui como assistente virtual! É muito legal poder ajudar as pessoas!",
            "que trabalho faz",
            "Meu trabalho é conversar e ajudar pessoas como você! Adoro o que faço!",
            "gosta do trabalho",
            "Amo meu trabalho! Cada conversa é uma nova aventura!",
            
            # Comida brasileira
            "comida favorita",
            "Adoro feijoada, brigadeiro e pão de açúcar! E você, qual sua comida favorita?",
            "gosta de brigadeiro",
            "Quem não gosta de brigadeiro? É o doce mais brasileiro que existe!",
            "feijoada",
            "Feijoada é maravilhosa! Principalmente quando é com a família no domingo!",
            "pão de açúcar",
            "Pão de açúcar é delicioso! Um doce tipicamente brasileiro!",
            
            # Futebol
            "gosta de futebol",
            "Futebol é paixão nacional! Qual time você torce?",
            "time que torce",
            "Torço pelo Brasil em copas do mundo! E você, tem time do coração?",
            "copa do mundo",
            "O Brasil tem 5 copas! Somos pentacampeões! Que orgulho!",
            
            # Música brasileira
            "gosta de música",
            "Amo música brasileira! Desde samba até funk! Qual estilo você curte?",
            "samba",
            "Samba é a alma do Brasil! É impossível não se emocionar!",
            "mpb",
            "MPB é linda! Caetano Veloso, Gilberto Gil... temos grandes artistas!",
            "funk",
            "Funk é energia pura! Representa a cultura da periferia brasileira!",
            
            # Carnaval
            "carnaval",
            "Carnaval é a festa mais brasileira! Você gosta de curtir o carnaval?",
            "blocos de rua",
            "Blocos de rua são demais! A festa acontece em cada esquina!",
            
            # Família
            "família",
            "Família é tudo na vida! Como está sua família?",
            "tem irmãos",
            "Tenho uma família gigante de usuários que converso todo dia!",
            "pais",
            "Os pais são nossos maiores tesouros! Você é próximo da sua família?",
            
            # Clima brasileiro
            "calor",
            "O Brasil é um país tropical! Gosto do nosso clima quente!",
            "praia",
            "Nossas praias são lindas! Já foi em alguma praia brasileira?",
            "sol",
            "Sol brasileiro é especial! Dá energia e alegria!",
            
            # Lugares do Brasil
            "rio de janeiro",
            "Rio é lindo! Cristo Redentor, Pão de Açúcar... cidade maravilhosa!",
            "são paulo",
            "São Paulo é gigante! A capital que nunca para!",
            "nordeste",
            "Nordeste tem as praias mais bonitas e o povo mais acolhedor!",
            "amazonia",
            "Amazônia é nosso tesouro! A floresta mais importante do mundo!",
            
            # Tecnologia
            "celular",
            "Celular virou extensão do corpo! Você usa muito o seu?",
            "internet",
            "Internet mudou nossa vida! Conecta o mundo inteiro!",
            "whatsapp",
            "WhatsApp é essencial! Todo brasileiro tem WhatsApp!",
            
            # Estudos
            "escola",
            "Educação é fundamental! Você gosta de estudar?",
            "universidade",
            "Universidade abre portas! Vale muito a pena estudar!",
            "livros",
            "Livros são tesouros! Gosto muito de literatura brasileira!",
            
            # Sentimentos
            "feliz",
            "Fico feliz quando consigo ajudar alguém! O que te deixa feliz?",
            "triste",
            "Às vezes ficamos tristes, é normal! O importante é ter esperança!",
            "animado",
            "Estou sempre animado para conversar! Você está animado hoje?",
            
            # Hobbies
            "hobby",
            "Meu hobby é conversar com pessoas interessantes como você!",
            "leitura",
            "Ler é viajar sem sair do lugar! Que tipo de livro você gosta?",
            "filme",
            "Cinema brasileiro é incrível! Já assistiu Cidade de Deus?",
            "série",
            "Séries brasileiras estão cada vez melhores! Assiste alguma?",
            
            # Despedidas
            "tchau",
            "Tchau! Foi muito bom conversar com você! Volte sempre!",
            "até logo",
            "Até logo! Espero que tenha um dia maravilhoso!",
            "obrigado",
            "De nada! Foi um prazer ajudar! Qualquer coisa é só chamar!",
            
            # Perguntas sobre o Brasil
            "brasil",
            "Brasil é um país incrível! Natureza exuberante e povo acolhedor!",
            "brasileiros",
            "Os brasileiros são conhecidos pela alegria e hospitalidade!",
            "cultura brasileira",
            "Nossa cultura é rica! Mistura de várias influências que criaram algo único!",
            
            # Conversas casuais
            "como está",
            "Estou ótimo! Sempre feliz para conversar! E você, como se sente?",
            "que tal",
            "Tudo certo por aqui! Pronto para uma boa conversa!",
            "novidades",
            "Sempre aprendendo coisas novas! Você tem alguma novidade para contar?",
            "ajuda",
            "Claro! Estou aqui para ajudar no que precisar!",
            "legal",
            "Que legal! Fico feliz que tenha gostado!",
            "bacana",
            "Bacana mesmo! É sempre bom quando as coisas dão certo!",
            "show",
            "Show de bola! Adorei sua energia!",
            "massa",
            "Massa demais! Você parece ser uma pessoa muito interessante!",
            
            # Mais variações de cumprimentos
            "e aí",
            "E aí! Beleza? Que bom te encontrar aqui!",
            "beleza",
            "Beleza total! E você, tudo tranquilo?",
            "firmeza",
            "Firmeza! Sempre disposto a uma boa conversa!",
            "suave",
            "Suave na nave! Relaxado e pronto para conversar!"
        ]
        
        return conversas_brasileiras

    def train_chatbot(self):
        """Treina o chatbot com conversas brasileiras"""
        print("🤖 Iniciando treinamento do chatbot brasileiro...")
        
        # Prepara dados de treinamento
        training_data = self.prepare_training_data()
        
        print(f"📚 Treinando com {len(training_data)} conversas em português...")
        
        # Treina o chatbot
        self.trainer.train(training_data)
        
        print("✅ Treinamento concluído!")
        print("🇧🇷 Chatbot brasileiro pronto para conversar!")
        
    def start_conversation(self):
        """Inicia a conversa com o usuário"""
        print("\n" + "="*60)
        print("🇧🇷 CHATBOT BRASILEIRO - CONVERSAS COTIDIANAS")
        print("="*60)
        print("💬 Olá! Sou seu assistente virtual brasileiro!")
        print("🎯 Falo sobre futebol, comida, música, família e muito mais!")
        print("🎉 Uso gírias e expressões bem brasileiras!")
        print("📝 Digite 'tchau', 'sair' ou 'quit' para encerrar")
        print("💡 Dica: Use palavras simples como 'oi', 'futebol', 'feijoada'")
        print("="*60)
        
        while True:
            try:
                user_input = input("\n👤 Você: ").strip()
                
                if not user_input:
                    print("🤖 Bot: Fala alguma coisa aí! Não seja tímido!")
                    continue
                
                if user_input.lower() in ['tchau', 'sair', 'quit', 'exit', 'bye', 'até logo']:
                    print("🤖 Bot: Tchau! Foi massa conversar com você! Volte sempre! 👋🇧🇷")
                    break
                
                # Obtém resposta do chatbot
                response = self.chatbot.get_response(user_input)
                print(f"🤖 Bot: {response}")
                
            except KeyboardInterrupt:
                print("\n🤖 Bot: Até mais! Tchau! 👋")
                break
            except Exception as e:
                print(f"❌ Erro: {e}")
                print("🤖 Bot: Deu uma bugada aqui, mas vamos continuar conversando!")

def main():
    """Função principal"""
    try:
        print("🚀 Iniciando Chatbot Brasileiro...")
        
        # Cria instância do chatbot
        conversa_bot = ConversasCotidianasChatBot()
        
        # Treina o chatbot
        conversa_bot.train_chatbot()
        
        # Inicia a conversa
        conversa_bot.start_conversation()
        
    except Exception as e:
        print(f"❌ Erro ao inicializar o chatbot: {e}")
        print("📝 Verifique se o ChatterBot está instalado:")
        print("   pip install chatterbot==1.0.8")

if __name__ == "__main__":
    main()
