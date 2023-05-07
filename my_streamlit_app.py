import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Charger les données
data = pd.read_csv("https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv")

# Ajouter des boutons pour filtrer par région
regions = ['US', 'Europe', 'Japon']
selected_region = st.sidebar.selectbox('Sélectionner une région', regions)

filtered_data = data[data['continent'] == selected_region]

# Afficher une analyse de corrélation
st.subheader('Analyse de corrélation')
correlation = data.corr()
fig, ax = plt.subplots()
sns.heatmap(correlation, annot=True, ax=ax)
st.pyplot(fig)

# Afficher des graphiques de distribution
st.subheader('Distribution des variables')
selected_columns = st.multiselect('Sélectionner les variables', data.columns)
for column in selected_columns:
    fig, ax = plt.subplots()
    sns.histplot(data[column], ax=ax)
    st.pyplot(fig)
