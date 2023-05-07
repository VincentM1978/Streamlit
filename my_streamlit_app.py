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
    st.write("À partir de la carte thermique de corrélation, nous pouvons observer les relations suivantes :")
    st.write("- Il existe une forte corrélation négative entre la consommation de carburant (mpg) et les caractéristiques telles que le nombre de cylindres, les pouces cubes du moteur, les chevaux et le poids en livres. Cela suggère que les voitures ayant un rendement énergétique plus élevé ont tendance à avoir moins de cylindres, une cylindrée plus petite, moins de puissance et un poids inférieur.")
    st.write("- Il existe une forte corrélation positive entre le nombre de cylindres, les pouces cubes du moteur, les chevaux et le poids en livres. Cela indique que les voitures avec plus de cylindres, une plus grande cylindrée, plus de puissance et un poids plus élevé sont généralement corrélées les unes aux autres.")

   # Afficher des graphiques de distribution
    st.subheader('Distribution des variables')
    selected_columns = st.multiselect('Sélectionner les variables', df_selected_region.columns)
    for column in selected_columns:
        fig, ax = plt.subplots()
        sns.histplot(df_selected_region[column], ax=ax)
        st.pyplot(fig)

    st.write("D'après les histogrammes de distribution, nous pouvons observer les caractéristiques suivantes :")
    st.write("- La consommation de carburant (mpg) suit approximativement une distribution normale, avec un pic autour de 20 mpg.")
    st.write("- Le nombre de cylindres présente des pics à 4 et 8 cylindres.")
    st.write("- Le poids en livres a une distribution approximativement normale, avec un pic autour de 3000 lbs.")
    st.write("- Le temps nécessaire pour atteindre 60 mph (time-to-60) suit approximativement une distribution normale, avec un pic autour de 15 secondes.")
    st.write("- L'année de fabrication présente une distribution uniforme, avec un nombre égal de voitures fabriquées chaque
