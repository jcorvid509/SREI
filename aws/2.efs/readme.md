![](/.resGen/_bannerD.png#gh-dark-mode-only)
![](/.resGen/_bannerL.png#gh-light-mode-only)

<a href="/aws/readme.md"><img src="/.resGen/_back.svg" width="52.5"></a>

---

# Elastic File System (EFS)

EFS es un servicio de almacenamiento de archivos en la nube que permite a los usuarios almacenar y compartir archivos de manera segura y escalable.

- Vamos al menú de **AWS** y buscamos **EFS**, entramos en el servicio y seleccionamos **Crear un sistema de archivos**.

![alt text](image.png)

- En **Crear un sistema de archivos**
  - **Nombre**: `serverwp-efs`
  - **Virtual Private Cloud (VPC)**: `proyecto-vpc`
  
  ![alt text](image-1.png)

- Comprobamos que se ha creado correctamente

![alt text](image-2.png)

# Añadir EFS a nuestra VPC

- En el menú de **AWS** buscamos **VPC**, **Panel de VPC > Seguridad > Grupos de seguridad** y sellecionamos nuestro grupo.

![alt text](image-3.png)

- Dentro del grupo de seguridad, seleccionamos **Reglas de entrada** y **Editar reglas de entrada**.

![alt text](image-4.png)

- Una vez dentro, seleccionamos **Agregar regla** y seleccionamos **EFS** como protocolo y agregamos el grupo de seguridad de `serverwp-db-sg` 

![alt text](image-5.png)

