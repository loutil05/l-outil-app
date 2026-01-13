import streamlit as st
from pyairtable import Table

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(page_title="L'OUTIL", layout="centered")

# 2. INJECTION CSS "GLASSMORPHISM" PUR (CORRIGÉ)
st.markdown("""
    <style>
    /* Fond Noir & Suppression éléments Streamlit */
    .stApp {
        background: radial-gradient(circle at center, #111 0%, #050505 100%) !important;
    }
    [data-testid="stHeader"], [data-testid="stToolbar"], footer { display: none !important; }

    /* TITRE SIGNATURE (Image 2) */
    .brand-container {
        text-align: center;
        margin-top: 50px;
        margin-bottom: 30px;
    }
    .brand-header {
        color: #D4AF37 !important;
        letter-spacing: 20px;
        font-size: 45px;
        font-weight: 100;
        text-transform: uppercase;
        font-family: 'Inter', sans-serif;
    }

    /* LE CADRE CENTRAL PROTOCOL */
    [data-testid="stVerticalBlock"] > div:nth-child(2) {
        border: 1px solid rgba(212, 175, 55, 0.1) !important;
        background-color: rgba(255, 255, 255, 0.01) !important;
        backdrop-filter: blur(20px) !important;
        padding: 50px !important;
        border-radius: 4px !important;
    }

    /* EFFET VERRE SUR LES INPUTS */
    div[data-baseweb="input"], div[data-baseweb="select"] {
        background-color: rgba(255, 255, 255, 0.04) !important;
        border: 1px solid rgba(212, 175, 55, 0.2) !important;
        backdrop-filter: blur(10px) !important;
        border-radius: 4px !important;
        transition: all 0.3s ease !important;
    }

    .stTextInput input, .stSelectbox div[data-baseweb="select"] {
        color: #FFFFFF !important;
        font-weight: 200 !important;
        background-color: transparent !important;
        border: none !important;
    }
    
    /* Focus : Le verre s'illumine */
    div[data-baseweb="input"]:focus-within, div[data-baseweb="select"]:focus-within {
        border: 1px solid #D4AF37 !important;
        box-shadow: 0 0 15px rgba(212, 175, 55, 0.15) !important;
    }

    /* Labels dorés */
    label p {
        color: rgba(212, 175, 55, 0.8) !important;
        font-size: 10px !important;
        letter-spacing: 3px !important;
        text-transform: uppercase;
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
        margin-top: 30px;
        text-transform: uppercase;
    }
    div.stButton > button:hover {
        background-color: rgba(212, 175, 55, 0.05) !important;
        box-shadow: 0px 0px 30px rgba(212, 175, 55, 0.2);
    }
    </style>
    <div class="brand-container">
        <div class="brand-header">L'OUTIL</div>
        <p style="text-align:center; color:rgba(212,175,55,0.4); letter-spacing:8px; font-size:10px; text-transform:uppercase;">AI Command Protocol</p>
    </div>
""", unsafe_allow_html=True)

# 3. LOGIQUE TECHNIQUE
try:
    api_key = st.secrets["AIRTABLE_API_KEY"]
    base_id = st.secrets["AIRTABLE_BASE_ID"]
    table = Table(api_key, base_id, "Table 1")
except:
    st.error("CONFIGURATION SECRETS REQUISE.")

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
            st.warning("SAISIE REQUISE")
