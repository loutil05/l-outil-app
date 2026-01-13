import streamlit as st
from pyairtable import Table

# 1. ARCHITECTURE DE BASE
st.set_page_config(page_title="L'OUTIL", layout="centered")

# 2. INJECTION CSS : LUXE ÉPURÉ & FIX IPHONE (ZÉRO ERREUR)
st.markdown("""
<style>
    /* 1. FOND NOIR MAT TEXTURÉ (PC & MOBILE) */
    .stApp {
        background-color: #000000 !important;
        background-image: radial-gradient(#1a1a1a 1px, transparent 1px) !important;
        background-size: 20px 20px !important;
        color: white !important;
    }
    [data-testid="stHeader"], [data-testid="stToolbar"], footer { display: none !important; }

    /* 2. TITRE DORÉ LUMINEUX (Fixé pour iPhone) */
    .brand-header {
        text-align: center;
        color: #D4AF37 !important;
        letter-spacing: 10px;
        font-size: 32px;
        font-weight: bold;
        text-transform: uppercase;
        margin-top: 30px;
        text-shadow: 0 0 15px rgba(212, 175, 55, 0.5);
    }

    /* 3. LE CADRE CENTRAL (FUMÉ SOMBRE) */
    [data-testid="stVerticalBlock"] > div:nth-child(2) {
        border: 1px solid rgba(212, 175, 55, 0.2) !important;
        background: rgba(10, 10, 10, 0.9) !important;
        padding: 30px !important;
        border-radius: 4px !important;
        margin: 0 auto !important;
    }

    /* 4. FIX BARRE BLANCHE PC : TRANSPARENCE TOTALE */
    /* On force chaque couche de l'input à être invisible */
    .stTextInput div, .stSelectbox div, [data-baseweb="input"], [data-baseweb="select"], input {
        background-color: transparent !important;
        background: transparent !important;
        border: none !important;
        color: white !important;
    }

    /* On recrée la ligne Or sous les cases */
    .stTextInput > div > div, .stSelectbox > div > div {
        border-bottom: 2px solid rgba(212, 175, 55, 0.4) !important;
        border-radius: 0px !important;
        background: rgba(255, 255, 255, 0.02) !important;
    }

    /* 5. BOUTON : LANCER LA GÉNÉRATION (CENTRÉ) */
    div.stButton {
        display: flex;
        justify-content: center;
        margin-top: 30px;
    }
    div.stButton > button {
        background-color: transparent !important;
        color: #D4AF37 !important;
        border: 1px solid #D4AF37 !important;
        border-radius: 0px !important;
        width: 100% !important;
        max-width: 280px !important;
        height: 55px !important;
        letter-spacing: 4px;
        text-transform: uppercase;
    }
    div.stButton > button:hover {
        background-color: rgba(212, 175, 55, 0.1) !important;
        border: 1px solid #FFD700 !important;
    }

    label p {
        color: rgba(212, 175, 55, 0.8) !important;
        font-size: 10px !important;
        letter-spacing: 3px !important;
        text-transform: uppercase;
    }
</style>

<div class="brand-header">L'OUTIL</div>
<p style="text-align:center; color:rgba(212,175,55,0.4); letter-spacing:5px; font-size:9px; text-transform:uppercase; margin-bottom: 30px;">AI Command Protocol</p>
""", unsafe_allow_html=True)

# 3. LOGIQUE TECHNIQUE
try:
    api_key = st.secrets["AIRTABLE_API_KEY"]
    base_id = st.secrets["AIRTABLE_BASE_ID"]
    table = Table(api_key, base_id, "Table 1")
except Exception:
    st.error("Liaison technique en attente.")

# 4. INTERFACE
with st.container():
    sujet = st.text_input("SUJET", placeholder="DÉFINIR LE PARAMÈTRE...")
    
    col1, col2 = st.columns(2)
    with col1:
        fmt = st.selectbox("FORMAT", ["REEL", "CARROUSEL", "STORY"])
    with col2:
        ton = st.selectbox("TONALITÉ", ["EXPERT", "ARROGANT", "VENTE"])
    
    if st.button("LANCER LA GÉNÉRATION"):
        if sujet:
            try:
                table.create({"Sujet": sujet, "Format": fmt, "Ton": ton})
                st.toast("PROTOCOLE LANCÉ", icon='✅')
            except Exception:
                st.error("Erreur de connexion Airtable.")
        else:
            st.warning("SAISIE REQUISE")
