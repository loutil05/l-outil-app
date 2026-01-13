import streamlit as st
from pyairtable import Table

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(page_title="L'OUTIL", layout="centered")

# 2. INJECTION CSS : EFFET CRISTAL & OR (VERSION FINALE)
st.markdown("""
<style>
    /* Fond Noir Profond avec dégradé radial pour la profondeur */
    .stApp {
        background: radial-gradient(circle at center, #1a1a1a 0%, #050505 100%) !important;
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

    /* LE CADRE "PROTOCOL" CENTRAL */
    [data-testid="stVerticalBlock"] > div:nth-child(2) {
        border: 1px solid rgba(212, 175, 55, 0.1) !important;
        background: rgba(255, 255, 255, 0.01) !important;
        backdrop-filter: blur(25px) !important;
        padding: 60px !important;
        border-radius: 4px !important;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.6) !important;
    }

    /* --- EFFET "MORCEAU DE VERRE" SUR LES CASES --- */
    /* On cible les éléments internes pour supprimer les styles standard */
    div[data-baseweb="input"], div[data-baseweb="select"] {
        background: rgba(255, 255, 255, 0.03) !important;
        backdrop-filter: blur(15px) !important; /* L'effet verre poli */
        
        /* Arêtes spéculaires : reflet de lumière sur le bord supérieur */
        border-top: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-left: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-bottom: 1px solid rgba(212, 175, 55, 0.3) !important;
        border-right: 1px solid rgba(212, 175, 55, 0.15) !important;
        
        border-radius: 2px !important;
        padding: 5px !important;
        transition: all 0.5s cubic-bezier(0.19, 1, 0.22, 1) !important;
    }

    /* Texte & Placeholder */
    .stTextInput input, .stSelectbox div[data-baseweb="select"] {
        background-color: transparent !important;
        color: white !important;
        font-weight: 200 !important;
        border: none !important;
        font-size: 15px !important;
    }
    
    /* Illumination au Focus (La plaque s'active) */
    div[data-baseweb="input"]:focus-within, div[data-baseweb="select"]:focus-within {
        background: rgba(255, 255, 255, 0.08) !important;
        border-bottom: 2px solid #D4AF37 !important;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5) !important;
    }

    /* Labels dorés discrets */
    label p {
        color: rgba(212, 175, 55, 0.7) !important;
        font-size: 11px !important;
        letter-spacing: 3px !important;
        text-transform: uppercase;
        margin-bottom: 12px !important;
    }

    /* BOUTON EXECUTE (IMAGE 2) */
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
        transition: 0.6s all;
    }
    div.stButton > button:hover {
        background-color: rgba(212, 175, 55, 0.08) !important;
        box-shadow: 0px 0px 40px rgba(212, 175, 55, 0.2);
        border-color: #FFD700 !important;
    }
</style>

<div class="brand-header">L'OUTIL</div>
<p style="text-align:center; color:rgba(212,175,55,0.4); letter-spacing:8px; font-size:10px; text-transform:uppercase; margin-bottom: 40px;">AI Command Protocol</p>
""", unsafe_allow_html=True)

# 3. LOGIQUE TECHNIQUE
try:
    # Airtable Base ID : appRGyGPT4atazrpx
    api_key = st.secrets["AIRTABLE_API_KEY"]
    base_id = st.secrets["AIRTABLE_BASE_ID"]
    table = Table(api_key, base_id, "Table 1")
except Exception:
    st.error("Protocol Configuration Required.")

# 4. INTERFACE DE COMMANDE
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
