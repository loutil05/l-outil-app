import streamlit as st
from pyairtable import Table

# 1. ARCHITECTURE DE LA PAGE
st.set_page_config(page_title="L'OUTIL", layout="centered")

# 2. INJECTION CSS "ULTRA-GLASS" (ZÉRO BLOC BLANC)
st.markdown("""
<style>
    /* 1. FOND NOIR RADIAL */
    .stApp {
        background: radial-gradient(circle at center, #1a1a1a 0%, #050505 100%) !important;
    }
    [data-testid="stHeader"], [data-testid="stToolbar"], footer { display: none !important; }

    /* 2. TITRE SIGNATURE OR (IMAGE 2) */
    .brand-header {
        color: #D4AF37 !important;
        text-align: center;
        letter-spacing: 20px;
        font-size: 45px;
        font-weight: 100;
        text-transform: uppercase;
        margin-top: 50px;
        font-family: 'Inter', sans-serif;
        text-shadow: 0 0 15px rgba(212, 175, 55, 0.2);
    }

    /* 3. LE CADRE CENTRAL PROTOCOL */
    [data-testid="stVerticalBlock"] > div:nth-child(2) {
        border: 1px solid rgba(212, 175, 55, 0.1) !important;
        background: rgba(255, 255, 255, 0.01) !important;
        backdrop-filter: blur(25px) !important;
        padding: 60px !important;
        border-radius: 4px !important;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.7) !important;
    }

    /* --- EFFET "MORCEAU DE VERRE" DÉFINITIF --- */
    
    /* On nettoie les fonds Streamlit par défaut */
    .stTextInput div, .stSelectbox div, div[data-baseweb="input"], div[data-baseweb="select"] {
        background-color: transparent !important;
        border: none !important;
    }

    /* On crée la plaque de verre avec reflets spéculaires */
    .stTextInput > div > div, .stSelectbox > div > div {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.05) 0%, rgba(255, 255, 255, 0.01) 100%) !important;
        backdrop-filter: blur(15px) !important;
        
        /* Reflet de lumière sur les arêtes (Effet Cristal) */
        border-top: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-left: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-bottom: 2px solid rgba(212, 175, 55, 0.3) !important;
        
        border-radius: 2px !important;
        height: 48px !important;
        transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
    }

    /* Texte & Curseur */
    input, .stSelectbox div[data-baseweb="select"] span {
        color: #FFFFFF !important;
        font-weight: 200 !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    /* Interaction : Le verre s'illumine */
    div[data-baseweb="input"]:focus-within, div[data-baseweb="select"]:focus-within {
        background: rgba(255, 255, 255, 0.08) !important;
        border-bottom: 2px solid #D4AF37 !important;
        box-shadow: 0 0 25px rgba(212, 175, 55, 0.2) !important;
    }

    /* Labels Dorés Stratégiques */
    label p {
        color: rgba(212, 175, 55, 0.8) !important;
        font-size: 11px !important;
        letter-spacing: 4px !important;
        text-transform: uppercase;
        margin-bottom: 12px !important;
    }

    /* BOUTON EXECUTE (STYLE TERMINAL DE LUXE) */
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
        transition: 0.6s all ease;
    }
    div.stButton > button:hover {
        background-color: rgba(212, 175, 55, 0.1) !important;
        box-shadow: 0px 0px 40px rgba(212, 175, 55, 0.2);
        border: 1px solid #FFD700 !important;
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
    
    if st.button("EXECUTE"):
        if sujet:
            table.create({"Sujet": sujet, "Format": fmt, "Ton": ton})
            st.toast("PROTOCOL EXECUTED", icon='✅')
        else:
            st.warning("INPUT REQUIRED")
