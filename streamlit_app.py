import streamlit as st
from pyairtable import Table

# 1. ARCHITECTURE DE LA PAGE
st.set_page_config(page_title="L'OUTIL", layout="centered")

# 2. INJECTION CSS : CENTRAGE CHIRURGICAL ET DESIGN LUXE
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400&display=swap');

    /* 1. NEUTRALISATION DES MARGES STREAMLIT (LE FIX DU DÉCALAGE) */
    .stApp {
        background-color: #020202 !important;
        background-image: radial-gradient(rgba(212, 175, 55, 0.05) 1.5px, transparent 0) !important;
        background-size: 25px 25px !important;
        font-family: 'Inter', sans-serif !important;
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
    }
    
    /* On force le container principal à ignorer les marges latérales par défaut */
    [data-testid="stAppViewContainer"] {
        display: flex !important;
        justify-content: center !important;
        width: 100% !important;
    }
    
    [data-testid="stHeader"], [data-testid="stToolbar"], footer { display: none !important; }

    /* 2. LOGO AVEC HALO DORÉ (CENTRÉ) */
    .brand-header {
        text-align: center !important;
        letter-spacing: 15px;
        font-size: clamp(35px, 10vw, 55px);
        font-weight: 200;
        text-transform: uppercase;
        margin-top: 20px;
        background: linear-gradient(to bottom, #FFD700, #D4AF37);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 
            0 0 10px rgba(255, 215, 0, 0.7),
            0 0 20px rgba(212, 175, 55, 0.5),
            0 0 40px rgba(212, 175, 55, 0.3);
        width: 100% !important;
    }

    /* 3. LE CADRE CENTRAL (SYMÉTRIE TOTALE ET TAILLE PC) */
    [data-testid="stVerticalBlock"] {
        align-items: center !important;
        width: 100% !important;
        margin: 0 auto !important;
    }

    [data-testid="stVerticalBlock"] > div:nth-child(2) {
        border: 1px solid rgba(212, 175, 55, 0.2) !important;
        background: rgba(10, 10, 10, 0.9) !important;
        -webkit-backdrop-filter: blur(30px) !important;
        backdrop-filter: blur(30px) !important;
        padding: clamp(30px, 5vw, 60px) !important;
        border-radius: 25px !important;
        margin: 20px auto !important;
        width: 95% !important;
        max-width: 800px !important; /* RE-AGRANDI POUR LE PC */
        box-shadow: 0 40px 120px rgba(0, 0, 0, 1);
    }

    /* --- CASES EN MODE BULLÉS ÉLARGIES --- */
    .stTextInput div, .stSelectbox div, [data-baseweb="input"], [data-baseweb="select"] {
        background-color: transparent !important;
        border: none !important;
    }

    .stTextInput > div > div, .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.02) !important;
        border: 1px solid rgba(212, 175, 55, 0.4) !important;
        border-radius: 50px !important;
        height: 65px !important; /* PLUS HAUT POUR LE LUXE */
        transition: 0.4s all ease;
    }

    /* Texte centré et doré à l'intérieur */
    input, .stSelectbox span {
        color: #D4AF37 !important;
        -webkit-text-fill-color: #D4AF37 !important;
        font-weight: 300 !important;
        text-align: center !important;
        font-size: 18px !important;
        letter-spacing: 1px !important;
    }

    input::placeholder {
        color: rgba(212, 175, 55, 0.3) !important;
    }

    /* 4. BOUTON (LA BARRE BULLE MAJESTUEUSE) */
    div.stButton {
        display: flex !important;
        justify-content: center !important;
        width: 100% !important;
        margin-top: 50px;
    }
    div.stButton > button {
        background-color: transparent !important;
        color: #D4AF37 !important;
        border: 1px solid #D4AF37 !important;
        border-radius: 50px !important;
        width: 100% !important;
        max-width: 450px !important;
        height: 75px !important;
        letter-spacing: 10px;
        text-transform: uppercase;
        font-weight: 200;
        transition: 0.6s all ease;
    }
    div.stButton > button:hover {
        background-color: #D4AF37 !important;
        color: black !important;
        box-shadow: 0px 0px 50px rgba(212, 175, 55, 0.5);
    }

    /* LABELS CENTRÉS */
    label p {
        color: rgba(212, 175, 55, 0.8) !important;
        font-size: 11px !important;
        letter-spacing: 4px !important;
        text-transform: uppercase;
        text-align: center !important;
        width: 100%;
        margin-bottom: 15px !important;
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
    st.error("Protocol Sync Required.")

# 4. INTERFACE
with st.container():
    sujet = st.text_input("INTENTION", placeholder="QUE SOUHAITES-TU CRÉER ?")
    
    col1, col2 = st.columns(2)
    with col1:
        fmt = st.selectbox("FORMAT", ["REEL", "CARROUSEL", "STORY"])
    with col2:
        ton = st.selectbox("TONALITÉ", ["EXPERT", "ARROGANT", "VENTE"])
    
    if st.button("INITIALISER LE PROTOCOLE"):
        if sujet:
            try:
                table.create({"Sujet": sujet, "Format": fmt, "Ton": ton})
                st.toast("PROTOCOL EXECUTED", icon='✅')
            except:
                st.error("Airtable Sync Error")
        else:
            st.warning("INPUT REQUIRED")
