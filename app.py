import streamlit as st
from agent import interpret
from glpi_client import init_session, create_ticket

st.set_page_config(page_title="Assistant GLPI IA")

st.title("🧠 Assistant GLPI avec IA (OpenRouter)")

query = st.text_input("Décris ce que tu veux faire :", "")

if st.button("Envoyer") and query:
    with st.spinner("🧠 Analyse en cours..."):
        action = interpret(query)

    if action.get("action") == "create_ticket":
        st.write("🎫 Création du ticket...")
        token = init_session()
        response = create_ticket(token, action["title"], action["content"])
        st.success(f"✅ Ticket #{response.get('id')} créé avec succès.")
    elif action.get("action") == "error":
        st.error(f"Erreur IA : {action['error']}")
    else:
        st.error("❌ Action non reconnue.")
