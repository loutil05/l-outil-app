import streamlit as st
from pyairtable import Table

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(page_title="L'OUTIL", layout="centered")

# 2. DESIGN "AI COMMAND PROTOCOL" - ANTI-BLOC BLANC
st.markdown("""
    <style>
    /* Fond noir absolu */
    .stApp { background-color: #050505 !important; }
    
    /* Titre Signature (Image 2) */
    .brand-header {
        color: #D4AF37;
        text-align: center;
        letter-spacing: 15px;
        font-size: 38px;
        font-weight: 200;
        margin-top: 50px;
        text-transform: uppercase;
        font-family: 'Inter', sans-serif;
    }
    .brand-sub {
        color: rgba(212, 175, 55, 0.4);
        text-align: center;
        letter-spacing: 6px;
        font-size: 10px;
        margin-bottom: 60px;
        text-transform: uppercase;
    }

    /* CADRE CENTRAL DORE (L'effet de l'Image 2) */
    [data-testid="stVerticalBlock"] > div:nth-child(2) {
        border: 1px solid rgba(212, 175, 55, 0.15) !important;
        padding: 60px !important;
        background: rgba(255, 255, 255, 0.01) !important;
        backdrop-filter: blur(15px);
        border-radius: 2px;
    }

    /* SUPPRESSION RADICALE DU BLANC (Correction Images 5 à 9) */
    /* On force la transparence sur TOUT le système Streamlit */
    .stTextInput input, .stSelectbox div[data-baseweb="select"], .stSelectbox div {
        background-color: transparent !important;
        background: transparent !important;
        border: none !important;
        border-bottom: 1px solid rgba(212, 175, 55, 0.4) !important;
        color: white !important;
        border-radius: 0px !important;
        padding-left: 0px !important;
        box-shadow: none !important;
    }

    /* Suppression des fonds gris/blancs au survol */
    div[data-baseweb="select"] > div {
        background-color: transparent !important;
    }
    
    /* Labels dorés fins */
    label p {
        color: rgba(212, 175, 55, 0.7) !important;
        font-size: 10px !important;
        letter-spacing: 3px;
        text-transform: uppercase;
        margin-bottom: 10px;
    }

    /* Bouton EXECUTE - Lignes Dorées (Image 2) */
    div.stButton > button {
        background-color: transparent !important;
        color: #D4AF37 !important;
        border: 1px solid #D4AF37 !important;
        border-radius: 0px !important;
        width: 140px !important;
        height: 45px !important;
        letter-spacing: 5px;
        font-weight: 300;
        margin-top: 40px;
        text-transform: uppercase;
        transition: 0.4s ease;
    }
    div.stButton > button:hover {
        background-color: rgba(212, 175, 55, 0.1) !important;
        box-shadow: 0px 0px 30px rgba(212, 175, 55, 0.2);
    }

    /* Masquer l'interface standard */
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    
    <div class="brand-header">L'OUTIL</div>
    <div class="brand-sub">AI COMMAND PROTOCOL</div>
""", unsafe_allow_html=True)

# 3. LOGIQUE TECHNIQUE (SANS TOUCHER AU SECRETS ICI)
try:
    api_key = st.secrets["AIRTABLE_API_KEY"]
    base_id = st.secrets["AIRTABLE_BASE_ID"]
    table = Table(api_key, base_id, "Table 1")
except:
    st.error("CONFIGURATION REQUISE")

# 4. INTERFACE DANS LE CADRE DORE
sujet = st.text_input("SUJET", placeholder="DÉFINIR LE PARAMÈTRE...")

col1, col2 = st.columns(2)
with col1:
    fmt = st.selectbox("FORMAT", ["REEL", "CARROUSEL", "STORY"])
with col2:
    ton = st.selectbox("TONALITÉ", ["EXPERT", "ARROGANT", "VENTE"])

# Centrage du bouton
st.markdown("<br>", unsafe_allow_html=True)
col_b1, col_b2, col_b3 = st.columns([1,1,1])
with col_b2:
    if st.button("EXECUTE"):
        if sujet:
            table.create({"Sujet": sujet, "Format": fmt, "Ton": ton})
            st.toast("PROTOCOL SUCCESSFUL", icon='✅')
