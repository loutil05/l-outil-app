import streamlit as st
from pyairtable import Table

# 1. CONFIGURATION
st.set_page_config(page_title="L'OUTIL", layout="centered")

# 2. INJECTION CSS : FINITIONS HAUTE-COUTURE
st.markdown("""
<style>
    /* Import de la police élégante 'Inter' */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400&display=swap');

    /* FOND TEXTURÉ NOIR MAT */
    .stApp {
        background-color: #020202 !important;
        background-image: radial-gradient(circle at 2px 2px, rgba(212, 175, 55, 0.03) 1px, transparent 0);
        background-size: 24px 24px;
        font-family: 'Inter', sans-serif !important;
    }
    
    [data-testid="stHeader"], [data-testid="stToolbar"], footer { display: none !important; }

    /* 1. TITRE QUI BRILLE (Effet Or Métallique) */
    .brand-header {
        text-align: center;
        letter-spacing: 20px;
        font-size: 48px;
        font-weight: 200;
        text-transform: uppercase;
        margin-top: 50px;
        /* Création de la texture dorée sur le texte */
        background: linear-gradient(to bottom, #FFD700, #D4AF37, #B8860B);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        /* Halo lumineux intense */
        text-shadow: 0px 0px 25px rgba(212, 175, 55, 0.6), 0px 0px 10px rgba(255, 215, 0, 0.8);
    }

    /* LE GRAND CADRE CENTRAL : VERRE FUMÉ */
    [data-testid="stVerticalBlock"] > div:nth-child(2) {
        border: 1px solid rgba(212, 175, 55, 0.2) !important;
        background: rgba(0, 0, 0, 0.85) !important;
        backdrop-filter: blur(40px) !important;
        padding: 65px !important;
        border-radius: 2px !important;
        box-shadow: 0 50px 120px rgba(0, 0, 0, 1), 0 0 30px rgba(212, 175, 55, 0.05) !important;
    }

    /* --- INPUTS & DROPDOWNS --- */
    
    /* Nettoyage des fonds par défaut */
    .stTextInput div, .stSelectbox div, div[data-baseweb="input"], div[data-baseweb="select"] {
        background-color: transparent !important;
        border: none !important;
    }

    /* 3. Police élégante à l'intérieur des champs */
    input, .stSelectbox div[data-baseweb="select"] span {
        color: rgba(255, 255, 255, 0.95) !important;
        font-weight: 300 !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 16px !important;
        letter-spacing: 1px !important;
    }

    /* Plaque de verre des champs */
    .stTextInput > div > div, .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.02) !important;
        backdrop-filter: blur(15px) !important;
        border-top: 1px solid rgba(255, 255, 255, 0.15) !important;
        border-bottom: 2px solid rgba(212, 175, 55, 0.25) !important;
        border-radius: 0px !important;
        height: 55px !important;
        transition: all 0.4s ease;
    }
    
    /* Focus : L'arête s'illumine */
    div[data-baseweb="input"]:focus-within, div[data-baseweb="select"]:focus-within {
        border-bottom: 2.5px solid #D4AF37 !important;
        background: rgba(255, 255, 255, 0.05) !important;
        box-shadow: 0 5px 20px rgba(212, 175, 55, 0.15) !important;
    }

    /* 2. CORRECTION DES MENUS DÉROULANTS (La liste qui s'ouvre) */
    ul[data-baseweb="menu"] {
        background-color: rgba(15, 15, 15, 0.98) !important; /* Fond très sombre */
        backdrop-filter: blur(20px) !important;
        border: 1px solid rgba(212, 175, 55, 0.3) !important;
        border-radius: 0px !important;
        padding: 0px !important;
    }
    /* Les options dans la liste */
    li[data-baseweb="option"] {
        color: rgba(255, 255, 255, 0.8) !important;
        font-weight: 300 !important;
        font-family: 'Inter', sans-serif !important;
        padding: 12px 20px !important;
    }
    /* L'option survolée/sélectionnée */
    li[aria-selected="true"], li[data-baseweb="option"]:hover {
        background-color: rgba(212, 175, 55, 0.15) !important;
        color: #D4AF37 !important;
        font-weight: 400 !important;
    }

    /* Labels Dorés */
    label p {
        color: rgba(212, 175, 55, 0.8) !important;
        font-size: 11px !important;
        letter-spacing: 4px !important;
        text-transform: uppercase;
        margin-bottom: 12px !important;
    }

    /* 4. BOUTON (NOUVEAU TEXTE & STYLE) */
    div.stButton > button {
        background-color: transparent !important;
        color: #D4AF37 !important;
        border: 1px solid #D4AF37 !important;
        border-radius: 0px !important;
        width: 100% !important;
        height: 65px !important;
        letter-spacing: 12px;
        font-weight: 200;
        font-size: 14px !important;
        margin-top: 45px;
        text-transform: uppercase;
        transition: 0.8s all cubic-bezier(0.19, 1, 0.22, 1);
    }
    div.stButton > button:hover {
        background-color: rgba(212, 175, 55, 0.08) !important;
        box-shadow: 0px 0px 60px rgba(212, 175, 55, 0.3);
        border: 1px solid #FFD700 !important;
        letter-spacing: 15px;
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
    st.error("Protocol Error: Check Secrets.")

# 4. INTERFACE
with st.container():
    sujet = st.text_input("SUJET", placeholder="DÉFINIR LE PARAMÈTRE STRATÉGIQUE...")
    
    col1, col2 = st.columns(2)
    with col1:
        fmt = st.selectbox("FORMAT", ["REEL", "CARROUSEL", "STORY"])
    with col2:
        ton = st.selectbox("TONALITÉ", ["EXPERT", "ARROGANT", "VENTE"])
    
    # 4. Changement du texte du bouton ici
    if st.button("INITIALISER LE PROTOCOLE"):
        if sujet:
            table.create({"Sujet": sujet, "Format": fmt, "Ton": ton})
            st.toast("PROTOCOL EXECUTED", icon='✅')
        else:
            st.warning("INPUT REQUIRED")
