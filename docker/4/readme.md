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
    - [📝 Introducción](#-introducción)
    - [⚙️ Prerrequisitos](#️-prerrequisitos)
    - [📌 Paso a Paso](#-paso-a-paso)
    - [🔄 Configuración Alternativa: Cambio de Nombre del Contenedor Redis](#-configuración-alternativa-cambio-de-nombre-del-contenedor-redis)
  - [🌡️ Ejemplo 2: Despliegue de la aplicación Temperaturas](#️-ejemplo-2-despliegue-de-la-aplicación-temperaturas)
  - [🌐 Ejemplo 3: Despliegue de Wordpress + MariaDB](#-ejemplo-3-despliegue-de-wordpress--mariadb)
  - [🚀 Ejemplo 4: Despliegue de Tomcat + Nginx](#-ejemplo-4-despliegue-de-tomcat--nginx)

</details>

## 🚀 Ejemplo 1: Despliegue de la aplicación Guestbook

### 📝 Introducción
En este documento se describe el proceso paso a paso para desplegar la aplicación web Guestbook utilizando Docker. La aplicación requiere dos servicios:

1. **Servicio Web**: Aplicación Guestbook basada en Python, que escucha en el puerto `5000/tcp`.
2. **Servicio de Base de Datos**: Base de datos Redis que funciona en el puerto `6379/tcp`.

### ⚙️ Prerrequisitos
Antes de comenzar, asegúrate de tener instalados los siguientes componentes en tu sistema:

- Docker
- Docker Compose (opcional pero recomendado)

### 📌 Paso a Paso

- **1️⃣ Crear una red Docker**
Para que los contenedores se comuniquen entre sí, creamos una red llamada `red_guestbook`:

```bash
$ docker network create red_guestbook
```

- **2️⃣ Desplegar la Base de Datos Redis**
Ejecutamos el contenedor de Redis asegurándonos de que los datos se almacenen de forma persistente en `/opt/redis`:

```bash
$ docker run -d --name redis --network red_guestbook -v /opt/redis:/data redis redis-server --appendonly yes
```

- **3️⃣ Desplegar la Aplicación Guestbook**
Ejecutamos el contenedor de la aplicación Guestbook y lo exponemos en el puerto 80:

```bash
$ docker run -d -p 80:5000 --name guestbook --network red_guestbook iesgn/guestbook
```

- **4️⃣ Verificar el Despliegue**
Para comprobar que los contenedores están corriendo, usamos:

```bash
$ docker ps
```

Si todo está configurado correctamente, deberíamos ver los contenedores `redis` y `guestbook` en ejecución.

### 🔄 Configuración Alternativa: Cambio de Nombre del Contenedor Redis
Si por alguna razón deseas utilizar un nombre diferente para el contenedor Redis, sigue estos pasos:

1. Crea el contenedor con un nombre distinto (ejemplo: `contenedor_redis`):

   ```bash
   $ docker run -d --name contenedor_redis --network red_guestbook -v /opt/redis:/data redis redis-server --appendonly yes
   ```

2. Ejecuta la aplicación Guestbook configurando la variable de entorno `REDIS_SERVER`:

   ```bash
   $ docker run -d -p 80:5000 --name guestbook -e REDIS_SERVER=contenedor_redis --network red_guestbook iesgn/guestbook
   ```

---

## 🌡️ Ejemplo 2: Despliegue de la aplicación Temperaturas



## 🌐 Ejemplo 3: Despliegue de Wordpress + MariaDB



## 🚀 Ejemplo 4: Despliegue de Tomcat + Nginx

