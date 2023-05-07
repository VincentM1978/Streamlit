import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Charger les données
df = pd.read_csv("https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv")
df['continent'] = df['continent'].str.replace('.', '')


# Define the different regions in the dataset
regions = ["US", "Europe", "Japan"]

def main():
    st.title('Streamlit : build and share data apps - Cars')
    
    # Ajouter des boutons pour filtrer par région
    regions = df['continent'].unique()
    selected_region = st.sidebar.selectbox('Sélectionner une région', regions)
    st.write('You selected', selected_region)
    df_selected_region = df[df['continent'] == selected_region]



    # Afficher une analyse de corrélation
    st.subheader('Analyse de corrélation')
    correlation = df_selected_region.corr()
    fig, ax = plt.subplots()
    sns.heatmap(correlation, annot=True, ax=ax,vmax=1, vmin=-1 )
    st.pyplot(fig)
    st.write("À partir de la carte thermique de corrélation, nous pouvons voir que :")
    st.write("Il existe une forte corrélation négative entre le mpg et les cylindres, les pouces cubes, les ch et les poids en livres.")
    st.write("Cela indique que les voitures avec un rendement énergétique plus élevé ont tendance à avoir moins de cylindres, une cylindrée de moteur plus petite, moins de puissance et un poids inférieur.")
    st.write("Il existe une forte corrélation positive entre les cylindres, les pouces cubes, les chevaux et les poids en livres.")
    st.write("Cela indique que les voitures avec plus de cylindres, une plus grande cylindrée, plus de puissance et un poids plus élevé ont tendance à être corrélées les unes aux autres.")

    # Ajouter un scatterplot de la relation entre puissance moteur et consommation
    st.subheader('Relation entre puissance moteur et consommation')
    fig, ax = plt.subplots()
    sns.scatterplot(x="hp", y="mpg", data=df_selected_region, ax=ax)
    st.pyplot(fig)
    st.write("Le graphique de dispersion montre une relation négative entre la puissance du moteur et le mpg (consommation). Cela indique que les voitures avec une puissance de moteur plus élevée ont tendance à consommer plus d'essence.")

    # Afficher des graphiques de distribution
    st.subheader('Distribution des variables')
    selected_columns = st.multiselect('Sélectionner les variables', df_selected_region.columns)
    for column in selected_columns:
        fig, ax = plt.subplots()
        sns.histplot(df_selected_region[column], ax=ax)
        st.pyplot(fig)

    st.write("D'après l'histogramme de distribution, nous pouvons voir que :")
    st.write("La fonction mpg a une distribution à peu près normale, avec un pic autour de 20 mpg.")
    st.write("La caractéristique des cylindres a une distribution avec des pics à 4 et 8 cylindres.")
    st.write("La fonction weightlbs a une distribution à peu près normale, avec un pic autour de 3000 lbs.")
