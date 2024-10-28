Usar "alias" para redireccionar a   ~ = /home/usuario

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


----------------------------------------------------------------------------------------------------

# Expresiones regulares

partido	abcdegg
partido	abcde
partido	abc
abc\w*

match	abc123xyz
match	define "123"
match	var g = 123;
\D+123\D+

match	cat.
match	896.
match	?=+.
skip	abc1
\.

### Que empiece por las letras [ __ ]

match	can
match	man
match	fan
skip	dan
skip	ran
[cmf]an

### Que no empiece por las letras [^__ ]

match	hog	Success
match	dog	Success
skip	bog
[^b]og

#### 
match	Ana
match	Bob
match	Cpc
skip	aax
skip	bby
skip	ccz
[A-Z]\w+

### Repetición de caracteres

``` html
match	wazzzzzup
match	wazzzup
skip	wazup
waz{3,5}up
```

match	aaaabcc
match	aabbbbc
match	aacc
skip	a
a{2,}

match	1 file found?
match	2 files found?
match	24 files found?
skip	No files found.
\d+\sfiles?\sfound\?

match	1.   abc
match	2.	abc             <br>
match	3.           abc    <br>
skip	4.abc               <br>
\d.\s+abc

### Indicar principio ^ y final $ de la línea

match	Mission: successful                             <br>
skip	Last Mission: unsuccessful                      <br>
skip	Next Mission: successful upon capture of target <br>
`^Mission`
`\ssuccessful$`

### Grupos de captura

capture	file_record_transcript.pdf	file_record_transcript  <br>
capture	file_07241999.pdf	        file_07241999           <br>
skip	testfile_fake.pdf.tmp                               <br>
`^(file.*)\.pdf`
