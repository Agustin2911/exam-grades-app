from back import *
from db import *
from gui_interface import *
from notas import *
from alumno import *
from curso import *
from mysql.connector.locales.eng import client_error
base=database()
back=backend(base)
sistema=gui(back)
base.cerrar()