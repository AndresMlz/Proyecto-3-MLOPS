FROM python:3.10-slim
 
# Crear y usar directorio de trabajo

WORKDIR /app
 
# Copiar archivos necesarios

COPY streamlit_app.py .

COPY requirements.txt .
 
# Instalar dependencias

RUN pip install --no-cache-dir -r requirements.txt
 
# Exponer puerto de Streamlit

EXPOSE 8501
 
# Ejecutar la app

CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]

 