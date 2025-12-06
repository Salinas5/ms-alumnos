# 📉 Análisis de Métricas de Test de Carga (Spike Test)

El siguiente análisis se basa en un **Spike Test** diseñado para evaluar la estabilidad y el rendimiento del microservicio `ms-alumnos` bajo una carga súbita de hasta 100 usuarios virtuales (VUs).

---

## 1. Resumen de Parámetros y Resultados

| Parámetro | Valor | Notas de K6 |
| :--- | :--- | :--- |
| **Tipo de Test** | Spike Test | Perfil de carga extremo |
| **Duración del Test** | 40 segundos | |
| **VUs Máximos** | 100 | Usuarios concurrentes |
| **Peticiones Totales** | 4275 | |
| **Resultado General** | **FALLIDO** | Cruzó los tres umbrales de fallo definidos. |

---

## 2. Análisis de Estabilidad y Fallos Críticos

El microservicio mostró una falla grave en las operaciones de escritura y una inestabilidad general.

### A. Tasa de Errores HTTP (`http_req_failed`)

La tasa de fallos HTTP fue significativamente alta, violando el umbral:

| Métrica | Umbral (Meta) | Resultado Obtenido | Estado |
| :--- | :--- | :--- | :--- |
| Tasa de Fallos | `< 1%` | **4.70%** | ❌ **FALLIDO** |

---

## 3. Análisis de Rendimiento (Latencia)

El rendimiento se va degradando, quedando muy por encima del objetivo de latencia.

| Métrica | Umbral (Meta) | Resultado Obtenido | Estado |
| :--- | :--- | :--- | :--- |
| **P95 Latencia** (95% de requests) | `< 200ms` | **1.34s (1340ms)** | ❌ **FALLIDO** |
| Mediana (P50) Latencia | N/A | **152.63ms** | Alto |

* **Conclusión de Latencia:** El percentil 95 está **6.7 veces por encima del objetivo** (1.34s). Esto significa que el 5% de los usuarios más lentos tuvieron una experiencia de usuario inaceptable (más de 1.3 segundos de espera).


Pasaron TODOS LOS GETS PERO NO LOS POST
