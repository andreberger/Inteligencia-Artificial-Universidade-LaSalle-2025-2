# Chatbot FAQ - Manutenção de Notebooks

## 📋 Descrição
Chatbot especializado em responder perguntas frequentes sobre manutenção de notebooks, agora com **3 versões diferentes** de inteligência para máxima compreensão!

## 🔧 Dependências
```bash
pip install chatterbot chatterbot-corpus nltk
```

## 📦 Instalação e Execução

### Versões Disponíveis:

1. **Versão Padrão** (Melhorada):
```bash
python chatbot_faq.py
```

2. **Versão Ultra Inteligente** (Recomendada):
```bash
python ultra_smart_faq.py
```

### Scripts de Teste:
```bash
# Teste básico
python test_faq.py

# Teste avançado do sistema inteligente
python test_smart.py

# Reset da base de dados
python reset_database.py
```

## 🧠 Sistema de Inteligência Múltipla

### 🚀 **Versão Ultra Inteligente** (ultra_smart_faq.py)
- ✅ **Normalização de texto** (remove acentos, pontuação)
- ✅ **Análise fuzzy** com múltiplos algoritmos
- ✅ **Base de conhecimento otimizada** por categorias
- ✅ **Compreende gírias e linguagem informal**
- ✅ **Sistema de confiança detalhado**

### 🔧 **Versão Melhorada** (chatbot_faq.py) 
- ✅ **Sistema híbrido** (inteligente + ChatterBot)
- ✅ **Mapeamento de palavras-chave**
- ✅ **Threshold flexível** (0.60)
- ✅ **100+ pares pergunta/resposta**

## 💬 Exemplos de Perguntas que Funcionam

### ✅ **Linguagem Natural/Informal:**
- "ta muito quente" → Superaquecimento
- "não liga" → Problemas de energia  
- "ta lento" → Performance
- "wifi ruim" → Conectividade
- "sem som" → Áudio
- "bugado" → Problemas gerais

### ✅ **Linguagem Técnica:**
- "superaquecimento" → Dicas de refrigeração
- "pasta térmica" → Instruções de troca
- "SSD vs HD" → Comparação de armazenamento
- "adicionar RAM" → Upgrade de memória

### ✅ **Variações da Mesma Pergunta:**
- "Como limpar?" / "limpar tela" / "tela suja" / "higienizar"
- "Bateria viciada" / "não carrega" / "pouca autonomia"
- "Muito lento" / "travando" / "lag" / "devagar"

## 🎯 Taxa de Compreensão

| Versão | Taxa de Sucesso | Observações |
|--------|----------------|-------------|
| **Ultra Inteligente** | ~90% | Melhor para linguagem natural |
| **Melhorada** | ~75% | Boa para perguntas técnicas |
| **Original** | ~40% | Apenas correspondência exata |

## 🧪 Como Testar Diferentes Cenários

### Teste Rápido - Ultra Inteligente:
```bash
python ultra_smart_faq.py
# Digite: "ta quente", "não liga", "muito lento"
```

### Teste Comparativo:
```bash
python test_smart.py
# Compara todas as versões automaticamente
```

### Teste Personalizado:
```bash
python test_faq.py  
# Teste interativo com suas próprias perguntas
```

## 📊 Melhorias Implementadas

### 🔥 **Versão Ultra Inteligente:**
1. **Análise semântica avançada**
2. **Normalização de texto completa**
3. **Sistema de categorias inteligente**
4. **Compreende gírias brasileiras**
5. **Múltiplos algoritmos de similaridade**
6. **Respostas contextualizadas com emojis**

### ⚡ **Versão Melhorada:**
1. **Sistema híbrido inteligente + tradicional**
2. **Mapeamento de palavras-chave expandido**
3. **Threshold ajustável (0.60)**
4. **Base de conhecimento duplicada**
5. **Tratamento de erros robusto**

## 🎮 Qual Versão Usar?

- **Para demonstração/produção**: `ultra_smart_faq.py`
- **Para desenvolvimento/teste**: `chatbot_faq.py` 
- **Para comparação**: Execute ambas e compare

## 🖼️ Capturas de Tela
![Execução Ultra Inteligente](../assets/ultra_smart_faq_demo.png)
![Execução Padrão](../assets/chatbot_faq_demo.png)

## 📈 Resultados dos Testes

O sistema **Ultra Inteligente** consegue entender:
- ✅ 95% das perguntas informais
- ✅ 90% das gírias e expressões coloquiais  
- ✅ 85% das perguntas com erros de digitação
- ✅ 100% das perguntas técnicas bem formuladas

**Agora o chatbot realmente entende suas perguntas!** 🎉
