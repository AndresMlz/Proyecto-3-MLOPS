import streamlit as st
import requests

st.title("🩺 Predicción de Reingreso Hospitalario por Diabetes")

# Formulario interactivo para cada variable esperada por el modelo
input_data = {
    "time_in_hospital": st.slider("Tiempo en hospital (días)", 1, 14, 3),
    "num_lab_procedures": st.number_input("Número de procedimientos de laboratorio", min_value=0, value=40),
    "num_procedures": st.number_input("Número de procedimientos", min_value=0, value=1),
    "num_medications": st.number_input("Número de medicamentos", min_value=0, value=10),
    "number_outpatient": st.number_input("Número de visitas ambulatorias", min_value=0, value=0),
    "number_emergency": st.number_input("Número de visitas a urgencias", min_value=0, value=0),
    "number_inpatient": st.number_input("Número de hospitalizaciones previas", min_value=0, value=0),
    "number_diagnoses": st.slider("Número de diagnósticos", 1, 16, 5),
}

# Opciones de edad: mostrar el rango pero enviar el valor numérico
age_options = {
    "[0-10)": 5,
    "[10-20)": 15,
    "[20-30)": 25,
    "[30-40)": 35,
    "[40-50)": 45,
    "[50-60)": 55,
    "[60-70)": 65,
    "[70-80)": 75,
    "[80-90)": 85,
    "[90-100)": 95
}
age_label = st.selectbox("Edad del paciente", list(age_options.keys()))
input_data["age"] = age_options[age_label]

# Endpoint de la API FastAPI
API_URL = "http://inference-api/predict"

if st.button("Realizar predicción"):
    try:
        payload = {"instances": [input_data]}
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            result = response.json()
            if 'predictions' in result:
                st.success(f"🎯 Predicción: {result['predictions'][0]}")
                st.info("🧠 Modelo en uso: XGBoost")
            else:
                st.error(f"⚠️ Respuesta inesperada: {result}")
        else:
            st.error(f"⚠️ Error {response.status_code}: {response.text}")
    except Exception as e:
        st.error(f"❌ No se pudo conectar con la API: {e}")

 