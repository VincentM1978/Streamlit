import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Charger les données
data = pd.read_csv("https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv")

# Ajouter des boutons pour filtrer par région
regions = ["US", "Europe", "Japon"]
selected_region = st.sidebar.selectbox("Sélectionner une région", regions)

filtered_data = data[data["region"] == selected_region]

# Afficher une analyse de corrélation
st.subheader("Analyse de corrélation")
correlation = filtered_data.corr()
sns.heatmap(correlation, annot=True)
st.pyplot()

# Afficher des graphiques de distribution
st.subheader("Distribution des variables")
selected_columns = st.multiselect("Sélectionner les variables", data.columns)
for column in selected_columns:
    sns.histplot(filtered_data[column])
    st.pyplot()
