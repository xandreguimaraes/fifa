import streamlit as st

st.set_page_config(
    page_title="Players",
    page_icon="",
    layout="wide"
)

df_data = st.session_state["data"]
    
clubes = df_data["Club"].value_counts().index
club = st.sidebar.selectbox("Clube", clubes)
    
df_players = df_data[df_data["Club"] == club]
players = df_players["Name"].value_counts().index
player = st.sidebar.selectbox("Jogador", players)

player_stats = df_data[df_data["Name"] == player].iloc[0]

st.image(player_stats["Photo"])
st.title(f"{player_stats['Name']}")
st.markdown(f"**Clube:** {player_stats['Club']}")
st.markdown(f"**Posição:** {player_stats['Position']}")

Col1, Col2, Col3, Col4 = st.columns(4)
Col1.markdown(f"**Idade:** {player_stats['Age']}")
Col2.markdown(f"**Altura:** {player_stats['Height(cm.)'] / 100}")
Col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)'] * 0.453:.2f}")

st.divider()
st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats['Overall']))

Col1, Col2, Col3 = st.columns(3)
Col1.metric(label="Valor de mercado", value=f"£ {player_stats['Value(£)']:,}")
Col2.metric(label="Remuneração semanal", value=f"£ {player_stats['Wage(£)']:,}")
Col3.metric(label="Cláusula de recisão", value=f"£ {player_stats['Release Clause(£)']:,}")