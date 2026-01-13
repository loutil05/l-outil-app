import streamlit as st
from pyairtable import Table

# 1. FORCER LE THÈME SOMBRE DANS LE CODE
st.set_page_config(page_title="L'OUTIL", layout="centered")

# 2. INJECTION CSS : ULTRA-COMPATIBILITÉ ET EFFET VERRE
st.markdown("""
<style>
    /* 1. SUPPRESSION TOTALE DU BLANC (PC & MOBILE) */
    /* On cible TOUS les composants pour forcer le noir */
    html, body, .stApp, [data-testid="stAppViewContainer"] {
        background-color: #000000 !important;
        background-image: radial-gradient(circle at 2px 2px, rgba(212, 175, 55, 0.05) 1px, transparent 0) !important;
        background-size: 25px 25px !important;
        color: white !important;
    }
    
    [data-testid="stHeader"], [data-testid="stToolbar"], footer { display: none !important; }

    /* 2. TITRE DORÉ QUI BRILLE */
    .brand-header {
        text-align: center;
        letter-spacing: 15px;
        font-size: clamp(24px, 8vw, 42px); /* S'adapte à l'iPhone */
        font-weight: 200;
        text-transform: uppercase;
        margin-top: 20px;
        color: #D4AF37 !important;
        text-shadow: 0 0 15px rgba(212, 175, 55, 0.6);
    }

    /* 3. LE CADRE CENTRAL (VERRE FUMÉ) */
    [data-testid="stVerticalBlock"] > div:nth-child(2) {
        border: 1px solid rgba(212, 175, 55, 0.2) !important;
        background: rgba(10, 10, 10, 0.9) !important;
        -webkit-backdrop-filter: blur(20px) !important; /* Fix iPhone Safari */
        backdrop-filter: blur(20px) !important;
        padding: clamp(20px, 5vw, 50px) !important;
        border-radius: 4px !important;
    }

    /* 4. FIX BARRE BLANCHE : TRANSPARENCE ABSOLUE */
    /* On détruit le fond blanc des inputs Streamlit */
    .stTextInput div, .stSelectbox div, [data-baseweb="input"], [data-baseweb="select"], input {
        background-color: transparent !important;
        background: transparent !important;
        border: none !important;
        color: white !important;
        -webkit-text-fill-color: white !important;
    }

    /* On recrée le liseré Or du verre */
    .stTextInput > div > div, .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.03) !important;
        border-bottom: 2px solid rgba(212, 175, 55, 0.4) !important;
        border-radius: 0px !important;
    }

    /* 5. BOUTON : LANCER LA GÉNÉRATION (CENTRÉ) */
    div.stButton {
        text-align: center;
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
        max-width: 300px !important;
        height: 60px !important;
        letter-spacing: 4px;
        text-transform: uppercase;
        font-weight: 300;
    }
</style>

<div class="brand-header">L'OUTIL</div>
<p style="text-align:center; color:rgba(212,175,55,0.4); letter-spacing:5px; font-size:10px; text-transform:uppercase; margin-bottom: 30px;">AI Command Protocol</p>
""", unsafe_allow_html=True)

# 3. LOGIQUE TECHNIQUE
try:
    api_key = st.secrets["AIRTABLE_API_KEY"]
    base_id = st.secrets["AIRTABLE_BASE_ID"]
    table = Table(api_key, base_id, "Table 1")
except:
    st.error("Liaison technique requise.")

# 4. INTERFACE
with st.container():
    sujet = st.text_input("SUJET", placeholder="DÉFINIR LE PARAMÈTRE...")
    
    col1, col2 = st.columns(2)
    with col1:
        fmt = st.selectbox("FORMAT", ["REEL", "CARROUSEL", "STORY"])
    with col2:
        ton = st.selectbox("TONALITÉ", ["EXPERT", "ARROGANT", "VENTE"])
    
    if st.button("LANCER LA GÉNÉRATION"):
        if sujet:
            try:
                table.create({"Sujet": sujet, "Format": fmt, "Ton": ton})
                st.toast("PROTOCOLE LANCÉ", icon='✅')
            except:
                st.error("Erreur Airtable")
        else:
            st.warning("SAISIE REQUISE")
