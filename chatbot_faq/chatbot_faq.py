#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chatbot FAQ - Manutenção de Notebooks
Autor: André Kroetz Berger
Disciplina: Inteligência Artificial 2025/2
Universidade La Salle
"""

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import re
from difflib import SequenceMatcher

class NotebookMaintenanceFAQ:
    def __init__(self):
        """Inicializa o chatbot FAQ sobre manutenção de notebooks"""
        self.chatbot = ChatBot(
            'NotebookMaintenanceFAQ',
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            database_uri='sqlite:///notebook_faq.sqlite3',
            logic_adapters=[
                {
                    'import_path': 'chatterbot.logic.BestMatch',
                    'default_response': 'Desculpe, não encontrei informações específicas sobre isso. Tente perguntar sobre: limpeza, bateria, superaquecimento, tela, WiFi, ou problemas gerais.',
                    'maximum_similarity_threshold': 0.60  # Ainda mais flexível
                }
            ]
        )
        
        self.trainer = ListTrainer(self.chatbot)
        self.knowledge_base = self._create_knowledge_base()
        self.keywords_map = self._create_keywords_map()
        
    def _create_keywords_map(self):
        """Cria mapeamento de palavras-chave para respostas"""
        return {
            # Limpeza
            'limpar|limpeza|sujo|suja|limpo|higiene': 
                "Use um pano de microfibra levemente umedecido com água destilada. Para o teclado, use ar comprimido entre as teclas.",
            
            'tela|display|monitor|tela': 
                "Use um pano de microfibra levemente umedecido com água destilada. Nunca borrife líquido diretamente na tela.",
            
            'teclado|tecla|teclas': 
                "Desligue o notebook, vire-o de cabeça para baixo e balance suavemente. Use ar comprimido entre as teclas.",
            
            'alcool|álcool|isopropilico': 
                "Use álcool isopropílico 70% apenas no gabinete externo. Nunca use na tela ou componentes internos.",
            
            'cooler|ventoinha|ventilador|ventilação': 
                "Abra o notebook com cuidado, use ar comprimido para remover poeira das ventoinhas e dissipadores de calor.",
            
            # Temperatura
            'quente|esquenta|superaquecimento|temperatura|calor|aquecimento': 
                "Verifique se as ventoinhas estão funcionando, limpe-as, use uma base refrigerada e evite superfícies que bloqueiem a ventilação.",
            
            'desliga|desligando|para': 
                "Sim, é um mecanismo de proteção. Limpe as ventoinhas, verifique a pasta térmica e mantenha as saídas de ar desobstruídas.",
            
            'pasta.termica|pasta.térmica|thermal': 
                "Se o notebook esquenta muito mesmo após limpeza, ou se a pasta tem mais de 2-3 anos, considere a troca. Pastas como Arctic MX-4 são boas opções.",
            
            # Bateria
            'bateria|battery|carga|carregador|energia': 
                "Evite descargas completas, mantenha entre 20-80%, não deixe sempre conectado na tomada se possível.",
            
            'viciada|viciado|autonomia|durando.pouco': 
                "Se a autonomia diminuiu drasticamente, o sistema indica desgaste da bateria ou ela não carrega adequadamente.",
            
            'tomada|carregando|sempre.conectado': 
                "Notebooks modernos têm proteção, mas idealmente alterne entre bateria e tomada para manter a saúde da bateria.",
            
            # Problemas gerais
            'não.liga|nao.liga|não.funciona|nao.funciona|morto': 
                "Teste o carregador, pressione o botão power por 15s, remova a bateria se possível e teste só na tomada.",
            
            'lento|devagar|travando|trava|lag|demora': 
                "Limpe arquivos temporários, desinstale programas desnecessários, verifique por malware e considere adicionar RAM ou SSD.",
            
            # Conectividade
            'wifi|wi-fi|internet|rede|conexao|conectar': 
                "Reinicie o roteador, esqueça e reconecte a rede, atualize drivers de rede ou redefina configurações de rede.",
            
            'bluetooth|blue.tooth': 
                "Verifique se está habilitado, atualize drivers, remova e reconecte dispositivos, ou reinicie o serviço Bluetooth.",
            
            'usb|porta|conector': 
                "Teste com diferentes dispositivos, atualize drivers USB, verifique no Gerenciador de Dispositivos e reinicie o sistema.",
            
            # Tela
            'pixel|pixels.mortos|pontos|manchas|tela.ruim': 
                "Pixels mortos são defeito permanente. Se muitos, pode precisar trocar a tela. Alguns poucos são toleráveis.",
            
            'amarela|amarelada|cor.estranha|cores': 
                "Pode ser desgaste natural, configuração de cor ou filtro de luz azul ativado. Verifique as configurações primeiro.",
            
            'brilho|escuro|claro': 
                "Use o brilho mínimo confortável. O display consome muita energia, então reduzir o brilho ajuda bastante.",
            
            # Áudio
            'som|audio|áudio|microfone|alto.falante': 
                "Verifique o volume, dispositivos de reprodução padrão, drivers de áudio e se não está no mudo.",
            
            'sem.som|mudo|silencioso': 
                "Verifique o volume, dispositivos de reprodução padrão, drivers de áudio e se não está no mudo.",
            
            # Hardware
            'ram|memoria|memória': 
                "Se o sistema fica lento, usa muito arquivo de paginação ou o Task Manager mostra uso alto da RAM constantemente.",
            
            'ssd|hd|disco|storage|armazenamento': 
                "SSD é muito mais rápido, consome menos energia e é mais resistente a impactos que o HD tradicional.",
            
            'backup|copia|segurança': 
                "Sim, sempre! Use serviços na nuvem, HDs externos ou faça imagem do sistema periodicamente.",
            
            # Manutenção
            'manutencao|manutenção|cuidados|preventiva': 
                "Limpeza regular, backup de dados, atualizações do sistema, antivírus, e cuidados físicos com o equipamento.",
            
            'virus|malware|antivirus|segurança': 
                "Use antivírus atualizado, evite sites suspeitos, não baixe arquivos duvidosos e mantenha o sistema atualizado.",
            
            'atualizar|update|driver|drivers': 
                "Use o Windows Update, site do fabricante do notebook, ou ferramentas como Driver Booster com cuidado."
        }
    
    def smart_response(self, user_input):
        """Sistema inteligente de resposta usando palavras-chave"""
        user_input_clean = re.sub(r'[^\w\s]', ' ', user_input.lower())
        user_input_clean = re.sub(r'\s+', ' ', user_input_clean).strip()
        
        best_match_score = 0
        best_response = None
        
        for keywords, response in self.keywords_map.items():
            # Divide as palavras-chave por |
            keyword_options = keywords.split('|')
            
            for keyword_pattern in keyword_options:
                # Substitui . por espaço para padrões como "pasta.termica"
                keyword_pattern = keyword_pattern.replace('.', r'\s*')
                
                # Verifica se o padrão existe na entrada do usuário
                if re.search(keyword_pattern, user_input_clean):
                    # Calcula similaridade usando SequenceMatcher
                    similarity = SequenceMatcher(None, keyword_pattern.replace(r'\s*', ' '), user_input_clean).ratio()
                    
                    if similarity > best_match_score:
                        best_match_score = similarity
                        best_response = response
        
        return best_response, best_match_score
        
    def _create_knowledge_base(self):
        """Cria a base de conhecimento com 50+ pares pergunta/resposta"""
        return [
            # Limpeza básica - Múltiplas variações
            "Como limpar a tela do notebook?",
            "Use um pano de microfibra levemente umedecido com água destilada. Nunca borrife líquido diretamente na tela.",
            
            "Como limpo a tela?",
            "Use um pano de microfibra levemente umedecido com água destilada. Nunca borrife líquido diretamente na tela.",
            
            "Limpar tela notebook",
            "Use um pano de microfibra levemente umedecido com água destilada. Nunca borrife líquido diretamente na tela.",
            
            "Tela suja como limpar?",
            "Use um pano de microfibra levemente umedecido com água destilada. Nunca borrife líquido diretamente na tela.",
            
            "Como limpar o teclado?",
            "Desligue o notebook, vire-o de cabeça para baixo e balance suavemente. Use ar comprimido entre as teclas e pano úmido para a superfície.",
            
            "Limpar teclado",
            "Desligue o notebook, vire-o de cabeça para baixo e balance suavemente. Use ar comprimido entre as teclas e pano úmido para a superfície.",
            
            "Teclado sujo",
            "Desligue o notebook, vire-o de cabeça para baixo e balance suavemente. Use ar comprimido entre as teclas e pano úmido para a superfície.",
            
            "Como limpo o teclado?",
            "Desligue o notebook, vire-o de cabeça para baixo e balance suavemente. Use ar comprimido entre as teclas e pano úmido para a superfície.",
            
            "Posso usar álcool para limpar o notebook?",
            "Use álcool isopropílico 70% apenas no gabinete externo. Nunca use na tela ou componentes internos.",
            
            "Álcool no notebook",
            "Use álcool isopropílico 70% apenas no gabinete externo. Nunca use na tela ou componentes internos.",
            
            "Pode usar álcool?",
            "Use álcool isopropílico 70% apenas no gabinete externo. Nunca use na tela ou componentes internos.",
            
            "Como limpar as ventoinhas?",
            "Abra o notebook com cuidado, use ar comprimido para remover poeira das ventoinhas e dissipadores de calor.",
            
            "Limpar cooler",
            "Abra o notebook com cuidado, use ar comprimido para remover poeira das ventoinhas e dissipadores de calor.",
            
            "Ventilador sujo",
            "Abra o notebook com cuidado, use ar comprimido para remover poeira das ventoinhas e dissipadores de calor.",
            
            "Com que frequência devo limpar internamente?",
            "Recomenda-se limpeza interna a cada 6-12 meses, dependendo do ambiente de uso.",
            
            "Quando limpar por dentro?",
            "Recomenda-se limpeza interna a cada 6-12 meses, dependendo do ambiente de uso.",
            
            # Problemas de superaquecimento - Múltiplas variações
            "Meu notebook está esquentando muito, o que fazer?",
            "Verifique se as ventoinhas estão funcionando, limpe-as, use uma base refrigerada e evite superfícies que bloqueiem a ventilação.",
            
            "Notebook muito quente",
            "Verifique se as ventoinhas estão funcionando, limpe-as, use uma base refrigerada e evite superfícies que bloqueiem a ventilação.",
            
            "Esquentando demais",
            "Verifique se as ventoinhas estão funcionando, limpe-as, use uma base refrigerada e evite superfícies que bloqueiem a ventilação.",
            
            "Superaquecimento",
            "Verifique se as ventoinhas estão funcionando, limpe-as, use uma base refrigerada e evite superfícies que bloqueiem a ventilação.",
            
            "Notebook quente demais",
            "Verifique se as ventoinhas estão funcionando, limpe-as, use uma base refrigerada e evite superfícies que bloqueiem a ventilação.",
            
            "O notebook desliga sozinho por superaquecimento?",
            "Sim, é um mecanismo de proteção. Limpe as ventoinhas, verifique a pasta térmica e mantenha as saídas de ar desobstruídas.",
            
            "Desliga sozinho",
            "Sim, é um mecanismo de proteção. Limpe as ventoinhas, verifique a pasta térmica e mantenha as saídas de ar desobstruídas.",
            
            "Para de funcionar do nada",
            "Sim, é um mecanismo de proteção. Limpe as ventoinhas, verifique a pasta térmica e mantenha as saídas de ar desobstruídas.",
            
            "Como saber se preciso trocar a pasta térmica?",
            "Se o notebook esquenta muito mesmo após limpeza, ou se a pasta tem mais de 2-3 anos, considere a troca.",
            
            "Trocar pasta térmica",
            "Se o notebook esquenta muito mesmo após limpeza, ou se a pasta tem mais de 2-3 anos, considere a troca.",
            
            "Pasta térmica velha",
            "Se o notebook esquenta muito mesmo após limpeza, ou se a pasta tem mais de 2-3 anos, considere a troca.",
            
            "Posso trocar a pasta térmica sozinho?",
            "Sim, mas requer cuidado e conhecimento técnico. Se não tem experiência, procure um técnico.",
            
            "Trocar pasta térmica sozinho",
            "Sim, mas requer cuidado e conhecimento técnico. Se não tem experiência, procure um técnico.",
            
            "Qual a melhor pasta térmica?",
            "Pastas de alta qualidade como Arctic MX-4, Thermal Grizzly Kryonaut ou Noctua NT-H1 são boas opções.",
            
            "Pasta térmica boa",
            "Pastas de alta qualidade como Arctic MX-4, Thermal Grizzly Kryonaut ou Noctua NT-H1 são boas opções.",
            
            # Bateria - Múltiplas variações
            "Como cuidar da bateria do notebook?",
            "Evite descargas completas, mantenha entre 20-80%, não deixe sempre conectado na tomada se possível.",
            
            "Cuidar da bateria",
            "Evite descargas completas, mantenha entre 20-80%, não deixe sempre conectado na tomada se possível.",
            
            "Bateria durando pouco",
            "Evite descargas completas, mantenha entre 20-80%, não deixe sempre conectado na tomada se possível.",
            
            "Dicas para bateria",
            "Evite descargas completas, mantenha entre 20-80%, não deixe sempre conectado na tomada se possível.",
            
            "É ruim deixar o notebook sempre na tomada?",
            "Notebooks modernos têm proteção, mas idealmente alterne entre bateria e tomada para manter a saúde da bateria.",
            
            "Sempre na tomada faz mal?",
            "Notebooks modernos têm proteção, mas idealmente alterne entre bateria e tomada para manter a saúde da bateria.",
            
            "Deixar carregando sempre",
            "Notebooks modernos têm proteção, mas idealmente alterne entre bateria e tomada para manter a saúde da bateria.",
            
            "Como saber se a bateria precisa ser trocada?",
            "Se a autonomia diminuiu drasticamente, o sistema indica desgaste da bateria ou ela não carrega adequadamente.",
            
            "Bateria viciada",
            "Se a autonomia diminuiu drasticamente, o sistema indica desgaste da bateria ou ela não carrega adequadamente.",
            
            "Trocar bateria",
            "Se a autonomia diminuiu drasticamente, o sistema indica desgaste da bateria ou ela não carrega adequadamente.",
            
            "Bateria não carrega",
            "Se a autonomia diminuiu drasticamente, o sistema indica desgaste da bateria ou ela não carrega adequadamente.",
            
            # Problemas gerais - Múltiplas variações
            "O notebook não liga, o que verificar?",
            "Teste o carregador, pressione o botão power por 15s, remova a bateria se possível e teste só na tomada.",
            
            "Notebook não liga",
            "Teste o carregador, pressione o botão power por 15s, remova a bateria se possível e teste só na tomada.",
            
            "Não funciona",
            "Teste o carregador, pressione o botão power por 15s, remova a bateria se possível e teste só na tomada.",
            
            "Não consegue ligar",
            "Teste o carregador, pressione o botão power por 15s, remova a bateria se possível e teste só na tomada.",
            
            "O sistema está muito lento, como melhorar?",
            "Limpe arquivos temporários, desinstale programas desnecessários, verifique por malware e considere adicionar RAM ou SSD.",
            
            "Notebook lento",
            "Limpe arquivos temporários, desinstale programas desnecessários, verifique por malware e considere adicionar RAM ou SSD.",
            
            "Sistema travando",
            "Limpe arquivos temporários, desinstale programas desnecessários, verifique por malware e considere adicionar RAM ou SSD.",
            
            "Muito devagar",
            "Limpe arquivos temporários, desinstale programas desnecessários, verifique por malware e considere adicionar RAM ou SSD.",
            
            # WiFi e conectividade - Múltiplas variações
            "O WiFi está lento ou não conecta?",
            "Reinicie o roteador, esqueça e reconecte a rede, atualize drivers de rede ou redefina configurações de rede.",
            
            "WiFi não funciona",
            "Reinicie o roteador, esqueça e reconecte a rede, atualize drivers de rede ou redefina configurações de rede.",
            
            "Internet lenta",
            "Reinicie o roteador, esqueça e reconecte a rede, atualize drivers de rede ou redefina configurações de rede.",
            
            "Sem internet",
            "Reinicie o roteador, esqueça e reconecte a rede, atualize drivers de rede ou redefina configurações de rede.",
            
            "Não conecta WiFi",
            "Reinicie o roteador, esqueça e reconecte a rede, atualize drivers de rede ou redefina configurações de rede.",
            
            # Tela e display
            "Apareceram pixels mortos na tela, e agora?",
            "Pixels mortos são defeito permanente. Se muitos, pode precisar trocar a tela. Alguns poucos são toleráveis.",
            
            "Pixels mortos",
            "Pixels mortos são defeito permanente. Se muitos, pode precisar trocar a tela. Alguns poucos são toleráveis.",
            
            "Pontos na tela",
            "Pixels mortos são defeito permanente. Se muitos, pode precisar trocar a tela. Alguns poucos são toleráveis.",
            
            "Tela com problema",
            "Pixels mortos são defeito permanente. Se muitos, pode precisar trocar a tela. Alguns poucos são toleráveis.",
            
            "A tela está amarelada, é normal?",
            "Pode ser desgaste natural, configuração de cor ou filtro de luz azul ativado. Verifique as configurações primeiro.",
            
            "Tela amarela",
            "Pode ser desgaste natural, configuração de cor ou filtro de luz azul ativado. Verifique as configurações primeiro.",
            
            "Cor estranha na tela",
            "Pode ser desgaste natural, configuração de cor ou filtro de luz azul ativado. Verifique as configurações primeiro.",
            
            # Áudio
            "Não sai som do notebook?",
            "Verifique o volume, dispositivos de reprodução padrão, drivers de áudio e se não está no mudo.",
            
            "Sem som",
            "Verifique o volume, dispositivos de reprodução padrão, drivers de áudio e se não está no mudo.",
            
            "Áudio não funciona",
            "Verifique o volume, dispositivos de reprodução padrão, drivers de áudio e se não está no mudo.",
            
            "Som baixo",
            "Verifique o volume, dispositivos de reprodução padrão, drivers de áudio e se não está no mudo.",
            
            # Armazenamento
            "HD ou SSD, qual é melhor?",
            "SSD é muito mais rápido, consome menos energia e é mais resistente a impactos que o HD tradicional.",
            
            "SSD vale a pena?",
            "SSD é muito mais rápido, consome menos energia e é mais resistente a impactos que o HD tradicional.",
            
            "Trocar por SSD",
            "SSD é muito mais rápido, consome menos energia e é mais resistente a impactos que o HD tradicional.",
            
            "Como saber se preciso mais memória RAM?",
            "Se o sistema fica lento, usa muito arquivo de paginação ou o Task Manager mostra uso alto da RAM constantemente.",
            
            "Pouca RAM",
            "Se o sistema fica lento, usa muito arquivo de paginação ou o Task Manager mostra uso alto da RAM constantemente.",
            
            "Adicionar memória",
            "Se o sistema fica lento, usa muito arquivo de paginação ou o Task Manager mostra uso alto da RAM constantemente.",
            
            "Preciso de backup regularmente?",
            "Sim, sempre! Use serviços na nuvem, HDs externos ou faça imagem do sistema periodicamente.",
            
            "Fazer backup",
            "Sim, sempre! Use serviços na nuvem, HDs externos ou faça imagem do sistema periodicamente.",
            
            "Backup importante?",
            "Sim, sempre! Use serviços na nuvem, HDs externos ou faça imagem do sistema periodicamente."
        ]
    
    def train_chatbot(self):
        """Treina o chatbot com a base de conhecimento"""
        print("Treinando o chatbot FAQ sobre manutenção de notebooks...")
        self.trainer.train(self.knowledge_base)
        print("Treinamento concluído!")
    
    def start_conversation(self):
        """Inicia a conversa com o usuário"""
        print("=" * 60)
        print("🔧 CHATBOT FAQ - MANUTENÇÃO DE NOTEBOOKS 🔧")
        print("=" * 60)
        print("Olá! Sou seu assistente para dúvidas sobre manutenção de notebooks.")
        print("Posso te ajudar com limpeza, problemas técnicos, cuidados com bateria e muito mais!")
        print("🧠 Agora com sistema inteligente de compreensão melhorado!")
        print("Digite 'sair' para encerrar a conversa.")
        print("-" * 60)
        
        while True:
            try:
                user_input = input("\n👤 Você: ")
                
                if user_input.lower() in ['sair', 'exit', 'quit', 'tchau', 'bye']:
                    print("\n🤖 Bot: Obrigado por usar o FAQ de manutenção de notebooks! Até mais! 👋")
                    break
                
                if user_input.strip() == "":
                    print("\n🤖 Bot: Por favor, digite sua pergunta sobre manutenção de notebooks.")
                    continue
                
                # Primeiro tenta o sistema inteligente
                smart_response, confidence = self.smart_response(user_input)
                
                if smart_response and confidence > 0.3:
                    print(f"\n🧠 Bot (Smart): {smart_response}")
                    print(f"📊 Confiança: {confidence:.2f}")
                else:
                    # Se o sistema inteligente não encontrar, usa o ChatterBot tradicional
                    try:
                        response = self.chatbot.get_response(user_input)
                        print(f"\n🤖 Bot: {response}")
                    except Exception as e:
                        print(f"\n🤖 Bot: Desculpe, não consegui processar sua pergunta. Erro: {e}")
                        print("💡 Tente usar palavras-chave como: limpeza, quente, bateria, lento, WiFi, som, tela")
                
            except KeyboardInterrupt:
                print("\n\n🤖 Bot: Conversa interrompida. Até mais!")
                break
            except Exception as e:
                print(f"\n❌ Erro: {e}")
                print("Tente novamente com uma pergunta diferente.")

def main():
    """Função principal"""
    try:
        # Cria instância do chatbot
        faq_bot = NotebookMaintenanceFAQ()
        
        # Verifica se já foi treinado
        db_path = "notebook_faq.sqlite3"
        if not os.path.exists(db_path):
            faq_bot.train_chatbot()
        else:
            print("Base de dados encontrada. Carregando chatbot...")
        
        # Inicia conversa
        faq_bot.start_conversation()
        
    except Exception as e:
        print(f"❌ Erro ao inicializar o chatbot: {e}")
        print("Verifique se todas as dependências estão instaladas.")

if __name__ == "__main__":
    main()
