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

- En el menú de **EFS** entramos en nuestro sistema de archivos.

![alt text](image-6.png)

![alt text](image-7.png)

- Una vez dentro, bajamos y seleccionamos la pestaña **Red > Administrar**

![alt text](image-8.png)

- Cambiamos la VPC por la nuestra.

![alt text](image-9.png)

- Volvemos a la página del sistema **EFS** y pulsamos en **Asociar**

![alt text](image-10.png)

- Sellecionamos `Montaje a traves de IP` y `us-east-1a` y copiamos el código que nos aparece.

```bash
sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport 10.0.143.226:/ efs
```

![alt text](image-11.png)

# Montar EFS en nuestro servidor

- Volvemos a nuestra **instancia EC2** e instalamos **NFS**

```bash
sudo apt install nfs-common -y
```

![alt text](image-12.png)

- Creamos un directorio para montar el sistema de archivos.

```bash
sudo mkdir -p efs
```

![alt text](image-13.png)

- Montamos el sistema de archivos con el comando que copiamos anteriormente.

![alt text](image-14.png)

# Instalación de Wordpress

- Descargamos el archivo de instalación de Wordpress en la ruta `/var/www/html`.

```bash
sudo wget http://wordpress.org/latest.tar.gz
```

![alt text](image-15.png)

- Descomprimimos el archivo.

```bash
sudo tar -xvzf latest.tar.gz
```

![alt text](image-16.png)

- Creamos un cliente de MySQL para la base de datos de Wordpress.

```bash
sudo apt install mysql-client -y
```

![alt text](image-17.png)

- Entramos en MySQL.

```bash
mysql -h serverwp-db.cg8gix3k6fvc.us-east-1.rds.amazonaws.com -u admin -p
```

> Donde `serverwp-db.cg8gix3k6fvc.us-east-1.rds.amazonaws.com` es el nombre del servidor de la base de datos, `admin` es el nombre del usuario y `password` es la contraseña.

![alt text](image-18.png)

- Creamos una nueva base de datos para Wordpress.

```sql
CREATE DATABASE wordpress;
CREATE USER 'wordpress_user'@'%' IDENTIFIED BY 'password123';
GRANT ALL PRIVILEGES ON wordpress.* TO 'wordpress_user'@'%';
FLUSH PRIVILEGES;
```

![alt text](image-19.png)

- Si accedemos a la tuta `http://server_ip/wordpress/wp-admin/setup-config.php`, veremos la siguiente pantalla:

![alt text](image-20.png)

![alt text](image-21.png)

## <a href="../2.efs/readme.md"><img src="/.resGen/_arrow.svg" width="30" align="left"></a> <p style="text-align: center;">VPC</p>