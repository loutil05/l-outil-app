import streamlit as st
from pyairtable import Table

# 1. ARCHITECTURE DE LUXE
st.set_page_config(page_title="L'OUTIL", layout="centered")

# 2. INJECTION CSS "GLASSMORPHISM" (MÉTHODE CHIRURGICALE)
st.markdown("""
<style>
    /* 1. FOND NOIR PUR */
    .stApp {
        background: radial-gradient(circle at center, #1a1a1a 0%, #050505 100%) !important;
    }
    [data-testid="stHeader"], [data-testid="stToolbar"], footer { display: none !important; }

    /* 2. TITRE SIGNATURE OR (Image 2) */
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

    /* 3. LE CADRE CENTRAL PROTOCOL */
    [data-testid="stVerticalBlock"] > div:nth-child(2) {
        border: 1px solid rgba(212, 175, 55, 0.1) !important;
        background: rgba(255, 255, 255, 0.01) !important;
        backdrop-filter: blur(25px) !important;
        padding: 60px !important;
        border-radius: 4px !important;
    }

    /* --- TRANSFORMATION DES CASES EN MORCEAUX DE VERRE --- */
    
    /* On force la transparence de TOUS les blocs Streamlit */
    .stTextInput div, .stSelectbox div, div[data-baseweb="input"], div[data-baseweb="select"] {
        background-color: transparent !important;
        border: none !important;
    }

    /* On crée la plaque de verre sur la couche de saisie */
    .stTextInput > div > div, .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.04) !important; /* Transparence cristal */
        backdrop-filter: blur(15px) !important; /* Effet de profondeur */
        
        /* Reflet de lumière "Haute-Horlogerie" (Arête supérieure) */
        border-top: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-left: 1px solid rgba(255, 255, 255, 0.1) !important;
        
        /* Signature Or sur le bas */
        border-bottom: 2px solid rgba(212, 175, 55, 0.3) !important;
        border-radius: 2px !important;
        
        height: 45px !important;
    }

    /* Texte en Blanc Pur & Fin */
    input, .stSelectbox div[data-baseweb="select"] span {
        color: white !important;
        font-weight: 200 !important;
        background-color: transparent !important;
    }
    
    /* Effet d'activation : Le verre s'illumine (Image 2) */
    div[data-baseweb="input"]:focus-within, div[data-baseweb="select"]:focus-within {
        background: rgba(255, 255, 255, 0.08) !important;
        border-bottom: 2px solid #D4AF37 !important;
        box-shadow: 0 0 20px rgba(212, 175, 55, 0.2) !important;
    }

    /* Labels Dorés */
    label p {
        color: rgba(212, 175, 55, 0.8) !important;
        font-size: 11px !important;
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
        margin-top: 40px;
        text-transform: uppercase;
        transition: 0.5s ease-in-out;
    }
    div.stButton > button:hover {
        background-color: rgba(212, 175, 55, 0.08) !important;
        box-shadow: 0px 0px 40px rgba(212, 175, 55, 0.2);
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
    st.error("Protocol Configuration Required.")

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
