import streamlit as st
from pyairtable import Table

# 1. ARCHITECTURE DE LA PAGE
st.set_page_config(page_title="L'OUTIL", layout="centered")

# 2. INJECTION CSS "SILENT LUXURY" (OVERRIDE TOTAL)
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@100;200;400&display=swap" rel="stylesheet">
    <style>
    /* Fond et Suppression des éléments Streamlit */
    .stApp {
        background: radial-gradient(circle at center, #111 0%, #050505 100%) !important;
        font-family: 'Inter', sans-serif !important;
    }
    [data-testid="stHeader"], [data-testid="stToolbar"], footer { display: none !important; }

    /* TITRE SIGNATURE (IMAGE 2) */
    .brand-container {
        text-align: center;
        margin-top: 60px;
        margin-bottom: 40px;
    }
    .brand-header {
        color: #D4AF37 !important;
        letter-spacing: 20px;
        font-size: 45px;
        font-weight: 100;
        text-transform: uppercase;
        margin-bottom: 10px;
    }
    .brand-sub {
        color: rgba(212, 175, 55, 0.4);
        letter-spacing: 8px;
        font-size: 10px;
        text-transform: uppercase;
    }

    /* LE CADRE "TERMINAL" DORE */
    .stVerticalBlockBorderWrapper {
        border: 1px solid rgba(212, 175, 55, 0.1) !important;
        background-color: rgba(255, 255, 255, 0.01) !important;
        backdrop-filter: blur(20px) !important;
        padding: 60px !important;
        border-radius: 2px !important;
    }

    /* NETTOYAGE CHIRURGICAL DES INPUTS (Zéro bloc blanc) */
    div[data-baseweb="input"], div[data-baseweb="select"], .stTextInput input {
        background-color: transparent !important;
        border: none !important;
        border-bottom: 1px solid rgba(212, 175, 55, 0.3) !important;
        color: #FFFFFF !important;
        border-radius: 0px !important;
        font-weight: 200 !important;
        font-size: 15px !important;
    }
    
    /* Hover/Focus Effects */
    div[data-baseweb="input"]:focus-within, .stTextInput input:focus {
        border-bottom: 1px solid #D4AF37 !important;
        box-shadow: none !important;
    }

    /* LABELS (OR DISCRET) */
    label p {
        color: rgba(212, 175, 55, 0.7) !important;
        font-size: 10px !important;
        letter-spacing: 3px !important;
        text-transform: uppercase;
    }

    /* BOUTON EXECUTE (IMAGE 2) */
    div.stButton > button {
        background-color: transparent !important;
        color: #D4AF37 !important;
        border: 1px solid #D4AF37 !important;
        border-radius: 0px !important;
        width: 100% !important;
        height: 55px !important;
        letter-spacing: 10px;
        font-weight: 200;
        margin-top: 40px;
        text-transform: uppercase;
        transition: 0.6s cubic-bezier(0.165, 0.84, 0.44, 1);
    }
    div.stButton > button:hover {
        background-color: rgba(212, 175, 55, 0.05) !important;
        box-shadow: 0px 0px 30px rgba(212, 175, 55, 0.15);
        border: 1px solid #FFD700 !important;
    }

    /* Correction des listes de sélection */
    ul[role="listbox"] {
        background-color: #0A0A0A !important;
        border: 1px solid #D4AF37 !important;
    }
    li[role="option"] { color: white !important; }
    </style>
""", unsafe_allow_html=True)

# 3. INTERFACE VISUELLE
st.markdown("""
    <div class="brand-container">
        <div class="brand-header">L'OUTIL</div>
        <div class="brand-sub">AI COMMAND PROTOCOL</div>
    </div>
""", unsafe_allow_html=True)

# 4. LOGIQUE TECHNIQUE (SÉCURISÉE)
try:
    # Rappel : AIRTABLE_BASE_ID doit être UNIQUEMENT "appRGyGPT4atazrpx"
    api_key = st.secrets["AIRTABLE_API_KEY"]
    base_id = st.secrets["AIRTABLE_BASE_ID"]
    table = Table(api_key, base_id, "Table 1")
except:
    st.error("CONFIGURATION SECRETS REQUISE.")

# 5. SYSTÈME DE COMMANDE
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
            st.warning("SAISIE REQUISE")
