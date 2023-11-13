import matplotlib
matplotlib.use('agg')
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  
import pydeck as pdk





st.set_page_config(page_title="Baayvin CV")

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image("assets/baayvin.png", width=230)

with col2:
    
    st.title("Baayvin SOUBRAMANIEN")
    st.write("Etudiant en Bachelor 2 Informatique à Paris Ynov Campus / 19ans ")
    st.info("Je suis actuellement à la recherche d'un stage en Data d'une dureé minimum de 6 semaines")
    st.write("📫", "baayvin@gmail.com")

# Bouton de téléchargement du CV
if st.button("Télécharger CV"):
    with open("assets/cv_baayvin.pdf", "rb") as pdf_file:
        pdf_data = pdf_file.read()
    
    # Forcer le nom du fichier de téléchargement
    st.download_button(
        label="Cliquez ici pour télécharger le CV",
        data=pdf_data,
        key="cv_baayvin",
        help="Cliquez sur le bouton pour télécharger le CV",
        on_click=None,  
        file_name="cv_baayvin.pdf"  
    )

# --- QUALIFICATIONS ---
st.write('\n')
st.subheader("Parcours")
df = pd.DataFrame({
     'Anneé': ['2023-2024', '2022-2023', '2019-2021'],
     'Classe ': ['Bachelor 2 Informatique','Bachelor 1 Informatique', 'Baccalaurat Géneral Mathématique & Science de l ingénieur'],
     'Etablissement': ['Paris Ynov Campus','Paris Ynov Campus', 'Lycée Louis Jouvet'],
     })
st.write(df)

# --- EXPERIENCE ---
st.write('\n')
st.subheader("Experiences")
df = pd.DataFrame({
     'Anneé': ['2023-2024', '2018'],
     'Travail ': ['Job saisonnier ( Caissie & Rayons )','Stage en pharmacie '],
     'Etablissement': ['Leclerc Francoville','Pharmacie de Vaucelle'],
     })
st.write(df)

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻    
    - Réseaux informatique
    - Data & Python
    - Infrastructure
    - Java , Js , Go , Html , Css , Linux
    - SQL , VMWare , PHP , Cisco paket
"""
)



# --- Soft -SKILLS ---
st.write('\n')
st.subheader("Soft Skills")
st.write(
    """
- 👩‍💻    
    - Esprit d'équipe   
    - Motivation
    - Créativité
    - Curieux  
            
"""
)


# --- MES PROJETS ---
st.write('\n')
st.subheader("Mes Projets")

# Liste d'images de projets avec des liens
project_info = [
        {
        "image": "assets/project1.jpg",
        "lien": "https://github.com/baayvin17/Portfolio_baayvin"
    },
    {
        "image": "assets/project2.webp",
        "lien": "https://github.com/baayvin17/Forum"
    },
    {
        "image": "assets/project3.jpg",
        "lien": "https://github.com/baayvin17/Groupie-Tracker"
    },

     {
        "image": "assets/projetc4.webp",
        "lien": "https://github.com/baayvin17/ProjetSiteJEU"
    },
]


image_index = st.session_state.get("image_index", 0)


st.image(project_info[image_index]["image"], use_column_width=True)
st.write(f"Lien vers le projet : {project_info[image_index]['lien']}")

# Boutons de navigation
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Précédent", key="prev_button"):
        image_index = (image_index - 1) % len(project_info)
with col2:
    st.write("")  
with col3:
    if st.button("Suivant", key="next_button"):
        image_index = (image_index + 1) % len(project_info)


st.session_state.image_index = image_index


# --- Contact Details ---
st.write('\n')
st.subheader("Contact ")
st.write(
    """
- 📞 0602481788
- 📧 baayvin@gmail.com
- 📍  Maison-Lafitte, France
-      "LinkedIn": "https://www.linkedin.com/in/baayvin-soubramanien-b18090252/",
-       "GitHub": "https://github.com/baayvin17",
"""
)

# Données sur les langages et les niveaux
langages = ['Français', 'Anglais', 'Tamoul ( Indien )', 'Allemand']
niveaux = [5, 4, 4, 2]  

# Créer un graphique en barres
fig, ax = plt.subplots()
ax.barh(langages, niveaux, color='skyblue')
ax.set_xlabel('Niveau de compétence')  

# Afficher le graphique dans Streamlit
st.write('\n')
fig.set_size_inches(4, 2)  
st.subheader("Niveaux de compétence en langues")
st.pyplot(fig)

