import streamlit as st
from pyairtable import Table

# 1. CONFIGURATION INITIALE
st.set_page_config(page_title="L'OUTIL", layout="centered")

# 2. INJECTION CSS "BRUTE FORCE" (ZÉRO COMPROMIS)
st.markdown("""
    <style>
    /* Force le fond noir sur TOUTE l'application */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #050505 !important;
    }

    /* TITRE SIGNATURE OR (Image 2) */
    .brand-header {
        color: #D4AF37 !important;
        text-align: center;
        letter-spacing: 18px;
        font-size: 42px;
        font-weight: 200;
        margin-top: 30px;
        text-transform: uppercase;
        font-family: 'Inter', sans-serif;
        text-shadow: 0px 0px 10px rgba(212, 175, 55, 0.2);
    }
    .brand-sub {
        color: rgba(212, 175, 55, 0.4);
        text-align: center;
        letter-spacing: 7px;
        font-size: 10px;
        margin-bottom: 50px;
        text-transform: uppercase;
    }

    /* LE CADRE "PROTOCOL" (L'effet central de l'Image 2) */
    .main-protocol-container {
        border: 1px solid rgba(212, 175, 55, 0.15) !important;
        padding: 50px !important;
        background: rgba(255, 255, 255, 0.01) !important;
        backdrop-filter: blur(20px);
        border-radius: 2px;
        margin-top: 20px;
    }

    /* SUPPRESSION RADICALE DU BLANC ET DU GRIS (Images 5-9) */
    /* On cible tous les éléments de saisie sans exception */
    div[data-baseweb="input"], 
    div[data-baseweb="select"], 
    .stTextInput input,
    .stSelectbox div {
        background-color: transparent !important;
        background: transparent !important;
        border: none !important;
        border-bottom: 1px solid rgba(212, 175, 55, 0.3) !important;
        color: white !important;
        border-radius: 0px !important;
        box-shadow: none !important;
    }

    /* Retire l'effet gris au survol/focus de Streamlit */
    div[data-baseweb="base-input"], [data-baseweb="select"] > div {
        background-color: transparent !important;
    }

    /* LABELS (TITRES DES CHAMPS) */
    label p {
        color: rgba(212, 175, 55, 0.8) !important;
        font-size: 11px !important;
        letter-spacing: 3px !important;
        text-transform: uppercase;
        font-weight: 300;
    }

    /* BOUTON EXECUTE (Style Image 2) */
    div.stButton > button {
        background-color: transparent !important;
        color: #D4AF37 !important;
        border: 1px solid #D4AF37 !important;
        border-radius: 0px !important;
        width: 180px !important;
        height: 50px !important;
        letter-spacing: 6px;
        margin: 40px auto;
        display: block;
        text-transform: uppercase;
        font-weight: 200;
        transition: all 0.6s ease;
    }
    div.stButton > button:hover {
        background-color: rgba(212, 175, 55, 0.08) !important;
        box-shadow: 0px 0px 30px rgba(212, 175, 55, 0.15);
        border: 1px solid #FFD700 !important;
    }

    /* MASQUAGE INTERFACE STANDARD */
    #MainMenu, footer, header { visibility: hidden !important; }
    </style>
""", unsafe_allow_html=True)

# 3. STRUCTURE VISUELLE
st.markdown('<div class="brand-header">L\'OUTIL</div>', unsafe_allow_html=True)
st.markdown('<div class="brand-sub">AI COMMAND PROTOCOL</div>', unsafe_allow_html=True)

# Conteneur central
with st.container():
    st.markdown('<div class="main-protocol-container">', unsafe_allow_html=True)
    
    sujet = st.text_input("SUJET", placeholder="DÉFINIR LE PARAMÈTRE...")
    
    col1, col2 = st.columns(2)
    with col1:
        fmt = st.selectbox("FORMAT", ["REEL", "CARROUSEL", "STORY"])
    with col2:
        ton = st.selectbox("TONALITÉ", ["EXPERT", "ARROGANT", "VENTE"])
    
    if st.button("EXECUTE"):
        try:
            # Envoi vers Airtable
            api_key = st.secrets["AIRTABLE_API_KEY"]
            base_id = st.secrets["AIRTABLE_BASE_ID"]
            table = Table(api_key, base_id, "Table 1")
            table.create({"Sujet": sujet, "Format": fmt, "Ton": ton})
            st.toast("PROTOCOL EXECUTED", icon='✅')
        except Exception as e:
            st.error("System Error: Check Secrets Configuration.")
            
    st.markdown('</div>', unsafe_allow_html=True)
