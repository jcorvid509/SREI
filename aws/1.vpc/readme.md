![](/.resGen/_bannerD.png#gh-dark-mode-only)
![](/.resGen/_bannerL.png#gh-light-mode-only)

<a href="/aws/readme.md"><img src="/.resGen/_back.svg" width="52.5"></a>

---

# Virtual Private Cloud (VPC)

## Índice

- [Virtual Private Cloud (VPC)](#virtual-private-cloud-vpc)
  - [Índice](#índice)
  - [1. Crear una VPC](#1-crear-una-vpc)
  - [2. Crear una instancia EC2](#2-crear-una-instancia-ec2)
  - [3. Instalación de WordPress en la instancia EC2](#3-instalación-de-wordpress-en-la-instancia-ec2)
  - [](#)
  - [EFS ](#efs-)


---

## 1. Crear una VPC

El primer paso es crear una VPC. Una VPC es una red virtual que permite a los usuarios crear y configurar redes privadas seguras dentro de la nube de AWS.

- Vamos al menú de **AWS** y buscamos **VPC** y entramos en el servicio.

![alt text](image.png)

- En el menú de **VPC**, seleccionamos **Crear VPC**

![alt text](image-1.png)

- En la página de **Configuración de la VPC**, configuramos los siguientes parámetros:

  - **Nombre de la VPC**: `proyecto` (Activamos Generar automáticamente)
  - **Bloque de CIDR IPv4**: `10.0.0.0/16`
  - **Bloque de CIDR IPv6**: `Sin bloque de CIDR IPv6`
  - **Tenencia**: `Predeterminado`

![alt text](image-2.png)

  - **Número de zonas de disponibilidad (AZ)**: `2`
  -  **Personalizar las zonas de disponibilidad**
     -  **Primera zona de disponibilidad**: `us-east-1a`
     -  **Segunda zona de disponibilidad**: `us-east-1b`

![alt text](image-3.png)

  - **Cantidad de subredes públicas**: `2`
  - **Cantidada de subredes privadas**: `2`
  - **Personalizar bloques de CIDR de subredes**
    - **Bloque de CIDR de la subred pública en us-east-1a**: `10.0.1.0/24`
    -  **Bloque de CIDR de la subred pública en us-east-1b**: `10.0.2.0/24`
    -  **Bloque de CIDR de la subred privada en us-east-1a**: `10.0.3.0/24`
    -  **Bloque de CIDR de la subred privada en us-east-1b**: `10.0.4.0/24`

![alt text](image-4.png)

  - **Gateways NAT**: `Ninguna`
  - **Puntos de enlace de la VPC**: `Ninguno`
  - **Opciones de DNS**
    - **Habilitar nombres de host DNS**: ✅
    - **Habilitar resolución de nombres DNS**: ✅

![alt text](image-5.png)

  - Creamos la VPC pulsando en el botón **Crear VPC**

![alt text](image-6.png)

 
![alt text](image-7.png)

---

## 2. Crear una instancia EC2


- Vamos al menú de AWS y buscamos **EC2** y entramos en el servicio.

![alt text](image-8.png)

- En el menú de **EC2 > Instancias > Instancia**, pulsamos en el botón **Lanzar instancias**.

![alt text](image-9.png)

![alt text](image-10.png)

- En el menú de **Lanzar una instancia**, configuramos los siguientes parámetros:

  - **Nombre y etiquetas**: `serverwp`

![alt text](image-11.png)

  - **Imágenes de aplicaciones y sistemas operativos (Imagen de máquina de Amazon)**: `Ubuntu Server 20.04 LTS (HVM) - 64 bits`

![alt text](image-12.png)

  - **Tipo de instancia**: `t2.medium`

![alt text](image-13.png)

  - **Par de claves (inicio de sesión)**: `vockey`

![alt text](image-14.png)

  - **Configuraciones de red > Editar**
    - **VPC**: `proyecto-vpc`
    - **Subred**: `proyecto-subnet-public1-us-east-1a`
    - **Asignar automáticamente la IP pública**: `Habilitar`
    - **Firewall (grupos de seguridad)**: `Crear grupo de seguridad`
    - **Nombre del grupo de seguridad**: `serverwp-sg`

![alt text](image-15.png)

  - **Reglas de grupos de seguridad de entrada**
    - **Regla del grupo de seguridad 1**: `ssh` → `Cualquier lugar`
    - **Regla del grupo de seguridad 2**: `HTTP` → `Cualquier lugar`

![alt text](image-16.png)

  - **Configurar almacenamiento**: `1x 10 GiB gp3`

![alt text](image-17.png)

- **Revisamos el resumen y lanzamos la instancia**

![alt text](image-18.png)

- **Verificamos que la instancia esté en ejecución**

![alt text](image-19.png)

- **Conectamos a la instancia**

![alt text](image-20.png)

  - En la ventana **Conectarse a la instancia**
    - **Tipo de conexión**: `Conectarse mediante la Conexión de la instancia EC2`
    - Marcamos **Dirección IPv4 pública**
    - **Nombre de usuario**: `ubuntu`
  - Pulsamos en **Conectar**

![alt text](image-21.png)

![alt text](image-22.png)

---

## 3. Instalación de WordPress en la instancia EC2

- **Actualizamos el sistema**

```bash
sudo apt update && sudo apt upgrade -y
```

![alt text](image-23.png)

- **Instalamos Apache2**

```bash
sudo apt install apache2 -y
```

![alt text](image-24.png)

- **Activamos el servicio Apache2**

```bash
sudo systemctl start apache2 && sudo systemctl enable apache2
```

![alt text](image-25.png)

Comprobamos que todo esta correctamente configurado y que el servicio Apache2 se encuentra en ejecución, para ello, verificamos el servidor poniendo la dirección IP de la instancia EC2 en el navegador.

![alt text](image-26.png)

- **Añadimos el repositorio de PHP**

```bash
sudo add-apt-repository ppa:ondrej/php -y
```

![alt text](image-27.png)

- **Instalamos PHP**

```bash
sudo apt install php7.4 libapache2-mod-php7.4 php7.4-cli -y
```

![alt text](image-28.png)

- **Instalamos MySQL**

```bash
sudo apt install php7.4-mysql -y
```

![alt text](image-29.png)

- **Reiniciamos el servicio Apache2**

```bash
sudo systemctl restart apache2
```

![alt text](image-30.png)

- **Comprobamos que PHP esta correctamente instalado**

```bash
php -v
```

![alt text](image-31.png)

---

## 

## EFS <a href="../2.efs/readme.md"><img src="/.resGen/_arrow.svg" width="30" align="right"></a>