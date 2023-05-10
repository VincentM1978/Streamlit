import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Charger les données
df = pd.read_csv("https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv")
df['continent'] = df['continent'].str.replace('.', '')

# Ajouter la colonne "consommation_litre_100km"
df['L/100km'] = round(235.21 / df['mpg'],2)
df = df.drop('mpg', axis=1)

# Créer la colonne "cm3" à partir de la colonne "cubicinches"
df['cm3'] = df['cubicinches'] * 16.387
df = df.drop('cubicinches', axis=1)

# Define the different regions in the dataset
regions = ["US", "Europe", "Japan"]

def main():
    st.title('Streamlit : build and share data apps - Cars')

    # Ajouter des boutons pour filtrer par région
    regions = df['continent'].unique()
    st.sidebar.subheader('Sélectionner une région')
    selected_region = st.sidebar.selectbox('', regions)
    df_selected_region = df[df['continent'] == selected_region]

    # Ajouter un sélecteur slider pour choisir les années
    min_year = df['year'].min()
    max_year = df['year'].max()
    selected_year = st.sidebar.slider('Sélectionner une année', min_value=min_year, max_value=max_year)

    # Filtrer les données en fonction de l'année sélectionnée
    df_selected_year = df[df['year'] == selected_year]

    # Afficher une analyse de corrélation
    st.subheader('Analyse de corrélation')
    correlation = df_selected_year.corr()
    fig, ax = plt.subplots()
    sns.heatmap(correlation, annot=True, ax=ax, vmax=1, vmin=-1, cmap='coolwarm')
    st.pyplot(fig)
    st.markdown("À partir de la carte thermique de corrélation, nous pouvons voir que la consommation des véhicules est fortement corrélée à leur puissance, leur masse et la taille de leur moteur. ")
    st.write("On constate une corrélation négative entre la consommation et l'année, ce qui signifie que les constructeurs ont tendance à faire des véhicules moins gourmands au fil des améliorations techniques.")
    
    st.write("Sans suprise, les véhicules plus lourds ont un moteur plus gros et une consommation supérieure aux plus légers.")
   

    # Ajouter un regplot de la relation entre puissance moteur et consommation
    st.subheader('Relation entre puissance moteur et consommation')
    fig, ax = plt.subplots()
    sns.regplot(x="hp", y="L/100km", data=df_selected_year, ax=ax)
    st.pyplot(fig)
    
    # Ajouter un scatterplot de la relation entre taille du moteur, année et consommation
    st.subheader('Relation entre taille du moteur et consommation')
    fig2, ax = plt.subplots()
    sns.scatterplot(x='cm3', y='L/100km', data=df_selected_year, hue="year")
    plt.xlabel('Taille du moteur en cm³')
    plt.ylabel

