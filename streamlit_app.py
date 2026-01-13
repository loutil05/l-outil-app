import streamlit as st
from pyairtable import Table
import os

# --- CONFIGURATION STRICTE ---
st.set_page_config(page_title="L'OUTIL", page_icon="⚡", layout="centered")

# --- LE VRAI DESIGN "L'OUTIL" (NOIR & OR) ---
st.markdown("""
    <style>
    /* Fond Noir Intégral */
    .stApp {
        background-color: #000000 !important;
    }
    /* Titre en Or Massif */
    .gold-title {
        color: #D4AF37 !important;
        font-family: 'Helvetica Neue', sans-serif;
        font-size: 3.5rem !important;
        font-weight: 800;
        text-align: center;
        text-transform: uppercase;
        margin-bottom: 0px;
        letter-spacing: -2px;
    }
    /* Input design */
    .stTextInput > div > div > input {
        background-color: #111 !important;
        color: white !important;
        border: 1px solid #D4AF37 !important;
        border-radius: 0px !important;
    }
    /* Bouton Or */
    .stButton > button {
        width: 100%;
        background-color: #D4AF37 !important;
        color: black !important;
        font-weight: bold !important;
        border: none !important;
        border-radius: 0px !important;
        height: 60px !important;
        font-size: 1.2rem !important;
    }
    /* Masquer les menus Streamlit */
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    <h1 class="gold-title">L'OUTIL</h1>
    <p style='text-align: center; color: #D4AF37; font-weight: 300; margin-top: -10px;'>SYSTÈME DE COMMANDE PRIVÉ</p>
    """, unsafe_allow_html=True)

# --- CONNEXION AIRTABLE ---
try:
    api_key = st.secrets["AIRTABLE_API_KEY"]
    base_id = st.secrets["AIRTABLE_BASE_ID"]
    table = Table(api_key, base_id, "Table 1")
except Exception as e:
    st.error("En attente de configuration Airtable...")

# --- INTERFACE ---
with st.container():
    st.write("---")
    sujet = st.text_input("SUJET DU POST", placeholder="Tape ton idée ici...")
    
    col1, col2 = st.columns(2)
    with col1:
        format_type = st.selectbox("FORMAT", ["Réel Viral", "Carrousel Stratégique", "Story"])
    with col2:
        tonalite = st.selectbox("TONALITÉ", ["Arrogant", "Expert", "Agressif"])

    if st.button("LANCER LA GÉNÉRATION"):
        if sujet:
            with st.spinner("Transmission..."):
                table.create({"Sujet": sujet, "Format": format_type, "Ton": tonalite})
                st.success("ENVOYÉ DANS AIRTABLE.")
        else:
            st.warning("Précise un sujet.")
