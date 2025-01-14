import requests
from PIL import Image
from io import BytesIO
from rembg import remove

def remove_background(image_url: str):
    # Descargar la imagen
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))

    # Eliminar el fondo
    img_without_bg = remove(img)

    # Guardar la nueva imagen
    img_without_bg.save("image_without_bg.png")

    print("El fondo ha sido eliminado y la imagen se ha guardado como 'image_without_bg.png'.")

# Ejemplo de uso
image_url = 'https://ejemplo.com/ruta/a/tu/imagen.jpg'
remove_background(image_url)
