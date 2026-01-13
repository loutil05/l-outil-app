import streamlit as st
from pyairtable import Table

# 1. CONFIGURATION (STABILITÉ MOBILE)
st.set_page_config(page_title="L'OUTIL", layout="centered")

# 2. INJECTION CSS : CENTRAGE MILLIMÉTRÉ & LUXE
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400&display=swap');

    /* FOND NOIR ABSOLU */
    .stApp {
        background-color: #000000 !important;
        background-image: radial-gradient(rgba(212, 175, 55, 0.05) 1px, transparent 1px) !important;
        background-size: 20px 20px !important;
        display: flex;
        justify-content: center;
    }
    
    [data-testid="stHeader"], [data-testid="stToolbar"], footer { display: none !important; }

    /* TITRE DORÉ LUMINEUX (CENTRAGE FORCÉ) */
    .brand-header {
        width: 100%;
        text-align: center;
        letter-spacing: 12px;
        font-size: clamp(28px, 8vw, 45px); /* S'adapte dynamiquement à l'écran */
        font-weight: 200;
        text-transform: uppercase;
        margin-top: 50px;
        color: #D4AF37 !important;
        text-shadow: 0px 0px 15px rgba(212, 175, 55, 0.3);
    }

    /* LE CADRE CENTRAL (SYMÉTRIE TOTALE PC/MOBILE) */
    [data-testid="stVerticalBlock"] > div:nth-child(2) {
        border: 1px solid rgba(212, 175, 55, 0.2) !important;
        background: rgba(10, 10, 10, 0.9) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        backdrop-filter: blur(20px) !important;
        padding: clamp(20px, 5vw, 60px) !important;
        border-radius: 2px !important;
        margin: 0 auto !important; /* Force le centrage horizontal */
        width: 100% !important;
        max-width: 600px !important; /* Évite qu'il soit trop large sur PC */
        box-shadow: 0 40px 100px rgba(0, 0, 0, 1);
    }

    /* SUPPRESSION DU BLANC DÉFINITIVE */
    .stTextInput div, .stSelectbox div, [data-baseweb="input"], [data-baseweb="select"], [data-baseweb="base-input"] {
        background-color: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }

    /* Plaque de verre poli (Inputs) */
    .stTextInput > div > div, .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.02) !important;
        border-bottom: 2px solid rgba(212, 175, 55, 0.3) !important;
        border-radius: 0px !important;
        height: 50px !important;
    }

    /* Texte en blanc pur */
    input, .stSelectbox span {
        color: white !important;
        -webkit-text-fill-color: white !important;
        font-weight: 200 !important;
        text-align: left;
    }

    /* BOUTON (LA BARRE) : CENTRAGE ABSOLU */
    div.stButton {
        display: flex !important;
        justify-content: center !important;
        width: 100% !important;
        margin-top: 40px;
    }
    
    div.stButton > button {
        background-color: transparent !important;
        color: #D4AF37 !important;
        border: 1px solid #D4AF37 !important;
        border-radius: 0px !important;
        width: 100% !important;
        max-width: 320px !important; /* Largeur de barre élégante */
        height: 60px !important;
        letter-spacing: 8px;
        font-weight: 200;
        text-transform: uppercase;
        transition: 0.5s ease-in-out;
    }
    
    div.stButton > button:hover {
        background-color: rgba(212, 175, 55, 0.08) !important;
        box-shadow: 0px 0px 30px rgba(212, 175, 55, 0.2);
        border: 1px solid #FFD700 !important;
    }

    /* LABELS DORÉS */
    label p {
        color: rgba(212, 175, 55, 0.8) !important;
        font-size: 10px !important;
        letter-spacing: 3px !important;
        text-transform: uppercase;
        width: 100%;
        text-align: left;
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
    st.error("Liaison technique requise.")

# 4. INTERFACE CENTRÉE
with st.container():
    sujet = st.text_input("SUJET", placeholder="DÉFINIR LE PARAMÈTRE STRATÉGIQUE...")
    
    col1, col2 = st.columns(2)
    with col1:
        fmt = st.selectbox("FORMAT", ["REEL", "CARROUSEL", "STORY"])
    with col2:
        ton = st.selectbox("TONALITÉ", ["EXPERT", "ARROGANT", "VENTE"])
    
    if st.button("LANCER LA GÉNÉRATION"):
        if sujet:
            try:
                table.create({"Sujet": sujet, "Format": fmt, "Ton": ton})
                st.toast("PROTOCOL EXECUTED", icon='✅')
            except:
                st.error("Erreur de liaison")
        else:
            st.warning("SAISIE REQUISE")
