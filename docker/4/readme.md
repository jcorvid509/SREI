![](/.resGen/_bannerD.png#gh-dark-mode-only)
![](/.resGen/_bannerL.png#gh-light-mode-only)

<a href="../readme.md"><img src="/.resGen/_back.svg" width="52.5"></a>

<a href="../3/readme.md"><img src="/.resGen/_arrow_r.svg" width="30" align="left"></a>
<a href="../5/readme.md"><img src="/.resGen/_arrow.svg" width="30" align="right"></a>

<br>

---

# 🗂️ Gestión de Almacenamiento y Redes en Docker

<details>

<summary>

## 📌 Indice

</summary>

- [🗂️ Gestión de Almacenamiento y Redes en Docker](#️-gestión-de-almacenamiento-y-redes-en-docker)
  - [📌 Indice](#-indice)
  - [🚀 Ejemplo 1: Despliegue de la aplicación Guestbook](#-ejemplo-1-despliegue-de-la-aplicación-guestbook)
    - [1️⃣ Crear una red Docker](#1️⃣-crear-una-red-docker)
    - [2️⃣ Desplegar la Base de Datos Redis](#2️⃣-desplegar-la-base-de-datos-redis)
    - [3️⃣ Desplegar la Aplicación Guestbook](#3️⃣-desplegar-la-aplicación-guestbook)
    - [4️⃣ Verificar el Despliegue](#4️⃣-verificar-el-despliegue)
  - [🌡️ Ejemplo 2: Despliegue de la aplicación Temperaturas](#️-ejemplo-2-despliegue-de-la-aplicación-temperaturas)
    - [1️⃣ Crear una red Docker](#1️⃣-crear-una-red-docker-1)
    - [2️⃣ Desplegar el Backend](#2️⃣-desplegar-el-backend)
    - [3️⃣ Desplegar el Frontend](#3️⃣-desplegar-el-frontend)
  - [🌐 Ejemplo 3: Despliegue de Wordpress + MariaDB](#-ejemplo-3-despliegue-de-wordpress--mariadb)
  - [🚀 Ejemplo 4: Despliegue de Tomcat + Nginx](#-ejemplo-4-despliegue-de-tomcat--nginx)

</details>

---

## 🚀 Ejemplo 1: Despliegue de la aplicación Guestbook

### 1️⃣ Crear una red Docker
Para que los contenedores se comuniquen entre sí, creamos una red llamada `red_guestbook`:

```bash
sudo docker network create red_guestbook
```

![alt text](image.png)

### 2️⃣ Desplegar la Base de Datos Redis
Ejecutamos el contenedor de Redis asegurándonos de que los datos se almacenen de forma persistente en `/opt/redis`:

```bash
sudo docker run -d --name redis --network red_guestbook -v /opt/redis:/data redis redis-server --appendonly yes
```

![alt text](image-1.png)

### 3️⃣ Desplegar la Aplicación Guestbook
Ejecutamos el contenedor de la aplicación Guestbook y lo exponemos en el puerto 80:

```bash
sudo docker run -d -p 80:5000 --name guestbook --network red_guestbook iesgn/guestbook
```

![alt text](image-2.png)

### 4️⃣ Verificar el Despliegue
Para comprobar que los contenedores están corriendo, usamos:

```bash
sudo docker ps
```

![alt text](image-3.png)

Si todo está configurado correctamente, deberíamos ver los contenedores `redis` y `guestbook` en ejecución.

Ademas de que podremos ver lo siguiente si accedemos a la url `http://localhost:80`:

![alt text](image-4.png)

---

## 🌡️ Ejemplo 2: Despliegue de la aplicación Temperaturas

### 1️⃣ Crear una red Docker

```bash
sudo docker network create red_temperaturas
```

### 2️⃣ Desplegar el Backend

```bash
sudo docker run -d --name temperaturas-backend --network red_temperaturas iesgn/temperaturas_backend
```

### 3️⃣ Desplegar el Frontend

```bash
sudo docker run -d -p 80:3000 --name temperaturas-frontend --network red_temperaturas iesgn/temperaturas_frontend
```

---

## 🌐 Ejemplo 3: Despliegue de Wordpress + MariaDB



## 🚀 Ejemplo 4: Despliegue de Tomcat + Nginx

