import requests
url = "https://dog.ceo/api/breeds/image/random"
respuesta = requests.get(url)
if respuesta.status_code == 200:
    datos = respuesta.json()
    print(f"Imagen de perro: {datos['message']}")
else:
    print("Error al obtener la imagen.")
    