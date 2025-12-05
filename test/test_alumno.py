import unittest
import os
from datetime import date
from app import create_app, db
from app.services import AlumnoService
from test.instancias import nuevoalumno, nuevotipodocumento

class AlumnoTestCase(unittest.TestCase):
    
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
        
    def test_crear_alumno(self):
        alumno = nuevoalumno()
        self.assertIsNotNone(alumno)
        self.assertGreaterEqual(alumno.alumno_id, 1)
        self.assertEqual(alumno.nombre, 'Julian')
        self.assertEqual(alumno.apellido, 'Alvarez')
        self.assertIsNotNone(alumno.tipo_documento)
        self.assertEqual(alumno.tipo_documento.sigla, 'DNI')
        
    def test_buscar_alumno_id(self):
        alumno = nuevoalumno()
        buscar = AlumnoService.buscar_alumno_id(alumno.alumno_id)
        self.assertIsNotNone(buscar)
        self.assertEqual(buscar.nombre, 'Julian')
        self.assertEqual(buscar.apellido, 'Alvarez')
        
    def test_buscar_todos(self):
        alumno1 = nuevoalumno()
        tipodoc2 = nuevotipodocumento(sigla='LC', nombre='Libreta Civica')
        alumno2 = nuevoalumno(
            nombre = 'Julian',
            apellido = 'Alvarez',
            sexo = 'M',
            nroDocumento = '44305104',
            tipo_documento = tipodoc2 ,
            nro_legajo = '9975',
            fechaNacimiento = date(2006,1,5), 
            fechaIngreso = date(2023,3,1)
            
        )
        
        alumnos = AlumnoService.buscar_todos()
        self.assertEqual(len(alumnos),2)
        
    def test_actualizar_alumno(self):
        alumno = nuevoalumno()
        alumno.nombre = 'Julian Actualizado'
        alumno.apellido = 'Alvarez Actualizado'
        alumno_actualizado = AlumnoService.actualizar_alumno(alumno)
        self.assertEqual(alumno_actualizado.nombre, 'Julian Actualizado')
        self.assertEqual(alumno_actualizado.apellido, 'Alvarez Actualizado') 
    
    def test_borrar_alumno_id(self):
        alumno = nuevoalumno()
        resultado = AlumnoService.borrar_alumno_id(alumno.alumno_id)
        self.assertTrue(resultado)
        busqueda = AlumnoService.buscar_alumno_id(alumno.alumno_id)
        self.assertIsNone(busqueda)
        