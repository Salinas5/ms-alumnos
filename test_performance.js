import http from 'k6/http';
import { check, sleep } from 'k6';
import { SharedArray } from 'k6/data';

export const options = {
    scenarios: {
        stress_test: {
            executor: 'constant-vus',
            vus: 20,
            duration: '30s',
        },
    },
    thresholds: {
        'http_req_duration': ['p(95) < 200'],
        // El 99% de las peticiones deben ser exitosas (código 200 o 201)
        'checks': ['rate>0.99'],
        // El número de peticiones con error del servidor (5xx) debe ser cero.
        'http_req_failed': ['rate<0.01'],
    },
};

// Se asume que Traefik expone el servicio en este dominio.
const BASE_URL = 'https://alumnos.universidad.localhost/api';

// Se asume que existe un tipo de documento con ID 1 (p. ej., DNI),
// como se infiere del archivo de test de la base de datos de prueba.
const TIPO_DOCUMENTO_ID = 1;

// 2. Función de Test
export default function () {
    // Generación de datos únicos para evitar conflictos en la BD (nroDocumento, nro_legajo)
    const random = Math.floor(Math.random() * 1000000);
    const uniqueNumber = random + Date.now();
    const headers = { 'Content-Type': 'application/json' };

    // Simulación de Tráfico:
    // 70% de probabilidad de GET (lectura) para probar la caché y el balanceo.
    if (Math.random() < 0.7) {
        // --- 70% - Operación de Lectura (GET /alumnos) ---
        const res = http.get(`${BASE_URL}/alumnos`);

        check(res, {
            'GET /alumnos es 200': (r) => r.status === 200,
        });
        
    } else {
        // --- 30% - Operación de Escritura (POST /alumnos) ---
        const payload = JSON.stringify({
            "numero_legajo": `legajo-${uniqueNumber}`,
            "nombre": "Test",
            "apellido": "K6",
            "numero_documento": `${uniqueNumber}`,
            "tipo_documento_id": TIPO_DOCUMENTO_ID,
            "fecha_nacimiento": "2000-01-01",
            "sexo": "M",
            "fecha_ingreso": "2023-01-01"
        });

        const res = http.post(`${BASE_URL}/alumnos`, payload, { headers: headers });

        check(res, {
            'POST /alumnos es 201': (r) => r.status === 201,
        });
    }


    sleep(1);
}

export function setup() {
    console.log("Verificando Tipo de Documento inicial...");
    const url = `${BASE_URL}/tipos-documento`;
    const headers = { 'Content-Type': 'application/json' };
    

    const tipoDocPayload = JSON.stringify({
        "sigla": "DNI",
        "nombre": "Documento Nacional de Identidad K6"
    });
    

    const correctPayload = JSON.stringify({
        "sigla": "DNI",
        "nombre": "Documento Nacional de Identidad K6"
    });

    try {
        const createRes = http.post(`${BASE_URL}/tipos-documento`, correctPayload, { headers: headers });
        if (createRes.status === 201) {
            console.log(`TipoDocumento creado con ID: ${createRes.json('id')}`);
            return { tipo_documento_id: createRes.json('id') };
        }
    } catch (e) {
        console.log("No se pudo crear TipoDocumento, asumiendo ID 1 existente.");
    }
    
    return { tipo_documento_id: TIPO_DOCUMENTO_ID };
}