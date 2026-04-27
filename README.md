# 🌦️ Pipeline ETL de Datos Climáticos CDMX

Este proyecto implementa un **pipeline ETL (Extract, Transform, Load)** que extrae datos climáticos desde una API externa, los procesa y los almacena tanto en un archivo CSV como en una base de datos local.

Este proyecto demuestra habilidades prácticas en:

* Consumo de APIs
* Transformación de datos con pandas
* Validación de datos
* Logging y monitoreo
* Persistencia de datos (CSV + SQLite)
* Diseño de pipelines end-to-end

---

## 📌 Descripción General

El pipeline realiza los siguientes pasos:

1. Extrae datos climáticos horarios desde la API de Open-Meteo
2. Limpia y transforma los datos
3. Filtra los registros en un rango horario relevante (06:00–22:00)
4. Valida la calidad de los datos (valores nulos y negativos)
5. Almacena los resultados en:

   * Un archivo CSV
   * Una base de datos local (SQLite)
6. Registra todo el proceso mediante logs

---

## 🧱 Estructura del Proyecto

```bash
cdmx-weather-etl/
│
├── datos_clima_cdmx.csv   # Dataset generado
├── base.db                # Base de datos SQLite
├── etl_clima.log          # Logs de ejecución
│
├── daily_update.py        # Script principal del pipeline ETL
├── demo.ipynb             # Análisis exploratorio de datos
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Requisitos

* Python 3.8 o superior
* pip

---

## 📦 Instalación

Clona el repositorio:

```bash
git clone https://github.com/your-username/cdmx-weather-etl.git
cd cdmx-weather-etl
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```

---

## 🚀 Uso

Ejecuta el pipeline:

```bash
python daily_update.py
```

---

## 🔄 Detalles del Pipeline

### 🔹 Extracción

* Fuente: API de Open-Meteo
* Datos: Temperatura y precipitación por hora en CDMX (últimos 7 días)

### 🔹 Transformación

* Conversión a timestamps
* Renombrado de columnas:

  * `time` → `fecha`
  * `temperature_2m` → `temperatura_c`
  * `precipitation` → `precipitacion_mm`
* Filtrado de datos entre las 06:00 y 22:00 horas

### 🔹 Validación

* Conteo de valores nulos
* Detección de valores negativos en temperatura y precipitación

### 🔹 Carga

* Almacenamiento en:

  * `datos_clima_cdmx.csv`
  * Base de datos SQLite (`base.db`)
* Nombre de la tabla: `clima_cdmx`
* Llave primaria: `fecha`

---

## 🗃️ Base de Datos

El proyecto utiliza **SQLite**, una base de datos ligera local.

Estructura de la tabla:

| columna          | tipo      |
| ---------------- | --------- |
| fecha            | TIMESTAMP |
| temperatura_c    | NUMERIC   |
| precipitacion_mm | NUMERIC   |

---

## 📊 Análisis Exploratorio

El archivo `demo.ipynb` contiene:

* Exploración de los datos
* Análisis básico de tendencias climáticas

---

## 📝 Logs

Los logs se almacenan en:

```
etl_clima.log
```

Incluyen:

* Estado de la API
* Número de registros procesados
* Advertencias de validación
* Estado general del pipeline

---

## 🧠 Conceptos de Data Engineering Aplicados

* Diseño de pipelines ETL
* Consumo de APIs con manejo de errores
* Limpieza y transformación de datos
* Validación de calidad de datos
* Logging para observabilidad
* Integración con bases de datos relacionales (SQLite)
* Creación de tablas (`CREATE TABLE IF NOT EXISTS`)

---

## ⚠️ Notas

* La columna `fecha` es llave primaria, por lo que registros duplicados pueden generar errores en inserciones.
* Actualmente el script no maneja duplicados explícitamente.

---

## 🔮 Mejoras Futuras

* Manejo de duplicados (UPSERT)
* Parametrización de fechas y ubicación
* Automatización (cron o Airflow)
* Orquestar el flujo desde un módulo principal (main) para mejorar mantenibilidad y escalabilidad.
* Almacenamiento en la nube (S3, BigQuery, etc.)
* Pruebas unitarias
* Reglas más robustas de validación de datos

---

## 🤝 Contribuciones

Siéntete libre de hacer fork y mejorar el proyecto.

---

## 📬 Contacto

Abierto a retroalimentación y colaboración.
