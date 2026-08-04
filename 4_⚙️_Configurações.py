import streamlit as st

st.title("⚙️ Configurações")

st.subheader("Fontes de dados")
st.text_input("API de futebol", type="password", placeholder="Será configurada na próxima etapa")
st.text_input("API de basquete", type="password", placeholder="Será configurada na próxima etapa")

st.subheader("Perfil de análise")
st.selectbox("Perfil de risco", ["Conservador", "Moderado", "Agressivo"])
st.slider("Confiança mínima", 50, 95, 75)

st.info(
    "Nesta versão as configurações ainda não são salvas. "
    "Na próxima etapa, as chaves serão armazenadas com segurança fora do GitHub."
)
