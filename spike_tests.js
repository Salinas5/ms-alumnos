import http from 'k6/http';
import { check, sleep } from 'k6';
// No es necesario importar Trend, Counter ni SharedArray para este test básico.

// Se asume que Traefik expone el servicio en este dominio
const BASE_URL = 'https://alumnos.universidad.localhost/api';
const ALUMNOS_URL = 'https://alumnos.universidad.localhost/api/alumnos';
const TIPO_DOCUMENTO_URL = 'https://alumnos.universidad.localhost/api/tipos-documento';

const TIPO_DOCUMENTO_ID_FALLBACK = 1;

export const options = {
    scenarios: {
        spike_test: {
            executor: 'ramping-vus',
            stages: [
                { duration: "10s", target: 100 }, // Rápido ascenso (Spike) a 100 VUs.
                { duration: "20s", target: 100 }, // Mantener la carga pico.
                { duration: "10s", target: 0 },  // Descenso a 0 VUs.
            ],
        },
    },
    thresholds: {
        'http_req_duration': ['p(95) < 200'],
        'checks': ['rate>0.99'],
        'http_req_failed': ['rate<0.01'],
    },
};


export function setup() {
    let tipoDocumentoId = TIPO_DOCUMENTO_ID_FALLBACK;
    const headers = { 'Content-Type': 'application/json' };
    
    const tempPayload = JSON.stringify({
        "sigla": "SPI",
        "nombre": "Tipo Doc Spike"
    });

    try {
        const createRes = http.post(TIPO_DOCUMENTO_URL, tempPayload, { headers: headers });
        if (createRes.status === 201) {
            tipoDocumentoId = createRes.json('id');
        } else {
            console.log("No se pudo crear TipoDocumento, usando ID de fallback: " + TIPO_DOCUMENTO_ID_FALLBACK);
        }
    } catch (e) {
        console.log("Error de conexión al crear TipoDocumento, usando ID de fallback: " + TIPO_DOCUMENTO_ID_FALLBACK);
    }
    
    return { tipo_documento_id: tipoDocumentoId };
}


export default function (data) {
    const tipoDocumentoId = data.tipo_documento_id || TIPO_DOCUMENTO_ID_FALLBACK;

    const uniqueNumber = `${__VU}-${__ITER}-${Date.now()}`;
    const headers = { 'Content-Type': 'application/json' };
    
    let res;

    // Lógica de Tráfico: 70% GET / 30% POST
    if (Math.random() < 0.7) {
        // --- 70% - Operación de Lectura (GET /api/alumnos) ---
        res = http.get(ALUMNOS_URL, { headers: headers });

        check(res, {
            'GET /alumnos es 200': (r) => r.status === 200,
        });
        
    } else {
        // --- 30% - Operación de Escritura (POST /api/alumnos) ---
        const payload = JSON.stringify({
            "numero_legajo": `legajo-${uniqueNumber}`,
            "nombre": "Test",
            "apellido": "Spike",
            "numero_documento": `${uniqueNumber}`,
            "tipo_documento_id": tipoDocumentoId, // Usamos el ID de TipoDocumento.
            "fecha_nacimiento": "2000-01-01",
            "sexo": "M",
            "fecha_ingreso": "2023-01-01"
        });

        res = http.post(ALUMNOS_URL, payload, { headers: headers });

        check(res, {
            'POST /alumnos es 201': (r) => r.status === 201,
        });
    }

    // Se recomienda un breve tiempo de espera entre iteraciones para simular un usuario real
    sleep(1);
}