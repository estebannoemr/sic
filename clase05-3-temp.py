import requests
"""
latitud = -34.61   # Buenos Aires
longitud = -58.38
"""

latitud = -33.20513   # Santa Catalina de Holmberg, Córdoba, Argentina
longitud = -64.43625


# latitud = -24.16   # Los Alisos
# longitud = -65.17
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitud}&longitude={longitud}&current_weather=true"
respuesta = requests.get(url)
if respuesta.status_code == 200:
    datos = respuesta.json()
    clima = datos["current_weather"]
    print("Temperatura:", clima["temperature"], "°C")
    print("Viento:", clima["windspeed"], "km/h")
else:
    print("Error al obtener el clima.")
