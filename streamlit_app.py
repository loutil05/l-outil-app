import streamlit as st
from pyairtable import Table

# 1. CONFIGURATION UNIVERSELLE
st.set_page_config(page_title="L'OUTIL", layout="centered")

# 2. INJECTION CSS : ÉPURATION ET COMPATIBILITÉ TOTALE
st.markdown("""
<style>
    /* Import police luxe */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;200;400&display=swap');

    /* FOND NOIR ABSOLU AVEC GRAIN SUBTIL */
    .stApp {
        background-color: #020202 !important;
        background-image: radial-gradient(rgba(212, 175, 55, 0.05) 1px, transparent 1px) !important;
        background-size: 15px 15px !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    /* Masquer l'interface Streamlit */
    [data-testid="stHeader"], [data-testid="stToolbar"], footer { display: none !important; }

    /* 1. TITRE AVEC EFFET OR MÉTALLIQUE ET HALO */
    .brand-header {
        text-align: center;
        letter-spacing: 12px;
        font-size: 42px;
        font-weight: 200;
        text-transform: uppercase;
        margin-top: 30px;
        color: #D4AF37 !important;
        text-shadow: 0px 0px 20px rgba(212, 175, 55, 0.5), 0px 0px 40px rgba(212, 175, 55, 0.2) !important;
    }

    /* 2. LE CADRE CENTRAL PROTOCOL (VERRE FUMÉ) */
    [data-testid="stVerticalBlock"] > div:nth-child(2) {
        border: 1px solid rgba(212, 175, 55, 0.1) !important;
        background: rgba(10, 10, 10, 0.8) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        backdrop-filter: blur(20px) !important;
        padding: 40px !important;
        border-radius: 2px !important;
        box-shadow: 0 40px 100px rgba(0, 0, 0, 1) !important;
    }

    /* 3. FIX RADICAL : SUPPRESSION DU BLANC SUR TOUS LES APPAREILS */
    /* On force TOUT à être transparent de manière agressive */
    div[data-baseweb="input"], 
    div[data-baseweb="select"], 
    .stTextInput div, 
    .stSelectbox div {
        background-color: transparent !important;
        background: transparent !important;
        border: none !important;
    }

    /* On recrée la "plaque de verre" manuellement */
    .stTextInput > div > div, .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.03) !important;
        border-bottom: 2px solid rgba(212, 175, 55, 0.3) !important;
        border-radius: 0px !important;
        height: 50px !important;
        color: white !important;
    }

    /* Fix pour le texte tapé (Zéro blanc) */
    input {
        color: white !important;
        background-color: transparent !important;
        -webkit-text-fill-color: white !important;
    }

    /* 4. STYLE DES MENUS DÉROULANTS (Matching total) */
    div[role="listbox"] {
        background-color: #0A0A0A !important;
        border: 1px solid #D4AF37 !important;
    }

    /* 5. BOUTON (NOUVEAU TEXTE : LANCER LA GÉNÉRATION) */
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
        letter-spacing: 5px;
        font-weight: 300;
        text-transform: uppercase;
        transition: 0.3s !important;
    }
    div.stButton > button:hover {
        background-color: rgba(212, 175, 55, 0.05) !important;
        box-shadow: 0px 0px 30px rgba(212, 175, 55, 0.2);
    }

    /* Labels dorés discrets */
    label p {
        color: rgba(212, 175, 55, 0.7) !important;
        font-size: 10px !important;
        letter-spacing: 3px !important;
        text-transform: uppercase;
    }
</style>

<div class="brand-header">L'OUTIL</div>
<p style="text-align:center; color:rgba(212,175,55,0.4); letter-spacing:8px; font-size:9px; text-transform:uppercase; margin-bottom: 30px;">AI Command Protocol</p>
""", unsafe_allow_html=True)

# 3. LOGIQUE TECHNIQUE
try:
    api_key = st.secrets["AIRTABLE_API_KEY"]
    base_id = st.secrets["AIRTABLE_BASE_ID"]
    table = Table(api_key, base_id, "Table 1")
except:
    st.error("Protocol Connection Required.")

# 4. INTERFACE
with st.container():
    sujet = st.text_input("SUJET", placeholder="DÉFINIR LE PARAMÈTRE...")
    
    col1, col2 = st.columns(2)
    with col1:
        fmt = st.selectbox("FORMAT", ["REEL", "CARROUSEL", "STORY"])
    with col2:
        ton = st.selectbox("TONALITÉ", ["EXPERT", "ARROGANT", "VENTE"])
    
    # Bouton avec le nouveau texte demandé
    if st.button("LANCER LA GÉNÉRATION"):
        if sujet:
            try:
                table.create({"Sujet": sujet, "Format": fmt, "Ton": ton})
                st.toast("PROTOCOL EXECUTED", icon='✅')
            except:
                st.error("Liaison Airtable interrompue")
        else:
            st.warning("SAISIE REQUISE")
