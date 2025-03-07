![](/.resGen/_bannerD.png#gh-dark-mode-only)
![](/.resGen/_bannerL.png#gh-light-mode-only)

<a href="/aws/readme.md"><img src="/.resGen/_back.svg" width="52.5"></a>

---

# Elastic File System (EFS)

## Creación de EFS

- Accedemos a la consola de **Amazon EFS** y **Crear un nuevo EFS**.

![alt text](image.png)

- Añadimos el **Nombre** y el **VPC**
  - **Nombre**: `efs-practica1`
  - **VPC**: `proyecto-vpc`

![alt text](image-1.png)

![alt text](image-2.png)

- Volvemos a la **VPC > Seguridad > Grupos de Seguridad** 

![alt text](image-3.png)

- Creamos un nuevo grupo de seguridad para el EFS y lo asociamos a la VPC.