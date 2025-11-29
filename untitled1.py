import streamlit as st
import pandas as pd

st.set_page_config(page_title="Clasificador de Leads – Calzados Dayana", page_icon="👠", layout="wide")

st.title("Clasificador de Leads – Calzados Dayana 👠")

st.markdown("""
Esta aplicación permite cargar una base de leads de Calzados Dayana, 
clasificarlos según su probabilidad de compra y generar una recomendación 
automática de acción comercial para cada uno.
""")

st.subheader("1. Sube tu base de leads (CSV)")

uploaded_file = st.file_uploader("Selecciona el archivo CSV generado en Google Colab", type=["csv"])

if uploaded_file is None:
    st.info("Sube un archivo CSV con las columnas: nombre_completo, fuente, producto_visto, probabilidad_compra, etc.")
else:
    # Leemos el CSV
    df = pd.read_csv(uploaded_file)

    # Verificamos que exista la columna probabilidad_compra
    if "probabilidad_compra" not in df.columns:
        st.error("El archivo no contiene la columna 'probabilidad_compra'. Revisa el CSV exportado desde Colab.")
    else:
        # Función para clasificar priori
commit message: app funcional streamlit para clasificador de leads
