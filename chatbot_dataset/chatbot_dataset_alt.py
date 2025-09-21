#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chatbot Dataset Alternativo - Daily Dialog (Sem Dependência Problemática)
Autor: André Kroetz Berger
Disciplina: Inteligência Artificial 2025/2
Universidade La Salle
"""

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import json
import urllib.request
import urllib.error

class DailyDialogChatBotAlt:
    def __init__(self):
        """Inicializa o chatbot com dataset Daily Dialog alternativo"""
        self.chatbot = ChatBot(
            'DailyDialogBotAlt',
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            database_uri='sqlite:///daily_dialog_alt_chatbot.sqlite3',
            logic_adapters=[
                {
                    'import_path': 'chatterbot.logic.BestMatch',
                    'default_response': 'That\'s interesting! Can you tell me more about that?',
                    'maximum_similarity_threshold': 0.80
                }
            ]
        )
        
        self.trainer = ListTrainer(self.chatbot)
        
    def get_daily_dialog_data(self):
        """Obtém dados de diálogo do dia a dia sem usar datasets library"""
        # Dados simulando o daily_dialog dataset
        daily_conversations = [
            # Conversas cotidianas em inglês
            ["Good morning! How are you today?", "Good morning! I'm doing well, thank you. How about you?"],
            ["What are your plans for the weekend?", "I'm thinking of going to the movies and maybe having dinner with friends."],
            ["How was your day at work?", "It was quite busy but productive. I finished several important projects."],
            ["What's the weather like today?", "It's sunny and warm outside. Perfect weather for outdoor activities!"],
            ["Do you have any hobbies?", "Yes, I enjoy reading books and playing guitar in my free time."],
            ["What kind of music do you like?", "I like various genres, but I'm especially fond of jazz and classical music."],
            ["Have you seen any good movies lately?", "Yes, I watched a great thriller last week. The plot was really engaging."],
            ["What do you usually have for breakfast?", "I typically have coffee, toast, and some fruit. Sometimes eggs on weekends."],
            ["How do you usually spend your evenings?", "I like to relax by reading or watching TV shows. Sometimes I cook dinner."],
            ["Do you exercise regularly?", "I try to go to the gym three times a week and take walks on other days."],
            
            # Conversas sobre trabalho
            ["How long have you been working here?", "I've been with this company for about three years now."],
            ["What do you do for a living?", "I work as a software engineer at a tech company downtown."],
            ["Do you enjoy your job?", "Yes, I find it challenging and rewarding. I love solving complex problems."],
            ["What time do you usually start work?", "I usually start around 9 AM and finish by 6 PM."],
            ["Do you work from home sometimes?", "Yes, we have a flexible policy. I work from home twice a week."],
            
            # Conversas sobre comida
            ["What's your favorite type of cuisine?", "I really enjoy Italian food, especially pasta dishes and pizza."],
            ["Do you like to cook?", "Yes, I love cooking! It's relaxing and I enjoy trying new recipes."],
            ["Have you tried any new restaurants recently?", "Yes, I went to a great Mexican restaurant last week. The tacos were amazing."],
            ["What's your favorite dessert?", "I have a weakness for chocolate cake and ice cream."],
            ["Do you prefer eating at home or going out?", "I enjoy both, but I prefer cooking at home during weekdays."],
            
            # Conversas sobre viagens
            ["Do you like to travel?", "Absolutely! I love exploring new places and experiencing different cultures."],
            ["What's the most interesting place you've visited?", "I really enjoyed my trip to Japan. The culture and food were fascinating."],
            ["Do you prefer beach or mountain vacations?", "I like both, but I think I prefer mountains for the hiking opportunities."],
            ["How do you usually plan your trips?", "I research online, read travel blogs, and ask friends for recommendations."],
            ["What's on your travel bucket list?", "I'd love to visit New Zealand and go on a photography tour there."],
            
            # Conversas sobre família e amigos
            ["Do you have any siblings?", "Yes, I have an older brother and a younger sister."],
            ["How often do you see your family?", "I try to visit them at least once a month for dinner."],
            ["What do you like to do with your friends?", "We often go out for coffee, watch movies, or have game nights."],
            ["Are you close to your family?", "Yes, we're very close. We support each other through everything."],
            ["How did you meet your best friend?", "We met in college and have been friends for over ten years now."],
            
            # Conversas sobre tecnologia
            ["Do you use social media much?", "I use it occasionally to keep in touch with friends and family."],
            ["What's your favorite app on your phone?", "I really like the podcast app. I listen to educational content daily."],
            ["How has technology changed your life?", "It's made communication easier and given me access to unlimited information."],
            ["Do you prefer reading books or e-books?", "I still prefer physical books, but e-books are convenient for travel."],
            ["What do you think about artificial intelligence?", "I think it's fascinating and has great potential to help humanity."],
            
            # Conversas sobre saúde e bem-estar
            ["How do you stay healthy?", "I try to eat balanced meals, exercise regularly, and get enough sleep."],
            ["Do you have any stress management techniques?", "I practice meditation and deep breathing exercises when I feel stressed."],
            ["What time do you usually go to bed?", "I try to be in bed by 11 PM to get a good night's sleep."],
            ["Do you take any vitamins or supplements?", "I take vitamin D and omega-3 supplements, especially during winter."],
            ["How important is work-life balance to you?", "Very important. I make sure to disconnect from work during evenings and weekends."],
            
            # Conversas sobre aprendizado
            ["Are you learning anything new lately?", "Yes, I'm taking an online course in digital photography."],
            ["What's the best way to learn a new skill?", "I think consistent practice and learning from others is key."],
            ["Do you enjoy reading?", "Yes, I love reading both fiction and non-fiction books."],
            ["What's the last book you read?", "I recently finished a biography of Steve Jobs. It was very inspiring."],
            ["Do you prefer learning online or in person?", "Both have advantages, but I prefer in-person for interactive subjects."],
            
            # Conversas sobre entretenimento
            ["What do you do in your free time?", "I enjoy painting, listening to music, and spending time in nature."],
            ["Do you play any musical instruments?", "I play piano and I'm learning to play the ukulele."],
            ["What's your favorite TV show?", "I really enjoy documentaries about nature and science."],
            ["Do you like to go to concerts?", "Yes, I love live music. The energy and atmosphere are amazing."],
            ["What kind of books do you prefer?", "I enjoy mystery novels and biographies of interesting people."],
            
            # Conversas sobre clima e estações
            ["What's your favorite season?", "I love autumn because of the beautiful colors and comfortable temperatures."],
            ["How do you feel about rainy days?", "I actually enjoy them. It's nice to stay inside and read a book."],
            ["Do you prefer hot or cold weather?", "I prefer mild temperatures, not too hot or too cold."],
            ["What do you like to do in summer?", "I enjoy going to the beach, having barbecues, and outdoor concerts."],
            ["How do you stay warm in winter?", "I like to drink hot tea, wear cozy sweaters, and spend time by the fireplace."],
            
            # Conversas sobre metas e sonhos
            ["What are your goals for this year?", "I want to learn a new language and improve my cooking skills."],
            ["Do you have any long-term dreams?", "I'd love to start my own business someday and travel the world."],
            ["What motivates you?", "The desire to grow as a person and make a positive impact on others."],
            ["How do you define success?", "Success to me is being happy, healthy, and surrounded by people I love."],
            ["What advice would you give to your younger self?", "Don't be afraid to take risks and always believe in yourself."],
            
            # Conversas sobre problemas cotidianos
            ["I'm feeling a bit tired today.", "Maybe you should take a short break and have some coffee or tea."],
            ["I can't decide what to wear.", "Check the weather forecast and choose something comfortable."],
            ["I'm having trouble sleeping lately.", "Try avoiding screens before bedtime and create a relaxing routine."],
            ["I'm stressed about work.", "Take some deep breaths and try to focus on one task at a time."],
            ["I'm bored and don't know what to do.", "How about trying a new hobby or calling a friend to catch up?"],
            
            # Conversas de cortesia
            ["Thank you for your help.", "You're very welcome! I'm glad I could assist you."],
            ["Sorry, I'm running late.", "No problem at all. These things happen sometimes."],
            ["Excuse me, could you help me?", "Of course! What do you need help with?"],
            ["Have a great day!", "Thank you! You have a wonderful day too!"],
            ["Nice to meet you.", "It's nice to meet you too! Welcome!"],
            
            # Conversas sobre transporte
            ["How do you usually get to work?", "I take the subway. It's faster than driving in traffic."],
            ["Do you have a car?", "Yes, but I prefer using public transportation in the city."],
            ["What's the traffic like today?", "It seems heavier than usual. Maybe there's construction somewhere."],
            ["Do you enjoy driving?", "I do, especially on long road trips with good music."],
            ["Have you ever taken a train trip?", "Yes, I took a scenic train ride through the mountains last year."],
            
            # Conversas sobre compras
            ["Do you like shopping?", "I enjoy it occasionally, especially for books and clothes."],
            ["Where do you usually buy groceries?", "I shop at the local supermarket, but I also visit the farmer's market."],
            ["Do you prefer shopping online or in stores?", "For clothes I prefer stores, but for electronics I usually shop online."],
            ["What's the last thing you bought?", "I recently bought a new book and some plants for my apartment."],
            ["Do you look for sales when shopping?", "Yes, I always compare prices and look for good deals."]
        ]
        
        return daily_conversations
    
    def prepare_training_data(self):
        """Prepara os dados de treinamento"""
        print("Preparando dados de treinamento com conversas cotidianas...")
        
        daily_conversations = self.get_daily_dialog_data()
        training_data = []
        
        # Converte as conversas em formato de treinamento
        for conversation in daily_conversations:
            if len(conversation) >= 2:
                training_data.extend(conversation)
        
        print(f"Preparado {len(training_data)//2} pares de conversação.")
        return training_data
    
    def train_chatbot(self):
        """Treina o chatbot com os dados preparados"""
        print("Iniciando treinamento do chatbot...")
        
        # Prepara dados de treinamento
        training_data = self.prepare_training_data()
        
        if training_data:
            print(f"Treinando com {len(training_data)//2} pares de conversação...")
            self.trainer.train(training_data)
            print("Treinamento concluído!")
        else:
            print("Nenhum dado de treinamento disponível.")
    
    def start_conversation(self):
        """Inicia a conversa com o usuário"""
        print("=" * 60)
        print("📅 CHATBOT DAILY DIALOG - CONVERSAÇÃO COTIDIANA 📅")
        print("=" * 60)
        print("Hello! I'm a chatbot trained on daily conversations.")
        print("I can chat about everyday topics and situations!")
        print("💡 Try topics like: work, food, travel, weather, hobbies")
        print("Type 'exit' to end our conversation.")
        print("-" * 60)
        
        while True:
            try:
                user_input = input("\n👤 You: ")
                
                if user_input.lower() in ['exit', 'quit', 'bye', 'goodbye']:
                    print("\n🤖 Bot: It was great talking with you! Goodbye! 👋")
                    break
                
                if user_input.strip() == "":
                    print("\n🤖 Bot: Hi there! Please type something so we can chat.")
                    continue
                
                # Obtém resposta do chatbot
                response = self.chatbot.get_response(user_input)
                print(f"\n🤖 Bot: {response}")
                
            except KeyboardInterrupt:
                print("\n\n🤖 Bot: Conversation interrupted. See you later!")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}")
                print("Let's try to continue our conversation...")

def main():
    """Função principal"""
    try:
        # Cria instância do chatbot
        dialog_bot = DailyDialogChatBotAlt()
        
        # Verifica se já foi treinado
        db_path = "daily_dialog_alt_chatbot.sqlite3"
        if not os.path.exists(db_path):
            dialog_bot.train_chatbot()
        else:
            print("Database found. Loading chatbot...")
        
        # Inicia conversa
        dialog_bot.start_conversation()
        
    except Exception as e:
        print(f"❌ Error initializing chatbot: {e}")
        print("Please check if all dependencies are installed.")

if __name__ == "__main__":
    main()
