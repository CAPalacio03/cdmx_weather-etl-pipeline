/* Consulta A — Temperatura promedio por día */
SELECT 
    DATE(fecha) AS fecha,
    AVG(temperatura_c) AS avg_temperatura_c
FROM clima_cdmx
GROUP BY 1
ORDER BY 2 DESC;

/* Consulta B — Horas con precipitación */
SELECT 
    fecha,
    precipitacion_mm
FROM clima_cdmx
WHERE precipitacion_mm > 0 
ORDER BY 1;

/*  Consulta C — Día con mayor variación térmica */
SELECT 
    DATE(fecha),
    MAX(temperatura_c) AS temperatura_max,
    MIN(temperatura_c) AS temperatura_min,
    MAX(temperatura_c) - MIN(temperatura_c) AS variacion_termica
FROM clima_cdmx
GROUP BY 1
ORDER BY 4 DESC
LIMIT 1;

/* Consulta D — Resumen diario */ 

SELECT 
    DATE(fecha) AS dia,
    MIN(temperatura_c) AS min_temperatura_c,
    MAX(temperatura_c) AS max_temperatura_c,
    AVG(temperatura_c) AS avg_temperatura_c,
    SUM(precipitacion_mm) AS precipitacion_acumulada_mm
FROM clima_cdmx
GROUP BY 1
ORDER BY 1;

