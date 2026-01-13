import streamlit as st
from pyairtable import Table

# 1. ARCHITECTURE TECHNIQUE
st.set_page_config(page_title="L'OUTIL", layout="centered")

# 2. INJECTION CSS : "CRISTAL & OR" (ZÉRO BLOC BLANC)
st.markdown("""
<style>
    /* 1. Fond Noir Absolu */
    .stApp {
        background: radial-gradient(circle at center, #1a1a1a 0%, #050505 100%) !important;
    }
    [data-testid="stHeader"], [data-testid="stToolbar"], footer { display: none !important; }

    /* 2. TITRE SIGNATURE OR (Image 2) */
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

    /* 3. LE CADRE "PROTOCOL" (L'effet de l'Image 2) */
    [data-testid="stVerticalBlock"] > div:nth-child(2) {
        background: rgba(255, 255, 255, 0.01) !important;
        backdrop-filter: blur(20px) !important;
        border: 1px solid rgba(212, 175, 55, 0.1) !important;
        padding: 60px !important;
        border-radius: 4px !important;
    }

    /* 4. TRANSFORMATION DES CASES EN "MORCEAUX DE VERRE" */
    /* On cible les div internes pour supprimer le blanc/gris par défaut */
    div[data-baseweb="input"], 
    div[data-baseweb="select"], 
    div[data-baseweb="base-input"] {
        background-color: rgba(255, 255, 255, 0.03) !important;
        backdrop-filter: blur(15px) !important; /* L'effet verre poli */
        border: 1px solid rgba(255, 255, 255, 0.1) !important; /* Bordure fine cristal */
        border-bottom: 2px solid rgba(212, 175, 55, 0.3) !important; /* Ligne de base Or */
        border-radius: 2px !important;
        transition: all 0.4s ease !important;
    }

    /* On force l'input à être invisible pour laisser voir le verre */
    .stTextInput input, .stSelectbox div[data-baseweb="select"] {
        background-color: transparent !important;
        color: white !important;
        font-weight: 200 !important;
        border: none !important;
    }
    
    /* Effet "Focus" : Le verre s'illumine au clic */
    div[data-baseweb="input"]:focus-within, div[data-baseweb="select"]:focus-within {
        background-color: rgba(255, 255, 255, 0.07) !important;
        border-bottom: 2px solid #D4AF37 !important;
        box-shadow: 0 0 20px rgba(212, 175, 55, 0.15) !important;
    }

    /* Labels dorés discrets */
    label p {
        color: rgba(212, 175, 55, 0.7) !important;
        font-size: 10px !important;
        letter-spacing: 3px !important;
        text-transform: uppercase;
        margin-bottom: 12px !important;
    }

    /* 5. BOUTON EXECUTE (IMAGE 2) */
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
        transition: 0.5s ease;
    }
    div.stButton > button:hover {
        background-color: rgba(212, 175, 55, 0.08) !important;
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
    st.error("Protocol Error: Check Secrets.")

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
