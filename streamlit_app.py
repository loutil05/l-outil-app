import streamlit as st
from pyairtable import Table

# 1. SETUP DE LA PAGE
st.set_page_config(page_title="L'OUTIL", layout="centered")

# 2. INJECTION DU DESIGN LUXE (IMAGE 2)
st.markdown("""
    <style>
    /* Fond Noir Profond */
    .stApp {
        background-color: #050505 !important;
    }
    
    /* Titre OR 'AI COMMAND PROTOCOL' */
    .protocol-header {
        font-family: 'Inter', sans-serif;
        color: #D4AF37;
        text-align: center;
        letter-spacing: 10px;
        font-size: 40px;
        font-weight: 200;
        margin-top: 20px;
    }

    /* Champs de saisie TRANSPARENTS (Glassmorphism) */
    .stTextInput > div > div > input, .stSelectbox div[data-baseweb="select"] {
        background-color: rgba(255, 255, 255, 0.03) !important;
        border: 1px solid rgba(212, 175, 55, 0.3) !important;
        color: white !important;
        border-radius: 0px !important;
        height: 45px;
    }

    /* Bouton EXECUTE - Bordure Or */
    div.stButton > button {
        background-color: transparent !important;
        color: #D4AF37 !important;
        border: 1px solid #D4AF37 !important;
        border-radius: 0px !important;
        width: 140px;
        height: 45px;
        text-transform: uppercase;
        letter-spacing: 2px;
        transition: 0.3s;
    }
    
    div.stButton > button:hover {
        background-color: rgba(212, 175, 55, 0.1) !important;
        box-shadow: 0px 0px 15px rgba(212, 175, 55, 0.2);
    }

    /* Masquer les éléments inutiles */
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    
    <div class="protocol-header">L'OUTIL</div>
    <p style="text-align:center; color:rgba(212,175,55,0.5); letter-spacing:3px; font-size:10px; margin-bottom:50px;">AI COMMAND PROTOCOL</p>
""", unsafe_allow_html=True)

# 3. CONNEXION AIRTABLE (CORRECTE)
try:
    # Rappel : AIRTABLE_BASE_ID = "appRGyGPT4atazrpx"
    api_key = st.secrets["AIRTABLE_API_KEY"]
    base_id = st.secrets["AIRTABLE_BASE_ID"]
    table = Table(api_key, base_id, "Table 1")
except:
    st.error("CONFIGURATION REQUISE")

# 4. INTERFACE EPURÉE
sujet = st.text_input("SUJET", placeholder="Entrez le paramètre...")

col1, col2 = st.columns(2)
with col1:
    fmt = st.selectbox("FORMAT", ["REEL", "CARROUSEL", "STORY"])
with col2:
    ton = st.selectbox("TONALITÉ", ["EXPERT", "ARROGANT", "VENTE"])

st.markdown("<br>", unsafe_allow_html=True)
if st.button("EXECUTE"):
    if sujet:
        table.create({"Sujet": sujet, "Format": fmt, "Ton": ton})
        st.success("COMMAND EXECUTED")
