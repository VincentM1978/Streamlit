import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Charger les données
df = pd.read_csv("https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv")
df['continent'] = df['continent'].str.replace('.', '')

# Ajouter la colonne "consommation_litre_100km"
df['consommation_litre_100km'] = round(235.21 / df['mpg'],2)

# Créer la colonne "cm3" à partir de la colonne "cubicinches"
df['cm3'] = df['cubicinches'] * 16.387


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
   

    # Ajouter un regplot de la relation entre puissance moteur et consommation
    st.subheader('Relation entre puissance moteur et consommation')
    fig, ax = plt.subplots()
    sns.regplot(x="hp", y="mpg", data=df_selected_region, ax=ax)
    st.pyplot(fig)
    
    # Ajouter un scatterplot de la relation entre taille du moteur, année et consommation
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='cm3', y='consommation_litre_100km', data=df_selected_region, hue = "year")
    plt.xlabel('Taille du moteur en cm³')
    plt.ylabel('Consommation litres aux 100km')
    plt.title('Relation entre la consommation et la taille des moteurs')
    plt.show()

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

if __name__ == '__main__':
    main()
