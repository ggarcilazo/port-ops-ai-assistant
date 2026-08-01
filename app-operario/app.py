import streamlit as st

st.set_page_config(page_title="Asistente IA Portuaria", page_icon="⚓")
st.title("⚓ Asistente de IA - Operaciones Portuarias (Navis N4)")
st.write("Consulte procedimientos operativos y protocolos de muelle en tiempo real.")

# Campo de texto para la consulta del operario
pregunta = st.text_input("Escriba su consulta técnica:")

if st.button("Consultar Asistente"):
    if "grúa" in pregunta.lower() or "sts" in pregunta.lower():
        st.info("**Respuesta de la IA (RAG):** Según el procedimiento 01, el operador debe validar la orden en la sección 'Vessel Planning' para posicionar las grúas STS.")
    elif "falla" in pregunta.lower() or "incidente" in pregunta.lower():
        st.warning("**Respuesta de la IA (RAG):** El protocolo de incidentes exige cambiar el estado del contenedor a 'Hold-Mechanical' en Navis N4 para detener las grúas.")
    else:
        st.error("Consulta no mapeada en el fragmento base actual. Intente con palabras como 'grúa' o 'falla'.")
