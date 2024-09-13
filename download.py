import os
import requests
import json

# API key de Serper.dev
API_KEY = 'c4ab3b2ca9fdd7141b68dddef595d59e04e3ad5b'

# Función para buscar y descargar imágenes desde Serper.dev
def descargar_imagenes(consulta, num_imagenes, carpeta_destino):
    url = "https://google.serper.dev/images"
    payload = json.dumps({
      "q": consulta
    })
    headers = {
      'X-API-KEY': API_KEY,
      'Content-Type': 'application/json'
    }

    # Realizar la solicitud a Serper.dev
    response = requests.post(url, headers=headers, data=payload)
    resultados = response.json()

    # Verificar si hay resultados
    if "images" not in resultados:
        print("No se encontraron imágenes en la respuesta.")
        return

    # Crear la carpeta de destino si no existe
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    # Descargar las imágenes
    contador = 0
    for imagen in resultados["images"]:
        if contador >= num_imagenes:
            break
        try:
            # Obtener la URL de la imagen
            url_imagen = imagen["imageUrl"]
            # Descargar y guardar la imagen
            img_data = requests.get(url_imagen).content
            with open(os.path.join(carpeta_destino, f"imagen_{contador + 1}.jpg"), "wb") as handler:
                handler.write(img_data)
            contador += 1
            print(f"Descargada {contador} imagen: {url_imagen}")
        except Exception as e:
            print(f"Error al descargar la imagen {contador + 1}: {e}")

# Ejemplo de uso
consulta = "wlc ruckus"
num_imagenes = 30  # Número de imágenes a descargar
carpeta_destino = "dataset/wireless/ruckus"

descargar_imagenes(consulta, num_imagenes, carpeta_destino)
