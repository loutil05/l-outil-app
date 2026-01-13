import streamlit as st
from pyairtable import Table

# 1. SETUP DE LA PAGE
st.set_page_config(page_title="L'OUTIL", layout="centered")

# 2. INJECTION CSS : EFFET CRISTAL & OR
# Cette partie définit l'aspect visuel de l'Image 2
st.markdown("""
<style>
    /* Fond Noir Profond */
    .stApp {
        background: radial-gradient(circle at center, #1a1a1a 0%, #050505 100%) !important;
    }
    [data-testid="stHeader"], [data-testid="stToolbar"], footer { display: none !important; }

    /* TITRE SIGNATURE OR */
    .brand-header {
        color: #D4AF37 !important;
        text-align: center;
        letter-spacing: 18px;
        font-size: 42px;
        font-weight: 100;
        text-transform: uppercase;
        margin-top: 40px;
        font-family: 'Inter', sans-serif;
    }

    /* LE CADRE "PROTOCOL" EN VERRE (IMAGE 2) */
    /* On cible le conteneur principal pour lui donner de la profondeur */
    [data-testid="stVerticalBlock"] > div:nth-child(2) {
        background: rgba(255, 255, 255, 0.02) !important;
        backdrop-filter: blur(20px) !important; /* L'effet de flou qui fait le verre */
        border: 1px solid rgba(212, 175, 55, 0.15) !important;
        padding: 60px !important;
        border-radius: 4px !important;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.5) !important;
    }

    /* LES INPUTS : EFFET PLAQUE DE VERRE POLI */
    /* Correction des blocs blancs vus sur les Images 9, 10, 14, 15 */
    div[data-baseweb="input"], div[data-baseweb="select"] {
        background-color: rgba(255, 255, 255, 0.04) !important;
        backdrop-filter: blur(12px) !important;
        border: 1px solid rgba(212, 175, 55, 0.1) !important;
        border-radius: 2px !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }

    /* Suppression des fonds par défaut de Streamlit */
    input, .stSelectbox div[data-baseweb="select"] {
        color: white !important;
        font-weight: 200 !important;
        background-color: transparent !important;
    }
    
    /* Effet d'illumination au clic */
    div[data-baseweb="input"]:focus-within, div[data-baseweb="select"]:focus-within {
        background-color: rgba(255, 255, 255, 0.08) !important;
        border: 1px solid rgba(212, 175, 55, 0.5) !important;
        box-shadow: 0 0 20px rgba(212, 175, 55, 0.1) !important;
    }

    /* Labels (Titre des cases) */
    label p {
        color: rgba(212, 175, 55, 0.7) !important;
        font-size: 11px !important;
        letter-spacing: 3px !important;
        text-transform: uppercase;
        margin-bottom: 12px !important;
    }

    /* BOUTON EXECUTE (STYLE TERMINAL) */
    div.stButton > button {
        background-color: transparent !important;
        color: #D4AF37 !important;
        border: 1px solid #D4AF37 !important;
        border-radius: 0px !important;
        width: 100% !important;
        height: 55px !important;
        letter-spacing: 12px;
        font-weight: 100;
        margin-top: 35px;
        text-transform: uppercase;
        transition: 0.5s ease-in-out;
    }
    div.stButton > button:hover {
        background-color: rgba(212, 175, 55, 0.1) !important;
        box-shadow: 0px 0px 40px rgba(212, 175, 55, 0.2);
        border-color: #FFD700 !important;
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
except Exception:
    st.error("Configuration Requise.")

# 4. INTERFACE DE COMMANDE
with st.container():
    sujet = st.text_input("SUJET", placeholder="DÉFINIR LE PARAMÈTRE STRATÉGIQUE...")
    
    col1, col2 = st.columns(2)
    with col1:
        fmt = st.selectbox("FORMAT", ["REEL", "CARROUSEL", "STORY"])
    with col2:
        ton = st.selectbox("TONALITÉ", ["EXPERT", "ARROGANT", "VENTE"])
    
    if st.button("EXECUTE"):
        if sujet:
            table.create({"Sujet": sujet, "Format": fmt, "Ton": ton})
            st.toast("PROTOCOL EXECUTED", icon='✅')
        else:
            st.warning("INPUT REQUIRED")
