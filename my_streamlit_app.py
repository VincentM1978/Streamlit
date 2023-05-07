# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import subprocess

# Install Streamlit using pip
subprocess.call(['pip', 'install', 'streamlit'])
pip install matplotlib

# Load the car dataset into a pandas DataFrame
url = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df = pd.read_csv(url)


# Define the different regions in the dataset
regions = ["US", "Europe", "Japan"]

def main():
    st.title('Car Dataset Analysis')
    
    # Create a selectbox for selecting the region
    selected_region = st.sidebar.selectbox('Select a region:', regions)
    
    
    # Calculate the correlation matrix for the filtered dataset
    correlation = df.corr()
    
    # Create a heatmap for the correlation matrix
    fig1, ax1 = plt.subplots()
    sns.heatmap(correlation, annot=True, cmap="coolwarm", ax=ax1)
    st.pyplot(fig1)
    
    st.write("À partir de la carte thermique de corrélation, nous pouvons voir que :")
    st.write("Il existe une forte corrélation négative entre le mpg et les cylindres, les pouces cubes, les ch et les poids en livres.")
    st.write("Cela indique que les voitures avec un rendement énergétique plus élevé ont tendance à avoir moins de cylindres, une cylindrée de moteur plus petite, moins de puissance et un poids inférieur.")
    st.write("Il existe une forte corrélation positive entre les cylindres, les pouces cubes, les chevaux et les poids en livres.")
    st.write("Cela indique que les voitures avec plus de cylindres, une plus grande cylindrée, plus de puissance et un poids plus élevé ont tendance à être corrélées les unes aux autres.")

    # Create a histogram for each feature in the filtered dataset
    fig2, ax2 = plt.subplots(figsize=(10,10))
    df.hist(bins=20, ax=ax2)
    st.pyplot(fig2)

    st.write("D'après l'histogramme de distribution, nous pouvons voir que :")
    st.write("La fonction mpg a une distribution à peu près normale, avec un pic autour de 20 mpg.")
    st.write("La caractéristique des cylindres a une distribution avec des pics à 4 et 8 cylindres.")
    st.write("La fonction weightlbs a une distribution à peu près normale, avec un pic autour de 3000 lbs.")
    st.write("La fonction time-to-60 a une distribution à peu près normale, avec un pic autour de 15 secondes.")
    st.write("La caractéristique de l'année a une distribution uniforme, avec un nombre égal de voitures fabriquées chaque année de 1970 à 1982.") 


if __name__ == '__main__':
    main()
