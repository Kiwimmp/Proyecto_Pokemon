import requests
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

pokemon = input("Nombre de pokemon: ")

url = "https://pokeapi.co/api/v2/pokemon/" + pokemon
res = requests.get(url)

if res.status_code != 200:
    print("No se ha encontrado el Pokemon")
    exit()

# Abrir la imagen con Pillow y convertirla a un array numpy
imagen_pillow = Image.open(requests.get(res.json()['sprites']['front_default'], stream=True).raw)
imagen_np = np.array(imagen_pillow)

plt.title(res.json()['name'])
imgplot = plt.imshow(imagen_np)
plt.show()
