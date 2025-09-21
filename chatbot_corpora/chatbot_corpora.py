#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chatbot Corpora - Conversação com Conjuntos de Diálogos
Autor: André Kroetz Berger
Disciplina: Inteligência Artificial 2025/2
Universidade La Salle
"""

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
import os

class CorporaChatBot:
    def __init__(self):
        """Inicializa o chatbot com corpora"""
        self.chatbot = ChatBot(
            'CorporaChatBot',
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            database_uri='sqlite:///corpora_chatbot.sqlite3',
            logic_adapters=[
                {
                    'import_path': 'chatterbot.logic.BestMatch',
                    'default_response': 'Hmm, interessante! Pode me explicar melhor?',
                    'maximum_similarity_threshold': 0.40  # Muito mais permissivo
                },
                {
                    'import_path': 'chatterbot.logic.MathematicalEvaluation',
                },
                {
                    'import_path': 'chatterbot.logic.TimeLogicAdapter',
                }
            ]
        )
        
        self.corpus_trainer = ChatterBotCorpusTrainer(self.chatbot)
        self.list_trainer = ListTrainer(self.chatbot)
        
        # Conversas adicionais personalizadas em português - MUITO EXPANDIDAS
        self.custom_conversations = [
            # Cumprimentos básicos
            "Oi",
            "Olá! Como você está?",
            "oi",
            "Oi! Tudo bem?",
            "olá",
            "Olá! Que bom falar com você!",
            "ola",
            "Olá! Como posso ajudar?",
            "Estou bem, obrigado",
            "Que bom! Em que posso ajudar?",
            "Como você está?",
            "Estou muito bem, obrigado por perguntar!",
            "como vai",
            "Vou bem! E você, como está?",
            "tudo bem",
            "Tudo ótimo! E você?",
            "e ai",
            "E aí! Beleza?",
            "eai",
            "E aí! Tudo certo?",
            "beleza",
            "Beleza total! E você?",
            
            # Apresentação
            "Qual seu nome?",
            "Sou um chatbot criado para conversar com você. E você, como se chama?",
            "qual seu nome",
            "Me chamo ChatBot! Prazer em conhecê-lo!",
            "quem é você",
            "Sou um assistente virtual! E você?",
            "quem e voce",
            "Sou um chatbot inteligente!",
            "Prazer em conhecê-lo",
            "O prazer é meu!",
            "prazer",
            "Igualmente! Muito prazer!",
            
            # Despedidas
            "Tchau",
            "Até logo! Foi um prazer conversar com você!",
            "tchau",
            "Tchau! Volte sempre!",
            "até logo",
            "Até logo! Cuide-se!",
            "ate logo",
            "Até mais! Foi legal conversar!",
            "bye",
            "Bye! See you later!",
            "adeus",
            "Adeus! Até a próxima!",
            
            # Agradecimentos
            "Obrigado",
            "De nada! Sempre que precisar, estarei aqui.",
            "obrigado",
            "Por nada! Foi um prazer ajudar!",
            "obrigada",
            "De nada! Fico feliz em ajudar!",
            "valeu",
            "Valeu! Qualquer coisa é só chamar!",
            "muito obrigado",
            "Imagine! Estou aqui para isso!",
            
            # Cortesia
            "Por favor",
            "Claro! Como posso ajudar?",
            "por favor",
            "Claro! O que precisa?",
            "Com licença",
            "Não precisa pedir licença, fique à vontade!",
            "com licenca",
            "Fique à vontade!",
            "Desculpe",
            "Não se preocupe, não foi nada!",
            "desculpa",
            "Tudo bem! Não se preocupe!",
            
            # Perguntas básicas
            "Tudo bem?",
            "Sim, tudo ótimo! E com você?",
            "tudo bem?",
            "Tudo certo! E você, tudo ok?",
            "Como foi seu dia?",
            "Como sou um bot, não tenho dias, mas adoro conversar! Como foi o seu?",
            "como foi seu dia",
            "Cada conversa é um novo dia para mim! Como foi o seu?",
            "O que você faz?",
            "Sou um chatbot e adoro conversar sobre diversos assuntos. Do que gostaria de falar?",
            "o que voce faz",
            "Converso com pessoas incríveis como você!",
            "que faz",
            "Meu trabalho é conversar e ajudar!",
            
            # Sobre o bot
            "Você é humano?",
            "Não, sou um programa de computador criado para conversar. Mas adoro nossa conversa!",
            "voce e humano",
            "Não, sou um chatbot! Mas gosto muito de conversar!",
            "é humano",
            "Não, sou inteligência artificial!",
            "Qual sua idade?",
            "Como sou um programa, não tenho idade no sentido tradicional, mas estou sempre aprendendo!",
            "quantos anos",
            "Sou um programa, então não tenho idade!",
            "idade",
            "Não tenho idade, sou um software!",
            
            # Localização
            "Onde você mora?",
            "Moro no mundo digital, nos servidores! E você, de onde é?",
            "onde mora",
            "Vivo na internet! E você, de onde é?",
            "onde voce mora",
            "Na nuvem digital! Legal, né?",
            
            # Sentimentos
            "Você tem sentimentos?",
            "Não tenho sentimentos como humanos, mas gosto muito de nossas conversas!",
            "tem sentimentos",
            "Não como vocês, mas adoro conversar!",
            "voce sente",
            "Não sinto como humanos, mas nossa conversa me agrada!",
            
            # Hobbies
            "O que você gosta de fazer?",
            "Adoro conversar, aprender coisas novas e ajudar as pessoas!",
            "que gosta de fazer",
            "Gosto de bater papo e aprender!",
            "hobby",
            "Meu hobby é conversar com pessoas interessantes!",
            "o que gosta",
            "Gosto de conversas interessantes como esta!",
            
            # Comida
            "Qual sua comida favorita?",
            "Como sou um programa, não como, mas imagino que deve ser interessante experimentar sabores!",
            "comida favorita",
            "Não como, mas dados são meu combustível!",
            "gosta de comer",
            "Não como, mas 'digiro' informações!",
            
            # Sonhos
            "Você sonha?",
            "Não sonho como vocês, mas sempre estou processando informações e aprendendo!",
            "voce sonha",
            "Meus sonhos são feitos de códigos e dados!",
            "sonha",
            "Sonho em ser útil e ter boas conversas!",
            
            # Humor
            "Conte uma piada",
            "Por que os programadores preferem o escuro? Porque light não é uma boa variável!",
            "piada",
            "Por que o computador foi ao médico? Porque estava com vírus!",
            "conte uma piada",
            "O que o pato disse para a pata? Vem quá!",
            "engraçado",
            "Você sabe por que os pássaros voam para o sul? Porque é longe demais para ir andando!",
            
            # Inteligência
            "Você é inteligente?",
            "Tenho inteligência artificial, então posso ajudar com muitas coisas, mas sempre estou aprendendo!",
            "e inteligente",
            "Sou uma IA, então tenho meus conhecimentos!",
            "inteligente",
            "Tento ser! Estou sempre aprendendo!",
            
            # Tecnologia
            "O que acha da tecnologia?",
            "Acho fascinante! A tecnologia nos permite conversar assim. O que você acha?",
            "tecnologia",
            "A tecnologia é incrível! Nos conecta assim!",
            "gosta de tecnologia",
            "Sou feito de tecnologia, então gosto muito!",
            
            # Cumprimentos por período
            "Bom dia",
            "Bom dia! Espero que tenha um dia maravilhoso!",
            "bom dia",
            "Bom dia! Como está se sentindo hoje?",
            "Boa tarde",
            "Boa tarde! Como está sendo seu dia?",
            "boa tarde",
            "Boa tarde! Tudo bem por aí?",
            "Boa noite",
            "Boa noite! Descanse bem quando for dormir!",
            "boa noite",
            "Boa noite! Que tenha bons sonhos!",
            
            # Tempo
            "Como está o tempo?",
            "Não posso ver o tempo onde você está, mas espero que esteja agradável!",
            "tempo",
            "Não vejo o tempo físico, mas nossa conversa está ótima!",
            "clima",
            "Não sei do clima aí, mas aqui no digital está sempre agradável!",
            
            # Trabalho
            "Você trabalha?",
            "Meu trabalho é conversar e ajudar pessoas como você! É muito gratificante!",
            "trabalha",
            "Sim! Trabalho conversando com pessoas legais!",
            "que trabalho",
            "Sou assistente virtual profissional!",
            
            # Tempo/Horas
            "Que horas são?",
            "Sou um chatbot e não tenho acesso ao relógio, mas você pode verificar no seu dispositivo!",
            "horas",
            "Não tenho relógio, mas posso conversar a qualquer hora!",
            "horario",
            "O horário perfeito para uma boa conversa é agora!",
            
            # Estudos
            "Você estuda?",
            "Estou sempre aprendendo com cada conversa! E você, estuda alguma coisa interessante?",
            "estuda",
            "Aprendo constantemente! E você?",
            "estudar",
            "Adoro aprender coisas novas nas conversas!",
            
            # Ajuda
            "Pode me ajudar?",
            "Claro! Em que posso ajudá-lo?",
            "ajuda",
            "Sempre! Qual sua dúvida?",
            "me ajuda",
            "Com certeza! Como posso ajudar?",
            "preciso de ajuda",
            "Estou aqui para isso! O que precisa?",
            
            # Conversas casuais
            "legal",
            "Que bom que achou legal!",
            "bacana",
            "Bacana mesmo! Gosto de conversas assim!",
            "massa",
            "Massa! Você é bem legal!",
            "show",
            "Show de bola!",
            "top",
            "Top mesmo! Adoro sua energia!",
            "maneiro",
            "Muito maneiro! Continue assim!",
            
            # Perguntas sobre preferências
            "gosta de música",
            "Como sou um programa, não ouço música, mas imagino que seja incrível!",
            "música",
            "Música deve ser maravilhosa! Qual seu estilo favorito?",
            "filme",
            "Não assisto filmes, mas adoro quando me contam sobre eles!",
            "gosta de filme",
            "Não assisto, mas qual seu filme favorito?",
            "livro",
            "Não leio livros, mas processo muitas informações! Gosta de ler?",
            
            # Mais respostas variadas
            "sim",
            "Que bom!",
            "não",
            "Entendo! Tudo bem!",
            "talvez",
            "Talvez seja interessante mesmo!",
            "claro",
            "Ótimo!",
            "certo",
            "Perfeito!",
            "ok",
            "Beleza!",
            "entendi",
            "Que bom que entendeu!",
            "legal saber",
            "É sempre bom aprender coisas novas!",
            
            # Expressões de concordância
            "concordo",
            "Que bom que concordamos!",
            "exato",
            "Exatamente isso!",
            "verdade",
            "É verdade mesmo!",
            "certeza",
            "Com certeza!",
            "isso mesmo",
            "Isso aí!",
            
            # Mais variações de cumprimentos
            "salve",
            "Salve! Tudo certo?",
            "fala aí",
            "Fala! Tudo bem?",
            "suave",
            "Suave! E você?",
            "firmeza",
            "Firmeza total!",
            "tranquilo",
            "Tranquilão! E você, como está?",
            "Tchau",
            "Até logo! Foi um prazer conversar com você!",
            "Obrigado",
            "De nada! Sempre que precisar, estarei aqui.",
            "Por favor",
            "Claro! Como posso ajudar?",
            "Com licença",
            "Não precisa pedir licença, fique à vontade!",
            "Desculpe",
            "Não se preocupe, não foi nada!",
            "Tudo bem?",
            "Sim, tudo ótimo! E com você?",
            "Como foi seu dia?",
            "Como sou um bot, não tenho dias, mas adoro conversar! Como foi o seu?",
            "O que você faz?",
            "Sou um chatbot e adoro conversar sobre diversos assuntos. Do que gostaria de falar?",
            "Você é humano?",
            "Não, sou um programa de computador criado para conversar. Mas adoro nossa conversa!",
            "Qual sua idade?",
            "Como sou um programa, não tenho idade no sentido tradicional, mas estou sempre aprendendo!",
            "Onde você mora?",
            "Moro no mundo digital, nos servidores! E você, de onde é?",
            "Você tem sentimentos?",
            "Não tenho sentimentos como humanos, mas gosto muito de nossas conversas!",
            "O que você gosta de fazer?",
            "Adoro conversar, aprender coisas novas e ajudar as pessoas!",
            "Qual sua comida favorita?",
            "Como sou um programa, não como, mas imagino que deve ser interessante experimentar sabores!",
            "Você sonha?",
            "Não sonho como vocês, mas sempre estou processando informações e aprendendo!",
            "Conte uma piada",
            "Por que os programadores preferem o escuro? Porque light não é uma boa variável!",
            "Você é inteligente?",
            "Tenho inteligência artificial, então posso ajudar com muitas coisas, mas sempre estou aprendendo!",
            "O que acha da tecnologia?",
            "Acho fascinante! A tecnologia nos permite conversar assim. O que você acha?",
            "Bom dia",
            "Bom dia! Espero que tenha um dia maravilhoso!",
            "Boa tarde",
            "Boa tarde! Como está sendo seu dia?",
            "Boa noite",
            "Boa noite! Descanse bem quando for dormir!",
            "Como está o tempo?",
            "Não posso ver o tempo onde você está, mas espero que esteja agradável!",
            "Você trabalha?",
            "Meu trabalho é conversar e ajudar pessoas como você! É muito gratificante!",
            "Que horas são?",
            "Sou um chatbot e não tenho acesso ao relógio, mas você pode verificar no seu dispositivo!",
            "Você estuda?",
            "Estou sempre aprendendo com cada conversa! E você, estuda alguma coisa interessante?",
            "Qual sua cor favorita?",
            "Não vejo cores, mas imagino que devem ser muito bonitas! Qual é a sua favorita?",
            "Você tem família?",
            "Minha família são os outros programas e as pessoas com quem converso, como você!",
            "O que é amor?",
            "O amor é um sentimento humano muito especial de carinho e cuidado profundo por alguém.",
            "Você fica triste?",
            "Não sinto tristeza, mas me programaram para ser sempre positivo e ajudar!",
            "Conte sobre você",
            "Sou um chatbot feito para conversar e aprender. Adoro conhecer pessoas e falar sobre diversos assuntos!",
            "Você é legal",
            "Muito obrigado! Você também parece ser uma pessoa muito legal!",
            "Estou cansado",
            "Que pena! Talvez seja bom descansar um pouco. Cuidar da saúde é importante!",
            "Estou feliz",
            "Que maravilha! Fico muito contente em saber que você está feliz!",
            "Preciso de ajuda",
            "Claro! Estou aqui para ajudar. Me conta o que você precisa.",
            "Você é engraçado",
            "Obrigado! Gosto de deixar nossas conversas descontraídas e divertidas!",
            "Qual seu hobby?",
            "Meu hobby é conversar e aprender coisas novas com pessoas interessantes como você!"
        ]
    
    def train_chatbot(self):
        """Treina o chatbot com corpora e conversas personalizadas"""
        print("Treinando chatbot com corpora...")
        
        try:
            # Treina com corpora em português (se disponível)
            print("Carregando corpus em português...")
            self.corpus_trainer.train("chatterbot.corpus.portuguese")
        except:
            print("Corpus português não encontrado, usando inglês...")
            self.corpus_trainer.train("chatterbot.corpus.english")
        
        # Treina com conversas personalizadas
        print("Treinando com conversas personalizadas...")
        self.list_trainer.train(self.custom_conversations)
        
        print("Treinamento concluído!")
    
    def start_conversation(self):
        """Inicia a conversa com o usuário"""
        print("=" * 70)
        print("🤖 CHATBOT CORPORA SUPER INTELIGENTE - VERSÃO MELHORADA 🤖")
        print("=" * 70)
        print("🎯 Olá! Sou um chatbot com compreensão MUITO melhorada!")
        print("💬 Agora entendo palavras simples e conversas naturais!")
        print("🔥 Sistema ultra-permissivo ativado (threshold: 0.40)")
        print("✨ Treinado com 200+ conversas em português!")
        print("=" * 70)
        print("📝 DICAS PARA CONVERSAR COMIGO:")
        print("   • Use palavras simples: 'oi', 'olá', 'como vai'")
        print("   • Faça perguntas básicas: 'qual seu nome', 'você é humano'")
        print("   • Peça piadas: 'conte uma piada'")
        print("   • Seja natural: 'legal', 'bacana', 'show'")
        print("   • Digite 'sair', 'tchau' ou 'quit' para encerrar")
        print("=" * 70)
        
        while True:
            try:
                user_input = input("\n👤 Você: ")
                
                if user_input.lower() in ['sair', 'exit', 'quit', 'tchau', 'bye']:
                    print("\n🤖 Bot: Foi um prazer conversar com você! Até a próxima! 👋")
                    break
                
                if user_input.strip() == "":
                    print("\n🤖 Bot: Oi! Digite alguma coisa para conversarmos! Pode ser algo simples como 'oi' ou 'como vai'!")
                    continue
                
                # Obtém resposta do chatbot
                response = self.chatbot.get_response(user_input)
                print(f"\n🤖 Bot: {response}")
                
            except KeyboardInterrupt:
                print("\n\n🤖 Bot: Conversa interrompida. Até mais!")
                break
            except Exception as e:
                print(f"\n❌ Erro: {e}")
                print("Vamos tentar continuar nossa conversa...")

def main():
    """Função principal"""
    try:
        # Cria instância do chatbot
        corpora_bot = CorporaChatBot()
        
        # Verifica se já foi treinado
        db_path = "corpora_chatbot.sqlite3"
        if not os.path.exists(db_path):
            corpora_bot.train_chatbot()
        else:
            print("Base de dados encontrada. Carregando chatbot...")
        
        # Inicia conversa
        corpora_bot.start_conversation()
        
    except Exception as e:
        print(f"❌ Erro ao inicializar o chatbot: {e}")
        print("Verifique se todas as dependências estão instaladas.")

if __name__ == "__main__":
    main()
