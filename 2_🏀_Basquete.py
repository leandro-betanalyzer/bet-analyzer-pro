import streamlit as st
from analysis_engine import basketball_analysis

st.title("🏀 Basquete")
st.caption("Analise jogadores em pontos, rebotes, assistências ou PRA.")

c1, c2 = st.columns(2)
game = c1.text_input("Jogo", "Lakers x Warriors")
player = c2.text_input("Jogador", "Jogador exemplo")

market = st.selectbox(
    "Mercado",
    ["Pontos", "Rebotes", "Assistências", "Pontos + Rebotes + Assistências (PRA)"],
)
line = st.number_input("Linha da casa", min_value=0.5, value=24.5, step=0.5)
odd = st.number_input("Odd", min_value=1.01, value=1.85, step=0.01)

values_text = st.text_input(
    "Resultados do jogador nos últimos jogos",
    "27, 31, 22, 29, 26, 24, 33, 21, 28, 30",
)

if st.button("🔎 Analisar jogador", type="primary", use_container_width=True):
    result = basketball_analysis(values_text, line, odd)

    st.subheader(f"{player} — {market}")
    st.caption(game)

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Média", f'{result["average"]:.2f}')
    c2.metric("Acima da linha", f'{result["over_rate"]:.0f}%')
    c3.metric("Odd justa", f'{result["fair_odd"]:.2f}')
    c4.metric("Valor estimado", f'{result["edge"]:.1f}%')

    if result["recommendation"] == "OVER":
        st.success(f'**Tendência estatística: OVER {line}**')
    else:
        st.warning(f'**Tendência estatística: UNDER {line}**')

    st.write(result["explanation"])
    st.caption(
        "A comparação usa apenas a amostra digitada. Minutos, lesões, adversário e escalação "
        "serão adicionados quando conectarmos os dados reais."
    )
