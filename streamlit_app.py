import streamlit as st
from pyairtable import Table

# 1. CONFIGURATION (STABILITÉ MOBILE)
st.set_page_config(page_title="L'OUTIL", layout="centered")

# 2. INJECTION CSS : L'ARMURE LUXE (ZÉRO BLANC / ZÉRO BUG)
st.markdown("""
<style>
    /* FOND NOIR ABSOLU TEXTURÉ */
    .stApp {
        background-color: #000000 !important;
        background-image: radial-gradient(rgba(212, 175, 55, 0.05) 1px, transparent 1px) !important;
        background-size: 20px 20px !important;
    }
    
    /* SUPPRESSION INTERFACE */
    [data-testid="stHeader"], [data-testid="stToolbar"], footer { display: none !important; }

    /* TITRE OR MÉTALLIQUE (IMAGE 2) */
    .brand-header {
        text-align: center;
        color: #D4AF37 !important;
        letter-spacing: 15px;
        font-size: 42px;
        font-weight: 200;
        text-transform: uppercase;
        margin-top: 40px;
        text-shadow: 0px 0px 20px rgba(212, 175, 55, 0.4);
    }

    /* LE CADRE CENTRAL (VERRE FUMÉ) */
    [data-testid="stVerticalBlock"] > div:nth-child(2) {
        border: 1px solid rgba(212, 175, 55, 0.2) !important;
        background: rgba(10, 10, 10, 0.9) !important;
        -webkit-backdrop-filter: blur(20px) !important; /* Fix iPhone */
        backdrop-filter: blur(20px) !important;
        padding: 40px !important;
        border-radius: 4px !important;
        box-shadow: 0 40px 100px rgba(0, 0, 0, 1);
    }

    /* --- DESTRUCTION RADICALE DU BLANC (PC & MOBILE) --- */
    /* On cible TOUT : le container, le fond, et l'ombre interne */
    .stTextInput div, .stSelectbox div, [data-baseweb="input"], [data-baseweb="select"], [data-baseweb="base-input"] {
        background-color: transparent !important;
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }

    /* On recrée la ligne Or sous les cases (Image 2) */
    .stTextInput > div > div, .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.02) !important;
        border-bottom: 2px solid rgba(212, 175, 55, 0.4) !important;
        border-radius: 0px !important;
        height: 50px !important;
    }

    /* Force le texte en blanc pour iPhone/Safari */
    input, .stSelectbox span {
        color: white !important;
        -webkit-text-fill-color: white !important;
        font-weight: 200 !important;
    }

    /* BOUTON INITIALISER (CENTRAGE ET STYLE) */
    div.stButton {
        display: flex;
        justify-content: center;
        margin-top: 40px;
    }
    div.stButton > button {
        background-color: transparent !important;
        color: #D4AF37 !important;
        border: 1px solid #D4AF37 !important;
        border-radius: 0px !important;
        width: 100% !important;
        max-width: 350px !important;
        height: 60px !important;
        letter-spacing: 10px;
        font-weight: 200;
        text-transform: uppercase;
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
    st.error("Protocol Connection Required.")

# 4. INTERFACE
with st.container():
    sujet = st.text_input("SUJET", placeholder="DÉFINIR LE PARAMÈTRE...")
    
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
                st.error("Airtable Link Error")
        else:
            st.warning("INPUT REQUIRED")
