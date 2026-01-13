import streamlit as st
from pyairtable import Table

# 1. CONFIGURATION
st.set_page_config(page_title="L'OUTIL", layout="wide")

# 2. DESIGN EXACT (LIGNES FINES, GLASSMORPHISM, OR)
st.markdown("""
    <style>
    /* Fond sombre avec dégradé subtil */
    .stApp {
        background: radial-gradient(circle at center, #1a1a1a 0%, #050505 100%) !important;
    }
    
    /* Titre Central Style 'Protocol' */
    .protocol-title {
        font-family: 'Inter', sans-serif;
        color: #D4AF37;
        text-align: center;
        letter-spacing: 12px;
        font-size: 50px;
        font-weight: 200;
        margin-top: 50px;
        text-shadow: 0px 0px 15px rgba(212, 175, 55, 0.3);
    }
    
    .subtitle {
        color: rgba(212, 175, 55, 0.6);
        text-align: center;
        letter-spacing: 4px;
        font-size: 12px;
        margin-bottom: 60px;
    }

    /* Cadre Central Glassmorphism */
    .main-box {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(212, 175, 55, 0.2);
        padding: 40px;
        border-radius: 2px;
        backdrop-filter: blur(10px);
    }

    /* Inputs style ligne fine */
    .stTextInput input, .stSelectbox div[data-baseweb="select"] {
        background-color: transparent !important;
        border: none !important;
        border-bottom: 1px solid rgba(212, 175, 55, 0.4) !important;
        border-radius: 0px !important;
        color: white !important;
        padding-left: 0px !important;
    }

    /* Bouton 'EXECUTE' Minimaliste */
    div.stButton > button {
        background-color: transparent !important;
        color: #D4AF37 !important;
        border: 1px solid #D4AF37 !important;
        border-radius: 2px !important;
        width: 100%;
        height: 50px;
        letter-spacing: 5px;
        font-weight: 300;
        margin-top: 40px;
        transition: 0.5s;
    }
    
    div.stButton > button:hover {
        background-color: rgba(212, 175, 55, 0.1) !important;
        box-shadow: 0px 0px 20px rgba(212, 175, 55, 0.2);
    }

    /* Masquer les éléments Streamlit */
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    
    <div class="protocol-title">L'OUTIL</div>
    <div class="subtitle">AI COMMAND PROTOCOL</div>
""", unsafe_allow_html=True)

# 3. CONNEXION AIRTABLE (CORRECTION DU BUG 404)
try:
    # IMPORTANT : AIRTABLE_BASE_ID doit être "appRGyGPT4atazrpx" uniquement
    api_key = st.secrets["AIRTABLE_API_KEY"]
    base_id = st.secrets["AIRTABLE_BASE_ID"]
    table = Table(api_key, base_id, "Table 1")
except:
    st.error("CONFIGURATION REQUISE")

# 4. INTERFACE
with st.container():
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    
    sujet = st.text_input("SUJET", placeholder="Entrez le paramètre...")
    
    c1, c2 = st.columns(2)
    with c1:
        fmt = st.selectbox("FORMAT", ["REEL", "CARROUSEL", "STORY"])
    with c2:
        ton = st.selectbox("TONALITÉ", ["EXPERT", "ARROGANT", "VENTE"])

    if st.button("EXECUTE"):
        if sujet:
            with st.spinner("Processing..."):
                # Envoi propre sans URL parasite
                table.create({"Sujet": sujet, "Format": fmt, "Ton": ton})
                st.success("COMMAND EXECUTED.")
        else:
            st.warning("INPUT REQUIRED.")
    
    st.markdown('</div>', unsafe_allow_html=True)
