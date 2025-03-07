![](/.resGen/_bannerD.png#gh-dark-mode-only)
![](/.resGen/_bannerL.png#gh-light-mode-only)

<a href="/aws/readme.md"><img src="/.resGen/_back.svg" width="52.5"></a>

---

# Virtual Private Cloud (VPC)

## Introducción
En esta guía, aprenderás a configurar una infraestructura de red segura y escalable utilizando Amazon Virtual Private Cloud (Amazon VPC). Amazon VPC permite la creación de redes privadas dentro de AWS, proporcionando control total sobre la conectividad y seguridad de los recursos en la nube. 

Siguiendo estos pasos, configurarás una VPC con subredes públicas y privadas, establecerás conectividad segura mediante instancias EC2 y aplicarás buenas prácticas para gestionar el tráfico de red. 

---

## Requisitos
- Acceso a AWS a través de AWS Academy.

## Creación de una VPC con el asistente

1. Accede a la consola de **Amazon VPC** y selecciona **Create VPC**.

![alt text](image.png)

2. En **Resources to create**, elige **VPC and more**.

![alt text](image-1.png)

3. Configura los siguientes parámetros:
   - **Name tag auto-generation**: `proyecto` (Auto-generate activado)
   - **IPv4 CIDR block**: `10.2.0.0/16`
   - **IPv6 CIDR block**: `No IPv6 CIDR block`
   - **Tenancy**: `Default`
   - **Number of Availability Zones**: `2` (us-east-1a y us-east-1b)
   - **Number of public subnets**: `2`
   - **Number of private subnets**: `2`
   - **Customize subnets CIDR blocks**:
     - `10.2.0.0/24` (Pública - us-east-1a)
     - `10.2.1.0/24` (Pública - us-east-1b)
     - `10.2.2.0/24` (Privada - us-east-1a)
     - `10.2.3.0/24` (Privada - us-east-1b)
   - **NAT gateways**: `None`
   - **VPC endpoints**: `None`
   - **DNS options**: Activar **Enable DNS hostnames** y **Enable DNS resolution**.

| ![alt text](image-2.png) | ![alt text](image-3.png) | ![alt text](image-4.png) |
|:-----------------------:|:-----------------------:|:-----------------------:|

4. Haz clic en **Create VPC**.

---

## Creación de una VPC personalizada
1. Accede a **Amazon VPC** y selecciona **Create VPC**.
2. Configura los siguientes valores:
   - **Name tag**: `custom-vpc`
   - **IPv4 CIDR block**: `10.2.0.0/16`
   - **IPv6 CIDR block**: `No IPv6 CIDR block`
   - **Tenancy**: `Default`
3. Haz clic en **Create VPC**.
4. Habilita **Enable DNS hostnames** y **Enable DNS resolution** en **Edit VPC settings**.

---

## Creación de un Internet Gateway
1. En **Amazon VPC**, ve a **Internet Gateways**.
2. Haz clic en **Create Internet Gateway**.
3. Asigna el nombre `custom-igw` y crea el gateway.
4. Adjunta el Internet Gateway a la `custom-vpc`.

---

## Creación de Subredes
1. Accede a **Amazon VPC > Subnets** y haz clic en **Create Subnet**.
2. Selecciona la `custom-vpc` y añade las siguientes subredes:
   - `custom-subnet-public1-us-east-1a` → `10.2.0.0/24`
   - `custom-subnet-public2-us-east-1b` → `10.2.1.0/24`
   - `custom-subnet-private1-us-east-1a` → `10.2.2.0/24`
   - `custom-subnet-private2-us-east-1b` → `10.2.3.0/24`
3. Habilita **Auto-assign public IPv4 address** en las subredes públicas.

---

## Creación de Tablas de Rutas
1. Accede a **Amazon VPC > Route Tables** y selecciona **Create Route Table**.
2. Crea las siguientes tablas:
   - **custom-rtb-public**: Redirige tráfico `0.0.0.0/0` al Internet Gateway.
   - **custom-rtb-private1-us-east-1a**: Sin acceso a Internet.
   - **custom-rtb-private1-us-east-1b**: Sin acceso a Internet.
3. Asocia **custom-rtb-public** a las subredes públicas.
4. Asocia las tablas privadas a sus respectivas subredes.

---

## Lanzamiento de Instancias EC2
1. Accede a **Amazon EC2 > Instances** y selecciona **Launch Instance**.
2. Configura las siguientes opciones:
   - **AMI**: `Amazon Linux 2023`
   - **Tipo de instancia**: `t4g.micro`
   - **VPC**: `custom-vpc`
   - **Subred**:
     - `custom-subnet-public1-us-east-1a` (pública)
     - `custom-subnet-private2-us-east-1b` (privada)
   - **Grupos de seguridad**:
     - `ssh-sg` para acceso SSH desde fuera
     - `default` para comunicación interna
3. Asigna una IP pública a la instancia pública.
4. Lanza las instancias.

---

## Conexión a las Instancias EC2
### Conexión SSH a la Instancia Pública
```sh
ssh -i <clave-privada> ec2-user@<ip-publica>
```

### Conexión desde la Instancia Pública a la Privada
```sh
ssh ec2-user@<ip-privada>
```

### Conexión Directa a la Instancia Privada con Port Forwarding
1. En la máquina local, ejecuta:
```sh
ssh -i <clave-privada> -L 2022:<ip-privada>:22 ec2-user@<ip-publica>
```
2. En una nueva terminal, conéctate a la instancia privada:
```sh
ssh -i <clave-privada> ec2-user@localhost -p 2022
```

---

## Limpieza de Recursos
1. **Eliminar instancias EC2**:
   - Accede a **Amazon EC2** y termina las instancias.
2. **Eliminar la VPC** (opcional):
   - Accede a **Amazon VPC**, selecciona la VPC y elige **Delete VPC**.

---

## Conclusión
Esta guía proporciona una estructura sólida para configurar redes privadas con Amazon VPC, asegurando conectividad eficiente y segura en AWS.
