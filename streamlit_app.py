import streamlit as st
from pyairtable import Table

# 1. ARCHITECTURE DE LA PAGE
st.set_page_config(page_title="L'OUTIL", layout="centered")

# 2. INJECTION CSS "VERRE & OR"
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@100;200;400&display=swap" rel="stylesheet">
    <style>
    /* Fond et Nettoyage */
    .stApp {
        background: radial-gradient(circle at center, #111 0%, #050505 100%) !important;
        font-family: 'Inter', sans-serif !important;
    }
    [data-testid="stHeader"], [data-testid="stToolbar"], footer { display: none !important; }

    /* TITRE SIGNATURE */
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

    /* LE CADRE "TERMINAL" PRINCIPAL */
    .stVerticalBlockBorderWrapper {
        border: 1px solid rgba(212, 175, 55, 0.1) !important;
        background-color: rgba(255, 255, 255, 0.01) !important;
        backdrop-filter: blur(20px) !important;
        padding: 60px !important;
        border-radius: 2px !important;
    }

    /* --- NOUVEAU : EFFET "VERRE" SUR LES INPUTS --- */
    div[data-baseweb="input"], div[data-baseweb="select"] {
        background-color: rgba(255, 255, 255, 0.03) !important; /* Légère transparence blanche */
        border: 1px solid rgba(212, 175, 55, 0.2) !important; /* Bordure fine dorée */
        backdrop-filter: blur(5px) !important; /* Effet de flou "verre" */
        border-radius: 4px !important; /* Coins légèrement arrondis */
        padding: 5px !important;
        transition: all 0.3s ease !important;
    }

    /* Texte à l'intérieur des inputs */
    .stTextInput input, .stSelectbox div[data-baseweb="select"] div {
        color: #FFFFFF !important;
        font-weight: 200 !important;
        font-size: 15px !important;
        background-color: transparent !important;
        border: none !important;
    }
    
    /* Effet au survol et au focus (Le verre s'illumine) */
    div[data-baseweb="input"]:focus-within, div[data-baseweb="select"]:focus-within {
        border: 1px solid #D4AF37 !important; /* Bordure or vif */
        background-color: rgba(255, 255, 255, 0.05) !important;
        box-shadow: 0 0 15px rgba(212, 175, 55, 0.1) !important; /* Halo lumineux */
    }

    /* LABELS (OR DISCRET) */
    label p {
        color: rgba(212, 175, 55, 0.7) !important;
        font-size: 10px !important;
        letter-spacing: 3px !important;
        text-transform: uppercase;
        margin-bottom: 8px !important;
    }

    /* BOUTON EXECUTE */
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

    /* Correction des menus déroulants (Style verre sombre) */
    ul[role="listbox"] {
        background-color: rgba(10, 10, 10, 0.95) !important;
        border: 1px solid #D4AF37 !important;
        backdrop-filter: blur(10px) !important;
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

# 4. LOGIQUE TECHNIQUE
try:
    # Rappel Airtable ID: appRGyGPT4atazrpx
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
    with c2:
        ton = st.selectbox("TONALITÉ", ["EXPERT", "ARROGANT", "VENTE"])
    
    if st.button("EXECUTE"):
        if sujet:
            table.create({"Sujet": sujet, "Format": fmt, "Ton": ton})
            st.toast("PROTOCOL EXECUTED", icon='✅')
        else:
            st.warning("SAISIE REQUISE")
