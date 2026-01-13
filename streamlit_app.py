import streamlit as st
from pyairtable import Table
import os

# --- CONFIGURATION STRICTE "L'OUTIL" ---
st.set_page_config(page_title="L'OUTIL - Automation", page_icon="⚡", layout="centered")

# --- DESIGN PREMIUM NOIR & OR ---
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #FFFFFF; }
    h1 { color: #D4AF37 !important; text-align: center; font-family: 'Impact', sans-serif; letter-spacing: 2px; }
    .stButton > button { 
        width: 100%; background: linear-gradient(145deg, #D4AF37, #AA8A2E); 
        color: black; font-weight: bold; border: none; height: 50px; border-radius: 5px;
    }
    .stTextInput > div > div > input, .stSelectbox > div > div > div {
        background-color: #1A1A1A !input; border: 1px solid #D4AF37 !important; color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ L'OUTIL : SYSTÈME DE COMMANDE")
st.markdown("<p style='text-align: center; color: #888;'>Ne réfléchis plus. Commande. Encaisse.</p>", unsafe_allow_html=True)

# --- FORMULAIRE DE COMMANDE ---
with st.container():
    sujet = st.text_input("SUJET DU POST", placeholder="Ex: Pourquoi l'IA va remplacer les freelances...")
    
    col1, col2 = st.columns(2)
    with col1:
        format_type = st.selectbox("FORMAT", ["Réel Viral", "Carrousel Stratégique", "Story de Vente"])
    with col2:
        tonalite = st.selectbox("TONALITÉ", ["Arrogant & Direct", "Expert / Éducatif", "Aggressif"])

    # --- CONNEXION AIRTABLE ---
    # Ces champs seront remplis par tes "Secrets" dans Streamlit pour la sécurité
    try:
        api_key = st.secrets["AIRTABLE_API_KEY"]
        base_id = st.secrets["AIRTABLE_BASE_ID"]
        table_name = "Table 1"
        table = Table(api_key, base_id, table_name)
    except:
        st.warning("🔗 Connexion Airtable en attente des clés de sécurité.")

    if st.button("LANCER LA GÉNÉRATION & ENVOYER"):
        if not sujet:
            st.error("Précise un sujet pour l'outil.")
        else:
            with st.spinner("L'IA travaille pour toi..."):
                # Simulation de la data prête à l'envoi
                data = {
                    "Sujet": sujet,
                    "Format": format_type,
                    "Ton": tonalite,
                    "Status": "À Publier"
                }
                
                try:
                    table.create(data)
                    st.success(f"✅ COMMANDE ENREGISTRÉE DANS AIRTABLE. Va tourner ton contenu.")
                    st.balloons()
                except Exception as e:
                    st.error(f"Erreur d'envoi : {e}. Vérifie tes IDs Airtable.")

st.divider()
st.markdown("<p style='text-align: center; font-size: 0.8em;'>Propriété exclusive de L'OUTIL. Utilisation restreinte.</p>", unsafe_allow_html=True)
