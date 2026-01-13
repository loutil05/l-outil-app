import streamlit as st
from pyairtable import Table

# 1. SETUP UNIVERSEL
st.set_page_config(page_title="L'OUTIL", layout="centered")

# 2. INJECTION CSS : LUXE, GLOW & ANTI-BLANC
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300&display=swap');

    /* FOND NOIR PROFOND TEXTURÉ */
    .stApp {
        background-color: #020202 !important;
        background-image: radial-gradient(rgba(212, 175, 55, 0.03) 1px, transparent 1px) !important;
        background-size: 20px 20px !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    [data-testid="stHeader"], [data-testid="stToolbar"], footer { display: none !important; }

    /* 1. TITRE QUI BRILLE (Animation Gold Glow) */
    .brand-header {
        text-align: center;
        letter-spacing: 20px;
        font-size: 48px;
        font-weight: 200;
        text-transform: uppercase;
        margin-top: 50px;
        background: linear-gradient(90deg, #B8860B, #FFD700, #B8860B);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: shine 4s linear infinite;
        filter: drop-shadow(0 0 10px rgba(212, 175, 55, 0.5));
    }
    @keyframes shine {
        to { background-position: 200% center; }
    }

    /* 2. LE CADRE CENTRAL (FUMÉ PLUS FONCÉ) */
    [data-testid="stVerticalBlock"] > div:nth-child(2) {
        border: 1px solid rgba(212, 175, 55, 0.15) !important;
        background: rgba(0, 0, 0, 0.85) !important;
        -webkit-backdrop-filter: blur(30px) !important;
        backdrop-filter: blur(30px) !important;
        padding: 60px !important;
        border-radius: 4px !important;
        box-shadow: 0 40px 100px rgba(0, 0, 0, 1);
    }

    /* 3. FIX RADICAL BARRE BLANCHE PC (ZÉRO BLANC) */
    .stTextInput div, .stSelectbox div, [data-baseweb="input"], [data-baseweb="select"] {
        background-color: transparent !important;
        background: transparent !important;
        border: none !important;
    }

    /* On recrée la plaque de verre poli */
    .stTextInput > div > div, .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.02) !important;
        border-bottom: 2px solid rgba(212, 175, 55, 0.3) !important;
        border-radius: 0px !important;
        height: 55px !important;
        transition: 0.4s ease;
    }

    /* Style du texte (Police fine style machine à écrire) */
    input, .stSelectbox span {
        color: white !important;
        font-weight: 200 !important;
        font-size: 16px !important;
        letter-spacing: 1px !important;
        -webkit-text-fill-color: white !important;
    }

    /* Style des menus déroulants (Assortis au verre) */
    div[role="listbox"] {
        background-color: #0A0A0A !important;
        border: 1px solid #D4AF37 !important;
    }

    /* 4. LE BOUTON (NOUVEAU TEXTE & CENTRAGE) */
    div.stButton {
        display: flex;
        justify-content: center;
        margin-top: 40px;
    }
    div.stButton > button {
        background-color: transparent !important;
        color: #D4AF37 !important;
        border: 1px solid #D4AF37 !important;
        border-radius: 0px !important;
        width: 100% !important;
        max-width: 350px !important;
        height: 65px !important;
        letter-spacing: 10px;
        font-weight: 200;
        text-transform: uppercase;
        transition: 0.6s all;
    }
    div.stButton > button:hover {
        background-color: rgba(212, 175, 55, 0.05) !important;
        box-shadow: 0px 0px 40px rgba(212, 175, 55, 0.2);
    }

    label p {
        color: rgba(212, 175, 55, 0.8) !important;
        font-size: 11px !important;
        letter-spacing: 4px !important;
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
    
    # Nouveau texte du bouton
    if st.button("LANCER LA GÉNÉRATION"):
        if sujet:
            try:
                table.create({"Sujet": sujet, "Format": fmt, "Ton": ton})
                st.toast("PROTOCOL EXECUTED", icon='✅')
            except:
                st.error("Liaison Airtable interrompue")
        else:
            st.warning("INPUT REQUIRED")
