import streamlit as st
from pyairtable import Table

# 1. ARCHITECTURE DE LA PAGE
st.set_page_config(page_title="L'OUTIL", layout="centered")

# 2. INJECTION CSS : ÉQUILIBRE LUXE ET SYMÉTRIE
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400&display=swap');

    /* FOND ET CENTRAGE GLOBAL */
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

    /* LOGO AVEC HALO DORÉ */
    .brand-header {
        text-align: center !important;
        letter-spacing: 15px;
        font-size: clamp(35px, 10vw, 55px);
        font-weight: 200;
        text-transform: uppercase;
        margin-top: 0px !important; 
        margin-bottom: 0px !important;
        background: linear-gradient(to bottom, #FFD700, #D4AF37);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 10px rgba(255, 215, 0, 0.7), 0 0 20px rgba(212, 175, 55, 0.4);
        width: 100% !important;
    }

    /* LE SOUS-TITRE (LÉGÈREMENT DESCENDU) */
    .brand-subtitle {
        text-align: center; 
        color: rgba(212,175,55,0.4); 
        letter-spacing: 8px; 
        font-size: 10px; 
        text-transform: uppercase; 
        margin-top: 10px !important; /* Petit espace sous le logo */
        margin-bottom: 35px !important; /* DESCEND TOUT LE RESTE */
    }

    /* LE CADRE CENTRAL (PARFAITEMENT SYMÉTRIQUE) */
    [data-testid="stVerticalBlock"] {
        align-items: center !important;
        width: 100% !important;
        gap: 0px !important;
    }

    [data-testid="stVerticalBlock"] > div:nth-child(2) {
        border: 1px solid rgba(212, 175, 55, 0.2) !important;
        background: rgba(10, 10, 10, 0.9) !important;
        -webkit-backdrop-filter: blur(30px) !important;
        backdrop-filter: blur(30px) !important;
        padding: clamp(20px, 5vw, 45px) !important;
        border-radius: 25px !important;
        margin: 0 auto !important;
        width: 95% !important;
        max-width: 850px !important;
        box-shadow: 0 40px 120px rgba(0, 0, 0, 1);
    }

    /* CASES BULLES ÉLARGIES */
    .stTextInput div, .stSelectbox div, [data-baseweb="input"], [data-baseweb="select"] {
        background-color: transparent !important;
        border: none !important;
    }

    .stTextInput > div > div, .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.02) !important;
        border: 1px solid rgba(212, 175, 55, 0.4) !important;
        border-radius: 50px !important;
        height: 65px !important;
    }

    input, .stSelectbox span {
        color: #D
