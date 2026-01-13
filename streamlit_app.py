import streamlit as st
from pyairtable import Table

# 1. CONFIGURATION
st.set_page_config(page_title="L'OUTIL", layout="centered")

# 2. INJECTION CSS : TEXTURE NOIRE & VERRE POLI
st.markdown("""
<style>
    /* FOND TEXTURÉ NOIR MAT (Fini le rond blanc) */
    .stApp {
        background-color: #050505 !important;
        background-image: 
            radial-gradient(at 0% 0%, rgba(212, 175, 55, 0.05) 0px, transparent 50%),
            radial-gradient(at 100% 100%, rgba(20, 20, 20, 1) 0px, transparent 50%) !important;
        /* Ajout d'un grain subtil pour la texture */
        background-attachment: fixed;
    }
    
    [data-testid="stHeader"], [data-testid="stToolbar"], footer { display: none !important; }

    /* TITRE SIGNATURE OR (IMAGE 2) */
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

    /* LE CADRE CENTRAL PROTOCOL */
    [data-testid="stVerticalBlock"] > div:nth-child(2) {
        border: 1px solid rgba(212, 175, 55, 0.08) !important;
        background: rgba(10, 10, 10, 0.4) !important;
        backdrop-filter: blur(30px) !important;
        padding: 60px !important;
        border-radius: 4px !important;
        box-shadow: 0 40px 100px rgba(0, 0, 0, 0.9) !important;
    }

    /* --- EFFET "VRAI MORCEAU DE VERRE" --- */
    
    .stTextInput div, .stSelectbox div, div[data-baseweb="input"], div[data-baseweb="select"] {
        background-color: transparent !important;
        border: none !important;
    }

    /* Plaque de verre avec reflets spéculaires acérés */
    .stTextInput > div > div, .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.02) !important;
        backdrop-filter: blur(15px) !important;
        
        /* Arêtes de cristal (Image 2) */
        border-top: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-left: 1px solid rgba(255, 255, 255, 0.05) !important;
        border-bottom: 1.5px solid rgba(212, 175, 55, 0.2) !important;
        
        border-radius: 2px !important;
        height: 48px !important;
        transition: all 0.4s ease-in-out;
    }

    /* Texte & Placeholder */
    input, .stSelectbox div[data-baseweb="select"] span {
        color: rgba(255, 255, 255, 0.9) !important;
        font-weight: 200 !important;
    }
    
    /* Interaction : Le verre capte la lumière */
    div[data-baseweb="input"]:focus-within, div[data-baseweb="select"]:focus-within {
        background: rgba(255, 255, 255, 0.05) !important;
        border-bottom: 2.5px solid #D4AF37 !important;
        box-shadow: 0 0 30px rgba(212, 175, 55, 0.1) !important;
    }

    /* Labels Dorés */
    label p {
        color: rgba(212, 175, 55, 0.7) !important;
        font-size: 10px !important;
        letter-spacing: 4px !important;
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
        transition: 0.6s all ease;
    }
    div.stButton > button:hover {
        background-color: rgba(212, 175, 55, 0.05) !important;
        box-shadow: 0px 0px 50px rgba(212, 175, 55, 0.15);
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
