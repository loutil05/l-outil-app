import streamlit as st
from pyairtable import Table

# 1. SETUP TECHNIQUE
st.set_page_config(page_title="L'OUTIL", layout="centered")

# 2. INJECTION CSS : CENTRAGE ABSOLU & DESIGN LUXE
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400&display=swap');

    /* 1. FORCE LE CENTRAGE DE TOUTE LA PAGE (PC & MOBILE) */
    .stApp {
        background-color: #020202 !important;
        background-image: radial-gradient(rgba(212, 175, 55, 0.05) 1.5px, transparent 0) !important;
        background-size: 25px 25px !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
    }
    
    /* Masquer les éléments inutiles */
    [data-testid="stHeader"], [data-testid="stToolbar"], footer { display: none !important; }

    /* 2. LOGO AVEC HALO DORÉ (CENTRÉ) */
    .brand-header {
        text-align: center !important;
        letter-spacing: 15px;
        font-size: clamp(30px, 8vw, 48px);
        font-weight: 200;
        text-transform: uppercase;
        background: linear-gradient(to bottom, #FFD700, #D4AF37);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 15px rgba(212, 175, 55, 0.5), 0 0 30px rgba(212, 175, 55, 0.2);
        margin-bottom: 5px;
        width: 100% !important;
    }

    /* 3. LE CADRE CENTRAL (FIXÉ AU MILIEU) */
    /* On cible le bloc vertical pour annuler le décalage à gauche */
    [data-testid="stVerticalBlock"] {
        align-items: center !important;
        width: 100% !important;
    }

    .main-card {
        border: 1px solid rgba(212, 175, 55, 0.2) !important;
        background: rgba(10, 10, 10, 0.9) !important;
        -webkit-backdrop-filter: blur(25px) !important;
        backdrop-filter: blur(25px) !important;
        padding: clamp(25px, 5vw, 50px) !important;
        border-radius: 20px !important;
        box-shadow: 0 40px 100px rgba(0, 0, 0, 1);
        width: 100% !important;
        max-width: 600px !important;
        margin: 20px auto !important;
    }

    /* --- BULLES DE SAISIE (PILLS) --- */
    .stTextInput div, .stSelectbox div, [data-baseweb="input"], [data-baseweb="select"] {
        background-color: transparent !important;
        border: none !important;
    }

    .stTextInput > div > div, .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.02) !important;
        border: 1px solid rgba(212, 175, 55, 0.4) !important;
        border-radius: 50px !important;
        height: 55px !important;
        padding: 0 20px !important;
    }

    /* Texte centré et doré */
    input, .stSelectbox span {
        color: #D4AF37 !important;
        -webkit-text-fill-color: #D4AF37 !important;
        font-weight: 300 !important;
        text-align: center !important;
        font-size: 15px !important;
    }

    /* Placeholder discret */
    input::placeholder {
        color: rgba(212, 175, 55, 0.3) !important;
    }

    /* 4. BOUTON INITIALISER (CENTRE) */
    div.stButton {
        display: flex !important;
        justify-content: center !important;
        width: 100% !important;
        margin-top: 30px;
    }
    div.stButton > button {
        background-color: transparent !important;
        color: #D4AF37 !important;
        border: 1px solid #D4AF37 !important;
        border-radius: 50px !important;
        width: 100% !important;
        max-width: 380px !important;
        height: 60px !important;
        letter-spacing: 6px;
        text-transform: uppercase;
        font-weight: 200;
        transition: 0.4s ease-in-out;
    }
    div.stButton > button:hover {
        background-color: rgba(212, 175, 55, 0.08) !important;
        box-shadow: 0 0 30px rgba(212, 175, 55, 0.3);
        border-color: #FFD700 !important;
    }

    /* LABELS CENTRÉS */
    label p {
        color: rgba(212, 175, 55, 0.7) !important;
        font-size: 10px !important;
        letter-spacing: 4px !important;
        text-transform: uppercase;
        text-align: center !important;
        width: 100%;
        margin-bottom: 10px !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. INTERFACE
st.markdown('<div class="brand-header">L\'OUTIL</div>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:rgba(212,175,55,0.4); letter-spacing:8px; font-size:10px; text-transform:uppercase; margin-bottom: 20px;">AI Command Protocol</p>', unsafe_allow_html=True)

# 4. LE CADRE (CONTAINER)
with st.container():
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    
    sujet = st.text_input("INTENTION", placeholder="QUE SOUHAITES-TU CRÉER ?")
    
    col1, col2 = st.columns(2)
    with col1:
        fmt = st.selectbox("FORMAT", ["REEL", "CARROUSEL", "STORY"])
    with col2:
        ton = st.selectbox("TONALITÉ", ["EXPERT", "ARROGANT", "VENTE"])
    
    st.markdown('</div>', unsafe_allow_html=True)

# 5. LOGIQUE TECHNIQUE
try:
    api_key = st.secrets["AIRTABLE_API_KEY"]
    base_id = st.secrets["AIRTABLE_BASE_ID"]
    table = Table(api_key, base_id, "Table 1")
except:
    st.error("System configuration required.")

if st.button("INITIALISER LE PROTOCOLE"):
    if sujet:
        try:
            table.create({"Sujet": sujet, "Format": fmt, "Ton": ton})
            st.toast("PROTOCOL EXECUTED", icon='✅')
        except:
            st.error("Connection failed.")
    else:
        st.warning("Input required.")
