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

- [�️ Gestión de Almacenamiento y Redes en Docker](#️-gestión-de-almacenamiento-y-redes-en-docker)
  - [📌 Indice](#-indice)
  - [📖 Introducción](#-introducción)
  - [📂 Ejemplo 1: Volúmenes en Docker](#-ejemplo-1-volúmenes-en-docker)
    - [✅ Paso 1: Crear un volumen](#-paso-1-crear-un-volumen)
    - [✅ Paso 2: Usar el volumen en un contenedor](#-paso-2-usar-el-volumen-en-un-contenedor)
    - [✅ Paso 3: Acceder al volumen desde el contenedor](#-paso-3-acceder-al-volumen-desde-el-contenedor)
  - [🌐 Ejemplo 2: Redes en Docker](#-ejemplo-2-redes-en-docker)
    - [✅ Paso 1: Crear una red personalizada](#-paso-1-crear-una-red-personalizada)
    - [✅ Paso 2: Ejecutar contenedores en la misma red](#-paso-2-ejecutar-contenedores-en-la-misma-red)
    - [✅ Paso 3: Comunicación entre contenedores](#-paso-3-comunicación-entre-contenedores)
  - [🗃️ Ejemplo 3: Bind Mounts](#️-ejemplo-3-bind-mounts)
    - [✅ Paso 1: Crear un directorio en el host](#-paso-1-crear-un-directorio-en-el-host)
    - [✅ Paso 2: Ejecutar un contenedor con Bind Mount](#-paso-2-ejecutar-un-contenedor-con-bind-mount)
    - [✅ Paso 3: Crear un archivo desde el host](#-paso-3-crear-un-archivo-desde-el-host)
  - [📸 Capturas de pantalla](#-capturas-de-pantalla)
  - [🎯 Conclusión](#-conclusión)

</details>

## 📖 Introducción
En esta práctica, exploraremos el uso del almacenamiento y redes en Docker, siguiendo la documentación del módulo 3 del curso: [Almacenamiento y redes Docker](https://github.com/josedom24/curso_docker_ies). Se llevarán a cabo tres ejemplos y se documentará el proceso con capturas de pantalla.

---

## 📂 Ejemplo 1: Volúmenes en Docker

### ✅ Paso 1: Crear un volumen
Ejecutamos el siguiente comando para crear un volumen:

```sh
docker volume create mi_volumen
```

Podemos verificar la creación del volumen con:

```sh
docker volume ls
```

### ✅ Paso 2: Usar el volumen en un contenedor
Ejecutamos un contenedor que monte el volumen:

```sh
docker run -d --name contenedor_volumen -v mi_volumen:/data busybox tail -f /dev/null
```

Verificamos que el contenedor esté corriendo:

```sh
docker ps
```

### ✅ Paso 3: Acceder al volumen desde el contenedor
Entramos en el contenedor y creamos un archivo dentro del volumen:

```sh
docker exec -it contenedor_volumen sh
cd /data
echo "Hola desde Docker Volumes" > archivo.txt
exit
```

Podemos verificar que el archivo persiste incluso si eliminamos y volvemos a ejecutar un contenedor con el mismo volumen.

---

## 🌐 Ejemplo 2: Redes en Docker

### ✅ Paso 1: Crear una red personalizada
Ejecutamos el siguiente comando para crear una red:

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

## 🗃️ Ejemplo 3: Bind Mounts

### ✅ Paso 1: Crear un directorio en el host

```sh
mkdir -p ~/docker_data
```

### ✅ Paso 2: Ejecutar un contenedor con Bind Mount

```sh
docker run -d --name contenedor_bind -v ~/docker_data:/app busybox tail -f /dev/null
```

### ✅ Paso 3: Crear un archivo desde el host

```sh
echo "Este archivo está en el host" > ~/docker_data/archivo_host.txt
```

Verificamos dentro del contenedor:

```sh
docker exec -it contenedor_bind sh
ls /app
cat /app/archivo_host.txt
```

Si todo está correcto, deberíamos ver el archivo dentro del contenedor.

---

## 📸 Capturas de pantalla
Para documentar esta práctica, se deben incluir capturas de pantalla de:
- La lista de volúmenes (`docker volume ls`)
- La inspección de la red (`docker network inspect mi_red`)
- El contenido del bind mount desde dentro del contenedor (`cat /app/archivo_host.txt`)

---

## 🎯 Conclusión
En esta práctica hemos aprendido a:
- 🗂️ Usar volúmenes en Docker para almacenamiento persistente.
- 🌍 Configurar redes personalizadas y conectar contenedores.
- 📂 Utilizar Bind Mounts para compartir archivos entre el host y el contenedor.
