Voici le code final complet, prêt à être copié-collé dans ton fichier streamlit_app.py.

J'ai supprimé tout ce qui polluait le design (blocs blancs, gris, bordures par défaut) pour ne garder que l'esthétique "AI Command Protocol" : du noir pur, des lignes dorées ultra-fines et une typographie aérée comme dans l'image que tu as validée.

Python

import streamlit as st
from pyairtable import Table

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(page_title="L'OUTIL", layout="centered")

# 2. DESIGN PROPRIÉTAIRE (OR & TRANSPARENCE)
st.markdown("""
    <style>
    /* Fond Noir Intégral */
    .stApp { background-color: #050505 !important; }
    
    /* Titre OR Signature (Image 2) */
    .brand-header {
        color: #D4AF37;
        text-align: center;
        letter-spacing: 15px;
        font-size: 38px;
        font-weight: 200;
        margin-top: 50px;
        text-transform: uppercase;
    }
    .brand-sub {
        color: rgba(212, 175, 55, 0.4);
        text-align: center;
        letter-spacing: 6px;
        font-size: 10px;
        margin-bottom: 60px;
        text-transform: uppercase;
    }

    /* NETTOYAGE DES BLOCS BLANCS (Correction Image 5, 6, 7) */
    .stTextInput input, .stSelectbox div[data-baseweb="select"] {
        background-color: transparent !important;
        border: none !important;
        border-bottom: 1px solid rgba(212, 175, 55, 0.3) !important;
        color: white !important;
        border-radius: 0px !important;
        padding-left: 0px !important;
    }
    
    /* Labels dorés et discrets */
    label p {
        color: rgba(212, 175, 55, 0.6) !important;
        font-size: 11px !important;
        letter-spacing: 2px;
        text-transform: uppercase;
    }

    /* Bouton EXECUTE (Image 2) */
    div.stButton > button {
        background-color: transparent !important;
        color: #D4AF37 !important;
        border: 1px solid #D4AF37 !important;
        border-radius: 0px !important;
        width: 100% !important;
        height: 55px !important;
        letter-spacing: 8px;
        font-weight: 200;
        margin-top: 40px;
        text-transform: uppercase;
        transition: 0.5s ease;
    }
    div.stButton > button:hover {
        background-color: rgba(212, 175, 55, 0.05) !important;
        box-shadow: 0px 0px 25px rgba(212, 175, 55, 0.2);
    }

    /* Masquage des éléments Streamlit */
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    
    <div class="brand-header">L'OUTIL</div>
    <div class="brand-sub">AI COMMAND PROTOCOL</div>
""", unsafe_allow_html=True)

# 3. LOGIQUE TECHNIQUE (SÉCURISÉE)
try:
    # Rappel : AIRTABLE_BASE_ID doit être "appRGyGPT4atazrpx"
    api_key = st.secrets["AIRTABLE_API_KEY"]
    base_id = st.secrets["AIRTABLE_BASE_ID"]
    table = Table(api_key, base_id, "Table 1")
except:
    st.error("CONFIGURATION REQUISE")

# 4. INTERFACE CENTRÉE
with st.container():
    # Champ Sujet
    sujet = st.text_input("SUJET", placeholder="DÉFINIR LE PARAMÈTRE...")
    
    # Séparateur invisible
    st.markdown("<div style='margin-top:20px;'></div>", unsafe_allow_html=True)
    
    # Format et Tonalité côte à côte
    c1, c2 = st.columns(2)
    with c1:
        fmt = st.selectbox("FORMAT", ["REEL", "CARROUSEL", "STORY"])
    with c2:
        ton = st.selectbox("TONALITÉ", ["EXPERT", "ARROGANT", "VENTE"])
    
    # Exécution
    if st.button("EXECUTE"):
        if sujet:
            try:
                table.create({"Sujet": sujet, "Format": fmt, "Ton": ton})
                st.toast("PROTOCOL SUCCESSFUL", icon='✅')
            except Exception as e:
                st.error(f"Erreur de transmission : {e}")
        else:
            st.warning("SAISIE REQUISE")
