import streamlit as st
from pyairtable import Table

# --- CONFIGURATION LUXE ---
st.set_page_config(page_title="L'OUTIL - Administration", layout="wide")

# --- STYLE CSS "SILENT LUXURY" ---
st.markdown("""
    <style>
    .stApp { background-color: #050505 !important; }
    
    /* Menu Latéral (Sidebar) */
    [data-testid="stSidebar"] {
        background-color: #0a0a0a !important;
        border-right: 1px solid #262626;
    }

    /* Titre Or Brossé */
    .brand-title {
        font-family: 'Playfair Display', serif;
        background: linear-gradient(135deg, #a67c00 0%, #ffbf00 50%, #a67c00 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 45px;
        font-weight: 700;
        text-align: center;
        letter-spacing: 2px;
        margin-bottom: 30px;
    }

    /* Bouton Exécuter Premium */
    div.stButton > button {
        background: linear-gradient(135deg, #8a6d3b 0%, #c5a059 100%) !important;
        color: #000 !important;
        border: none !important;
        border-radius: 4px !important;
        font-weight: bold !important;
        height: 50px;
        width: 100%;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Inputs Glassmorphism */
    div.stTextInput > div > div > input, .stSelectbox div[data-baseweb="select"] {
        background-color: rgba(255,255,255,0.03) !important;
        border: 1px solid #262626 !important;
        color: white !important;
    }

    #MainMenu, footer, header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- NAVIGATION ---
with st.sidebar:
    st.markdown('<div class="brand-title">L\'OUTIL</div>', unsafe_allow_html=True)
    page = st.radio("NAVIGATION", ["⚙️ SYSTÈME DE COMMANDE", "💎 GALERIE PRIVÉE"])
    st.info("Compte Premium Actif")

# --- LOGIQUE AIRTABLE ---
try:
    # Rappel : AIRTABLE_BASE_ID doit être uniquement 'appRGyGPT4atazrpx'
    api_key = st.secrets["AIRTABLE_API_KEY"]
    base_id = st.secrets["AIRTABLE_BASE_ID"]
    table = Table(api_key, base_id, "Table 1")
except:
    st.error("ERREUR DE CONFIGURATION SECRETS")

# --- PAGE 1 : COMMANDE ---
if page == "⚙️ SYSTÈME DE COMMANDE":
    st.markdown("<h2 style='color: white; font-weight: 200;'>NOUVEL ORDRE DE GÉNÉRATION</h2>", unsafe_allow_html=True)
    
    with st.container():
        sujet = st.text_input("VOTRE PROCHAINE VIRALITÉ", placeholder="Ex: Pourquoi l'IA va dominer 2026...")
        c1, c2 = st.columns(2)
        with c1:
            format_type = st.selectbox("FORMAT", ["REEL VIRAL", "CARROUSEL LUXE", "STORY"])
        with c2:
            ton = st.selectbox("ANGLE", ["EXPERT", "ARROGANT", "VENDEUR"])
        
        if st.button("LANCER LA GÉNÉRATION"):
            if sujet:
                table.create({"Sujet": sujet, "Format": format_type, "Ton": ton})
                st.toast("Ordre transmis avec succès.", icon='✅')
            else:
                st.warning("Veuillez saisir un sujet.")

# --- PAGE 2 : GALERIE ---
elif page == "💎 GALERIE PRIVÉE":
    st.markdown("<h2 style='color: white; font-weight: 200;'>VOS CRÉATIONS VALIDÉES</h2>", unsafe_allow_html=True)
    # Remplacer par ton lien de Gallery View Airtable partagée
    st.components.v1.iframe("https://airtable.com/embed/appRGyGPT4atazrpx/shrXXXXXXXXXXXXXX", height=800, scrolling=True)
