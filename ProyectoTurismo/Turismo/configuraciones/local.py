from .settings import *

# Configuración de base de datos para desarrollo local
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'turismo_db',  # Nombre de tu base de datos
        'USER': 'root',
        'PASSWORD': '12345',  # Tu contraseña de MySQL
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Opcional: Configuraciones adicionales para desarrollo
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
