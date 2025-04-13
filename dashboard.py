import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt

# Carregar o modelo salvo (ou você pode treinar na hora)
try:
    model = joblib.load('screen_time_predictor.pkl')
except:
    st.error("Modelo não encontrado. Por favor, treine o modelo primeiro.")
    st.stop()

# Título do dashboard
st.title("📱 Predição de Tempo de Tela em Crianças e Adolescentes")

# Sidebar com controles de entrada
st.sidebar.header("Parâmetros de Entrada")

age = st.sidebar.slider("Idade", 5, 15, 10)
gender = st.sidebar.selectbox("Gênero", ["Feminino", "Masculino", "Outro/Prefere não dizer"])
day_type = st.sidebar.radio("Tipo de Dia", ["Weekday", "Weekend"])
screen_time_type = st.sidebar.selectbox("Tipo de Tempo de Tela", ["Educacional", "Recreacional", "Total"])

# Converter entradas para o formato do modelo
gender_map = {
    "Feminino": 0,
    "Masculino": 1,
    "Outro/Prefere não dizer": 2
}
screen_time_type_map = {
    "Educacional": 0,
    "Recreacional": 1,
    "Total": 2
}

# Criar DataFrame com as entradas
input_data = pd.DataFrame({
    'Age': [age],
    'Gender': [gender_map[gender]],
    'Screen Time Type': [screen_time_type_map[screen_time_type]],
    'Day Type': [1 if day_type == "Weekend" else 0]
})

# Fazer a predição
prediction = model.predict(input_data)

# Mostrar resultados
st.subheader("Resultado da Predição")
st.metric(label="Tempo Total de Tela Previsto", value=f"{float(prediction[0]):.2f} horas")

# Gráfico de tendência por idade
st.subheader("Tendência por Idade")
st.write("Como o tempo de tela varia conforme a idade para esta configuração:")

# Criar dados para o gráfico
ages = range(5, 16)
predictions = []
for a in ages:
    input_data['Age'] = a
    predictions.append(model.predict(input_data)[0])

# Plotar o gráfico
fig, ax = plt.subplots()
ax.plot(ages, predictions, marker='o')
ax.set_xlabel("Idade")
ax.set_ylabel("Tempo de Tela (horas)")
ax.set_title(f"Tempo de Tela por Idade ({gender}, {screen_time_type} ,{day_type})")
ax.grid(True)
st.pyplot(fig)

# Explicação do modelo
st.subheader("Sobre o Modelo")
st.write("""
Este modelo prediz o tempo total de tela (educacional + recreacional) com base em:
- Idade da criança/adolescente
- Gênero
- Tipo de dia (dia de semana ou final de semana)

O modelo foi treinado usando Random Forest com dados de crianças de 5 a 15 anos.
""")

# Rodar o dashboard com: streamlit run dashboard.py
