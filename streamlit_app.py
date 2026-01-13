import streamlit as st
from pyairtable import Table

# 1. INITIALISATION TECHNIQUE
st.set_page_config(page_title="L'OUTIL", layout="centered")

# 2. INJECTION CSS : MINIMALISME ABSOLU & OR PUR
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400&display=swap');

    /* 1. FOND NOIR TOTAL ET TEXTURE CARBONE */
    .stApp {
        background-color: #000000 !important;
        background-image: radial-gradient(rgba(212, 175, 55, 0.05) 1.5px, transparent 0) !important;
        background-size: 30px 30px !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    [data-testid="stHeader"], [data-testid="stToolbar"], footer { display: none !important; }

    /* 2. LOGO "SIGNATURE" AVEC HALO INTENSE */
    .brand-header {
        text-align: center;
        letter-spacing: 25px;
        font-size: clamp(32px, 12vw, 55px);
        font-weight: 100;
        text-transform: uppercase;
        margin-top: 80px;
        color: #D4AF37 !important;
        text-shadow: 
            0 0 15px rgba(212, 175, 55, 0.6),
            0 0 30px rgba(212, 175, 55, 0.2);
        width: 100%;
    }

    /* 3. STRUCTURE MINIMALISTE (ZÉRO TABLEAU, ZÉRO ARRONDIS) */
    /* On rend le container totalement invisible */
    [data-testid="stVerticalBlock"] > div {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }

    /* 4. LES ENTRÉES : LIGNES D'OR ÉPURÉES */
    .stTextInput div, .stSelectbox div, [data-baseweb="input"], [data-baseweb="select"] {
        background-color: transparent !important;
        border: none !important;
    }

    /* Suppression des bordures de boîtes pour un look "Ligne" */
    .stTextInput > div > div, .stSelectbox > div > div {
        background: transparent !important;
        border-bottom: 1px solid rgba(212, 175, 55, 0.4) !important;
        border-radius: 0px !important;
        height: 50px !important;
        transition: 0.8s all cubic-bezier(0.19, 1, 0.22, 1);
    }

    /* Interaction : La ligne s'illumine */
    div[data-baseweb="input"]:focus-within, div[data-baseweb="select"]:focus-within {
        border-bottom: 1px solid #FFD700 !important;
        box-shadow: 0 10px 20px -10px rgba(212, 175, 55, 0.3) !important;
    }

    /* STYLE DU TEXTE (OR ET FINESSE) */
    input, .stSelectbox span {
        color: #D4AF37 !important;
        -webkit-text-fill-color: #D4AF37 !important;
        font-weight: 200 !important;
        font-size: 17px !important;
        letter-spacing: 2px !important;
        text-align: center !important; /* Texte centré pour l'harmonie */
    }

    /* 5. BOUTON : LA BARRE DE COMMANDE */
    div.stButton {
        display: flex;
        justify-content: center;
        margin-top: 60px;
    }
    div.stButton > button {
        background-color: transparent !important;
        color: #D4AF37 !important;
        border: 1px solid #D4AF37 !important;
        border-radius: 0px !important;
        width: 100% !important;
        max-width: 400px !important;
        height: 70px !important;
        letter-spacing: 12px;
        font-weight: 100;
        text-transform: uppercase;
        transition: 1s all ease;
    }
    div.stButton > button:hover {
        background-color: rgba(212, 175, 55, 0.05) !important;
        letter-spacing: 15px;
        box-shadow: 0 0 50px rgba(212, 175, 55, 0.2);
    }

    /* LABELS (MICRO-TYPOGRAPHIE) */
    label p {
        color: rgba(212, 175, 55, 0.5) !important;
        font-size: 9px !important;
        letter-spacing: 5px !important;
        text-transform: uppercase;
        text-align: center !important;
        margin-bottom: 20px !important;
    }
</style>

<div class="brand-header">L'OUTIL</div>
<p style="text-align:center; color:rgba(212,175,55,0.3); letter-spacing:10px; font-size:9px; text-transform:uppercase; margin-bottom: 60px;">Protocol Interface v1.0</p>
""", unsafe_allow_html=True)

# 3. LOGIQUE TECHNIQUE
try:
    api_key = st.secrets["AIRTABLE_API_KEY"]
    base_id = st.secrets["AIRTABLE_BASE_ID"]
    table = Table(api_key, base_id, "Table 1")
except:
    st.error("SYSTEM_OFFLINE_ERR")

# 4. INTERFACE HARMONISÉE
with st.container():
    sujet = st.text_input("SUJET", placeholder="INPUT_STRATEGY")
    
    col1, col2 = st.columns(2)
    with col1:
        fmt = st.selectbox("FORMAT", ["REEL", "CARROUSEL", "STORY"])
    with col2:
        ton = st.selectbox("TONALITÉ", ["EXPERT", "ARROGANT", "VENTE"])
    
    if st.button("INITIALISER LE PROTOCOLE"):
        if sujet:
            try:
                table.create({"Sujet": sujet, "Format": fmt, "Ton": ton})
                st.toast("DATA_TRANSMITTED", icon='✅')
            except:
                st.error("CONNECTION_LOST")
        else:
            st.warning("FIELD_REQUIRED")
