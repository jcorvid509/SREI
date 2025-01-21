import requests
from PIL import Image
from io import BytesIO
import cv2
import numpy as np
import os

def remove_background(image_url: str, output_path: str):
    # Descargar la imagen
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    img = np.array(img)

    # Convertir la imagen a formato HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

    # Definir el rango de color para el fondo (ajusta estos valores según tu imagen)
    lower_bound = np.array([0, 0, 0])
    upper_bound = np.array([180, 255, 30])

    # Crear una máscara para el fondo
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Invertir la máscara
    mask_inv = cv2.bitwise_not(mask)

    # Usar la máscara invertida para obtener la imagen sin fondo
    img_without_bg = cv2.bitwise_and(img, img, mask=mask_inv)

    # Convertir la imagen resultante a formato PIL y guardar
    img_without_bg = Image.fromarray(img_without_bg)
    img_without_bg.save(output_path, format='PNG')

    print(f"El fondo ha sido eliminado y la imagen se ha guardado como '{output_path}'.")

if __name__ == "__main__":
    # Solicitar la URL de la imagen al usuario
    image_url = input("Introduce la URL de la imagen: ")
    
    # Definir la ruta de salida en el directorio actual
    output_path = os.path.join(os.getcwd(), 'image_without_bg.png')
    
    # Llamar a la función para eliminar el fondo
    remove_background(image_url, output_path)
