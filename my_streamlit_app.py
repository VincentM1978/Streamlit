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



    # Afficher une analyse de corrélation
    st.subheader('Analyse de corrélation')
    correlation = df_selected_region.corr()
    fig, ax = plt.subplots()
    sns.heatmap(correlation, annot=True, ax=ax,vmax=1, vmin=-1, cmap='coolwarm' )
    st.pyplot(fig)
    st.markdown("À partir de la carte thermique de corrélation, nous pouvons voir que la consommation des véhicules est fortement corrélée à leur puissance, leur masse et la taille de leur moteur. ")
    st.write("On constate une corrélation négative entre la consommation et l'année, ce qui signifie que les constructeurs ont tendance à faire des véhicules moins gourmands au fil des améliorations techniques.")
    
    st.write("Sans suprise, les véhicules plus lourds ont un moteur plus gros et une consommation supérieure aux plus légers.")
   

    # Ajouter un regplot de la relation entre puissance moteur et consommation
    st.subheader('Relation entre puissance moteur et consommation')
    fig, ax = plt.subplots()
    sns.regplot(x="hp", y="L/100km", data=df_selected_region, ax=ax)
    st.pyplot(fig)
    
    # Ajouter un scatterplot de la relation entre taille du moteur, année et consommation
    st.subheader('Relation entre taille du moteur et consommation')
    fig2, ax = plt.subplots()
    sns.scatterplot(x='cm3', y='L/100km', data=df_selected_region, hue = "year")
    plt.xlabel('Taille du moteur en cm³')
    plt.ylabel('Consommation litres aux 100km')
    plt.title('Relation entre la consommation et la taille des moteurs')
    st.pyplot(fig2)
    
    st.write("Nous ne serons pas étonnés de vérifier la forte corrélation entre la puissance et la taille du moteur et sa consommation en carburant.")
    
    # Afficher des graphiques de distribution
    st.subheader('Distribution des variables')
    selected_columns = st.multiselect('Sélectionner les variables', df_selected_region.columns)
    for column in selected_columns:
        fig, ax = plt.subplots()
        sns.histplot(df_selected_region[column], ax=ax)
        st.pyplot(fig)
    
    st.sidebar.subheader('Valeurs remarquables du jeu de données intégral')
    df2=df.drop('year', axis = 1)
    st.sidebar.dataframe(df2.describe())
    
    df_selected_region2 = df_selected_region.drop('year', axis=1)
    st.subheader("Valeurs remarquables du jeu de données de la région ", selected_region)
    st.dataframe(df_selected_region2.describe())

    st.write("D'après l'histogramme de distribution, nous pouvons voir que :")
    st.write("Sur 261 véhicules, 125 sont en 4 cylindres ( 47,89 % ) , 55 en 6 cylindres (21 % ) et 76 en 8 cylindres (29 %)")
    st.write("Si la moyenne des tailles des moteurs est à 3291 cm³, c'est parce qu'il y a un fort déséquilibre entre les véhicules de la région US ")
    st.write("par rapport aux régions Japan et Europe.")
    st.write("Si les véhicules japonais sont souvent bien moins gourmands que la moyenne, les records de consommation se trouvent encore du côté de la région US")
    st.write("Enfin, il serait très intéressant d'avoir un plus grand jeu de données sur des véhicules plus récents afin de vérifier si nos prédictions de baisse ")
    st.write("de consommation sont réalisées.")

if __name__ == '__main__':
    main()
