Python

import streamlit as st
from pyairtable import Table

# 1. CONFIGURATION (STABILITÉ MOBILE)
st.set_page_config(page_title="L'OUTIL", layout="centered")

# 2. INJECTION CSS : CENTRAGE PARFAIT & LUEUR DORÉE INTENSE
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400&display=swap');

    /* FOND NOIR MAT AVEC GRAIN SUBTIL */
    .stApp {
        background-color: #020202 !important;
        background-image: radial-gradient(rgba(212, 175, 55, 0.05) 1px, transparent 1px) !important;
        background-size: 20px 20px !important;
        font-family: 'Inter', sans-serif !important;
        /* Force le centrage vertical et horizontal de tout le contenu */
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    
    [data-testid="stHeader"], [data-testid="stToolbar"], footer { display: none !important; }

    /* --- LE CHANGEMENT EST ICI : TITRE AVEC LUEUR INTENSE --- */
    .brand-header {
        text-align: center;
        letter-spacing: 15px;
        font-size: 38px;
        font-weight: 200;
        text-transform: uppercase;
        margin-top: 40px;
        /* Le dégradé DANS le texte */
        background: linear-gradient(to bottom, #FFD700, #D4AF37);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        /* LA LUEUR DORÉE MULTI-COUCHES (C'est ça qui fait l'effet) */
        text-shadow: 
            0 0 10px rgba(255, 215, 0, 0.8), /* Cœur brillant */
            0 0 20px rgba(212, 175, 55, 0.6), /* Halo moyen */
            0 0 40px rgba(212, 175, 55, 0.4); /* Aura large */
        width: 100%;
    }
    /* --------------------------------------------------------- */

    /* FIX CENTRAGE : LE CONTENEUR PRINCIPAL */
    [data-testid="stVerticalBlock"] {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
    }

    /* LE CADRE CENTRAL (VERRE FUMÉ) - ALIGNÉ */
    [data-testid="stVerticalBlock"] > div:nth-child(2) {
        border: 1px solid rgba(212, 175, 55, 0.2) !important;
        background: rgba(10, 10, 10, 0.9) !important;
        -webkit-backdrop-filter: blur(30px) !important;
        backdrop-filter: blur(30px) !important;
        padding: 50px !important;
        border-radius: 4px !important;
        box-shadow: 0 40px 100px rgba(0, 0, 0, 1) !important;
        width: 100% !important;
        max-width: 700px !important; 
        margin: 0 auto;
    }

    /* STYLE DORÉ SUR LES INPUTS */
    .stTextInput div, .stSelectbox div, [data-baseweb="input"], [data-baseweb="select"] {
        background-color: transparent !important;
        background: transparent !important;
        border: none !important;
    }

    .stTextInput > div > div, .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.02) !important;
        border-bottom: 2px solid #D4AF37 !important;
        border-radius: 0px !important;
        height: 55px !important;
        transition: 0.4s ease;
    }

    /* Texte et Placeholder en OR */
    input, .stSelectbox span, ::placeholder {
        color: #D4AF37 !important;
        -webkit-text-fill-color: #D4AF37 !important;
        font-weight: 300 !important;
        font-size: 16px !important;
        letter-spacing: 1px !important;
    }
    
    /* Focus */
    div[data-baseweb="input"]:focus-within, div[data-baseweb="select"]:focus-within {
        border-bottom: 2px solid #FFD700 !important;
        box-shadow: 0 5px 15px rgba(212, 175, 55, 0.2) !important;
    }

    /* MENUS DÉROULANTS ASSORTIS */
    div[role="listbox"] {
        background-color: #0A0A0A !important;
        border: 1px solid #D4AF37 !important;
    }

    /* BOUTON CENTRÉ ET DORÉ */
    div.stButton {
        display: flex;
        justify-content: center;
        margin-top: 40px;
        width: 100%;
    }
    div.stButton > button {
        background-color: transparent !important;
        color: #D4AF37 !important;
        border: 1px solid #D4AF37 !important;
        border-radius: 0px !important;
        width: 100% !important;
        max-width: 350px !important;
        height: 65px !important;
        letter-spacing: 8px;
        font-weight: 200;
        text-transform: uppercase;
        transition: 0.5s all;
    }
    div.stButton > button:hover {
        background-color: rgba(212, 175, 55, 0.08) !important;
        box-shadow: 0px 0px 40px rgba(212, 175, 55, 0.25);
        border-color: #FFD700 !important;
    }
    
    /* LABELS DORÉS */
    label p {
        color: rgba(212, 175, 55, 0.8) !important;
        font-size: 11px !important;
        letter-spacing: 3px !important;
        text-transform: uppercase;
    }
</style>

<div class="brand-header">L'OUTIL</div>
<p style="text-align:center; color:rgba(212,175,55,0.4); letter-spacing:8px; font-size:10px; text-transform:uppercase; margin-bottom: 40px;">AI Command Protocol</p>
""", unsafe_allow_html=True)

# 3. LOGIQUE TECHNIQUE
try:
    api_key = st.secrets["AIRTABLE_API_KEY"]
    base_id = st.secrets["AIRTABLE_BASE_ID"]
    table = Table(api_key, base_id, "Table 1")
except:
    st.error("Configuration Requise.")

# 4. INTERFACE
with st.container():
    sujet = st.text_input("SUJET", placeholder="DÉFINIR LE PARAMÈTRE STRATÉGIQUE...")
    
    col1, col2 = st.columns(2)
    with col1:
        fmt = st.selectbox("FORMAT", ["REEL", "CARROUSEL", "STORY"])
    with col2:
        ton = st.selectbox("TONALITÉ", ["EXPERT", "ARROGANT", "VENTE"])
    
    if st.button("LANCER LA GÉNÉRATION"):
        if sujet:
            try:
                table.create({"Sujet": sujet, "Format": fmt, "Ton": ton})
                st.toast("PROTOCOL EXECUTED", icon='✅')
            except:
                st.error("Erreur de liaison Airtable")
        else:
            st.warning("SAISIE REQUISE")
