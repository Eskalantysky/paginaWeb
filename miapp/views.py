from .models import Usuario
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
import stat

FILE_PATH = '/home/kali/Documents/paginaWeb/datos.json'

@csrf_exempt  # Desactiva CSRF solo para pruebas
def crear_usuario(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nombre = data.get('nombre')
            edad = data.get('edad')  # Asegúrate de que coincida con el campo en index.html

            # Guardar los datos en JSON
            guardar_en_json(data)
            usuario = Usuario(nombre=nombre, edad=edad)
            usuario.save()

            return JsonResponse({"mensaje": f"Usuario {nombre} creado con éxito"}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Formato JSON inválido"}, status=400)

    return JsonResponse({"error": "Método no permitido"}, status=405)


def guardar_en_json(data):
    """Guarda los datos en datos.json sin sobrescribir los anteriores."""
    try:
        # Crear archivo si no existe y asignar permisos
        if not os.path.exists(FILE_PATH):
            with open(FILE_PATH, 'w') as file:
                json.dump([], file)
            os.chmod(FILE_PATH, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IWGRP | stat.S_IROTH | stat.S_IWOTH)
        
        # Leer datos existentes
        with open(FILE_PATH, 'r') as file:
            try:
                existing_data = json.load(file)
            except json.JSONDecodeError:
                existing_data = []

        # Agregar nuevos datos
        existing_data.append(data)

        # Guardar en el archivo
        with open(FILE_PATH, 'w') as file:
            json.dump(existing_data, file, indent=4)

    except Exception as e:
        print(f"Error al escribir en JSON: {e}")
