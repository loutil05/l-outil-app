import streamlit as st
from pyairtable import Table

# 1. SETUP
st.set_page_config(page_title="L'OUTIL", layout="centered")

# 2. CSS "FORCE BRUTE" POUR LE DESIGN IMAGE 2
st.markdown("""
    <style>
    /* 1. Fond et suppression des bordures Streamlit */
    .stApp { background-color: #050505 !important; }
    [data-testid="stHeader"] { background: rgba(0,0,0,0) !important; }
    
    /* 2. Titre OR Signature */
    .brand-header {
        color: #D4AF37 !important;
        text-align: center;
        letter-spacing: 15px;
        font-size: 38px;
        font-weight: 200;
        margin-top: 20px;
        text-transform: uppercase;
    }

    /* 3. CADRE DORE CENTRAL (Correction visuelle) */
    .main-box {
        border: 1px solid rgba(212, 175, 55, 0.2) !important;
        padding: 40px !important;
        background: rgba(255, 255, 255, 0.01) !important;
        border-radius: 2px;
        margin-top: 20px;
    }

    /* 4. SUPPRESSION DES BLOCS BLANCS (La clé de ton problème) */
    div[data-baseweb="input"], div[data-baseweb="select"], .stTextInput input {
        background-color: transparent !important;
        background: transparent !important;
        border: none !important;
        border-bottom: 1px solid rgba(212, 175, 55, 0.4) !important;
        color: white !important;
        border-radius: 0px !important;
    }
    
    /* On retire le gris qui apparaît au clic */
    div[data-baseweb="select"] > div, .stTextInput div {
        background-color: transparent !important;
    }

    /* 5. Labels dorés fins */
    label p {
        color: rgba(212, 175, 55, 0.7) !important;
        font-size: 11px !important;
        letter-spacing: 2px !important;
        text-transform: uppercase;
    }

    /* 6. Bouton EXECUTE (Style Image 2) */
    div.stButton > button {
        background-color: transparent !important;
        color: #D4AF37 !important;
        border: 1px solid #D4AF37 !important;
        border-radius: 0px !important;
        width: 140px !important;
        height: 45px !important;
        letter-spacing: 5px;
        margin: 20px auto;
        display: block;
        text-transform: uppercase;
    }
    
    #MainMenu, footer { visibility: hidden; }
    </style>
""", unsafe_allow_html=True)

# 3. INTERFACE VISUELLE
st.markdown('<div class="brand-header">L\'OUTIL</div>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:rgba(212,175,55,0.4); letter-spacing:5px; font-size:10px;">AI COMMAND PROTOCOL</p>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    
    sujet = st.text_input("SUJET", placeholder="DÉFINIR LE PARAMÈTRE...")
    
    c1, c2 = st.columns(2)
    with c1:
        fmt = st.selectbox("FORMAT", ["REEL", "CARROUSEL", "STORY"])
    with c2:
        ton = st.selectbox("TONALITÉ", ["EXPERT", "ARROGANT", "VENTE"])
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("EXECUTE"):
        try:
            api_key = st.secrets["AIRTABLE_API_KEY"]
            base_id = st.secrets["AIRTABLE_BASE_ID"]
            table = Table(api_key, base_id, "Table 1")
            table.create({"Sujet": sujet, "Format": fmt, "Ton": ton})
            st.toast("COMMAND EXECUTED", icon='✅')
        except:
            st.error("Erreur technique.")
            
    st.markdown('</div>', unsafe_allow_html=True)
