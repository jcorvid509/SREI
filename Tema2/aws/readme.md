![](/.resGen/_bannerD.png#gh-dark-mode-only)
![](/.resGen/_bannerL.png#gh-light-mode-only)

<a href="/Tema2/readme.md"><img src="/.resGen/_back.svg" width="52.5"></a>

&emsp;&emsp;
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
<a href="2.md"><img src="/.resGen/_arrow.svg" width="30"></a>
<a href="1.1.md"><img src="/.resGen/_notes.svg" width="30" align="right"></a>

---

# Amazon Web Services

```mermaid
architecture-beta
    group api(bxl:aws)[AWS]
    group database(bxl:unity)[Database]

    service db(logos:aws-aurora)[Database] in api
    service disk1(logos:aws-glacier)[Storage] in api
    service disk2(logos:aws-s3)[Storage] in api
    service server(logos:aws-ec2)[Server] in api

    db:L -- R:server
    disk1:T -- B:server
    disk2:T -- B:db

```

|||
| --- | --- |
| **Actividad VPC 1** | [<img src="/.resGen/_arrow.svg" width="30">](1.md) |
| **Actividad VPC 2** | [<img src="/.resGen/_arrow.svg" width="30">](2.md) |