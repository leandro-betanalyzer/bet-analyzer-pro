import pandas as pd
import streamlit as st
from utils import add_bet, get_bets, settle_bet

st.title("💰 Minhas Apostas")
st.caption("Registre entradas e acompanhe lucro, prejuízo e desempenho.")

with st.form("new_bet"):
    c1, c2 = st.columns(2)
    sport = c1.selectbox("Esporte", ["Futebol", "Basquete"])
    bookmaker = c2.selectbox("Casa", ["Bet365", "Superbet", "Outra"])

    event = st.text_input("Jogo/Evento")
    market = st.text_input("Mercado", placeholder="Ex.: Over 1.5 gols ou jogador Over 7.5 assistências")

    c3, c4 = st.columns(2)
    odd = c3.number_input("Odd", min_value=1.01, value=1.80, step=0.01)
    stake = c4.number_input("Valor apostado", min_value=0.01, value=10.00, step=1.00)

    submitted = st.form_submit_button("Registrar aposta", use_container_width=True)
    if submitted:
        if not event.strip() or not market.strip():
            st.error("Preencha o evento e o mercado.")
        else:
            add_bet(sport, bookmaker, event, market, odd, stake)
            st.success("Aposta registrada.")

bets = get_bets()

if not bets:
    st.info("Nenhuma aposta registrada.")
else:
    df = pd.DataFrame(bets)
    st.dataframe(df, use_container_width=True, hide_index=True)

    st.subheader("Finalizar aposta")
    open_bets = [b for b in bets if b["Resultado"] == "Pendente"]

    if not open_bets:
        st.info("Não existem apostas pendentes.")
    else:
        labels = {f'{b["ID"]} — {b["Evento"]} — {b["Mercado"]}': b["ID"] for b in open_bets}
        selected = st.selectbox("Selecione", list(labels.keys()))
        result = st.selectbox("Resultado", ["Ganhou", "Perdeu", "Anulada"])

        if st.button("Salvar resultado"):
            settle_bet(labels[selected], result)
            st.success("Resultado atualizado. Atualize a página para ver os novos números.")
