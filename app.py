import streamlit as st
from utils import init_db, get_dashboard_metrics

st.set_page_config(
    page_title="BetAnalyzer Pro",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

init_db()

st.title("📊 BetAnalyzer Pro")
st.caption("Seu painel de apoio para análise de futebol, basquete e controle de apostas.")

metrics = get_dashboard_metrics()

c1, c2, c3, c4 = st.columns(4)
c1.metric("Apostas registradas", metrics["total"])
c2.metric("Taxa de acerto", f'{metrics["hit_rate"]:.1f}%')
c3.metric("Lucro/Prejuízo", f'R$ {metrics["profit"]:.2f}')
c4.metric("ROI", f'{metrics["roi"]:.1f}%')

st.divider()

left, right = st.columns([1.2, 1])

with left:
    st.subheader("🔥 Oportunidades do dia")
    st.info(
        "Nesta primeira versão, as oportunidades são inseridas e analisadas manualmente. "
        "A próxima etapa conectará dados reais de futebol e basquete."
    )

    st.markdown("""
    **Fluxo sugerido**
    1. Abra a página **Futebol** ou **Basquete**.
    2. Informe jogo, mercado, linha e odd.
    3. Analise a frequência dos últimos resultados.
    4. Registre a aposta em **Minhas Apostas**.
    5. Acompanhe acerto, lucro e ROI neste Dashboard.
    """)

with right:
    st.subheader("🧭 Status do projeto")
    st.success("✅ Estrutura principal criada")
    st.success("✅ Futebol disponível")
    st.success("✅ Basquete disponível")
    st.success("✅ Registro de apostas disponível")
    st.warning("⏳ Dados reais via API")
    st.warning("⏳ IA explicando as oportunidades")
    st.warning("⏳ Publicação na internet")

st.divider()
st.caption(
    "A ferramenta organiza informações e não garante resultados. "
    "Aposte apenas valores que não comprometam seu orçamento."
)
