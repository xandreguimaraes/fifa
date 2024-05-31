import streamlit as st
import pandas as pd
import webbrowser
from datetime import datetime

# Definindo a data fixada
data_fixada = datetime(2023, 7, 19)

if 'data' not in st.session_state:
    url = 'https://raw.githubusercontent.com/xandreguimaraes/fifa/main/CLEAN_FIFA23_official_data.csv'
    df_data = pd.read_csv(url)
    df_data = df_data[df_data['Contract Valid Until'] >= data_fixada.year]
    df_data = df_data[df_data['Release Clause(£)'] > 0]  # Correção aqui
    df_data = df_data.sort_values(by='Overall', ascending=False)
    st.session_state['data'] = df_data

st.write('# FIFA23 OFFICIAL DATASET')
st.sidebar.markdown('Desenvolvido por [AlexandreFG](https://www.hapvida.com.br)')

bnt = st.button('Acesse os dados no Kaggle')
if bnt:
    webbrowser.open_new_tab('https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data/data')

st.markdown("""
    O conjunto de dados de jogadores de futebol de 2017 a 2023 fornece informações abrangentes sobre
    jogadores de futebol profissionais. O conjunto de dados contém uma ampla gam de atributos, incluindo
    dados demográficos do jogador, caracteristicas físicas, estatísticas de jogo, detalhes do contrato e
    afiliaçãos de clubes.

    com **mais de 17.000 registros**, este conjunto de dados oferece um recurso valioso para analístas de
    futebol, pesquisadores e entusiastas interessados em explorar vários aspectos do mundo do futebol, pois
    permite estudar atributos de jogadores, métricas de desempenho, avaliação de marcado, análise de
    clubes, posicionamento de jogadores e desenvolvimento do jogador ao longo do tempo.
""")

# Restante do código vai aqui...


