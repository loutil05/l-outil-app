import streamlit as st
from pyairtable import Table

# 1. ARCHITECTURE DE LA PAGE
st.set_page_config(page_title="L'OUTIL", layout="centered")

# 2. INJECTION CSS : COMPACITÉ & DESIGN LUXE
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400&display=swap');

    /* 1. FOND ET CENTRAGE GLOBAL */
    .stApp {
        background-color: #020202 !important;
        background-image: radial-gradient(rgba(212, 175, 55, 0.05) 1.5px, transparent 0) !important;
        background-size: 25px 25px !important;
        font-family: 'Inter', sans-serif !important;
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
    }
    
    [data-testid="stAppViewContainer"] {
        display: flex !important;
        justify-content: center !important;
        width: 100% !important;
    }
    
    [data-testid="stHeader"], [data-testid="stToolbar"], footer { display: none !important; }

    /* 2. LOGO AVEC HALO DORÉ (RAPPROCHÉ) */
    .brand-header {
        text-align: center !important;
        letter-spacing: 15px;
        font-size: clamp(35px, 10vw, 55px);
        font-weight: 200;
        text-transform: uppercase;
        margin-top: 10px !important; /* Logo plus haut */
        background: linear-gradient(to bottom, #FFD700, #D4AF37);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 10px rgba(255, 215, 0, 0.7), 0 0 20px rgba(212, 175, 55, 0.5);
        width: 100% !important;
    }

    /* 3. LE CADRE CENTRAL (SYMÉTRIE ET COMPACITÉ) */
    [data-testid="stVerticalBlock"] {
        align-items: center !important;
        width: 100% !important;
        gap: 0px !important; /* Supprime l'espace par défaut de Streamlit */
    }

    [data-testid="stVerticalBlock"] > div:nth-child(2) {
        border: 1px solid rgba(212, 175, 55, 0.2) !important;
        background: rgba(10, 10, 10, 0.9) !important;
        -webkit-backdrop-filter: blur(30px) !important;
        backdrop-filter: blur(30px) !important;
        padding: clamp(25px, 5vw, 50px) !important;
        border-radius: 25px !important;
        margin: 10px auto !important; /* Cadre rapproché du titre */
        width: 95% !important;
        max-width: 800px !important;
        box-shadow: 0 40px 120px rgba(0, 0, 0, 1);
    }

    /* --- CASES BULLES --- */
    .stTextInput div, .stSelectbox div, [data-baseweb="input"], [data-baseweb="select"] {
        background-color: transparent !important;
        border: none !important;
    }

    .stTextInput > div > div, .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.02) !important;
        border: 1px solid rgba(212, 175, 55, 0.4) !important;
        border-radius: 50px !important;
        height: 60px !important;
    }

    /* Texte centré et doré */
    input, .stSelectbox span {
        color: #D4AF37 !important;
        -webkit-text-fill-color: #D4AF37 !important;
        font-weight: 300 !important;
        text-align: center !important;
        font-size: 17px !important;
    }

    /* 4. BOUTON (RAPPROCHÉ DU CADRE) */
    div.stButton {
        display: flex !important;
        justify-content: center !important;
        width: 100% !important;
        margin-top: 15px !important; /* Bouton beaucoup plus près du cadre */
    }
    div.stButton > button {
        background-color: transparent !important;
        color: #D4AF37 !important;
        border: 1px solid #D4AF37 !important;
        border-radius: 50px !important;
        width: 100% !important;
        max-width: 450px !important;
        height: 70px !important;
        letter-spacing: 10px;
        text-transform: uppercase;
        font-weight: 200;
        transition: 0.4s all ease;
    }
    div.stButton > button:hover {
        background-color: #D4AF37 !important;
        color: black !important;
        box-shadow: 0px 0px 40px rgba(212, 175, 55, 0.4);
    }

    /* LABELS CENTRÉS */
    label p {
        color: rgba(212, 175, 55, 0.8) !important;
        font-size: 10px !important;
        letter-spacing: 4px !important;
        text-transform: uppercase;
        text-align: center !important;
        margin-bottom: 8px !important;
    }
</style>

<div class="brand-header">L'OUTIL</div>
<p style="text-align:center; color:rgba(212,175,55,0.4); letter-spacing:8px; font-size:10px; text-transform:uppercase; margin-bottom: 10px;">AI Command Protocol</p>
