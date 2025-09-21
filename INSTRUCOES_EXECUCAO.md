# 🚀 INSTRUÇÕES DE EXECUÇÃO

## 📋 Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Conexão com internet (para download dos modelos)

## 💾 Instalação

### Opção 1: Script Automático (Recomendado)
```bash
# Windows
install_dependencies.bat

# Linux/Mac
chmod +x install_dependencies.sh
./install_dependencies.sh
```

### Opção 2: Manual
```bash
pip install chatterbot==1.0.8 chatterbot-corpus==1.2.0 nltk==3.8.1 PyYAML==6.0.1
pip install transformers==4.36.0 datasets==2.14.0 torch==2.1.0 accelerate==0.24.0
```

## 🎮 Execução

### Menu Principal (Recomendado)
```bash
python main.py
```

### Execução Individual
```bash
# Chatbot FAQ
python chatbot_faq/chatbot_faq.py

# Chatbot Corpora  
python chatbot_corpora/chatbot_corpora.py

# Chatbot Dataset
python chatbot_dataset/chatbot_dataset.py

# LLM Conservador
python chatbot_llm/llm_conservative.py

# LLM Criativo
python chatbot_llm/llm_creative.py

# Comparação LLM
python chatbot_llm/llm_comparison.py
```

## ⚠️ Possíveis Problemas e Soluções

### Erro: "chatterbot not found"
```bash
pip install --upgrade chatterbot chatterbot-corpus
```

### Erro: "torch not found" 
```bash
pip install torch torchvision torchaudio
```

### Erro: "sqlite3.OperationalError"
- Problema: Banco de dados corrompido
- Solução: Delete os arquivos .sqlite3 e execute novamente

### Erro: "transformers not found"
```bash
pip install --upgrade transformers datasets
```

### Primeiro uso demora muito
- Normal: Os modelos são baixados na primeira execução
- Aguarde o download completo

## 📸 Capturando Screenshots

Para documentar a execução:
1. Execute cada chatbot
2. Faça algumas perguntas de teste
3. Capture screenshots das conversas
4. Salve na pasta `assets/`

## 📝 Estrutura Final

```
projeto/
├── chatbot_faq/
│   ├── chatbot_faq.py
│   ├── README.md
│   └── requirements.txt
├── chatbot_corpora/
│   ├── chatbot_corpora.py
│   ├── README.md  
│   └── requirements.txt
├── chatbot_dataset/
│   ├── chatbot_dataset.py
│   ├── README.md
│   └── requirements.txt
├── chatbot_llm/
│   ├── llm_conservative.py
│   ├── llm_creative.py
│   ├── llm_comparison.py
│   ├── README.md
│   ├── requirements.txt
│   └── PARAMETROS_EXPLICACAO.md
├── assets/
│   └── screenshots/
├── main.py
├── install_dependencies.bat
├── install_dependencies.sh
└── README.md
```

## 🎯 Testando os Chatbots

### Chatbot FAQ
- Pergunte sobre limpeza: "Como limpar a tela do notebook?"
- Pergunte sobre bateria: "Como cuidar da bateria?"
- Teste problemas: "Meu notebook está esquentando"

### Chatbot Corpora
- Cumprimente: "Oi", "Olá", "Bom dia"
- Converse naturalmente: "Como você está?"
- Faça perguntas pessoais: "Qual seu nome?"

### Chatbot Dataset
- Use inglês: "Hello, how are you?"
- Pergunte sobre hobbies: "What do you like to do?"
- Discuta tópicos cotidianos: "How was your day?"

### LLM Conservador vs Criativo
- Use o mesmo prompt em ambos
- Compare o tamanho das respostas
- Observe a diferença de criatividade
- Teste prompts como: "Tell me about AI"

## ✅ Verificação Final

Antes de entregar, verifique:
- [ ] Todos os 4 chatbots executam sem erro
- [ ] Screenshots foram capturadas
- [ ] READMEs estão completos
- [ ] Dependências estão listadas
- [ ] Código está comentado
- [ ] Repository está no GitHub
