import streamlit as st

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(page_title="L'OUTIL", layout="centered")

# 2. DESIGN HAUTE COUTURE (IMAGE 2)
st.markdown("""
    <style>
    /* Fond Noir Pur */
    .stApp { background-color: #050505 !important; }
    
    /* Titre OR 'AI COMMAND PROTOCOL' */
    .protocol-header {
        font-family: 'Inter', sans-serif;
        color: #D4AF37;
        text-align: center;
        letter-spacing: 12px;
        font-size: 35px;
        font-weight: 200;
        margin-top: 60px;
        text-transform: uppercase;
    }
    .protocol-sub {
        color: rgba(212, 175, 55, 0.4);
        text-align: center;
        letter-spacing: 5px;
        font-size: 9px;
        margin-bottom: 50px;
        text-transform: uppercase;
    }

    /* Boîte Centrale Glassmorphism (Image 2) */
    .stContainer {
        background: rgba(255, 255, 255, 0.01) !important;
        border: 1px solid rgba(212, 175, 55, 0.1) !important;
        padding: 50px !important;
        border-radius: 2px !important;
        box-shadow: 0px 10px 50px rgba(0,0,0,0.5);
    }

    /* Inputs Minimalistes (Lignes Or) */
    label { color: rgba(212, 175, 55, 0.7) !important; font-size: 10px !important; letter-spacing: 2px !important; }
    
    .stTextInput input, .stSelectbox div[data-baseweb="select"] {
        background-color: transparent !important;
        border: none !important;
        border-bottom: 1px solid rgba(212, 175, 55, 0.2) !important;
        color: white !important;
        border-radius: 0px !important;
        font-size: 14px !important;
    }

    /* Bouton EXECUTE - Laiton Brossé */
    div.stButton > button {
        background-color: transparent !important;
        color: #D4AF37 !important;
        border: 1px solid #D4AF37 !important;
        border-radius: 0px !important;
        width: 100% !important;
        height: 55px !important;
        letter-spacing: 6px;
        font-weight: 200;
        margin-top: 40px;
        transition: 0.5s all;
        text-transform: uppercase;
    }
    div.stButton > button:hover {
        background-color: rgba(212, 175, 55, 0.05) !important;
        border: 1px solid #FFD700 !important;
        box-shadow: 0px 0px 20px rgba(212, 175, 55, 0.2);
    }

    /* Masquer le surplus */
    #MainMenu, footer, header {visibility: hidden;}
    [data-testid="stHeader"] {background: rgba(0,0,0,0);}
    </style>
    
    <div class="protocol-header">L'OUTIL</div>
    <div class="protocol-sub">AI COMMAND PROTOCOL</div>
""", unsafe_allow_html=True)

# 3. INTERFACE CENTRÉE
with st.container():
    # Sujet sur une ligne
    sujet = st.text_input("SUJET", placeholder="DÉFINIR LE PARAMÈTRE...")
    
    # Format et Tonalité sur la même ligne
    col1, col2 = st.columns(2)
    with col1:
        fmt = st.selectbox("FORMAT", ["REEL", "CARROUSEL", "STORY"])
    with col2:
        ton = st.selectbox("TONALITÉ", ["EXPERT", "ARROGANT", "VENTE"])
    
    # Bouton d'exécution
    if st.button("EXECUTE"):
        st.write("Ordre transmis...")
