# BetAnalyzer Pro

MVP inicial para:

- análise manual de futebol;
- análise de jogadores de basquete;
- registro de apostas;
- acompanhamento de taxa de acerto, lucro e ROI.

## Instalação

No CMD, dentro da pasta do projeto:

```bat
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Estrutura

- `app.py`: Dashboard
- `pages/`: páginas de Futebol, Basquete, Minhas Apostas e Configurações
- `analysis_engine.py`: cálculos
- `utils.py`: banco local SQLite
- `data/`: banco criado automaticamente

## Próxima etapa

- conectar API de futebol;
- conectar API de basquete;
- buscar partidas e atletas automaticamente;
- incluir minutos, adversário, casa/fora e desfalques;
- publicar no Streamlit Community Cloud.
