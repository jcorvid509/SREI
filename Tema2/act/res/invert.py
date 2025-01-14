import os
from PIL import Image, ImageOps
import requests
from io import BytesIO

def descargar_e_invertir_imagen():
    # Solicitar al usuario la URL de la imagen y el nombre del archivo para guardar
    url = input("Por favor, introduce la URL de la imagen: ")
    nombre_guardado = input("Por favor, introduce el nombre del archivo para guardar (sin extensión): ")

    # Descargar imagen desde la URL
    response = requests.get(url)
    img = Image.open(BytesIO(response.content)).convert("RGBA")

    # Crear la ruta de guardado para la imagen original
    ruta_directorio = "Tema2/act/res/img"
    if not os.path.exists(ruta_directorio):
        os.makedirs(ruta_directorio)

    ruta_guardado_original = os.path.join(ruta_directorio, f"{nombre_guardado}.png")

    # Guardar la imagen original
    img.save(ruta_guardado_original)

    # Separar los canales
    r, g, b, a = img.split()

    # Invertir los canales de color
    r = ImageOps.invert(r)
    g = ImageOps.invert(g)
    b = ImageOps.invert(b)

    # Recombinar los canales invertidos con el canal alfa original
    inverted_img = Image.merge("RGBA", (r, g, b, a))

    # Añadir "_i" al nombre del archivo antes de la extensión
    ruta_guardado_invertido = os.path.join(ruta_directorio, f"{nombre_guardado}_i.png")

    # Guardar la imagen invertida
    inverted_img.save(ruta_guardado_invertido)
    
    print(f"Imagen original guardada en: {ruta_guardado_original}")
    print(f"Imagen invertida guardada en: {ruta_guardado_invertido}")

# Ejecutar la función
descargar_e_invertir_imagen()
