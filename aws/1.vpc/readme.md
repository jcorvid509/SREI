![](/.resGen/_bannerD.png#gh-dark-mode-only)
![](/.resGen/_bannerL.png#gh-light-mode-only)

<a href="/aws/readme.md"><img src="/.resGen/_back.svg" width="52.5"></a>

---

# Virtual Private Cloud (VPC)

## 1. Crear una VPC

El primer paso es crear una VPC. Una VPC es una red virtual que permite a los usuarios crear y configurar redes privadas seguras dentro de la nube de AWS.

- Vamos al menú de AWS y buscamos **VPC** y entramos en el servicio.

![alt text](image.png)

- En el menú de VPC, seleccionamos **Crear VPC**

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