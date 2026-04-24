# Documentación Técnica

## Flujo del pipeline

El pipeline realiza la extracción de datos climáticos desde la API de Open-Meteo utilizando requests. 
Posteriormente, los datos son transformados con pandas: se convierten a formato datetime, se renombran las columnas y se filtran los registros entre las 06:00 y las 22:00 horas. 
Se aplican validaciones básicas para identificar valores nulos y negativos en las variables numéricas. 
Finalmente, los datos limpios se exportan a un archivo CSV y se cargan en una base de datos para su posterior consulta.

## Decisiones técnicas

Se utilizó la librería pandas para la transformación de datos debido a su eficiencia en el manejo de estructuras tabulares. 
Para el consumo de la API se empleó requests por su simplicidad. 
Se implementó manejo de errores con try/except y logging para monitorear el pipeline.

## Mejoras futuras

Se podría integrar el pipeline en un scheduler como cron o Airflow para automatizar su ejecución periódica. 
También se podría migrar a una base de datos más robusta como PostgreSQL para mejorar la escalabilidad.

En términos de diseño, se podría refactorizar el script separando cada etapa del ETL (extracción, transformación y carga) en funciones independientes y bien documentadas, orquestadas desde un main principal. Asimismo, se integraría la carga a base de datos dentro del mismo flujo del pipeline.

Se mejoraría el manejo de errores y la lógica del pipeline para tener un mayor control del flujo de datos, reduciendo la intervención manual y aumentando la confiabilidad del proceso.

Desde la perspectiva de gobierno de datos, se podrían agregar columnas adicionales para auditoría, como fecha de carga y fecha de actualización, lo que permitiría rastrear cambios en el tiempo.

En cuanto a operación y seguridad, se implementarían backups periódicos para evitar pérdida de información. 
Además, se gestionaría la seguridad de credenciales y API keys mediante archivos de configuración (por ejemplo, variables de entorno o archivos .env), evitando exponer información sensible en el código.