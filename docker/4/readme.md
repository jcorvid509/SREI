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
    - [4️⃣ Verificar el Despliegue](#4️⃣-verificar-el-despliegue-1)
  - [🌍 Ejemplo 3: Despliegue de Wordpress + MariaDB](#-ejemplo-3-despliegue-de-wordpress--mariadb)
    - [1️⃣ Crear una red Docker](#1️⃣-crear-una-red-docker-2)
    - [2️⃣ Desplegar el Contenedor de Base de Datos MariaDB](#2️⃣-desplegar-el-contenedor-de-base-de-datos-mariadb)
    - [3️⃣ Desplegar el Contenedor de WordPress](#3️⃣-desplegar-el-contenedor-de-wordpress)
    - [4️⃣ Verificar el Despliegue](#4️⃣-verificar-el-despliegue-2)
    - [🔍 Observaciones](#-observaciones)
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

Si todo está configurado correctamente, deberíamos ver los contenedores `redis` y `guestbook` en ejecución.

![alt text](image-3.png)

Ademas de que podremos ver lo siguiente si accedemos a la url `http://localhost:80`:

![alt text](image-4.png)


---

## 🌡️ Ejemplo 2: Despliegue de la aplicación Temperaturas

> [!IMPORTANT]  
> Antes de realizar este ejemplo, deberemos de cerrar las aplicaciones Guestbook y Redis que se ejecutaron en el ejemplo anterior.

```bash
sudo docker stop $(sudo docker ps -aq)
```

### 1️⃣ Crear una red Docker

```bash
sudo docker network create red_temperaturas
```

![alt text](image-5.png)

### 2️⃣ Desplegar el Backend

```bash
sudo docker run -d --name temperaturas-backend --network red_temperaturas iesgn/temperaturas_backend
```

![alt text](image-6.png)

### 3️⃣ Desplegar el Frontend

```bash
sudo docker run -d -p 80:3000 --name temperaturas-frontend --network red_temperaturas iesgn/temperaturas_frontend
```

![alt text](image-7.png)

### 4️⃣ Verificar el Despliegue
Para comprobar que los contenedores están corriendo, usamos:

```bash
sudo docker ps
```

Si todo está configurado correctamente, deberíamos ver el contendor `temperaturas-frontend` en la lista de contenedores en ejecución.

![alt text](image-8.png)

Ademas de que podremos ver lo siguiente si accedemos a la url `http://localhost:80`:

![alt text](image-9.png)

---

## 🌍 Ejemplo 3: Despliegue de Wordpress + MariaDB

> [!IMPORTANT]  
> Antes de realizar este ejemplo, deberemos de cerrar las aplicaciones Guestbook y Redis que se ejecutaron en el ejemplo anterior.

```bash
sudo docker stop $(sudo docker ps -aq)
```

### 1️⃣ Crear una red Docker

```bash
sudo docker network create red_wp
```

![alt text](image-10.png)

### 2️⃣ Desplegar el Contenedor de Base de Datos MariaDB

```bash
sudo docker run -d --name servidor_mysql \
                --network red_wp \
                -v /opt/mysql_wp:/var/lib/mysql \
                -e MYSQL_DATABASE=bd_wp \
                -e MYSQL_USER=user_wp \
                -e MYSQL_PASSWORD=asdasd \
                -e MYSQL_ROOT_PASSWORD=asdasd \
                mariadb
```

![alt text](image-11.png)

### 3️⃣ Desplegar el Contenedor de WordPress

```bash
sudo docker run -d --name servidor_wp \
                --network red_wp \
                -v /opt/wordpress:/var/www/html/wp-content \
                -e WORDPRESS_DB_HOST=servidor_mysql \
                -e WORDPRESS_DB_USER=user_wp \
                -e WORDPRESS_DB_PASSWORD=asdasd \
                -e WORDPRESS_DB_NAME=bd_wp \
                -p 80:80 \
                wordpress
```

![alt text](image-12.png)

### 4️⃣ Verificar el Despliegue

Para comprobar que los contenedores están corriendo, usamos:

```bash
sudo docker ps
```

Si todo está configurado correctamente, deberíamos ver los contenedores `servidor_wp` y `servidor_mysql` en ejecución.

![alt text](image-13.png)

Ademas de que podremos ver lo siguiente si accedemos a la url `http://localhost:80`:

![alt text](image-14.png)

### 🔍 Observaciones

- **MariaDB** ejecuta un script `docker-entrypoint.sh` que configura la base de datos según las variables de entorno proporcionadas.
- **WordPress** también ejecuta su propio script `docker-entrypoint.sh`, que genera el archivo `wp-config.php` automáticamente.
- La variable `WORDPRESS_DB_HOST` se configura con el nombre del contenedor de la base de datos (`servidor_mysql`).
- Solo se expone el puerto del contenedor de **WordPress** (`80`), ya que la base de datos solo necesita ser accesible dentro de la red Docker.

---

## 🚀 Ejemplo 4: Despliegue de Tomcat + Nginx

> [!IMPORTANT]  
> Antes de realizar este ejemplo, deberemos de cerrar las aplicaciones Guestbook y Redis que se ejecutaron en el ejemplo anterior.

```bash
sudo docker stop $(sudo docker ps -aq)
```

