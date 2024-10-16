q- Usar "aliaas" para redireccionar a   ~ = /home/usuario

## Creamos un directorio en ~

``` bash
mkdir /home/usuario/img
```

## Bajamos una imagen y la guardamos en el directorio (o cualquier otro archivo)

/home/usuario/img/tux.png               /home/usuario/img/index.html

## Editamos "apache.conf"

``` bash
sudo nano /etc/apache2/apache2.conf
```

## Añadimos la línea

``` bash
Alias /imagenes   "/home/usuario/img"
```
> Esto crea unnalias, por el que si volvemos a preguntar o direccionar a </imagenes>, este nos dirigrá a </home/usuario/img>

``` bash
GET /   (localhost/)
Apache busca en /var/www/html

GET /imagenes
```
## Añadimos directiva directory

<Directory /home/usuario/img>
    Requier all granted
</Directory>

## Comprobamos la sintaxis

``` bash
apachectl configtext
```
## Reiniciamos el servicio de Apache

``` bash
sudo service apache2 restart
```
