# 📱 Análise Preditiva de Tempo de Tela em Crianças e Adolescentes

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.0.2-orange)
![Pandas](https://img.shields.io/badge/Pandas-1.4.0-red)

Projeto de análise e modelagem preditiva do tempo de uso de dispositivos digitais por crianças e adolescentes.

## 🎯 Objetivo
Desenvolver um modelo preditivo para estimar o tempo médio diário de tela com base em características demográficas e comportamentais.

## 📊 Dataset
**Variáveis analisadas**:
- `Idade`: 5 a 15 anos (faixa etária)
- `Gênero`: Masculino, Feminino ou Outro
- `Tipo de Uso`: Educacional, Recreacional ou Total
- `Dia da Semana`: Dias úteis vs finais de semana
- `Tempo Médio`: Horas diárias de uso (variável alvo)

## 🔍 Análise Exploratória

### Correlações Principais
![Heatmap de Correlação](https://github.com/maxMitsuya/streamlit_screen_time/blob/main/corr.png)
*Relações entre variáveis do dataset*

**Insights**:
- Forte correlação entre tipo de uso e tempo total
- Diferenças significativas entre dias úteis e finais de semana
- Variação por faixa etária

## 🤖 Modelagem Preditiva

### Desempenho dos Modelos

| Modelo | MSE | R² |
|--------|-----|----|
| Random Forest | 0.18 | 0.92 |
| Árvore de Decisão | 0.22 | 0.89 |
| Regressão Linear | 0.35 | 0.82 |

### Importância das Features
![Feature Importance](https://github.com/maxMitsuya/streamlit_screen_time/blob/main/feature_importance.png)
*Contribuição de cada variável nas previsões*

## 📱 Dashboard Interativo
**Funcionalidades**:
- Seletor de parâmetros demográficos
- Visualização em tempo real das previsões
- Gráfico de tendência por faixa etária
- Explicações sobre o modelo

**Principais Descobertas**:
1. Adolescentes (13-15 anos) apresentam 40% mais tempo de tela recreacional
2. Finais de semana têm 25% mais uso recreacional
3. Uso educacional mantém-se estável em todas as idades

## 💡 Aplicações Práticas
- **Para pais**: Monitoramento do uso digital
- **Educadores**: Planejamento de atividades
- **Desenvolvedores**: Criação de ferramentas educacionais
