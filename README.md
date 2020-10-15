# Pure-FTPd & FileZilla Client Dockerfiles
Este proyecto consiste en la creacion de dockerfiles para Pure-FTPd server y FileZilla Client, los cuales se asocian al protocolo FTP, para que ambos puedan generar trafico entre si.
## Instalacion
Como prerequistos, se encuentran la necesidad de tener instalados Docker y Git:

-Docker: https://docs.docker.com/engine/install/

-Git:  https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

**Server:**
```
$ docker build -t pure-ftpd:final
```
**Client:**
```
$ docker build -t filezilla:final
```
Para el cliente, el host es ftp://localhost

## Video
https://www.youtube.com/watch?v=7y6xFn3h1KI
