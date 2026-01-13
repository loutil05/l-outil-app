import streamlit as st
from pyairtable import Table

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(page_title="L'OUTIL", layout="centered")

# 2. DESIGN PROPRIÉTAIRE (OR & GLASS)
st.markdown("""
    <style>
    /* Fond noir et police épurée */
    .stApp {
        background-color: #050505 !important;
        font-family: 'Inter', sans-serif;
    }
    
    /* Titre OR avec espacement */
    .brand-header {
        color: #D4AF37;
        text-align: center;
        letter-spacing: 15px;
        font-size: 35px;
        font-weight: 200;
        margin-top: 50px;
        margin-bottom: 5px;
    }
    .brand-sub {
        color: rgba(212, 175, 55, 0.4);
        text-align: center;
        letter-spacing: 5px;
        font-size: 10px;
        margin-bottom: 40px;
    }

    /* Conteneur Central (L'effet de l'image 2) */
    .main-interface {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(212, 175, 55, 0.15);
        padding: 40px;
        border-radius: 4px;
        backdrop-filter: blur(10px);
    }

    /* Inputs transparents avec bordure basse */
    .stTextInput > div > div > input, .stSelectbox div[data-baseweb="select"] {
        background-color: rgba(0, 0, 0, 0.3) !important;
        border: none !important;
        border-bottom: 1px solid rgba(212, 175, 55, 0.3) !important;
        color: white !important;
        border-radius: 0px !important;
    }

    /* Bouton EXECUTE Rectangulaire */
    div.stButton > button {
        background-color: transparent !important;
        color: #D4AF37 !important;
        border: 1px solid #D4AF37 !important;
        border-radius: 0px !important;
        width: 100% !important;
        height: 50px !important;
        text-transform: uppercase;
        letter-spacing: 4px;
        font-weight: 300;
        margin-top: 20px;
        transition: 0.4s;
    }
    div.stButton > button:hover {
        background-color: rgba(212, 175, 55, 0.1) !important;
        box-shadow: 0px 0px 20px rgba(212, 175, 55, 0.1);
    }

    /* Suppression des éléments parasites */
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    
    <div class="brand-header">L'OUTIL</div>
    <div class="brand-sub">AI COMMAND PROTOCOL</div>
""", unsafe_allow_html=True)

# 3. CONNEXION AIRTABLE
try:
    # Rappel : AIRTABLE_BASE_ID doit être UNIQUEMENT "appRGyGPT4atazrpx"
    api_key = st.secrets["AIRTABLE_API_KEY"]
    base_id = st.secrets["AIRTABLE_BASE_ID"]
    table = Table(api_key, base_id, "Table 1")
except:
    st.error("ERREUR : Vérifie tes Secrets Streamlit.")

# 4. INTERFACE DE COMMANDE
with st.container():
    st.markdown('<div class="main-interface">', unsafe_allow_html=True)
    
    sujet = st.text_input("SUJET", placeholder="Saisir l'ordre...")
    
    c1, c2 = st.columns(2)
    with c1:
        fmt = st.selectbox("FORMAT", ["REEL", "CARROUSEL", "STORY"])
    with c2:
        ton = st.selectbox("TONALITÉ", ["EXPERT", "ARROGANT", "VENTE"])
    
    if st.button("EXECUTE"):
        if sujet:
            with st.spinner("Transmission..."):
                table.create({"Sujet": sujet, "Format": fmt, "Ton": ton})
                st.success("COMMAND EXECUTED")
        else:
            st.warning("SAISIE REQUISE")
            
    st.markdown('</div>', unsafe_allow_html=True)
