import streamlit as st
from pyairtable import Table

# 1. SETUP DE LA PAGE
st.set_page_config(page_title="L'OUTIL", layout="centered")

# 2. INJECTION CSS "TRUE GLASSMORPHISM"
st.markdown("""
    <style>
    /* 1. Fond Noir avec un léger dégradé pour la profondeur */
    .stApp {
        background: radial-gradient(circle at center, #151515 0%, #050505 100%) !important;
    }
    [data-testid="stHeader"], [data-testid="stToolbar"], footer { display: none !important; }

    /* 2. TITRE SIGNATURE OR */
    .brand-container {
        text-align: center;
        margin-top: 40px;
        margin-bottom: 20px;
    }
    .brand-header {
        color: #D4AF37 !important;
        letter-spacing: 18px;
        font-size: 42px;
        font-weight: 100;
        text-transform: uppercase;
        font-family: 'Inter', sans-serif;
    }

    /* 3. LE CADRE CENTRAL EN VERRE (IMAGE 2) */
    [data-testid="stVerticalBlock"] > div:nth-child(2) {
        background: rgba(255, 255, 255, 0.03) !important;
        backdrop-filter: blur(15px) !important; /* L'effet de flou qui fait le verre */
        border: 1px solid rgba(212, 175, 55, 0.15) !important;
        padding: 50px !important;
        border-radius: 4px !important;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.8) !important;
    }

    /* 4. LES INPUTS STYLE "PLAQUE DE VERRE" */
    div[data-baseweb="input"], div[data-baseweb="select"] {
        background-color: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(10px) !important;
        border: 1px solid rgba(212, 175, 55, 0.1) !important;
        border-radius: 2px !important;
        transition: all 0.4s ease !important;
    }

    /* Texte et Placeholder */
    input, .stSelectbox div[data-baseweb="select"] {
        color: white !important;
        font-weight: 200 !important;
        background-color: transparent !important;
    }
    
    /* Focus : La plaque de verre s'illumine comme sur l'Image 2 */
    div[data-baseweb="input"]:focus-within, div[data-baseweb="select"]:focus-within {
        background-color: rgba(255, 255, 255, 0.08) !important;
        border: 1px solid rgba(212, 175, 55, 0.5) !important;
        box-shadow: 0 0 15px rgba(212, 175, 55, 0.1) !important;
    }

    /* Labels (Titre des cases) */
    label p {
        color: rgba(212, 175, 55, 0.6) !important;
        font-size: 10px !important;
        letter-spacing: 3px !important;
        text-transform: uppercase;
        margin-bottom: 10px !important;
    }

    /* 5. BOUTON EXECUTE (CADRE DORE) */
    div.stButton > button {
        background-color: transparent !important;
        color: #D4AF37 !important;
        border: 1px solid #D4AF37 !important;
        border-radius: 0px !important;
        width: 100% !important;
        height: 55px !important;
        letter-spacing: 12px;
        font-weight: 100;
        margin-top: 30px;
        text-transform: uppercase;
        transition: 0.5s;
    }
    div.stButton > button:hover {
        background-color: rgba(212, 175, 55, 0.1) !important;
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
except Exception as e:
    st.error("CONFIGURATION SECRETS REQUISE.")

# 4. INTERFACE
with st.container():
    sujet = st.text_input("SUJET", placeholder="DÉFINIR LE PARAMÈTRE...")
    
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
