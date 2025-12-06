from app import create_app
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
app = create_app()

# YA NO ESNECESARIO FORZAR EL CONTEXTO EN app.py, Granian lo maneja.
#  app.app_context().push()