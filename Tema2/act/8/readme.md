![](/.resGen/_bannerD.png#gh-dark-mode-only)
![](/.resGen/_bannerL.png#gh-light-mode-only)

<a href="/Tema2/readme.md"><img src="/.resGen/_back.svg" width="52.5"></a>

---

# Subdominios

http://www.zytrax.com/books/dns/ch9/subdomain.html

http://www.zytrax.com/books/dns/ch9/delegate.html


Ejercicio
Configura un DNS primario para el dominio iesmarisma.intranet. Además queremos crear un subdominio “departamentos.iesmarisma.intranet” que resuelvan los siguientes nombres:

Nombre de dominio principal: iesmarisma.intranet
Nombre de hosts en el dominio principal: www, ftp, smtp
Nombre del subdominio: informatica.iesmarisma.intranet
Nombre de hosts en el subdominio: www, ftp, smtp

Configura el subdominio siguiendo las instrucciones de los apuntes:
Creando un subdominio virtual.
Delega el subdominio.

Creación mediante script de subdominios
http://bash.cyberciti.biz/domain/create-bind9-domain-zone-configuration-file/
http://www.freeos.com/guides/lsst/scripts/AddDomain
Otros
https://python-for-system-administrators.readthedocs.io/en/latest/

Actividad
Utiliza los enlaces anteriores para crear un script que permita crear subdominios
Utiliza la directiva $INCLUDE para incluir un fichero que contenga la descripción del subdominio
Opcionalmente se recomienda leer el enlace “Python for system admin” y tratar de llevar a cabo la misma tarea usando la clase “Popen” del módulo “subprocess” de Python

Nota
Lee el siguiente artículo una vez que compruebes que mediante dig (o nslookup) el servidor DNS resuelve el dominio correctamente, pero ping, firefox no lo hacen.
http://askubuntu.com/questions/81797/nslookup-finds-ip-but-ping-doesnt

...
Check in /etc/nsswitch.conf, you will probably see:
hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4
mdns4 is what is doing multicast dns. Try changing this to:

hosts: files dns
And see if it makes any difference. If it makes it work, you can remove mdns permanently with:

Try apt-get remove libnss-mdns
Which will do the nsswitch.conf change for you as well.
…
Nota: Persist DNS nameserver for Ubuntu
https://www.netroby.com/view/3630#.U2mTfHVdUc0

