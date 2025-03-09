![](/.resGen/_bannerD.png#gh-dark-mode-only)
![](/.resGen/_bannerL.png#gh-light-mode-only)

<a href="../readme.md"><img src="/.resGen/_back.svg" width="52.5"></a>

<a href="../4/readme.md"><img src="/.resGen/_arrow_r.svg" width="30" align="left"></a>
<a href="../6/readme.md"><img src="/.resGen/_arrow.svg" width="30" align="right"></a>

<br>

---

# 📋 Docker-Compose

<details>

<summary>

## 📌 Indice

</summary>

- [📋 Docker-Compose](#-docker-compose)
  - [📌 Indice](#-indice)
  - [� Ejemplo 1: Despliegue de la aplicación Guestbook](#-ejemplo-1-despliegue-de-la-aplicación-guestbook)
    - [🛠️ Configuración con Docker Compose](#️-configuración-con-docker-compose)
    - [🚀 Despliegue de la Aplicación](#-despliegue-de-la-aplicación)
    - [📊 Verificar el Estado de los Contenedores](#-verificar-el-estado-de-los-contenedores)
    - [🌍 Prueba de Acceso](#-prueba-de-acceso)
    - [🛑 Detener y Eliminar Contenedores](#-detener-y-eliminar-contenedores)

</details>

> [!TIP]
> Para volver a desplegar una aplicación de Docker, primero hemos de eliminar **todos** los contenedores existentes y volverlos a desplegar:
> 
> ```bash
> # Parar contenedor tu_contenedor
> sudo docker stop tu_contenedor
> ```
>
> ```bash
> # Eliminar contenedor tu_contenedor
> sudo docker rm tu_contenedor
> ```

## 📖 Ejemplo 1: Despliegue de la aplicación Guestbook

### 🛠️ Configuración con Docker Compose

Para definir y gestionar el despliegue de los servicios, utilizaremos el siguiente archivo [`docker-compose.yaml`](https://github.com/josedom24/curso_docker_ies/blob/main/ejemplos/modulo4/ejemplo1/docker-compose.yaml):

```yaml
version: '3.1'
services:
  app:
    container_name: guestbook
    image: iesgn/guestbook
    restart: always
    environment:
      REDIS_SERVER: redis
    ports:
      - "8080:5000"
  db:
    container_name: redis
    image: redis
    restart: always
    command: redis-server --appendonly yes
    volumes:
      - redis:/data

volumes:
  redis:
```

### 🚀 Despliegue de la Aplicación

> [!IMPORTANT]  
> Para desplegar la aplicación, ejecutamos el siguiente comando en el directorio donde se encuentra el archivo `docker-compose.yaml`:

```bash
sudo docker compose up -d
```

Esto creará la red por defecto, los volúmenes necesarios y levantará los contenedores:

```bash
[+] Running 4/4
 ✔ Network guestbook_default  Created
 ✔ Volume "guestbook_redis"   Created
 ✔ Container redis            Started
 ✔ Container guestbook        Started
```

![alt text](image.png)

### 📊 Verificar el Estado de los Contenedores

Para listar los contenedores en ejecución:

```bash
sudo docker compose ps
```

Salida esperada:

```bash
NAME        IMAGE             COMMAND                                                SERVICE   CREATED          STATUS          PORTS
guestbook   iesgn/guestbook   "python3 app.py"                                       app       18 seconds ago   Up 16 seconds   0.0.0.0:8080->5000/tcp, :::8080->5000/tcp
redis       redis             "docker-entrypoint.sh redis-server --appendonly yes"   db        18 seconds ago   Up 16 seconds   6379/tcp
```

![alt text](image-1.png)

### 🌍 Prueba de Acceso

Podemos acceder a la aplicación a través del navegador ingresando:

```
http://localhost:8080
```
![alt text](image-4.png)

### 🛑 Detener y Eliminar Contenedores

Para detener los contenedores sin eliminarlos:

```bash
sudo docker compose stop
```

Salida esperada:

```bash
[+] Stopping 2/2
 ✔ Container guestbook  Stopped  
 ✔ Container redis      Stopped  
```

![alt text](image-2.png)

Para eliminar completamente los contenedores, la red y los volúmenes:

```bash
sudo docker compose down -v
```

Salida esperada:

```bash
[+] Running 3/3
 ✔ Container redis            Removed  
 ✔ Container guestbook        Removed  
 ✔ Network guestbook_default  Removed  
```

![alt text](image-3.png)




