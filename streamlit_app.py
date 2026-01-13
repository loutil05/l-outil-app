import streamlit as st
from pyairtable import Table

# 1. CONFIGURATION
st.set_page_config(page_title="L'OUTIL", layout="centered")

# 2. INJECTION CSS "TOTAL OVERRIDE" (POUR EFFACER LE BLANC)
st.markdown("""
<style>
    /* 1. Fond et Suppression Globale */
    .stApp {
        background: radial-gradient(circle at center, #1a1a1a 0%, #050505 100%) !important;
    }
    [data-testid="stHeader"], [data-testid="stToolbar"], footer { display: none !important; }

    /* 2. TITRE SIGNATURE OR */
    .brand-header {
        color: #D4AF37 !important;
        text-align: center;
        letter-spacing: 20px;
        font-size: 45px;
        font-weight: 100;
        text-transform: uppercase;
        margin-top: 50px;
        font-family: 'Inter', sans-serif;
    }

    /* 3. LE CADRE CENTRAL */
    [data-testid="stVerticalBlock"] > div:nth-child(2) {
        border: 1px solid rgba(212, 175, 55, 0.1) !important;
        background: rgba(255, 255, 255, 0.01) !important;
        backdrop-filter: blur(20px) !important;
        padding: 60px !important;
        border-radius: 4px !important;
    }

    /* --- LA MÉTHODE NUCLÉAIRE POUR LE VERRE --- */
    
    /* On force TOUT le contenant à être transparent pour tuer le blanc */
    .stTextInput > div, .stSelectbox > div, div[data-baseweb="input"], div[data-baseweb="select"] {
        background-color: transparent !important;
        background: transparent !important;
        border: none !important;
    }

    /* On crée la plaque de verre sur la couche d'interaction */
    .stTextInput > div > div, .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.04) !important;
        backdrop-filter: blur(15px) !important;
        
        /* Arêtes de cristal (Reflets Image 2) */
        border-top: 1px solid rgba(255, 255, 255, 0.15) !important;
        border-left: 1px solid rgba(255, 255, 255, 0.05) !important;
        border-bottom: 1px solid rgba(212, 175, 55, 0.3) !important;
        border-right: 1px solid rgba(212, 175, 55, 0.1) !important;
        
        border-radius: 2px !important;
        color: white !important;
    }

    /* Suppression du gris au survol que Streamlit ajoute */
    .stTextInput > div > div:hover, .stSelectbox > div > div:hover {
        background: rgba(255, 255, 255, 0.06) !important;
        border-bottom: 1px solid #D4AF37 !important;
    }

    /* On force le texte à blanc et on enlève les bordures focus bleues */
    input {
        color: white !important;
        background: transparent !important;
    }
    
    /* Labels dorés */
    label p {
        color: rgba(212, 175, 55, 0.7) !important;
        font-size: 10px !important;
        letter-spacing: 3px !important;
        text-transform: uppercase;
        margin-bottom: 12px !important;
    }

    /* BOUTON EXECUTE */
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
