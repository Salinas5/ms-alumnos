# Microservicio Alumnos
------------
## Instalacion de uv
La herramienta uv se utiliza para la gestión de dependencias y el entorno virtual del proyecto.
(Instalacion)
- Abrir consola PowerShell como administrador:

-  powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
    

- Reiniciar pc

----------------------------
## Creacion de Proyecto
Para comenzar la configuración de uv hay que ubicarse en la carpeta raiz:

    uv init
-----------------------
## Instalación de entorno virtual (venv)

    uv venv
-----------------------
Agrego de dependencias

    uv add flask==3.1.2
----------------------
Sincronizar dependencias

    uv sync
--------------------
## Referencias
https://docs.astral.sh/uv/getting-started/first-steps/
----------------------------------------------------------------------------------
## Granian

Servidor HTTP optimizado y de gran velocidad desarrollado en Rust para proyectos en Python.
Está pensado para ejecutar aplicaciones web que utilicen los estándares ASGI, RSGI o WSGI.

----------------------------------
Ejecución de aplicación web

    granian --port 5000 --host 0.0.0.0 --http auto --workers 4 --blocking-threads 4 --backlog 2048 --interface wsgi wsgi:app
    
---------------------------------
## Referencias
https://github.com/emmett-framework/granian

-------------------------------
## Condiciones para que funcione 
- Tener Docker Desktop instalado.
- Asegurarse de que los archivos .env estén configurados correctamente.
-------------------------------
## Levantar infraestructura
Antes de levantar el microservicio de alumnos hace falta:

- Docker Desktop.
- Infraestrctura levantada:
- traefik (reverse proxy)
- redis (Redis)
- postgresql-servidor (PostgreSQL)
- pgadmin (pgAdmin4)
- Red Docker externa creada (por si no hay).
-----------------
## Crear la red
Verifica que la red externa de Docker, llamada mired, exista:

    docker network create mired

---------------
## Certificados y Traefik
Traefik es un proxy inverso y un equilibrador de tráfico, de código abierto y orientado a entornos cloud, que simplifica el despliegue de arquitecturas basadas en microservicios.

------------
Modificar archivo hosts
Agregar las siguientes líneas al final de 
- C:\Windows\System32\drivers\etc\hosts (o el equivalente en Linux/Mac):
- 127.0.0.1 traefik.universidad.localhost
- 127.0.0.1 alumnos.universidad.localhost
- 127.0.0.1 pgadmin.universidad.localhost
- 127.0.0.1 postgresql.universidad.localhost

-----------------------------
## Generar certificados (mkcert)
- Descargar e instalar mkcert ( https://github.com/FiloSottile/mkcert/releases/tag/v1.4.4).
- Generar e instalar los certificados para el dominio:
- .\mkcert -install
- .\mkcert -cert-file traefik/certs/cert.pem -key-file traefik/certs/key.pem "universidad.localhost" "*.universidad.localhost" 127.0.0.1 ::1
---------------------------
## Creacion de .env para Traefik

Crear el archivo .env en la carpeta traefik/ usando traefik/.env-example como base.
Desde la carpeta traefik/, levantar la infraestructura:

    docker compose up -d

-------------------------
#### URLs:
- PgAdmin: https://pgadmin.universidad.localhost/login

- Traefik Dashboard: https://traefik.universidad.localhost/dashboard/#/

------------------------
## Creacion del Servidor en PgAdmin
Podes usar un script SQL para inicializar las tablas y datos. 
El proyecto utiliza las tablas tipo_documento y alumnos
Ejecutar el script en el Query Tool de PgAdmin para la base de datos gestion_alumnos (o la que hayas configurado en NAME_DB):


DROP TABLE IF EXISTS alumnos CASCADE; 
DROP TABLE IF EXISTS tipo_documento CASCADE;

-- Creación de la tabla tipo_documento
CREATE TABLE tipo_documento ( 
	id SERIAL PRIMARY KEY, 
	sigla VARCHAR(10) NOT NULL, 
	nombre VARCHAR(100) NOT NULL
);

-- Creación de la tabla alumnos
CREATE TABLE alumnos (
    alumno_id SERIAL PRIMARY KEY, 
    nro_legajo VARCHAR(20) NOT NULL UNIQUE, 
    nombre VARCHAR(100) NOT NULL, 
    apellido VARCHAR(100) NOT NULL, 
    "fechaIngreso" DATE NOT NULL, 
    "fechaNacimiento" DATE NOT NULL, 
    tipo_documento_id INTEGER NOT NULL, 
    "nroDocumento" VARCHAR(20) NOT NULL UNIQUE, 
    sexo VARCHAR(1) NOT NULL, 
    id_universidad INTEGER, 
    especialidad_id INTEGER NOT NULL, 
    FOREIGN KEY(tipo_documento_id) REFERENCES tipo_documento(id)
);

-- Inserción de tipos de documento
INSERT INTO tipo_documento (sigla, nombre) VALUES 
    ('DNI', 'Documento Nacional de Identidad'), 
    ('LE', 'Libreta de Enrolamiento'), 
    ('LC', 'Libreta Cívica'), 
    ('PAS', 'Pasaporte');

 Inserción de alumnos de ejemplo
INSERT INTO alumnos ( 
    nombre, apellido, "nroDocumento", tipo_documento_id, "fechaNacimiento", sexo, nro_legajo, "fechaIngreso", id_universidad, especialidad_id
) VALUES 
    ('Martín', 'Ferreyra', '45890211', 1, '1999-09-14', 'M', '2001', '2018-03-01', 2, 3), 
    ('Carla', 'Ibáñez', '42311987', 1, '2000-12-02', 'F', '2002', '2019-03-01', 2, 3), 
    ('Bruno', 'Salvatierra', '18876543', 4, '1998-04-20', 'M', '2003', '2017-08-01', 1, 2), 
    ('Elena', 'Castro', '37900445', 1, '2001-03-27', 'F', '2004', '2020-03-01', 3, 1);

------------------------------------------
## Crear Imagen y Levantar Microservicio
crear .env para el microservicio MSALUMNOS (Docker)
El archivo .env del microservicio debe estar ubicado en la raíz del proyecto (donde también está .env_example) ya que el docker/docker-compose.yml lo busca allí.

---------------------------------
## Levantar imagen
En la raiz del proyecto
docker build -t gestion-alumnos:v1.0.0 .

-------------------------------
## Levantar el microservicio de alumnos
En la carpeta docker/ del proyecto MSALUMNOS (ubicacion de docker-compose.yml).
docker compose up --build
Si la imagen ya existe:
docker compose up

-----------------------
## Tests de Rendimiento con k6
El script de prueba de rendimiento ya se encuentra en spike_tests.js.

----------------------
## Ejecutar tests de carga
Ubicarse en la carpeta donde se encuentra el script de k6 (por ejemplo, la raíz del proyecto si el script está allí o en la subcarpeta test/).

Para ejecutar el test (asumiendo que está en la raíz y se llama spike_tests.js)

k6 run spike_tests.js

## Autores

- [@agustin_salinas](https://github.com/Salinas5)
- [@bustos_juliana](https://github.com/bustosjuliana)


