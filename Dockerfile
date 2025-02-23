# Usar una imagen con Python instalado
FROM python:3.9

# Configurar la zona horaria
ENV TZ=UTC

# Crear el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos del backend al contenedor
COPY API_Heroes /app/API_Heroes/
COPY requirements.txt /app/

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    apache2 \
    libapache2-mod-wsgi-py3 \
    && apt-get clean

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto en el que correrá la aplicación
EXPOSE 8282

# Ejecutar las migraciones y levantar el servidor con Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8282", "API_Heroes.wsgi:application"]
