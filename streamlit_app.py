import streamlit as st
from pyairtable import Table

# 1. CONFIGURATION (Adaptée mobile)
st.set_page_config(page_title="L'OUTIL", layout="centered")

# 2. INJECTION CSS : CORRECTIF SAFARI & CENTRAGE ABSOLU
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400&display=swap');

    /* FOND NOIR MAT TEXTURÉ */
    .stApp {
        background-color: #020202 !important;
        background-image: radial-gradient(circle at 2px 2px, rgba(212, 175, 55, 0.03) 1px, transparent 0);
        background-size: 24px 24px;
        font-family: 'Inter', sans-serif !important;
    }
    
    [data-testid="stHeader"], [data-testid="stToolbar"], footer { display: none !important; }

    /* TITRE DORÉ LUMINEUX */
    .brand-header {
        text-align: center;
        letter-spacing: 12px; /* Réduit pour mobile */
        font-size: 32px; /* Réduit pour mobile */
        font-weight: 200;
        text-transform: uppercase;
        margin-top: 40px;
        background: linear-gradient(to bottom, #FFD700, #D4AF37, #B8860B);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0px 0px 15px rgba(212, 175, 55, 0.3);
    }

    /* LE CADRE CENTRAL PROTOCOL (CENTRAGE MOBILE) */
    [data-testid="stVerticalBlock"] > div:nth-child(2) {
        border: 1px solid rgba(212, 175, 55, 0.2) !important;
        background: rgba(0, 0, 0, 0.85) !important;
        /* CORRECTIF IPHONE : Backdrop-filter avec préfixe Webkit */
        -webkit-backdrop-filter: blur(40px) !important;
        backdrop-filter: blur(40px) !important;
        padding: 30px !important; /* Réduit pour mobile */
        border-radius: 4px !important;
        width: 95% !important; /* S'adapte à l'écran iPhone */
        margin: 0 auto !important;
        box-shadow: 0 30px 60px rgba(0, 0, 0, 0.8);
    }

    /* INPUTS STYLE VERRE AVEC CORRECTIF SAFARI */
    .stTextInput > div > div, .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.02) !important;
        -webkit-backdrop-filter: blur(15px) !important;
        backdrop-filter: blur(15px) !important;
        border-top: 1px solid rgba(255, 255, 255, 0.15) !important;
        border-bottom: 2px solid rgba(212, 175, 55, 0.25) !important;
        border-radius: 0px !important;
        height: 50px !important;
    }

    /* CORRECTION CENTRAGE DU BOUTON (LA BARRE) */
    div.stButton {
        display: flex !important;
        justify-content: center !important;
        width: 100% !important;
    }

    div.stButton > button {
        background-color: transparent !important;
        color: #D4AF37 !important;
        border: 1px solid #D4AF37 !important;
        border-radius: 0px !important;
        width: 100% !important; /* Largeur complète dans le cadre */
        max-width: 300px !important; /* Mais pas trop large sur desktop */
        height: 60px !important;
        letter-spacing: 6px; /* Plus lisible sur iPhone */
        font-weight: 300;
        text-transform: uppercase;
        margin-top: 30px !important;
        transition: 0.5s all ease;
    }

    div.stButton > button:hover {
        background-color: rgba(212, 175, 55, 0.08) !important;
        box-shadow: 0px 0px 30px rgba(212, 175, 55, 0.2);
    }

    label p {
        color: rgba(212, 175, 55, 0.8) !important;
        font-size: 10px !important;
        letter-spacing: 3px !important;
        text-transform: uppercase;
    }
</style>

<div class="brand-header">L'OUTIL</div>
<p style="text-align:center; color:rgba(212,175,55,0.4); letter-spacing:6px; font-size:9px; text-transform:uppercase; margin-bottom: 30px;">AI Command Protocol</p>
""", unsafe_allow_html=True)

# 3. LOGIQUE TECHNIQUE
try:
    api_key = st.secrets["AIRTABLE_API_KEY"]
    base_id = st.secrets["AIRTABLE_BASE_ID"]
    table = Table(api_key, base_id, "Table 1")
except:
    st.error("Protocol Configuration Required.")

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
                st.error("Erreur Airtable")
        else:
            st.warning("INPUT REQUIRED")
