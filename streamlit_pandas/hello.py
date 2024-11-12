import pandas as pd
import streamlit as st

tables = pd.read_html("https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population")

df = tables[2]

col_names = [i[0] for i in df.columns]
df.columns = col_names

df_cut = df[df.columns[:3]]

st.title('Display the top 10 cities')
st.dataframe(df_cut)
st.bar_chart(df_cut['2023 estimate'])
