![](/.resGen/_bannerD.png#gh-dark-mode-only)
![](/.resGen/_bannerL.png#gh-light-mode-only)

<a href="../readme.md"><img src="/.resGen/_back.svg" width="52.5"></a>

<a href="../3/readme.md"><img src="/.resGen/_arrow_r.svg" width="30" align="left"></a>
<a href="../5/readme.md"><img src="/.resGen/_arrow.svg" width="30" align="right"></a>

<br>

---

# 🗂️ Gestión de Almacenamiento y Redes en Docker


> [!NOTE]  
> Highlights information that users should take into account, even when skimming.

> [!TIP]
> Optional information to help a user be more successful.

> [!IMPORTANT]  
> Crucial information necessary for users to succeed.

> [!WARNING]  
> Critical content demanding immediate user attention due to potential risks.

> [!CAUTION]
> Negative potential consequences of an action.

<details>

<summary>

## 📌 Indice

</summary>

- [🗂️ Gestión de Almacenamiento y Redes en Docker](#️-gestión-de-almacenamiento-y-redes-en-docker)
  - [📌 Indice](#-indice)
  - [📖 Introducción](#-introducción)
  - [🗃️ Ejemplo 1: Volúmenes Docker y Bind Mount](#️-ejemplo-1-volúmenes-docker-y-bind-mount)
    - [✅ Paso 1: Crear un volumen Docker](#-paso-1-crear-un-volumen-docker)
    - [✅ Paso 2: Crear un contenedor con un volumen](#-paso-2-crear-un-contenedor-con-un-volumen)
    - [✅ Paso 3: Bind Mount](#-paso-3-bind-mount)
  - [🌐 Ejemplo 2: Redes en Docker](#-ejemplo-2-redes-en-docker)
    - [✅ Paso 1: Crear una red definida por el usuario](#-paso-1-crear-una-red-definida-por-el-usuario)
    - [✅ Paso 2: Ejecutar contenedores en la misma red](#-paso-2-ejecutar-contenedores-en-la-misma-red)
    - [✅ Paso 3: Comunicación entre contenedores](#-paso-3-comunicación-entre-contenedores)
  - [📦 Ejemplo 3: Despliegue de Wordpress + MariaDB](#-ejemplo-3-despliegue-de-wordpress--mariadb)
    - [✅ Paso 1: Crear una red para la aplicación](#-paso-1-crear-una-red-para-la-aplicación)
    - [✅ Paso 2: Desplegar el contenedor de MariaDB](#-paso-2-desplegar-el-contenedor-de-mariadb)
    - [✅ Paso 3: Desplegar el contenedor de Wordpress](#-paso-3-desplegar-el-contenedor-de-wordpress)

</details>

## 📖 Introducción
En esta práctica, exploraremos el uso del almacenamiento y redes en Docker, siguiendo la documentación del módulo 3 del curso: [Almacenamiento y redes Docker](https://github.com/josedom24/curso_docker_ies). Se llevarán a cabo tres ejemplos y se documentará el proceso con capturas de pantalla.

---

## 🗃️ Ejemplo 1: Volúmenes Docker y Bind Mount

### ✅ Paso 1: Crear un volumen Docker
Ejecutamos el siguiente comando para crear un volumen:

```sh
docker volume create mi_volumen
```

Podemos verificar la creación del volumen con:

```sh
docker volume ls
```

### ✅ Paso 2: Crear un contenedor con un volumen
Ejecutamos un contenedor que monte el volumen:

```sh
docker run -d --name contenedor_volumen -v mi_volumen:/data busybox tail -f /dev/null
```

Verificamos que el contenedor esté corriendo:

```sh
docker ps
```

### ✅ Paso 3: Bind Mount
Para utilizar bind mount, primero creamos un directorio en el host:

```sh
mkdir -p ~/docker_data
```

Luego ejecutamos un contenedor con bind mount:

```sh
docker run -d --name contenedor_bind -v ~/docker_data:/app busybox tail -f /dev/null
```

Para verificarlo, creamos un archivo desde el host y lo revisamos dentro del contenedor:

```sh
echo "Este archivo está en el host" > ~/docker_data/archivo_host.txt

docker exec -it contenedor_bind sh
ls /app
cat /app/archivo_host.txt
```

---

## 🌐 Ejemplo 2: Redes en Docker

### ✅ Paso 1: Crear una red definida por el usuario
Ejecutamos el siguiente comando para crear una red personalizada:

```sh
docker network create mi_red
```

Verificamos la red creada:

```sh
docker network ls
```

### ✅ Paso 2: Ejecutar contenedores en la misma red
Creamos dos contenedores dentro de esta red:

```sh
docker run -d --name contenedor1 --network mi_red busybox tail -f /dev/null
docker run -d --name contenedor2 --network mi_red busybox tail -f /dev/null
```

Verificamos que ambos contenedores están en la misma red:

```sh
docker network inspect mi_red
```

### ✅ Paso 3: Comunicación entre contenedores
Accedemos al primer contenedor y verificamos que puede hacer ping al segundo:

```sh
docker exec -it contenedor1 sh
ping contenedor2
```

Si todo está configurado correctamente, deberíamos ver respuestas del ping.

---

## 📦 Ejemplo 3: Despliegue de Wordpress + MariaDB

### ✅ Paso 1: Crear una red para la aplicación
```sh
docker network create wordpress_net
```

### ✅ Paso 2: Desplegar el contenedor de MariaDB

```sh
docker run -d --name mariadb --network wordpress_net \
  -e MYSQL_ROOT_PASSWORD=rootpass \
  -e MYSQL_DATABASE=wordpress \
  -e MYSQL_USER=wp_user \
  -e MYSQL_PASSWORD=wp_pass \
  mariadb
```

### ✅ Paso 3: Desplegar el contenedor de Wordpress

```sh
docker run -d --name wordpress --network wordpress_net \
  -e WORDPRESS_DB_HOST=mariadb \
  -e WORDPRESS_DB_USER=wp_user \
  -e WORDPRESS_DB_PASSWORD=wp_pass \
  -e WORDPRESS_DB_NAME=wordpress \
  -p 8080:80 \
  wordpress
```

Accedemos a `http://localhost:8080` para completar la instalación de Wordpress.
