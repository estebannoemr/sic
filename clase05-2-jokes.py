import requests
#url = "https://v2.jokeapi.dev/joke/Any?lang=es"
url = "https://v2.jokeapi.dev/joke/Programming?lang=es"
respuesta = requests.get(url)
if respuesta.status_code == 200:
    datos = respuesta.json()
    if datos["type"] == "single":
        print("Chiste:", datos["joke"])
    else:
        print("Chiste:", datos["setup"])
        print("Remate:", datos["delivery"])
else:
    print("Error al obtener el chiste.")
