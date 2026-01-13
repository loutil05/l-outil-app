import streamlit as st
from pyairtable import Table

# 1. CONFIGURATION UNIVERSELLE
st.set_page_config(page_title="L'OUTIL", layout="centered")

# 2. DESIGN "CRISTAL" - ANTI-BLANC & COMPATIBILITÉ IPHONE
st.markdown("""
<style>
    /* 1. FOND NOIR MAT TEXTURÉ */
    .stApp {
        background-color: #050505 !important;
        background-image: radial-gradient(rgba(212, 175, 55, 0.05) 1px, transparent 1px) !important;
        background-size: 20px 20px !important;
    }
    [data-testid="stHeader"], [data-testid="stToolbar"], footer { display: none !important; }

    /* 2. TITRE OR LUMINEUX */
    .brand-header {
        text-align: center;
        letter-spacing: 15px;
        font-size: 38px;
        font-weight: 200;
        text-transform: uppercase;
        margin-top: 50px;
        color: #D4AF37 !important;
        text-shadow: 0px 0px 20px rgba(212, 175, 55, 0.4);
    }

    /* 3. LE CADRE CENTRAL (VERRE SOMBRE) */
    [data-testid="stVerticalBlock"] > div:nth-child(2) {
        border: 1px solid rgba(212, 175, 55, 0.15) !important;
        background: rgba(0, 0, 0, 0.8) !important;
        -webkit-backdrop-filter: blur(20px) !important; /* Pour iPhone */
        backdrop-filter: blur(20px) !important;
        padding: 40px !important;
        border-radius: 2px !important;
        box-shadow: 0 40px 80px rgba(0, 0, 0, 1);
    }

    /* 4. SUPPRESSION TOTALE DU BLANC (LE FIX POUR TES BARRES) */
    /* On force la transparence sur TOUTES les couches de Streamlit */
    .stTextInput > div > div, .stSelectbox > div > div, div[data-baseweb="input"], div[data-baseweb="select"] {
        background-color: rgba(255, 255, 255, 0.03) !important;
        border: none !important;
        border-bottom: 2px solid rgba(212, 175, 55, 0.3) !important;
        border-radius: 0px !important;
    }
    
    /* On retire le fond blanc spécifique à l'iPhone/PC */
    input, [data-baseweb="base-input"] {
        background-color: transparent !important;
        color: white !important;
        -webkit-text-fill-color: white !important; /* Pour Safari/iPhone */
    }

    /* 5. BOUTON (NOUVEAU TEXTE & STYLE) */
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
        max-width: 300px !important;
        height: 60px !important;
        letter-spacing: 10px;
        font-weight: 200;
        text-transform: uppercase;
    }
    div.stButton > button:hover {
        background-color: rgba(212, 175, 55, 0.05) !important;
        box-shadow: 0px 0px 30px rgba(212, 175, 55, 0.2);
    }

    label p {
        color: rgba(212, 175, 55, 0.8) !important;
        font-size: 10px !important;
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
    sujet = st.text_input("SUJET", placeholder="DÉFINIR LE PARAMÈTRE...")
    
    col1, col2 = st.columns(2)
    with col1:
        fmt = st.selectbox("FORMAT", ["REEL", "CARROUSEL", "STORY"])
    with col2:
        ton = st.selectbox("TONALITÉ", ["EXPERT", "ARROGANT", "VENTE"])
    
    # Changement du texte du bouton
    if st.button("LANCER LA GÉNÉRATION"):
        if sujet:
            try:
                table.create({"Sujet": sujet, "Format": fmt, "Ton": ton})
                st.toast("PROTOCOL EXECUTED", icon='✅')
            except:
                st.error("Erreur Airtable")
        else:
            st.warning("SAISIE REQUISE")
