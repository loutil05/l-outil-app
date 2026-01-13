import streamlit as st
from pyairtable import Table

# 1. CONFIGURATION UNIVERSELLE
st.set_page_config(page_title="L'OUTIL", layout="centered")

# 2. INJECTION CSS : PURETÉ & COMPATIBILITÉ IPHONE
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400&display=swap');

    /* FOND NOIR CARBONE (TEXTURE SUBTILE) */
    .stApp {
        background-color: #050505 !important;
        background-image: radial-gradient(rgba(212, 175, 55, 0.03) 1px, transparent 1px) !important;
        background-size: 20px 20px !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    [data-testid="stHeader"], [data-testid="stToolbar"], footer { display: none !important; }

    /* TITRE DORÉ AVEC HALO (IMAGE 2) */
    .brand-header {
        text-align: center;
        letter-spacing: 15px;
        font-size: 40px;
        font-weight: 200;
        text-transform: uppercase;
        margin-top: 40px;
        background: linear-gradient(to bottom, #FFD700, #D4AF37);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        /* Correction pour iPhone */
        text-shadow: 0px 10px 20px rgba(212, 175, 55, 0.2);
    }

    /* LE CADRE CENTRAL PROTOCOL (VERRE FUMÉ) */
    [data-testid="stVerticalBlock"] > div:nth-child(2) {
        border: 1px solid rgba(212, 175, 55, 0.15) !important;
        background: rgba(0, 0, 0, 0.7) !important;
        /* CORRECTIFS IPHONE / SAFARI */
        -webkit-backdrop-filter: blur(25px) !important;
        backdrop-filter: blur(25px) !important;
        padding: 40px !important;
        border-radius: 2px !important;
        margin: 0 auto !important;
        box-shadow: 0 40px 80px rgba(0, 0, 0, 0.9);
    }

    /* TRANSFORMATION DES CASES EN "MORCEAUX DE VERRE" */
    .stTextInput > div > div, .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.03) !important;
        -webkit-backdrop-filter: blur(15px) !important;
        backdrop-filter: blur(15px) !important;
        border: none !important;
        border-top: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-bottom: 1.5px solid rgba(212, 175, 55, 0.3) !important;
        border-radius: 0px !important;
        height: 50px !important;
    }

    /* TEXTE ET POLICE */
    input, .stSelectbox div[data-baseweb="select"] span {
        color: #FFFFFF !important;
        font-weight: 300 !important;
        font-size: 15px !important;
    }

    /* BOUTON INITIALISER (CENTRAGE ET STYLE) */
    div.stButton {
        display: flex;
        justify-content: center;
        margin-top: 30px;
    }

    div.stButton > button {
        background-color: transparent !important;
        color: #D4AF37 !important;
        border: 1px solid #D4AF37 !important;
        border-radius: 0px !important;
        width: 100% !important;
        max-width: 350px !important;
        height: 60px !important;
        letter-spacing: 8px;
        font-weight: 200;
        text-transform: uppercase;
        transition: 0.4s all ease-in-out;
    }

    div.stButton > button:hover {
        background-color: rgba(212, 175, 55, 0.05) !important;
        box-shadow: 0px 0px 30px rgba(212, 175, 55, 0.2);
        border: 1px solid #FFD700 !important;
    }

    /* LABELS DORÉS */
    label p {
        color: rgba(212, 175, 55, 0.8) !important;
        font-size: 10px !important;
        letter-spacing: 3px !important;
        text-transform: uppercase;
    }
</style>

<div class="brand-header">L'OUTIL</div>
<p style="text-align:center; color:rgba(212,175,55,0.4); letter-spacing:6px; font-size:9px; text-transform:uppercase; margin-bottom: 30px;">AI Command Protocol</p>
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
    sujet = st.text_input("SUJET", placeholder="DÉFINIR LE PARAMÈTRE...")
    
    col1, col2 = st.columns(2)
    with col1:
        fmt = st.selectbox("FORMAT", ["REEL", "CARROUSEL", "STORY"])
    with col2:
        ton = st.selectbox("TONALITÉ", ["EXPERT", "ARROGANT", "VENTE"])
    
    if st.button("INITIALISER LE PROTOCOLE"):
        if sujet:
            try:
                table.create({"Sujet": sujet, "Format": fmt, "Ton": ton})
                st.toast("PROTOCOL EXECUTED", icon='✅')
            except:
                st.error("Erreur de liaison")
        else:
            st.warning("SAISIE REQUISE")
