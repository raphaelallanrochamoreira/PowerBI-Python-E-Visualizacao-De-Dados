import streamlit as st
import pandas as pd
import plotly.express as px

# Configurações iniciais

st.set_page_config(page_title="Dashboard ISO 9001", layout="wide")

st.title("📊Dashboard de Qualidade - ISO 9001")
st.markdown("Monitoramento de indicadores de Não Conformidades (NCs)")


# Leitura dos dados

@st.cache_data
def carregar_dados(caminho):
    df = pd.read_excel(caminho)
    df['Data'] = pd.to_datetime(df['Data'])
    df['AnoMes'] = df['Data'].dt.to_period('M').astype(str)
    return df

# Planilha maior
df = carregar_dados("dados_ncs_maior.xlsx")


# Filtros 

col1, col2, col3 = st.columns(3)

with col1:
    area = st.multiselect("Filtrar por Área", sorted(df['Área'].unique()), default=sorted(df['Área'].unique()))
with col2:
    status = st.multiselect("Status", sorted(df['Status'].unique()), default=sorted(df['Status'].unique()))
with col3:
    gravidade = st.multiselect("Gravidade", sorted(df['Gravidade'].unique()), default=sorted(df['Gravidade'].unique()))

df_filtro = df[
    (df['Área'].isin(area)) &
    (df['Status'].isin(status)) &
    (df['Gravidade'].isin(gravidade))
]
# Métricas principais
total_ncs = len(df_filtro)
abertas = len(df_filtro[df_filtro['Status'] == 'Aberta'])
fechadas = len(df_filtro[df_filtro['Status'] == 'Fechada'])
tempo_medio = round(df_filtro['Dias_Atraso'].mean(), 1)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total de NCs", total_ncs)
col2.metric("NCs Abertas", abertas)
col3.metric("NCs Fechadas", fechadas)
col4.metric("Média de Dias de Atraso", tempo_medio)
# Gráficos
st.subheader("Análises Gráficas")

col1, col2 = st.columns(2)

# Configuração padrão para gráficos Plotly
plotly_config = {"responsive": True, "displayModeBar": True}

# Gráfico 1 – NCs por Categoria
with col1:
    fig1 = px.bar(
        df_filtro.groupby('Categoria_NC').size().reset_index(name='Quantidade'),
        x='Categoria_NC', y='Quantidade',
        title="NCs por Categoria",
        text='Quantidade', color='Categoria_NC'
    )
    fig1.update_layout(showlegend=False)
    st.plotly_chart(fig1, config=plotly_config)

# Gráfico 2 – Distribuição por Área
with col2:
    fig2 = px.pie(
        df_filtro,
        names='Área',
        title="Distribuição de NCs por Área",
        hole=0.4
    )
    st.plotly_chart(fig2, config=plotly_config)

# Gráfico 3 – NCs por Mês
st.subheader("Tendência Mensal de NCs")
fig3 = px.line(
    df_filtro.groupby('AnoMes').size().reset_index(name='Quantidade'),
    x='AnoMes', y='Quantidade',
    markers=True, title="Evolução das NCs ao longo do tempo"
)
st.plotly_chart(fig3, config=plotly_config)

# Tabela detalhada
st.subheader("Tabela Detalhada de NCs")
st.dataframe(df_filtro, use_container_width=True)
