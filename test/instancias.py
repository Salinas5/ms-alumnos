from datetime import date
from app.models import Alumno, TipoDocumento
from app.services import AlumnoService, TipoDocumentoService  

def nuevotipodocumento(sigla='DNI', nombre = 'Documento Nacional de Identidad'):
    tipo_documento = TipoDocumento(sigla = sigla, nombre = nombre)
    TipoDocumentoService.crear(tipo_documento)
    return tipo_documento

def nuevoalumno(
    nombre = 'Julian', 
    apellido = 'Alvarez',
    sexo = 'M',
    nroDocumento = '44305103',
    tipo_documento = None,
    nro_legajo = '9975',
    fechaNacimiento = date(206,1,5),
    fechaIngreso= date(2023,3,1)
):
    alumno = Alumno(
        nombre = nombre,
        apellido = apellido,
        sexo = sexo,
        nroDocumento = nroDocumento,
        tipo_documento = tipo_documento or nuevotipodocumento(),
        nro_legajo = nro_legajo,
        fechaNacimiento = fechaNacimiento,
        fechaIngreso = fechaIngreso
    )
    AlumnoService.crear(alumno)
    return alumno