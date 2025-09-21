# Experimento LLM - Duas Versões de Configuração

## 📋 Descrição
Experimento com Large Language Model (LLM) desenvolvendo duas versões:
1. **Versão Conservadora**: Respostas menores e mais coerentes
2. **Versão Criativa**: Respostas mais abertas e criativas

## 🔧 Dependências
```bash
pip install transformers torch accelerate
```

## 📦 Instalação
1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Execute as duas versões:
```bash
# Versão conservadora
python llm_conservative.py

# Versão criativa
python llm_creative.py
```

## 🎛️ Parâmetros de Configuração

### Versão Conservadora
- **Temperature**: 0.3 (baixa) - Respostas mais determinísticas
- **Max Length**: 50 tokens - Respostas curtas
- **Top-p**: 0.8 - Vocabulário mais restrito
- **Repetition Penalty**: 1.2 - Evita repetições

### Versão Criativa
- **Temperature**: 0.9 (alta) - Respostas mais variadas
- **Max Length**: 150 tokens - Respostas mais longas
- **Top-p**: 0.95 - Vocabulário mais amplo
- **Repetition Penalty**: 1.1 - Permite mais criatividade

## 🔍 Explicação dos Parâmetros

### Temperature
- **Baixa (0.3)**: Torna o modelo mais conservador e previsível
- **Alta (0.9)**: Permite maior aleatoriedade e criatividade

### Max Length
- **Curto (50)**: Força respostas concisas e diretas
- **Longo (150)**: Permite elaboração de ideias

### Top-p (Nucleus Sampling)
- **0.8**: Considera tokens que somam 80% da probabilidade
- **0.95**: Considera tokens que somam 95% da probabilidade

### Repetition Penalty
- **1.2**: Penaliza mais repetições, força diversidade
- **1.1**: Penalização suave, permite alguns padrões

## 🖼️ Capturas de Tela
![LLM Conservador](../assets/llm_conservative_demo.png)
![LLM Criativo](../assets/llm_creative_demo.png)
