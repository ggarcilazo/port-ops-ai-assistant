import streamlit as st
import requests

st.set_page_config(page_title="Asistente IA Portuaria", page_icon="⚓")
st.title("⚓ Asistente de IA - Operaciones Portuarias")

# Leemos el JSON que generó la IA de tu compañero en GitHub
url_json = "https://githubusercontent.com"

try:
    data_ia = requests.get(url_json).json()
except:
    data_ia = {}

pregunta = st.text_input("Escriba su consulta técnica (grúa / falla):")

if st.button("Consultar Asistente"):
    if ("grúa" in pregunta.lower() or "sts" in pregunta.lower()) and "maquinaria" in data_ia:
        st.info(f"**Respuesta entrenada por la IA:** {data_ia['maquinaria']}")
    elif ("falla" in pregunta.lower() or "incidente" in pregunta.lower()) and "seguridad" in data_ia:
        st.warning(f"**Respuesta entrenada por la IA:** {data_ia['seguridad']}")
    else:
        st.error("Consulta no mapeada o base de datos de IA actualizándose. Intente con 'grúa' o 'falla'.")
