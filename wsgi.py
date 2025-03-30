import sys
import os
import site

# Ruta del entorno virtual
venv_path = "/home/kali/Documents/paginaWeb/venv"

# Agregar los paquetes del entorno virtual
site.addsitedir(os.path.join(venv_path, "lib/python3.13/site-packages"))

# Agregar el entorno virtual al PATH
sys.path.insert(0, venv_path)
sys.path.insert(0, "/home/kali/Documents/paginaWeb")

# Activar el entorno virtual
activate_env = os.path.join(venv_path, "bin/activate_this.py")
exec(open(activate_env).read(), dict(__file__=activate_env))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'paginaWeb.settings')

application = get_wsgi_application()
