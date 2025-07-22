# Vamos a usar la API pública de JSONPlaceholder para obtener datos de prueba.
import requests
# 1. Definimos la URL (endpoint) a la que vamos a consultar.
# En este caso, queremos obtener la lista de "todos" (tareas).
url = "https://jsonplaceholder.typicode.com/todos"
# 2. Hacemos una solicitud GET a la API.
response = requests.get(url)
# 3. Verificamos el código de estado de la respuesta.
# Un código 200 significa que la solicitud fue exitosa.
if response.status_code == 200:
    # 4. Convertimos la respuesta JSON en un objeto de Python (una lista de diccionarios).
    datos = response.json()
   
    # 5. Mostramos los primeros 5 resultados para no saturar la pantalla.
    print("Primeras 5 tareas obtenidas de la API:")
    for tarea in datos[:5]:
        print(f"- ID: {tarea['id']}, Título: {tarea['title']}, Completada: {tarea['completed']}")
else:
    print(f"Error al consultar la API. Código de estado: {response.status_code}")
