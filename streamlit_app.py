import streamlit as st
from pyairtable import Table

# 1. SETUP UNIVERSEL
st.set_page_config(page_title="L'OUTIL", layout="centered")

# 2. INJECTION CSS : ANTI-BLANC & COMPATIBILITÉ IPHONE
st.markdown("""
<style>
    /* FOND NOIR MAT TEXTURÉ */
    .stApp {
        background-color: #020202 !important;
        background-image: radial-gradient(rgba(212, 175, 55, 0.05) 1px, transparent 1px) !important;
        background-size: 15px 15px !important;
    }
    
    /* Masquer l'interface Streamlit */
    [data-testid="stHeader"], [data-testid="stToolbar"], footer { display: none !important; }

    /* TITRE AVEC EFFET OR ET HALO (IMAGE 2) */
    .brand-header {
        text-align: center;
        letter-spacing: 15px;
        font-size: 38px;
        font-weight: 200;
        text-transform: uppercase;
        margin-top: 30px;
        color: #D4AF37 !important;
        text-shadow: 0px 0px 20px rgba(212, 175, 55, 0.4);
    }

    /* LE CADRE CENTRAL PROTOCOL (VERRE FUMÉ) */
    [data-testid="stVerticalBlock"] > div:nth-child(2) {
        border: 1px solid rgba(212, 175, 55, 0.15) !important;
        background: rgba(10, 10, 10, 0.8) !important;
        -webkit-backdrop-filter: blur(20px) !important; /* Fix iPhone */
        backdrop-filter: blur(20px) !important;
        padding: 40px !important;
        border-radius: 2px !important;
        box-shadow: 0 40px 100px rgba(0, 0, 0, 1) !important;
    }

    /* --- DESTRUCTION RADICALE DU BLANC SUR PC ET MOBILE --- */
    
    /* Ciblage de tous les fonds possibles de Streamlit pour forcer la transparence */
    .stTextInput div, .stSelectbox div, [data-baseweb="input"], [data-baseweb="select"], [data-baseweb="base-input"] {
        background-color: transparent !important;
        background: transparent !important;
        border: none !important;
    }

    /* On recrée la plaque de verre avec le liseré Or sur la couche visible */
    .stTextInput > div > div, .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.03) !important;
        border-bottom: 2px solid rgba(212, 175, 55, 0.3) !important;
        border-radius: 0px !important;
        height: 50px !important;
    }

    /* Force le texte en blanc et empêche le remplissage auto blanc des navigateurs */
    input {
        color: white !important;
        background-color: transparent !important;
        -webkit-text-fill-color: white !important; /* Fix Safari/iPhone */
    }

    /* STYLE DES MENUS DÉROULANTS */
    div[role="listbox"], ul[data-baseweb="menu"] {
        background-color: #0A0A0A !important;
        border: 1px solid rgba(212, 175, 55, 0.5) !important;
    }

    /* BOUTON INITIALISER (CENTRAGE ET STYLE) */
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
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: rgba(212, 175, 55, 0.05) !important;
        box-shadow: 0px 0px 30px rgba(212, 175, 55, 0.2);
    }

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
    
    if st.button("INITIALISER LE PROTOCOLE"):
        if sujet:
            try:
                table.create({"Sujet": sujet, "Format": fmt, "Ton": ton})
                st.toast("PROTOCOL EXECUTED", icon='✅')
            except:
                st.error("Liaison Airtable interrompue")
        else:
            st.warning("SAISIE REQUISE")

st.markdown("""
    <p style="text-align:center; color:rgba(212,175,55,0.2); font-size:8px; margin-top:50px;">
        Optimisé pour Safari et Chrome. Si vous êtes sur Instagram, ouvrez dans le navigateur du téléphone.
    </p>
""", unsafe_allow_html=True)
