import requests
import pandas as pd
import logging
import sqlite3
import csv

# Configuración del logger
logging.basicConfig(
    filename="etl_clima.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

#Consumo de API open-meteo
url_openmeteo = "https://api.open-meteo.com/v1/forecast"
end_point = "?latitude=19.43&longitude=-99.13&hourly=temperature_2m,precipitation&past_days=7&forecast_days=0"

try:
    logging.info("Iniciando consumo de API")

    response = requests.get(url=url_openmeteo + end_point, timeout=10)
    response.raise_for_status()

    data = response.json()
    logging.info(f"API OK - status {response.status_code}")

except requests.exceptions.RequestException as e:
    logging.error(f"Error en la API: {e}")
    raise SystemExit(e)


# Extracción
hourly = data.get("hourly", {})

time = hourly.get("time", [])
temperature = hourly.get("temperature_2m", [])
precipitation = hourly.get("precipitation", [])

logging.info(f"Registros obtenidos: {len(time)}")

# Transformación
df = pd.DataFrame({
    "time": time,
    "temperature_2m": temperature,
    "precipitation": precipitation
})

df["time"] = pd.to_datetime(df["time"])

df = df.rename(columns={
    "time": "fecha",
    "temperature_2m": "temperatura_c",
    "precipitation": "precipitacion_mm"
})

df = df[df["fecha"].dt.hour.between(6, 22)]

logging.info(f"Registros después de filtro horario: {df.shape[0]}")

# Validaciones
null_count = df.isnull().sum().sum()

negative_count = df[
    (df["temperatura_c"] < 0) | (df["precipitacion_mm"] < 0)
].shape[0]

logging.warning(f"Valores nulos encontrados: {null_count}")
logging.warning(f"Valores negativos encontrados: {negative_count}")


# Exportacion
df.to_csv("datos_clima_cdmx.csv", index=False)

logging.info("Archivo CSV generado correctamente")

# Carga de los datos 

logging.info("Conectando a la base de datos")

conn = sqlite3.connect("base_ENKI.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS clima_cdmx (
               fecha TIMESTAP,
               temperatura_c NUMERIC,
               precipitacion_mm NUMERIC,
               PRIMARY KEY (fecha)
               ) """)


logging.info("cargando datos del archivo csv")
with open("datos_clima_cdmx.csv", newline='', encoding='utf-8') as archivo:
    reader = csv.reader(archivo)
    
    next(reader)
    
    for fila in reader:
        cursor.execute(
            "INSERT INTO clima_cdmx (fecha, temperatura_c, precipitacion_mm) VALUES (?, ?, ?)", 
            fila
        )

conn.commit()
conn.close()

logging.info("carga completada")
