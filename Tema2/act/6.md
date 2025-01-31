![](/.resGen/_bannerD.png#gh-dark-mode-only)
![](/.resGen/_bannerL.png#gh-light-mode-only)

<a href="/Tema2/readme.md"><img src="/.resGen/_back.svg" width="52.5"></a>

<a href="5.md"><img src="/.resGen/_arrow_r.svg" width="30"></a>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
<a href="7.md"><img src="/.resGen/_arrow.svg" width="30"></a>
<a href="6.1.md"><img src="/.resGen/_notes.svg" width="30" align="right"></a>

---

# DNS Maestro

> [text](https://www.digitalocean.com/community/tutorials/how-to-configure-bind-as-an-authoritative-only-dns-server-on-ubuntu-14-04)
> 
> [text](http://www.zytrax.com/books/dns/ch6/)
> 
> [text](https://help.ubuntu.com/community/BIND9ServerHowto)
> 
> [text](http://askubuntu.com/questions/81797/nslookup-finds-ip-but-ping-doesnt)
> 
> [text](https://www.netroby.com/view/3630#.U2mTfHVdUc0)


## Actividades

Crea un fichero de zona para `marisma.intranet`, además de la zona de resolución inversa

En la zona se definirán los siguientes `FQND`:
> Servidor DNS: `ns1` <br>
> Servidor fpt: `ftp1` <br>
> Servidores de correo: `mail1`, `mail2` <br>
> Servidores web: `www`, `departamentos`

Se pide:

> Configura el servidor DNS con los registros necesarios <br>
> Cambia la configuración del cliente para que emplee el nuevo servidor DNS: /etc/resolv.conf (ver nota a pie de página)

Haz la consultas necesarias para comprobar el correcto funcionamiento del servidor DNS:
(SOA, MX, A, NS). Comprueba además de la resolución inversa.

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
