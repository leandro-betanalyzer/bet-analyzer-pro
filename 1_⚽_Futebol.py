import streamlit as st
from analysis_engine import football_analysis

st.title("⚽ Futebol")
st.caption("Analise tendências de gols, escanteios e cartões.")

c1, c2 = st.columns(2)
home = c1.text_input("Time mandante", "Flamengo")
away = c2.text_input("Time visitante", "Palmeiras")

st.subheader("Últimos resultados combinados")
st.caption("Digite os totais de cada partida separados por vírgula.")

goals = st.text_input("Gols totais", "2, 3, 1, 4, 2, 2, 3, 1, 2, 4")
corners = st.text_input("Escanteios totais", "10, 12, 8, 11, 9, 13, 10, 7, 12, 9")
cards = st.text_input("Cartões totais", "5, 4, 6, 3, 5, 7, 4, 5, 6, 4")
ht_goals = st.text_input("Gols no 1º tempo", "1, 1, 0, 2, 1, 0, 1, 0, 1, 2")

if st.button("🔎 Analisar futebol", type="primary", use_container_width=True):
    result = football_analysis(goals, corners, cards, ht_goals)

    st.subheader(f"{home} x {away}")

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Over 1.5 gols", f'{result["over_15"]:.0f}%')
    m2.metric("Over 2.5 gols", f'{result["over_25"]:.0f}%')
    m3.metric("Gol no 1º tempo", f'{result["over_05_ht"]:.0f}%')
    m4.metric("Over 8.5 escanteios", f'{result["over_85_corners"]:.0f}%')

    m5, m6, m7 = st.columns(3)
    m5.metric("Média de gols", f'{result["avg_goals"]:.2f}')
    m6.metric("Média de escanteios", f'{result["avg_corners"]:.2f}')
    m7.metric("Média de cartões", f'{result["avg_cards"]:.2f}')

    st.success(f'**Melhor tendência:** {result["best_market"]}')
    st.write(result["explanation"])

    st.warning(
        "Os dados desta página são informados manualmente. "
        "Eles servem para validar o cálculo e o formato da análise."
    )
