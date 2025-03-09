![](/.resGen/_bannerD.png#gh-dark-mode-only)
![](/.resGen/_bannerL.png#gh-light-mode-only)

<a href="../readme.md"><img src="/.resGen/_back.svg" width="52.5"></a>

<a href="../3/readme.md"><img src="/.resGen/_arrow_r.svg" width="30" align="left"></a>
<a href="../5/readme.md"><img src="/.resGen/_arrow.svg" width="30" align="right"></a>

<br>

---

# 🗂️ Almacenamiento y Redes en Docker

<details>

<summary>

## 📌 Indice

</summary>

- [🗂️ Almacenamiento y Redes en Docker](#️-almacenamiento-y-redes-en-docker)
  - [📌 Indice](#-indice)
  - [📖 Ejemplo 1: Despliegue de la aplicación Guestbook](#-ejemplo-1-despliegue-de-la-aplicación-guestbook)
    - [🔗 Crear una red Docker](#-crear-una-red-docker)
    - [🛢️ Desplegar la Base de Datos Redis](#️-desplegar-la-base-de-datos-redis)
    - [📟 Desplegar la Aplicación Guestbook](#-desplegar-la-aplicación-guestbook)
    - [🔍 Verificar el Despliegue](#-verificar-el-despliegue)
  - [🌡️ Ejemplo 2: Despliegue de la aplicación Temperaturas](#️-ejemplo-2-despliegue-de-la-aplicación-temperaturas)
    - [🔗 Crear una red Docker](#-crear-una-red-docker-1)
    - [🛢️ Desplegar el Backend](#️-desplegar-el-backend)
    - [📟 Desplegar el Frontend](#-desplegar-el-frontend)
    - [🔍 Verificar el Despliegue](#-verificar-el-despliegue-1)
  - [✒️ Ejemplo 3: Despliegue de Wordpress + MariaDB](#️-ejemplo-3-despliegue-de-wordpress--mariadb)
    - [🔗 Crear una red Docker](#-crear-una-red-docker-2)
    - [🛢️ Desplegar el Contenedor de Base de Datos MariaDB](#️-desplegar-el-contenedor-de-base-de-datos-mariadb)
    - [📟 Desplegar el Contenedor de WordPress](#-desplegar-el-contenedor-de-wordpress)
    - [🔍 Verificar el Despliegue](#-verificar-el-despliegue-2)
    - [👀 Observaciones](#-observaciones)
  - [🐱 Ejemplo 4: Despliegue de Tomcat + Nginx](#-ejemplo-4-despliegue-de-tomcat--nginx)
    - [🔗 Crear una red Docker](#-crear-una-red-docker-3)
    - [🛢️ Desplegar Tomcat](#️-desplegar-tomcat)
    - [📟 Desplegar Nginx como Proxy Inverso](#-desplegar-nginx-como-proxy-inverso)
    - [🔍 Verificar el Despliegue](#-verificar-el-despliegue-3)

</details>

---

## 📖 Ejemplo 1: Despliegue de la aplicación Guestbook

### 🔗 Crear una red Docker
Para que los contenedores se comuniquen entre sí, creamos una red llamada `red_guestbook`:

```bash
sudo docker network create red_guestbook
```

![alt text](image.png)

### 🛢️ Desplegar la Base de Datos Redis
Ejecutamos el contenedor de Redis asegurándonos de que los datos se almacenen de forma persistente en `/opt/redis`:

```bash
sudo docker run -d --name redis --network red_guestbook -v /opt/redis:/data redis redis-server --appendonly yes
```

![alt text](image-1.png)

### 📟 Desplegar la Aplicación Guestbook
Ejecutamos el contenedor de la aplicación Guestbook y lo exponemos en el puerto 80:

```bash
sudo docker run -d -p 80:5000 --name guestbook --network red_guestbook iesgn/guestbook
```

![alt text](image-2.png)

### 🔍 Verificar el Despliegue
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

### 🔗 Crear una red Docker

```bash
sudo docker network create red_temperaturas
```

![alt text](image-5.png)

### 🛢️ Desplegar el Backend

```bash
sudo docker run -d --name temperaturas-backend --network red_temperaturas iesgn/temperaturas_backend
```

![alt text](image-6.png)

### 📟 Desplegar el Frontend

```bash
sudo docker run -d -p 80:3000 --name temperaturas-frontend --network red_temperaturas iesgn/temperaturas_frontend
```

![alt text](image-7.png)

### 🔍 Verificar el Despliegue
Para comprobar que los contenedores están corriendo, usamos:

```bash
sudo docker ps
```

Si todo está configurado correctamente, deberíamos ver el contendor `temperaturas-frontend` en la lista de contenedores en ejecución.

![alt text](image-8.png)

Ademas de que podremos ver lo siguiente si accedemos a la url `http://localhost:80`:

![alt text](image-9.png)

---

## ✒️ Ejemplo 3: Despliegue de Wordpress + MariaDB

> [!IMPORTANT]  
> Antes de realizar este ejemplo, deberemos de cerrar las aplicaciones Guestbook y Redis que se ejecutaron en el ejemplo anterior.

```bash
sudo docker stop $(sudo docker ps -aq)
```

### 🔗 Crear una red Docker

```bash
sudo docker network create red_wp
```

![alt text](image-10.png)

### 🛢️ Desplegar el Contenedor de Base de Datos MariaDB

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

### 📟 Desplegar el Contenedor de WordPress

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

### 🔍 Verificar el Despliegue

Para comprobar que los contenedores están corriendo, usamos:

```bash
sudo docker ps
```

Si todo está configurado correctamente, deberíamos ver los contenedores `servidor_wp` y `servidor_mysql` en ejecución.

![alt text](image-13.png)

Ademas de que podremos ver lo siguiente si accedemos a la url `http://localhost:80`:

![alt text](image-14.png)

### 👀 Observaciones

- **MariaDB** ejecuta un script `docker-entrypoint.sh` que configura la base de datos según las variables de entorno proporcionadas.
- **WordPress** también ejecuta su propio script `docker-entrypoint.sh`, que genera el archivo `wp-config.php` automáticamente.
- La variable `WORDPRESS_DB_HOST` se configura con el nombre del contenedor de la base de datos (`servidor_mysql`).
- Solo se expone el puerto del contenedor de **WordPress** (`80`), ya que la base de datos solo necesita ser accesible dentro de la red Docker.

---

## 🐱 Ejemplo 4: Despliegue de Tomcat + Nginx

> [!IMPORTANT]  
> Antes de realizar este ejemplo, deberemos de cerrar las aplicaciones Guestbook y Redis que se ejecutaron en el ejemplo anterior.

```bash
sudo docker stop $(sudo docker ps -aq)
```

### 🔗 Crear una red Docker

```bash
sudo docker network create red_tomcat
```

![alt text](image-15.png)

### 🛢️ Desplegar Tomcat
Antes de desplegar Tomcat, asegurémonos de tener el archivo de la aplicación (sample.war) en un directorio específico: `/usr/local/tomcat/webapps/`:

Descargamos el archivo [`sample.war`](https://github.com/josedom24/curso_docker_ies/raw/refs/heads/main/ejemplos/modulo3/ejemplo4/sample.war), y lo copiamos a `/usr/local/tomcat/webapps/`:

```bash
sudo cp Descargas/sample.war /home/vagrant/tomcat/sample.war
```

Hacemos lo mismo con el archivo [`default.conf`](https://github.com/josedom24/curso_docker_ies/blob/main/ejemplos/modulo3/ejemplo4/default.conf):

```bash
sudo cp Descargas/default.conf /home/vagrant/tomcat/default.conf
```

```bash
ls /home/vagrant/tomcat/
```
```bash
# Deberíamos ver los siguientes archivos:
default.conf  sample.war
```

![alt text](image-20.png)

Creamos el contenedor Tomcat y montamos el archivo WAR en el directorio de despliegue:

```bash
sudo docker run -d --name aplicacionjava \
                --network red_tomcat \
                -v /home/vagrant/tomcat/sample.war:/usr/local/tomcat/webapps/sample.war:ro \
                tomcat:9.0
```

![alt text](image-16.png)

### 📟 Desplegar Nginx como Proxy Inverso

Tenemos el siguiente archivo de configuración `default.conf` para Nginx:

```nginx
server {
    listen       80;
    listen  [::]:80;
    server_name  localhost;

    location / {
        root   /usr/share/nginx/html;
        proxy_pass http://aplicacionjava:8080/sample/;
    }
    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   /usr/share/nginx/html;
    }
}
```

![alt text](image-17.png)

Ahora creamos el contenedor Nginx y montamos el archivo de configuración:

```bash
sudo docker run -d --name proxy \
                -p 80:80 \
                --network red_tomcat \
                -v /home/vagrant/tomcat/default.conf:/etc/nginx/conf.d/default.conf:ro \
                nginx
```

![alt text](image-18.png)

### 🔍 Verificar el Despliegue

Para comprobar que los contenedores están corriendo, usamos:

```bash
sudo docker ps
```

Si todo está configurado correctamente, deberíamos ver los contenedores `proxy` y `aplicaciónjava` en ejecución.

![alt text](image-19.png)

Ademas de que podremos ver lo siguiente si accedemos a la url `http://localhost:80`:

![alt text](image-21.png)