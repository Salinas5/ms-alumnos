from app import create_app
import logging
# Ref: https://docs.python.org/3/library/logging.html
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
app = create_app()

#https://flask.palletsprojects.com/en/stable/appcontext/
app.app_context().push()