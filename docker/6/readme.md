![](/.resGen/_bannerD.png#gh-dark-mode-only)
![](/.resGen/_bannerL.png#gh-light-mode-only)

<a href="../readme.md"><img src="/.resGen/_back.svg" width="52.5"></a>

<a href="../5/readme.md"><img src="/.resGen/_arrow_r.svg" width="30" align="left"></a>

<br>

---

# 🖼️ Creación de Imágenes Docker

<details>

<summary>

## 📌 Indice

</summary>

- [🖼️ Creación de Imágenes Docker](#️-creación-de-imágenes-docker)
  - [📌 Indice](#-indice)
  - [🏗️ Ejemplo 1: Construcción de imágenes con una página estática](#️-ejemplo-1-construcción-de-imágenes-con-una-página-estática)
    - [🛠️ Versión 1: Desde una Imagen Base](#️-versión-1-desde-una-imagen-base)
    - [🪶 Versión 2: Desde una Imagen con Apache2](#-versión-2-desde-una-imagen-con-apache2)
    - [🌍 Versión 3: Desde una Imagen con Nginx](#-versión-3-desde-una-imagen-con-nginx)

</details>

---

> [!TIP]
> Para borrar todas las imagenes de Docker, puedes utilizar el comando
> 
> ```bash
> sudo docker rmi -f $(sudo docker images -a)
> ```


## 🏗️ Ejemplo 1: Construcción de imágenes con una página estática

### 🛠️ Versión 1: Desde una Imagen Base

Para esta versión, partimos de una imagen base **Debian** sin servicios adicionales y agregamos manualmente el servidor web **Apache**.

Descargamos los siguientes [archivos](https://downgit.github.io/#/home?url=https://github.com/josedom24/curso_docker_ies/tree/main/ejemplos/modulo5/ejemplo1/version1), estos contienen el fichero `Dockerfile` y un directorio `public_html` con la página web:

Descomprimos el archivo `version1.zip`.

```bash
sudo unzip Descargas/version1.zip
```

```bash
cd version1
ls
```

```bash
Dockerfile  public_html
```

![alt text](image.png)

El `Dockerfile` será:

```dockerfile
# syntax=docker/dockerfile:1
FROM debian:stable-slim
RUN apt-get update && apt-get install -y apache2 && apt-get clean && rm -rf /var/lib/apt/lists/*
WORKDIR /var/www/html/
COPY public_html .
EXPOSE 80
CMD apache2ctl -D FOREGROUND
```

Para crear la imagen:

> [!IMPORTANT]  
> Para crear la imagen, debemos estar en el directorio donde se encuentra el archivo `Dockerfile`.

```bash
sudo docker build -t josedom24/ejemplo1:v1 .
```

![alt text](image-1.png)

Verificamos que la imagen se ha creado:

```bash
sudo docker images
```

![alt text](image-2.png)

Ejecutamos un contenedor:

```bash
sudo docker run -d -p 80:80 --name ejemplo1 josedom24/ejemplo1:v1
```

![alt text](image-3.png)

Comprobamos `http://localhost:80`

![alt text](image-4.png)

---

### 🪶 Versión 2: Desde una Imagen con Apache2

Descargamos los siguientes [archivos](https://downgit.github.io/#/home?url=https://github.com/josedom24/curso_docker_ies/tree/main/ejemplos/modulo5/ejemplo1/version2), estos contienen el fichero `Dockerfile` y un directorio `public_html` con la página web:

Descomprimos el archivo `version2.zip`.

```bash
sudo unzip Descargas/version2.zip
```

```bash
cd version2
ls
```

```bash
Dockerfile  public_html
```

![alt text](image-5.png)

`Dockerfile` para esta versión:

```dockerfile
# syntax=docker/dockerfile:1
FROM httpd:2.4
COPY public_html /usr/local/apache2/htdocs/
EXPOSE 80
```

Construcción y ejecución:

> [!IMPORTANT]  
> Para crear la imagen, debemos estar en el directorio donde se encuentra el archivo `Dockerfile`.

```bash
sudo docker build -t josedom24/ejemplo1:v2 .
```

![alt text](image-6.png)

```bash
sudo docker run -d -p 80:80 --name ejemplo1 josedom24/ejemplo1:v2
```

![alt text](image-7.png)

### 🌍 Versión 3: Desde una Imagen con Nginx
Descargamos los siguientes [archivos](https://downgit.github.io/#/home?url=https://github.com/josedom24/curso_docker_ies/tree/main/ejemplos/modulo5/ejemplo1/version3), estos contienen el fichero `Dockerfile` y un directorio `public_html` con la página web:

Descomprimos el archivo `version2.zip`.

```bash
sudo unzip Descargas/version3.zip
```

```bash
cd version3
ls
```

```bash
Dockerfile  public_html
```

`Dockerfile` para esta versión:

```dockerfile
# syntax=docker/dockerfile:1
FROM nginx:1.24
COPY public_html /usr/share/nginx/html
EXPOSE 80
```

Construcción y ejecución:

> [!IMPORTANT]  
> Para crear la imagen, debemos estar en el directorio donde se encuentra el archivo `Dockerfile`.

```bash
$ docker build -t josedom24/ejemplo1:v3 .
$ docker run -d -p 80:80 --name ejemplo1 josedom24/ejemplo1:v3
```

